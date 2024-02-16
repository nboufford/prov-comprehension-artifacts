# Run preprocess
# Run train_model with the variable SUCCEED set to False
# Run train_model with the variable SUCCEED set to True
# Run evaluate_model.py

preprocess: 
	python3 preprocess.py 

train_model: 
	python3 train_model.py

clean:
	rm temp_data.csv
	rm model.ckpt