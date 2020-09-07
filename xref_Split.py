import datetime as dt
import pandas as pd
import glob
import re

myFiles = glob.glob('*.xlsx')
print(myFiles)
for file in myFiles:
    print(file)
#    df=pd.read_excel(file,header=0,dtype=object)
    xls = pd.ExcelFile(file)
    a=xls.sheet_names
    sheet_to_df_map = {}
    for sheet_name in a:
        sheet_to_df_map[sheet_name] = xls.parse(sheet_name)
        
    for txtfile, dataframetxt in sheet_to_df_map.items(): 
        print(txtfile)
        filetext=txtfile+'.txt'
        dataframetxt.to_csv(filetext,sep='\t',index=False)