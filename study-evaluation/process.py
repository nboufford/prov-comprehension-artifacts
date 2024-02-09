# python process.py input.csv output.csv

import pandas as pd
import argparse

def merge_df(df, sup_df):
    # Add sup info to the df
    result = pd.merge(df, sup_df, left_on='ResponseId', right_on='id')
    return result

def remove_qualtrics_rows(df):
    # Remove the first two rows
    df = df.iloc[2:]
    return df

def get_t0_score(row, answer_key_row):
    score = 0
    for i in range(6):
        if (row[f't0_q_{i}'] == answer_key_row[f't0_q_{i}']):
            score = score + 1
    return score

def get_t0_score_percent(row):
    return row['t0_score'] / 6 * 100

def get_t1_score(row, answer_key_row):
    score = 0
    for i in range(7):
        if (row[f't1_q_{i}'] == answer_key_row[f't1_q_{i}']):
            score = score + 1
    return score
    
def get_t1_score_percent(row):
    return row['t1_score'] / 7 * 100

def get_t2_score(row, answer_key_row):
    score = 0
    for i in range(4):
        # q1 has four parts, assign one point if all four parts are correct (also labeled 1,3,4,5 annoyingly)
        if (i == 1):
            q1_score = 0
            for j in range(1,6):
                if (j == 2):
                    continue
                if (row[f't2_q_1_{j}'] == answer_key_row[f't2_q_1_{j}']):
                    q1_score = q1_score + 1
            if (q1_score == 4):
                score = score + 1
        if (row[f't1_q_{i}'] == answer_key_row[f't1_q_{i}']):
            score = score + 1
    return score

def get_t2_score_percent(row):
    return row['t2_score'] / 5 * 100

def get_t3_score(row, answer_key_row, sup_df):
    score = 0
    for i in range(2):
        if (row[f't1_q_{i}'] == answer_key_row[f't1_q_{i}']):
            score = score + 1
    if (sup_df['score_t3_q2'].iloc[row.name] == 1):
        score = score + 1
    if (sup_df['score_t3_q2'].iloc[row.name] == 2):
        score = score + 2
    return score

def get_t3_score_percent(row):
    return row['t3_score'] / 4 * 100

def get_scores(df, answer_key_df, sup_df):
    # Add new columns for overall tlx score
    #get_t0_score(df, answer_key_df)
    answer_key_df.replace(1, '1', inplace=True)
    answer_key_df.replace(2, '2', inplace=True)
    answer_key_df.replace(3, '3', inplace=True)
    answer_key_df.replace(4, '4', inplace=True)
  
    df['t0_score'] = df.apply(lambda row: get_t0_score(row, answer_key_df.iloc[0]), axis=1)
    df['t1_score'] = df.apply(lambda row: get_t1_score(row, answer_key_df.iloc[0]), axis=1)
    df['t2_score'] = df.apply(lambda row: get_t2_score(row, answer_key_df.iloc[0]), axis=1)
    df['t3_score'] = df.apply(lambda row: get_t3_score(row, answer_key_df.iloc[0], sup_df), axis=1)

    # Get scores as percent
    df['t0_score_percent'] = df.apply(lambda row: get_t0_score_percent(row), axis=1)
    df['t1_score_percent'] = df.apply(lambda row: get_t1_score_percent(row), axis=1)
    df['t2_score_percent'] = df.apply(lambda row: get_t2_score_percent(row), axis=1)
    df['t3_score_percent'] = df.apply(lambda row: get_t3_score_percent(row), axis=1)
    return df

