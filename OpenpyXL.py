# Read in excel data
from openpyxl.workbook.
from openpyxl import Workbook
from openpyxl import load_workbook
wb = load_workbook('Hiace2015.xlsx') #explicitly loading workbook, will automate later

# grab active worksheet in current workbook
#ws = wb.active
print wb.get_sheet_names()
N = len(wb.rows)
d = wb.cell(row=4, column=2, value=10)
print d
cell_range = ws['C7':'M7']
col_range = wb['C:M']
row_range = wb['9:31']
def get_all_data(sheet_in):
      Final_copy = Workbook()
      Final_copy = Final_copy.active()
      Final_copy.title = "Hiace Details"
      Final_copy = Final_copy["Hiace Details"]
      for row in row_range:
      #for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
        for column in col_range:
          wb.copy_worksheet()


            # create csv file that has all details to report on
# #
# #get max columns and rows
# #sheet = wb.get_sheet_by_name('15-9-17')
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