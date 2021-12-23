import os
from sys import argv
from os import system


FILE_NAME = argv[1]
FILE_PATH = "output/"
FILES = os.listdir(FILE_PATH)

system(f"python split_by_customer.py {FILE_NAME}")
system("python split_by_date.py")
system("python clear_invoice_data.py")