import openpyxl as xl
import csv
import numpy as np


def main(dargs):
    input_excel_name  = dargs["INPUT_EXCEL_NAME"]
    output_excel_name = dargs["OUTPUT_EXCEL_NAME"]
    input_csv_name    = dargs["INPUT_CSV_NAME"]
    
    
    ## READ Excel file
    wb = xl.load_workbook(input_excel_name)
    ws = wb.copy_worksheet(wb["Sheet1"])
    ws.title = "Sheet2"

    
    ## DELETE previous keywords
    keyword = ws[dargs["KEYWORD_RANGE"]]
    for i in range(len(keyword)):
        for j in range(len(keyword[i])):
            keyword[i][j].value=""
    
    
    ## ADD auto filter
    ws.auto_filter.ref = dargs["AUTO_FILTER_RANGE"]
    

    ## COPY color of auto filter
    target = ws["B10:DI10"]
    for i in range(len(target)):
        for j in range(len(target[i])):
            target[i][j]._style = ws["A10"]._style
    

    ## READ keyword from csv file and WRITE
    keyword_num = np.array([], dtype="int8")
    row = dargs["KEYWORD_START_ROW_NUM"]
    col = dargs["KEYWORD_START_COLUMN_NUM"]
    with open(input_csv_name) as f:
        reader = csv.reader(f)
        for r, data in enumerate(reader):
            ### ここで学籍番号 or name チェック
            ## if == :
            ## keyword_num = np.append(keyword_num, None)
            ## row++

            keyword_num = np.append(keyword_num, len(data))
            for index in range(len(data)):
                # ws.cell(row=row+r, column=col+index).value = data[index]
                ws.cell(row+r, col+index).value = data[index]
    

    # keyword_num = np.append(keyword_num, None)                
    # print(keyword_num)
    # print(keyword_num[3])


    ## SORT #keywords and select TOP3 score
    # REMOVE None
    filtered_list = [e for e in keyword_num if e is not None]
    if len(filtered_list) < 3:
        print("can\'t select TOP3. too few kinds of #keywords")
        first  = 10000
        second = 10000
        third  = 10000
    else:
        # SORT
        first  = sorted(set(filtered_list))[-1]
        second = sorted(set(filtered_list))[-2]
        third  = sorted(set(filtered_list))[-3]
        print(first, second, third)

    
    
    ## DRAW TOP3 and NOT submit persons { 
    ##----------------------------------##
    ##       TOP3 -> fill Yellow        ##
    ## NOT submit -> red                ##
    ##----------------------------------##
    yellow_fill = xl.styles.PatternFill(patternType='solid', fgColor='ffff00', bgColor='d7d7d7')
    red_char   = xl.styles.fonts.Font(color='FF0000')
    row_offset = dargs["KEYWORD_START_ROW_NUM"]
    
    for i, score in enumerate(keyword_num):
        print("i = ", i)
        if score is None:     # NOT submit
            start = "A" + str(row_offset+i)
            end   = dargs["KEYWORD_END_ROW"] + str(row_offset+i)
            cell  = ws[start:end]
            for i in range(len(cell)):
                for j in range(len(cell[i])):
                    cell[i][j].font = red_char
        else:
            if score < third: # NOT TOP3
                pass
            else:
                start = "A" + str(row_offset+i)
                end   = dargs["KEYWORD_END_ROW"] + str(row_offset+i)
                cell  = ws[start:end]
                if score < second:   # 3rd
                    for i in range(len(cell)):
                        for j in range(len(cell[i])):
                            cell[i][j].fill = yellow_fill
                elif score < first:  # 2nd
                    for i in range(len(cell)):
                        for j in range(len(cell[i])):
                            cell[i][j].fill = yellow_fill
                else:                # 1st
                    for i in range(len(cell)):
                        for j in range(len(cell[i])):
                            cell[i][j].fill = yellow_fill
    ## DRAW TOP3 and NOT submit persons }
        
    
    ## WRITE Excel file                
    wb.save(output_excel_name)

    

if __name__ == '__main__':
    dargs = {
        "INPUT_EXCEL_NAME"         : "module.xlsx",
        "OUTPUT_EXCEL_NAME"        : "temp.xlsx",
                                  
        "INPUT_CSV_NAME"           : "result.txt",
                                  
        "AUTO_FILTER_RANGE"        : "A10:DI81",
        "KEYWORD_RANGE"            : "J11:DI81",
        
        "KEYWORD_START_ROW_NUM"    : 11,
        "KEYWORD_START_COLUMN_NUM" : 10,

        "KEYWORD_END_ROW"          : "DI",
    }
    

    main(dargs)


    

