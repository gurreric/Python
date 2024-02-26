import os
from pathlib import Path
directory = 'T:\ETL\Ptest4'
files = Path(directory).glob('*')

for file in files:
    with open(file, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(file, 'w') as fout:
        fout.writelines(data[5:])