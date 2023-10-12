analysis: preprocess.R train_model.py data.csv
	Rscript preprocess.R 
	python3 train_model.py 

r_code: preprocess.R data.csv
	Rscript preprocess.R 

py_code: train_model.py temp_data.csv
	python3 train_model.py

clean:
	rm temp_data.csv
	rm model.ckpt