'''
Created on 26/02/2014

@author: The Forsaken
'''

# Write an XLS file with a single worksheet, containing
# a heading row and some rows of data.

import xlwt
import datetime
ezxf = xlwt.easyxf

class writeXls:

    def __init__(self):
        self.heading_xf = None
        self.kind_to_xf_map = None
        self.data_xfs = None

    def write_xls(self, file_name, sheet_name, headings, data, kinds):
        self.setDefaultParams(headings, data, kinds)
        book = xlwt.Workbook(encoding="UTF-8")
        sheet = book.add_sheet(sheet_name)
        rowx = 0
        for colx, value in enumerate(headings):
            sheet.write(rowx, colx, value, self.heading_xf)
        sheet.set_panes_frozen(True) # frozen headings instead of split panes
        sheet.set_horz_split_pos(rowx+1) # in general, freeze after last heading row
        sheet.set_remove_splits(True) # if user does unfreeze, don't leave a split there
        for row in data:
            rowx += 1
            for colx, value in enumerate(row):
                #print "col ", colx, " - ", len(self.data_xfs)
                sheet.write(rowx, colx, value, self.data_xfs[colx])
        book.save(file_name)

    def setDefaultParams(self, hdngs, data, kinds):
        self.heading_xf = ezxf('font: bold on; align: wrap on, vert centre, horiz center')
        self.kind_to_xf_map = {
            'text': ezxf()
            }
        self.data_xfs = [self.kind_to_xf_map[k] for k in kinds]
        #wxls.write_xls('xlwt_easyxf_simple_demo.xls', 'Demo', hdngs, data, heading_xf, data_xfs)
