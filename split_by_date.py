import pandas as pd
import os
from sys import argv

# import sys
from time import sleep

from os import name, system

file_name = argv[1]

system(f"python split_by_customer.py {file_name}")

file_path = "output/"
files = os.listdir(file_path)

for excel_file in files:
    df = pd.read_excel(f"output/" + excel_file, header=0)

    column_name = "Date"

    unique_values = df[column_name].unique()
    # print(unique_values)
    count = 1
    count_len_unique_values = len(unique_values)
    for unique_value in unique_values:

        unique_value = str(unique_value).replace("T00:00:00.000000000", "")
        df_output = df[df[column_name].astype(str).str.contains(unique_value)]
        if len(unique_values) != 1:

            name = excel_file.split(".")
            name = name[0]
            output_file = os.path.join(
                "output", f"sales_invoices_{name}_{count}" + ".xlsx"
            )
            # deleted_file = os.path.join("output", f"{excel_file}")
            deleted_file = "output\\" + f"{excel_file}"

            df_output.to_excel(output_file, header=True, index=False)
            if count_len_unique_values == 1:
                system(f"del {deleted_file}")
            count += 1
            count_len_unique_values -= 1
        print(count_len_unique_values)
        sleep(0.4)
