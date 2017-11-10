from openpyxl import utils
from openpyxl import workbook
from openpyxl import load_workbook
import csv

ofile = open('/home/troy/Downloads/rtc_vehicles.csv', "wb")
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
header = []
header.append('Date')
header.append('KM Covered')
header.append('Amount$')
writer.writerow(header)
# Read in excel data
wb = load_workbook('/home/troy/Downloads/HiaceBusPOL2015.xlsx', data_only=True)

startRow = 0
endRow = 0
startCol = 0
endCol = 0

for sheet in wb.worksheets:
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