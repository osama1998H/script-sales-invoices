import os
import pandas as pd


FILE_PATH = "output/"
OUT_FILE_PATH = "out/"
FILES = os.listdir(FILE_PATH)

main_df = pd.DataFrame()


for excel_file in FILES:

    second_df = pd.read_excel(FILE_PATH + excel_file)

    main_df = pd.concat([main_df, second_df], axis=0)

    deleted_file = "output\\" + f"{excel_file}"

    os.system(f"del {deleted_file}")

main_df.to_excel(OUT_FILE_PATH + "final_exported_data.xlsx", header=True, index=False)
