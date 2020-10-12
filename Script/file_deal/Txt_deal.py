'''
#文本附加模式：在源文件末添加文本
with open('d:/yyc/script/test/file_deal/Txt_deal.txt','at',encoding='utf-8') as f:
    print(f.readable())
    print(f.writable())
    f.write('abcdefg')

with open('d:/yyc/script/test/file_deal/Txt_deal.txt','r',encoding='utf-8') as rf:
    print(rf.read())
'''

'''
#文本读写w+t:该模式下写会将源文件内容擦掉并写入新内容
with open('d:/yyc/script/test/file_deal/Txt_deal.txt','w+t',encoding='utf-8') as f:
    #指针位于文件首
    print(f.tell())
    原始内容被擦掉
    print(f.read())
    
    f.write('higklmn')
    f.seek(0)
    print(f.read())
'''

'''
#文本读写a+t:该模式下初始指针位于文件尾
with open('d:/yyc/script/test/file_deal/Txt_deal.txt','a+t',encoding='utf-8') as f:
    f.write('123456')
    print(f.read())
    f.seek(0)
    print(f.read())
'''

#文本读写r+t:初始指针位于文件头，源文件内容未擦除，进行覆盖写；读的话严格按照指针位置进行读
with open('/Script/file_deal/Txt_deal.txt', 'r+t', encoding='utf-8') as f:
    # print(f.read())
    f.write('hahahahahaha')
    # print(f.tell())

with open('/Script/file_deal/Txt_deal.txt', 'r', encoding='utf-8') as rf:
    print(rf.read())