analysis: train_model.py data.csv
	python3 train_model.py --learning_rate 0.1
	python3 train_model.py --learning_rate 0.01
	python3 train_model.py --learning_rate 0.001
	python3 evaluate_models.py

clean:
	rm model_1.ckpt
	rm model_2.ckpt
	rm model_3.ckpt