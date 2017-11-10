from openpyxl import utils
from openpyxl import workbook
from openpyxl import load_workbook
import csv
import os
from os.path import join, getsize


Directory = "/Users/pc/Desktop/DataScientistRTC/DataScientists/Admin"
for root, dirs, files in os.walk(Directory, topdown=False): # We will walk across directory bottom-up approach
#the root is the directory, dirs is sub directory from root and files is all files from root and directories

   print root, 'takes', sum(getsize(join(root, name)) for name in files), "bytes in", len(files), "non-directory files"
# joins "/Users/pc/Desktop/DataScientistRTC/DataScientists/Admin" + "/filename"
   fileList = [] # lets create a list

   for name in os.listdir(Directory): # lists directories in an arbitrary order i.e
#Hiace Bus POL2015.xlsx
#TATA Bus POL 2015.xlsx
#Tata SFC Pick up (1).xlsx
#We want it in a list for indexing
       if name.endswith(".xlsx"): # let's look for xlsx files
           fileList.append(name) # we now have the list of excel files
       print fileList

ofile = open('rtc_vehicles.csv', "wb")
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
header = []
header.append('Sheet Name')
header.append('Date')
header.append('KM Covered')
header.append('Amount$')
writer.writerow(header)
#haha
#for look finding xlsx files
# Read in excel data
wb = load_workbook('Hiace2015.xlsx', data_only=True)

startRow = 0
endRow = 0
startCol = 0
endCol = 0

for sheet in wb.worksheets:
    title = sheet.title
    for row in sheet.iter_rows():
        for cell in row:
            cellValue = cell.value
            if cellValue == 'SL #':
                coord = cell.coordinate
                t = utils.coordinate_from_string(coord)
                startCol = utils.column_index_from_string(t[0])-1
                startRow = t[1]+4

            if type(cellValue) is unicode:
                if cellValue.strip() == 'Total':
                    coord = cell.coordinate
                    t = utils.coordinate_from_string(coord)
                    endCol = utils.column_index_from_string(t[0])+8
                    endRow = t[1]-1

    for irow in range(startRow, endRow):
        row = sheet[irow]
        rowOut = []
        rowOut.append(title)
        for icell in range(startCol, endCol):
            cell = row[icell]
            cellValue = cell.value
            coord = cell.coordinate
            t = utils.coordinate_from_string(coord)
            cellColumn = t[0]
            cellColumNumber = utils.column_index_from_string(cellColumn)
            if cellColumNumber==startCol+2:
                rowOut.append(cellValue)
                print coord
                print cellValue
            elif cellColumNumber==startCol+5:
                rowOut.append(cellValue)
                print coord
                print cellValue
            elif cellColumNumber==startCol+10:
                rowOut.append(cellValue)
                print coord
                print cellValue

        writer.writerow(rowOut)


ofile.close()

# sheet = dict(wb.active) # activating is an attribute and not a method
# sheetnames = list(wb.get_sheet_names())
# print sheetnames
# sum(sheet['C11:M31'].isnull())
# #sheet = int(sheet)
# cells = sheet['C11:M31']
# for c1, c2,c3,c4,c5,c6,c7,c8,c9,c10,c11 in cells:
#     print "{0:8} {1:8} {2:8} {3:8} {4:8} {5:8} {6:8} {7:8} {8:8} {9:8} {10:8}".format(c1.value, c2.value, c3.value, c4.value, c5.value, c6.value, c7.value, c8.value,
#                                c9.value, c10.value, c11.value)
#
# for row in sheet.iter_rows(cells):
#     for cell in row:
#         cells.append(cell.value)
#     print("Number of values: {0}".format(len(values)))
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



#
# import numpy as np
# def extract_data(filename):
#
#     #array to hold the labels and feature vectors.
#     labels = []
#     fvecs = []
#
#     #iterate over the rows, split the label from the features
#     #convert labels to integers and features to floats
#     for line in file(filename):
#         row = line.split(',')
#         labels.append(int(row[0]))
#         fvecs.append([float(x) for x in row[1:2]])

    #convert the array of float arrays into a numpy float matrix
    # fvecs_np = np.matrix(fvecs).astype(np.float32)
    #
    # #convert the array of int labels into a numpy array
    # labels_np = np.array(labels).astype(dtype=np.uint8)

    #convert the int numpy array into a one-hot matrix
  #  labels_onehot = (np.arange(NUM_LABELS) == labels_np[:, None]).astype(np.float32))
#