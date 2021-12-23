import os
from sys import argv
from os import system
from tqdm import tqdm


FILE_NAME = argv[1]
FILE_PATH = "output/"
FILES = os.listdir(FILE_PATH)

commands = [
    f"python split_by_customer.py {FILE_NAME}",
    "python split_by_date.py",
    "python clear_invoice_data.py",
    "python concat_excel_files.py"
]


for command in tqdm(commands, desc='Processing Excel Files', colour='GREEN', unit='Step'):
    system(command)
