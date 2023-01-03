import pandas as pd
pd1 = pd.read_excel("cddList_기술팀전달리스트_0404.xlsx", engine='openpyxl')
pd2 = pd.read_excel("cddList_기술팀전달리스트_0405.xlsx", engine='openpyxl')

pd1_cafe24 = pd1[pd1["호스팅"]=="카페24"]
pd2_cafe24 = pd2[pd2["호스팅"]=="카페24"]
pd_result = pd.concat([pd1_cafe24, pd2_cafe24], keys=["pd1","pd2"]).drop_duplicates(subset="가맹점ID", keep=False)

pd_result_filts = pd_result[pd_result.index.get_level_values(0)=="pd2"]
pd_result_filts.to_csv("results.csv", encoding="utf-8-sig")
