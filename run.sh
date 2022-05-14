python load_model.py
python dataset.py -i './data/sample_data.json' -o './data/sample_data.txt'
python trainer.py -i './data/sample_data.txt' -m '125M' -e 3 -o 'baseline' -c True
