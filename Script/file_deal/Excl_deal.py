import xlrd,xlwt
from xlutils.copy import copy as xl_copy


# book = xlrd.open_workbook("d:/yyc/script/test/file_deal/Excl_deal.xls")

'''
print(book.sheets())

# 读取第一张sheet
sheet0 = book.sheet_by_index(0)

print(sheet0.nrows) #查看行数量
print(sheet0.ncols) # 查看列数量

# 访问cell 并返回类型+value
print(sheet0.cell(0,0)) 

# 返回类型（1代表文本 2代表数字）
print(sheet0.cell(0,0).ctype)
print(sheet0.cell(1,1).ctype)

# 返回value 
print(sheet0.cell(0,0).value)

# 访sheet的行,行号从0开始
print(sheet0.row(0))

# #增加或修改一个cell(未写进文件,需save)
print(sheet0.cell(1,1))
sheet0.put_cell(1,1,2,100,None)
print(sheet0.cell(1,1))

# 构造book
#wbook = xlwt.Workbook()

# 复制book
wbook = xl_copy(book)

# 添加一个sheet
sheet1 = wbook.add_sheet('test02')

# write (行，列，值)
sheet1.write(0,0,"yyc")
print(sheet1.row(0))

# 保存
wbook.save(""d:/yyc/script/test/file_deal/Excl_deal.xls"") 
'''

'''
# 求和
sheet2 = book.sheet_by_index(0)
cols = sheet2.ncols

sheet2.put_cell(0,cols,1,'总分',None)
for row in range(1,sheet2.nrows):
    grade = sum(sheet2.row_values(row,1))
    sheet2.put_cell(row,cols,2,grade,None)

wbook = xlwt.Workbook()

# 创建一张临时表
wsheet = wbook.add_sheet("sheet")

# 将修改过的sheet值赋给临时表
for r in range(sheet2.nrows):
    for c in range(sheet2.ncols):
        wsheet.write(r,c,sheet2.cell(r,c).value)
wbook.save("d:/yyc/script/test/file_deal/Excl_deal.xls")
'''

class Compare_sheets():
    def __init__(self,sheet1,sheet2):
        self.sheet1 = sheet1
        self.sheet2 = sheet2
    
    def __sheet_to_set(self,sheet):
        tmpset = set()
        for row in range(1,sheet.nrows):
            info_tuple = tuple(sheet.row_values(row))
            tmpset.add(info_tuple)
        return tmpset

    def __compare_sets(self,set1,set2):
        print("sheet1中不同与sheet2的元素有：",set1-set2)
        print("sheet2中不同与sheet1的元素有：",set2-set1)

    def go(self):
        set1 = self.__sheet_to_set(self.sheet1)
        set2 = self.__sheet_to_set(self.sheet2)
        self.__compare_sets(set1,set2)

rbook = xlrd.open_workbook("/Script/file_deal/Excl_deal.xls")
sheet1 = rbook.sheet_by_index(0)
sheet2 = rbook.sheet_by_index(1)
Compare = Compare_sheets(sheet1,sheet2)
Compare.go()