# SAVES THE TRACKS FROM A PLAYLIST OR THE WHOLE LIBRARY INTO AN EXCEL FILE
# CAN USE WMP, ITUNES (WHOLE LIBRARY, PLAYLIST OR XML)
# MORE THAN ONE PLAYLIST CAN BE SELECTED
# WHEN CREATING AN EXCEL OUTPUT FOR THE LIBRARY, A NUMBER OF TRACKS CAN BE SPECIFIED.
# IF NOT SPECIFIED, IT'S ALL THE TRACKS.

import pandas as pd
from Files import file_w_ext


# MAIN CODE
def Save_Excel(PL_name=None,PL_nbr=None,Do_lib=False,rows=None,iTunes=True,XML=False,col_names = ["Arq","Art","Title"]):
    # CALLS Read_PL FUNCTION ,Do_lib=True,rows=10
    # col_names =  ["Arq","Art","Title","AA","Album","Genre","Covers","Year"]
    
    if iTunes:
       import Read_PL
       # EXCLUDE INVALID TAGS 
       col_names = [x for x in col_names if x in Read_PL.order_list_itunes]
       if not XML:
          dict = Read_PL.Read_PL(col_names,PL_name=PL_name,PL_nbr=PL_nbr,Do_lib=Do_lib,rows=rows)
          df = dict["DF"]
       else:
           # REMOVES INVALID COL. FOR XML (ID)
           try:
               col_names.remove("ID")  # 6 is not in the list
           except:
               pass
           df = Read_PL.Read_xml(col_names,rows=rows)
    else:
        import WMP_Read_PL
        # EXCLUDE INVALID TAGS 
        col_names = [x for x in col_names if x in WMP_Read_PL.order_list_wmp]
        dict = WMP_Read_PL.Read_WMP_PL(col_names,PL_name=PL_name,PL_nbr=PL_nbr,Do_lib=Do_lib,rows=rows)   
        df = dict["DF"]
    # ASSIGNS
    # App = dict["App"]
    # playlists = dict["PLs"]
    

    # KEEP ONLY SELECTED COLS.
    if iTunes and XML and "PID" in col_names:
       col_names.append("PID2") 
    df = df.loc[:, col_names]
    
    # RENAME THE COLUMNS HEADERS
    if "Arq" in col_names:
        df.loc[:, "File"] = df["Arq"].apply(file_w_ext)
        df = df.rename(columns={"Arq": "Location" })

    # SAVE TO EXCEL FILE:
    user_inp = input("\nOutput name (file will be saved to D:\iTunes\Excel\\all.xls): ")
    # user_inp = ""
    #user_inp = "Test"
    if user_inp == "":
       file_nm = "D:\\iTunes\\Excel\\all.xlsx"
    else:
        file_nm = "D:\\iTunes\\Excel\\" + user_inp + ".xlsx"
    
    # NAMES SHEET
    if iTunes:
       if not XML:
          sheet = "iTunes"
       else:
          sheet = "XML"   

       # ASSIGNS VARS
    #    ID = [x for x in df["ID"]]
    #    Track_ID = [id[3] for id in ID]
    #    df['Track ID'] = Track_ID
    #    df = df.sort_values(by='Track ID', ascending=True)
    else:
        sheet = "WMP"
    # save the dataframe to an Excel file
    df.to_excel(file_nm, sheet_name=sheet, index=False)
    # print("Hello, " + file_nm + "!")

# CHAMA PROGRAM PL_name="ALL",Fave-iPhone ["Arq","Art","Title","Len"] "ID", "PID", "Added"
Save_Excel(PL_name="House2",Do_lib=False,rows=None,iTunes=True,XML=0,col_names = ["Arq","Art","Title","AA","Album","Year","Genre"])