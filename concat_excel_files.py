import os
import pandas as pd
from tqdm import tqdm
from termcolor import colored


FILE_PATH = "output/"
OUT_FILE_PATH = "out/"
FILES = os.listdir(FILE_PATH)

main_df = pd.DataFrame()


for excel_file in tqdm(
    FILES, desc="Concat Invoices To One File:  ", colour="GREEN", unit=" File"
):

    second_df = pd.read_excel(FILE_PATH + excel_file)

    main_df = pd.concat([main_df, second_df], axis=0)

    deleted_file = "output\\" + f"{excel_file}"

    os.system(f"del {deleted_file}")

main_df.to_excel(
    f"{OUT_FILE_PATH}final_exported_data.xlsx", header=True, index=False
)

print("\n")
# print("File Was Exported To: ", OUT_FILE_PATH + "final_exported_data.xlsx")
print(
    colored("File Was Exported To: ", 'red'),
    colored(f"{OUT_FILE_PATH}final_exported_data.xlsx", 'green'),
)