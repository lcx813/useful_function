#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 10:42:07 2017

@author: cheng-xili
"""

from xlrd import open_workbook
import csv
 
NUM = 4
filename = 'filename'
wb = open_workbook(filename+str(NUM)+'.xlsx')


 
for i in range(4, 8):
    sheet = wb.sheet_by_index(i)
    print(sheet.name)
    with open("data/%s"%(sheet.name.replace(" ",""))+"_"+str(NUM)+".csv" , "w") as file:
        writer = csv.writer(file, delimiter = ",")
        print(sheet, sheet.name, sheet.ncols, sheet.nrows)
 
        header = [cell.value for cell in sheet.row(0)]
        writer.writerow(header)
 
        for row_idx in range(1, sheet.nrows):
            row = [int(cell.value) if isinstance(cell.value, float) else cell.value
                   for cell in sheet.row(row_idx)]
            writer.writerow(row) 