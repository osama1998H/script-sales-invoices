import pandas as pd
import os
from sys import argv
import numpy as np

FILE_NAME = argv[1]
COLUMN_NAME = "No"

df = pd.read_excel(FILE_NAME, header=0)

unique_values = df[COLUMN_NAME].unique()

print(unique_values)

count = 1
for unique_value in unique_values:

    df_output = df[df[COLUMN_NAME] == unique_value]
    output_file = os.path.join("output", f"sales_invoices_{count}" + ".xlsx")
    df_output.to_excel(output_file, header=True, index=False)
    count += 1
