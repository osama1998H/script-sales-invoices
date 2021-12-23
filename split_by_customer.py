import pandas as pd
import os
from sys import argv

file_name = argv[1]

df = pd.read_excel(file_name, header=0)

column_name = "Customer"


unique_values = df[column_name].unique()
print(len(unique_values))
count = 1
for unique_value in unique_values:
    df_output = df[df[column_name].str.contains(unique_value)]
    output_file = os.path.join("output", f"sales_invoices_{count}" + ".xlsx")
    df_output.to_excel(output_file, header=True, index=False)
    count += 1
