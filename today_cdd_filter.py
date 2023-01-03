import pandas as pd
pd1 = pd.read_csv("results.csv")
pd2 = pd.read_excel("CDD관리리스트.xlsx", engine='openpyxl')

pd_result = pd.merge(pd1, pd2, left_on='가맹점ID', right_on='ID', how='inner')
pd_result
pd_result.to_csv("today_cdd.csv", encoding="utf-8-sig")
