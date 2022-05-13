python load_model.py
python dataset.py -i './data/wiki_subset_100.json' -o './data/train_data.txt'
python trainer.py -i './data/train_data.txt' -m '125M' -e 3 -o save -c True
