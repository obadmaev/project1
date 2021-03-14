import csv
def save_table(FileName,data=''):
    with open(FileName, mode="w", encoding='utf-8') as w_file:
        if data=='':
            print('Введите названия столбцов через пробел')
            names = input().split(' ')
            file_writer = csv.DictWriter(w_file, delimiter=";",
                                         lineterminator="\r", fieldnames=names)
            file_writer.writeheader()
            print('Введите количество строк')
            try:
                stroki = int(input())
            except ValueError:
                print('Введите целое число строк')
                stroki = int(input())
            c = 1
            for g in range(stroki):
                print('Введите' ,c,'-ую строку')
                c+=1
                data = input().split(' ')
                if len(data) != len(names):
                    print('Неверный ввод, повторите попытку')
                    data = input().split(' ')
                rez = {}
                j = 0
                for i in names:
                    rez[i] = data[j]
                    j += 1
                file_writer.writerow(rez)
                print('Файл',FileName,'создан')
        else:
            names = data[0]
            file_writer = csv.DictWriter(w_file, delimiter=";",
                                         lineterminator="\r", fieldnames=names)
            file_writer.writeheader()
            stroki = len(data[1:])
            for g in range(1,stroki+1):
                datat = data[g]
                rez = {}
                j = 0
                for i in names:
                    rez[i] = datat[j]
                    j += 1
                file_writer.writerow(rez)
                rez = {}
def load_table(*FileName):
    rez = []
    for p in FileName:
        try:
            with open(p) as f:
                t = csv.reader(f, delimiter = ';')
                for i in t:
                    rez.append(i)
                # return rez[0], rez[1:]
        except IOError as err:
            print('Файла не существует')
    return rez[0], rez[1:]


def save_tables(*FileNames):
    max_rows=FileNames[-1]
    # print(max_rows)
    # # for p in FileNames:
    # #     print(p)
    rez = []
    for p in FileNames:
        if p!=max_rows:
            # print(p)
            try:
                with open(p) as f:
                    t = csv.reader(f, delimiter=';')
                    c=0
                    for i in t:
                        c+=1
                        if c<=max_rows:
                            rez.append(i)
            except IOError as err:
                print('Файла не существует')
    with open('SaveTables.csv','w',newline='') as f:
        writer=csv.writer(f,delimiter=';')
        for i in range(len(rez)):
            writer.writerow(rez[i])


def zapis(FileTxt,FileCsv):
    import re
    with open(FileTxt,mode='r',encoding='utf-8') as f:
        read = f.read()
    rez = re.findall(r'\w+:{0,1}',read)
    names=[]
    start=999
    finish=666
    for i in range(len(rez)):
        if ':' in rez[i]:
            if len(names)!=0:
                if finish==666:
                    finish=i
            names.append(rez[i][:-1])
            if start==999:
                start=i
    print(finish-start-1)
    data = [[] for i in range(finish-start-1)]
    for i in range(len(rez)):
        if ':' in rez[i]:
            j=0
            for q in range(i+1,i+finish-start):
                data[j].append(rez[q])
                j+=1
    print(data)
    print(names)
    with open(FileCsv, mode="w", encoding='utf-8') as w_file:
        file_writer = csv.DictWriter(w_file, delimiter=";",
                                     lineterminator="\r", fieldnames=names)
        file_writer.writeheader()
        stroki = len(data)
        for g in range(stroki):
            datat = data[g]
            rez = {}
            j = 0
            for i in names:
                rez[i] = datat[j]
                j += 1
            file_writer.writerow(rez)

