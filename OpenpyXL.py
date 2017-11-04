# Read in excel data
from openpyxl import workbook
from openpyxl import load_workbook
wb = load_workbook('Hiace2015.xlsx') #explicitly loading workbook, will automate later
sheet = list(wb.active) # activating is an attribute and not a method
sheetnames = list(wb.get_sheet_names())
print sheetnames

cells = sheet['C11':'M31']
for c1, c2,c3,c4,c5,c6,c7,c8,c9,c10,c11 in cells:
    print "{0:8} {1:8} {2:8} {3:8} {4:8} {5:8} {6:8} {7:8} {8:8} {9:8} {10:8}".format(c1.value, c2.value, c3.value, c4.value, c5.value, c6.value, c7.value, c8.value,
                               c9.value, c10.value, c11.value)

for row in sheet.iter_rows(min_row=20, min_col=11):
    for cell in row:
        cells.append(cell.value)
    print("Number of values: {0}".format(len(values)))
# def get_all_data(sheet_in):
#       Final_copy = Workbook()
#       Final_copy = Final_copy.active()
#       Final_copy.title = "Hiace Details"
#       Final_copy = Final_copy["Hiace Details"]
#       for row in row_range:
#           for column in col_range:
#             print row, column
#
#       wb.copy_worksheet()
#       wb.save('Final_Copy_Hiace_2016.xlsx')


            # create csv file that has all details to report on
# print ("Rows: ", sheet.max_row) # for debugging purposes
# print ("Columns: ", sheet.max_column) # for debugging purposes
# last_data_point = ws.cell(row = sheet.max_row, column = sheet.max_column).coordinate
# print ("Last data point in current worksheet:", last_data_point) #for debugging purposes
#
# #import next file and add to master
# append_point = ws.cell(row = sheet.max_row + 1, column = 1).coordinate
# print ("Start new data at:", append_point)
# wb = load_workbook('second_file.xlsx')
# sheet2 = wb.get_sheet_by_name('Sheet1')
# start = ws.cell(coordinate='A2').coordinate
# print("New data start: ", start)
# end = ws.cell(row = sheet2.max_row, column = sheet2.max_column).coordinate
# print ("New data end: ", end)
#
# # write a value to selected cell
# #sheet[append_point] = 311
# #print (ws.cell(append_point).value)
#
# #save file
# wb.save('master_file.xlsx')