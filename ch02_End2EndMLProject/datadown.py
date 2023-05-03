from pathlib import Path 
import pandas as pd 
import urllib.request
import tarfile as tar

def load_housing_data():
    tarball_path = Path('datasets/housing.tgz')
    if not tarball_path.is_file():
        Path('datasets').mkdir(parents=True,exist_ok=True)
        url = 'https://github.com/ageron/data/raw/main/housing.tgz'
        urllib.request.urlretrieve(url, tarball_path)
        with tar.open(tarball_path) as housing_tarfile: 
            housing_tarfile.extractall(path= 'datasets')
    return pd.read_csv('datasets/housing/housing.csv')
house = load_housing_data()
