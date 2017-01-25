
cp ../data/out.txt data/out.txt
python setup.py install
fxml.py a.model data/out.txt --standard-dataset --verbose train --iters 1 --threads 100 --trees 20 --label-weight propensity --alpha 1e-4 --leaf-classifiers

fxml.py a.model data/out.txt --standard-dataset inference --score