def get_overall_tlx(df):

    df.replace('1 - Very Low', '1', inplace=True)
    df.replace('5 - Very High', '5', inplace=True)
    df.replace('5 - Failure', '5', inplace=True)
    df.replace('1 - Perfect', '1', inplace=True)

    t0_columns = [f't0_tlx_{i}' for i in range(5)]
    t1_columns = [f't1_tlx_{i}' for i in range(5)]
    t2_columns = [f't2_tlx_{i}' for i in range(5)]
    t3_columns = [f't3_tlx_{i}' for i in range(5)]

    # Convert columns to numeric
    df[t0_columns] = df[t0_columns].apply(pd.to_numeric, errors='coerce')
    df[t1_columns] = df[t1_columns].apply(pd.to_numeric, errors='coerce')
    df[t2_columns] = df[t2_columns].apply(pd.to_numeric, errors='coerce')
    df[t3_columns] = df[t3_columns].apply(pd.to_numeric, errors='coerce')

    # Calculate the totals and averages using assign
    df = df.assign(
        t0_tlx_total=df[t0_columns].sum(axis=1),
        t1_tlx_total=df[t1_columns].sum(axis=1),
        t2_tlx_total=df[t2_columns].sum(axis=1),
        t3_tlx_total=df[t3_columns].sum(axis=1),
        t0_tlx_score=lambda x: x['t0_tlx_total'] / 5,
        t1_tlx_score=lambda x: x['t1_tlx_total'] / 5,
        t2_tlx_score=lambda x: x['t2_tlx_total'] / 5,
        t3_tlx_score=lambda x: x['t3_tlx_total'] / 5
    )

    return df

# Normalize values between -1 and 1
def normalize_column(column):
    min_val = column.min()
    max_val = column.max()
    normalized_column = -1 + 2 * (column - min_val) / (max_val - min_val)
    return normalized_column

def normalize_row(row):
    min_val = row.min()
    max_val = row.max()
    
    # Normalize the row
    normalized_row = (row - min_val) / (max_val - min_val)
    
    # Create new column names for normalized values
    new_column_names = [f"{col}_normalized" for col in row.index]
    
    # Add normalized values as new columns to the original DataFrame
    for new_col, value in zip(new_column_names, normalized_row):
        row[new_col] = value
    
    return row

def get_normalized_tlx(df):
    t0_columns = [f't0_tlx_{i}' for i in range(5)]
    t1_columns = [f't1_tlx_{i}' for i in range(5)]
    t2_columns = [f't2_tlx_{i}' for i in range(5)]
    t3_columns = [f't3_tlx_{i}' for i in range(5)]

    tlx_columns = df.filter(regex='tlx_[0-4]$')

    normalized_tlx_columns = tlx_columns.apply(normalize_row, axis=1)

    df = pd.merge(df, normalized_tlx_columns, how='left')
 
    return df

def get_normalized_average_tlx(df):

    t0_columns = [f't0_tlx_{i}_normalized' for i in range(5)]
    t1_columns = [f't1_tlx_{i}_normalized' for i in range(5)]
    t2_columns = [f't2_tlx_{i}_normalized' for i in range(5)]
    t3_columns = [f't3_tlx_{i}_normalized' for i in range(5)]

    # Calculate the totals and averages using assign
    df = df.assign(
        t0_tlx_total_norm=df[t0_columns].sum(axis=1),
        t1_tlx_total_norm=df[t1_columns].sum(axis=1),
        t2_tlx_total_norm=df[t2_columns].sum(axis=1),
        t3_tlx_total_norm=df[t3_columns].sum(axis=1),
        t0_tlx_avg_normalized=lambda x: x['t0_tlx_total_norm'] / 5,
        t1_tlx_avg_normalized=lambda x: x['t1_tlx_total_norm'] / 5,
        t2_tlx_avg_normalized=lambda x: x['t2_tlx_total_norm'] / 5,
        t3_tlx_avg_normalized=lambda x: x['t3_tlx_total_norm'] / 5
    )
    return df

if __name__ == "__main__":
    # Set up command line argument parser
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('input_csv', help='Input CSV file name')
    parser.add_argument('output_csv', help='Output CSV file name')

    # Parse command line arguments
    args = parser.parse_args()

    input_df = pd.read_csv(args.input_csv)

    sup_df = pd.read_csv('sup_info.csv')
    answer_key_df = pd.read_csv('answer_key.csv')

    input_df = remove_qualtrics_rows(input_df)
    input_df = merge_df(input_df, sup_df)
    input_df = get_overall_tlx(input_df)
    input_df = get_normalized_tlx(input_df)
    input_df = get_normalized_average_tlx(input_df)
    input_df = get_scores(input_df, answer_key_df, sup_df)

    input_df.to_csv(args.output_csv, index=False)