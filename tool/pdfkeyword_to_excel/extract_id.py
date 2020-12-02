import openpyxl as xl
import csv
import numpy as np


## flags {
TOP3 = False
TOP2 = True
TOP1 = True
## flags }


def main(dargs):
    input_excel_name  = dargs["INPUT_EXCEL_NAME"]
    output_excel_name = dargs["OUTPUT_EXCEL_NAME"]
    input_csv_name    = dargs["INPUT_CSV_NAME"]
    
    
    ## READ Excel file
    wb = xl.load_workbook(input_excel_name)
    # ws = wb.copy_worksheet(wb["Sheet1"])
    # ws.title = "Sheet2"
    ws = wb["Sheet1"]


    ## 学生番号抜き出し
    target = ws["C10:C89"]
    for i in range(len(target)):
        for j in range(len(target[i])):
            print(target[i][j].value)


            
if __name__ == '__main__':
    dargs = {
        "INPUT_EXCEL_NAME"         : "template.xlsx",
        "OUTPUT_EXCEL_NAME"        : "output.xlsx",
                                  
        #"INPUT_CSV_NAME"           : "result.csv",
        "INPUT_CSV_NAME"           : "id.csv",
                                  
        # "AUTO_FILTER_RANGE"        : "A10:DI81",
        # "KEYWORD_RANGE"            : "J11:DI81",
        "AUTO_FILTER_RANGE"        : "A10:DI89",
        "KEYWORD_RANGE"            : "J11:DI89",
        
        "KEYWORD_START_ROW_NUM"    : 11,
        "KEYWORD_START_COLUMN_NUM" : 10,

        "KEYWORD_START_COLUMN"     : "J",
        "KEYWORD_END_COLUMN"       : "DI",
        "KEYWORD_START_ROW"        : 11,
        "KEYWORD_END_ROW"          : 89,

        "ONE_COLUMN_RANGE"         : "C100:C9356",
    }
    

    main(dargs)


    

