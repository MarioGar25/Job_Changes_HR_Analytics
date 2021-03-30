from pathlib import Path
from typing import Union
import zipfile
import pandas as pd

def descompress_csv_files(path: Union[str, Path], csv):
    '''
    Unzip .zip file, obtains a .csv file from the .zip, and returns like DataFrame

    Input: path (path to file.zip), str (.csv file)
    Return: Dataframe from .csv file in .zip file

    '''

    #unzip the file
    zf = zipfile.ZipFile(path)
    #read csv and read like a pandas DataFrame
    df = pd.read_csv(zf.open(csv))
    #close zipfile
    zf.close()
    #returns DataFrame
    return df