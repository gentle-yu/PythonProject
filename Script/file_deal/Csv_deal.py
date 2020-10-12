import csv
from urllib.request import urlretrieve 
import chardet

def convert(file_name,new_file_name):
    with open(file_name,'rt',encoding='GB2312') as f:
        reader = csv.reader(f)
        header = next(reader)
        print(header)

        with open(new_file_name,'wt',encoding='utf-8') as wf:
            writer = csv.writer(wf)
            writer.writerow(header)
            for row in reader:
                if row[0] > '2016-01-01' and int(row[11]) > 500000:
                    writer.writerow(row)
            print('************ end')


# 爬取文件
url = 'http://quotes.money.163.com/service/chddata.html?code=1000001&start=20150104&end=20160108'
urlretrieve(url, '/Script/file_deal/Csv_deal.csv')
convert('/Script/file_deal/Csv_deal.csv', '/Script/file_deal/Csv_deal_result.csv')