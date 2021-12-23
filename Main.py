

import pandas as pd


template_name = "heading_template.xlsx"
file_name = 'Sales_Invoice for company.xlsx'

template_df = pd.read_excel(template_name, header=0)



# loop over all headings and check values
freq = {}  # ? this for store heading values

for column in template_df.columns:
    freq[column] = template_df[column][0]


main_df =  pd.read_excel(file_name, header=0)



for column in main_df.columns:
    for key, value in freq.items():
        if column == key:
            if "item" in str(key).lower():
                # print("pass")
                pass

                # ! write code here
                # * we passed the condition here
                pass
            elif value == 1:
                # ! write code here
                # ? loop for delete cells in data

                for i, item in enumerate(main_df[column]):
                    if i == 0:
                        pass
                    else:
                        main_df.at[i, column] = None
            elif value == 0:
                pass

# string = "welcome to my Items"
# if "item" in string.lower():
#     print("founded")


print(main_df.head())


main_df.to_excel("final_invoice_test.xlsx", header=True, index=False)

