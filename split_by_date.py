import pandas as pd
import os
from tqdm import tqdm

# from sys import argv
from os import system


# FILE_NAME = argv[1]
FILE_PATH = "output/"
FILES = os.listdir(FILE_PATH)


for excel_file in tqdm(FILES, desc="Generate Invoices Based On Date: ", colour="GREEN", unit=" Invoice"):
    df = pd.read_excel(f"output/" + excel_file, header=0)

    column_name = "Date"

    unique_values = df[column_name].unique()
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
