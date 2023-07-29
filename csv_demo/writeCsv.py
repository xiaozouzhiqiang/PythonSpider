import csv

def write_csv1():
    # 以字符串的形式写入
    head = ['id', 'name', 'age']
    values = [
        (1, "张三", 18),
        (2, "李四", 19),
        (3, "王五", 20)
    ]

    with open('writeCsv.scv', 'w', encoding='utf-8', newline='') as fp:
        write = csv.writer(fp)
        write.writerow(head)
        write.writerows(values)

def write_csv2():
    # 以字典的形式写入
    head = ['id', 'name', 'age']
    values = [
        {'id':1,'name':'张三','age':19},
        {'id':2,'name':'李四','age':19}
    ]
    with open('writeCsv2.scv','w',encoding='utf-8',newline="") as fp:
        writes = csv.DictWriter(fp,head)
        writes.writeheader()
        writes.writerows(values)

if __name__ == '__main__':
    write_csv1()
    write_csv2()
