import csv
def tip(x):
    try:
        if int(x):
            x=int(x)
            return (x)
    except:
        try:
            if float(x):
                x=float(x)
                return (x)
        except:
            try:
                if x=='':
                    return(None)
                elif x=='True' or x=='False':
                    return bool(x)
                else:
                    return(str(x))
            except:
                return(x)
def count(x,znak,y):
    x=tip(x)
    y=tip(y)
    if type(x)==int and type(y)==int:
        if znak=='сумма':
            return int(x)+int(y)
        elif znak=='разность':
            return int(x)-int(y)
        elif znak=='умножение':
            return int(x) * int(y)
        else:
            if y != 0:
                return x // y
            else:
                assert ZeroDivisionError, 'Деление на ноль запрещено'
    elif (type(x)==int or type(y)==int) and (type(x)==float or type(y)==float):
        if znak=='сумма':
            return float(x)+float(y)
        elif znak=='разность':
            return float(x)-float(y)
        elif znak=='умножение':
            return float(x) * float(y)
        else:
            if y != 0:
                return x // y
            else:
                assert ZeroDivisionError, 'Деление на ноль запрещено'
    elif type(x)==bool and type(y)==bool:
        if znak=='сумма':
            return bool(x)+bool(y)
        elif znak=='разность':
            return bool(x)-bool(y)
        elif znak=='умножение':
            return bool(x) * bool(y)
        else:
            if y!=False:
                return x//y
            else:
                assert False,'Деление на ноль запрещено'


#######################################################################################################################
def add(FileName,FirstColumnName=0,FirstDataName=0,SecondColumnName=0,SecondDataName=0):
    rez = []
    try:
        with open(FileName) as f:
            t = csv.reader(f, delimiter=';')
            for i in t:
                rez.append(i)
    except IOError as err:
        print('Файла не существует')
    '''НАХОЖДЕНИЕ ПЕРВОГО СТОЛБЦА'''
    NumberFirstColumn = -1
    if type(FirstColumnName) == str:
        for i in rez[0]:
            NumberFirstColumn += 1
            if i == FirstColumnName:
                break
    else:
        NumberFirstColumn = FirstColumnName
    '''НАХОЖДЕНИЕ ВТОРОГО СТОЛБЦА'''
    NumberSecondColumn = -1
    if type(SecondColumnName) == str:
        for i in rez[0]:
            NumberSecondColumn += 1
            if i == SecondColumnName:
                break
    else:
        NumberSecondColumn = SecondColumnName
    '''НАХОЖДЕНИЕ ЗНАЧЕНИЯ ПЕРВОГО СТОЛБЦА'''
    NumberFirstData = -1
    if type(FirstDataName) == str:
        for i in rez[NumberFirstColumn][i]:
            NumberFirstData += 1
            if i == FirstDataName:
                break
    else:
        NumberFirstData = FirstDataName
    '''НАХОЖДЕНИЕ ЗНАЧЕНИЯ ВТОРОГО СТОЛБЦА'''
    NumberSecondData = -1
    if type(SecondDataName) == str:
        for i in rez[NumberSecondColumn][i]:
            NumberSecondData += 1
            if i == SecondDataName:
                break
    else:
        NumberSecondData = SecondDataName
    # x=float(rez[NumberFirstData][NumberFirstColumn])+float(rez[NumberSecondData][NumberSecondColumn])
    x = count(rez[NumberFirstData][NumberFirstColumn],'сумма',rez[NumberSecondData][NumberSecondColumn])
    # print(type(rez[NumberFirstData][NumberFirstColumn]))
    p=[]
    # print(x)
    for i in range(len(rez[0])):
        if rez[0][i]!=FirstColumnName:
            # print(rez[NumberFirstData][FirstColumnName])
            # print(rez[0][i])
            p.append(None)
        else:
            p.append(x)
    # print(p)
    # print(rez)
    rez.append(p)
    # print(rez)
    with open(FileName, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        for i in range(len(rez)):
            writer.writerow(rez[i])
#######################################################################################################################

def sub(FileName,FirstColumnName=0,FirstDataName=0,SecondColumnName=0,SecondDataName=0):
    rez = []
    try:
        with open(FileName) as f:
            t = csv.reader(f, delimiter=';')
            for i in t:
                rez.append(i)
    except IOError as err:
        print('Файла не существует')
    '''НАХОЖДЕНИЕ ПЕРВОГО СТОЛБЦА'''
    NumberFirstColumn = -1
    if type(FirstColumnName) == str:
        for i in rez[0]:
            NumberFirstColumn += 1
            if i == FirstColumnName:
                break
    else:
        NumberFirstColumn = FirstColumnName
    '''НАХОЖДЕНИЕ ВТОРОГО СТОЛБЦА'''
    NumberSecondColumn = -1
    if type(SecondColumnName) == str:
        for i in rez[0]:
            NumberSecondColumn += 1
            if i == SecondColumnName:
                break
    else:
        NumberSecondColumn = SecondColumnName
    '''НАХОЖДЕНИЕ ЗНАЧЕНИЯ ПЕРВОГО СТОЛБЦА'''
    NumberFirstData = -1
    if type(FirstDataName) == str:
        for i in rez[NumberFirstColumn][i]:
            NumberFirstData += 1
            if i == FirstDataName:
                break
    else:
        NumberFirstData = FirstDataName
    '''НАХОЖДЕНИЕ ЗНАЧЕНИЯ ВТОРОГО СТОЛБЦА'''
    NumberSecondData = -1
    if type(SecondDataName) == str:
        for i in rez[NumberSecondColumn][i]:
            NumberSecondData += 1
            if i == SecondDataName:
                break
    else:
        NumberSecondData = SecondDataName
    '''ВЫЧИСЛЕНИЕ ЗНАЧЕНИЯ'''
    x = count(rez[NumberFirstData][NumberFirstColumn], 'разность', rez[NumberSecondData][NumberSecondColumn])
    # x=float(rez[NumberFirstData][NumberFirstColumn])-float(rez[NumberSecondData][NumberSecondColumn])
    # print(x)
    p=[]
    for i in range(len(rez[0])):
        if rez[0][i]!=FirstColumnName:
            # print(rez[NumberFirstData][FirstColumnName])
            # print(rez[0][i])
            p.append(None)
        else:
            p.append(x)
    # print(p)
    # print(rez)
    rez.append(p)
    # print(rez)
    with open(FileName, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        for i in range(len(rez)):
            writer.writerow(rez[i])
#######################################################################################################################

def mul(FileName,FirstColumnName=0,FirstDataName=0,SecondColumnName=0,SecondDataName=0):
    rez = []
    try:
        with open(FileName) as f:
            t = csv.reader(f, delimiter=';')
            for i in t:
                rez.append(i)
    except IOError as err:
        print('Файла не существует')
    '''НАХОЖДЕНИЕ ПЕРВОГО СТОЛБЦА'''
    NumberFirstColumn = -1
    if type(FirstColumnName) == str:
        for i in rez[0]:
            NumberFirstColumn += 1
            if i == FirstColumnName:
                break
    else:
        NumberFirstColumn = FirstColumnName
    '''НАХОЖДЕНИЕ ВТОРОГО СТОЛБЦА'''
    NumberSecondColumn = -1
    if type(SecondColumnName) == str:
        for i in rez[0]:
            NumberSecondColumn += 1
            if i == SecondColumnName:
                break
    else:
        NumberSecondColumn = SecondColumnName
    '''НАХОЖДЕНИЕ ЗНАЧЕНИЯ ПЕРВОГО СТОЛБЦА'''
    NumberFirstData = -1
    if type(FirstDataName) == str:
        for i in rez[NumberFirstColumn][i]:
            NumberFirstData += 1
            if i == FirstDataName:
                break
    else:
        NumberFirstData = FirstDataName
    '''НАХОЖДЕНИЕ ЗНАЧЕНИЯ ВТОРОГО СТОЛБЦА'''
    NumberSecondData = -1
    if type(SecondDataName) == str:
        for i in rez[NumberSecondColumn][i]:
            NumberSecondData += 1
            if i == SecondDataName:
                break
    else:
        NumberSecondData = SecondDataName
    '''ВЫЧИСЛЕНИЕ ЗНАЧЕНИЯ'''
    x = count(rez[NumberFirstData][NumberFirstColumn], 'умножение', rez[NumberSecondData][NumberSecondColumn])
    # x=float(rez[NumberFirstData][NumberFirstColumn])*float(rez[NumberSecondData][NumberSecondColumn])
    # print(x)
    p=[]
    for i in range(len(rez[0])):
        if rez[0][i]!=FirstColumnName:
            # print(rez[NumberFirstData][FirstColumnName])
            # print(rez[0][i])
            p.append(None)
        else:
            p.append(x)
    # print(p)
    # print(rez)
    rez.append(p)
    # print(rez)
    with open(FileName, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        for i in range(len(rez)):
            writer.writerow(rez[i])

#######################################################################################################################

def div(FileName,FirstColumnName=0,FirstDataName=0,SecondColumnName=0,SecondDataName=0):
    rez = []
    try:
        with open(FileName) as f:
            t = csv.reader(f, delimiter=';')
            for i in t:
                rez.append(i)
    except IOError as err:
        print('Файла не существует')
    '''НАХОЖДЕНИЕ ПЕРВОГО СТОЛБЦА'''
    NumberFirstColumn = -1
    if type(FirstColumnName) == str:
        for i in rez[0]:
            NumberFirstColumn += 1
            if i == FirstColumnName:
                break
    else:
        NumberFirstColumn = FirstColumnName
    '''НАХОЖДЕНИЕ ВТОРОГО СТОЛБЦА'''
    NumberSecondColumn = -1
    if type(SecondColumnName) == str:
        for i in rez[0]:
            NumberSecondColumn += 1
            if i == SecondColumnName:
                break
    else:
        NumberSecondColumn = SecondColumnName
    '''НАХОЖДЕНИЕ ЗНАЧЕНИЯ ПЕРВОГО СТОЛБЦА'''
    NumberFirstData = -1
    if type(FirstDataName) == str:
        for i in rez[NumberFirstColumn][i]:
            NumberFirstData += 1
            if i == FirstDataName:
                break
    else:
        NumberFirstData = FirstDataName
    '''НАХОЖДЕНИЕ ЗНАЧЕНИЯ ВТОРОГО СТОЛБЦА'''
    NumberSecondData = -1
    if type(SecondDataName) == str:
        for i in rez[NumberSecondColumn][i]:
            NumberSecondData += 1
            if i == SecondDataName:
                break
    else:
        NumberSecondData = SecondDataName
    '''ВЫЧИСЛЕНИЕ ЗНАЧЕНИЯ'''
    print(rez[NumberFirstData][NumberFirstColumn],rez[NumberSecondData][NumberSecondColumn])
    x = count(rez[NumberFirstData][NumberFirstColumn], 'деление', rez[NumberSecondData][NumberSecondColumn])
    # x=float(rez[NumberFirstData][NumberFirstColumn])//float(rez[NumberSecondData][NumberSecondColumn])
    print(x)
    p=[]
    for i in range(len(rez[0])):
        if rez[0][i]!=FirstColumnName:
            # print(rez[NumberFirstData][FirstColumnName])
            # print(rez[0][i])
            p.append(None)
        else:
            p.append(x)
    print(p)
    print(rez)
    rez.append(p)
    print(rez)
    with open(FileName, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        for i in range(len(rez)):
            writer.writerow(rez[i])

#######################################################################################################################

def eq(FileName,by_number_one=0,by_number_two=0):
    rez = []
    bool_list=[]
    try:
        with open(FileName) as f:
            t = csv.reader(f, delimiter = ';')
            for i in t:
                rez.append(i)
            # return rez[start:stop]
    except IOError as err:
        print('Файла не существует')
    n1=-1
    if type(by_number_one)==str:
        for i in rez[0]:
            n1+=1
            if i==by_number_one:
                break
    else:
        n1=by_number_one
    n2 = -1
    if type(by_number_two) == str:
        for i in rez[0]:
            n2 += 1
            if i == by_number_two:
                break
    else:
        n2 = by_number_two
    for i in range(1,len(rez)):
        rez[i][n1]=tip(rez[i][n1])
        rez[i][n2]=tip(rez[i][n2])
        bool_list.append(rez[i][n1]==rez[i][n2])
    print(bool_list)
#(==), gr (&gt;), ls (&lt;), ge (&gt;=), le (&lt;=), ne (==),
def ne(FileName,by_number_one=0,by_number_two=0):
    rez = []
    bool_list=[]
    try:
        with open(FileName) as f:
            t = csv.reader(f, delimiter = ';')
            for i in t:
                rez.append(i)
            # return rez[start:stop]
    except IOError as err:
        print('Файла не существует')
    n1=-1
    if type(by_number_one)==str:
        for i in rez[0]:
            n1+=1
            if i==by_number_one:
                break
    else:
        n1=by_number_one
    n2 = -1
    if type(by_number_two) == str:
        for i in rez[0]:
            n2 += 1
            if i == by_number_two:
                break
    else:
        n2 = by_number_two
    for i in range(1,len(rez)):
        rez[i][n1]=tip(rez[i][n1])
        rez[i][n2]=tip(rez[i][n2])
        bool_list.append(rez[i][n1]!=rez[i][n2])
    print(bool_list)

def le(FileName,by_number_one=0,by_number_two=0):
    rez = []
    bool_list=[]
    try:
        with open(FileName) as f:
            t = csv.reader(f, delimiter = ';')
            for i in t:
                rez.append(i)
            # return rez[start:stop]
    except IOError as err:
        print('Файла не существует')
    n1=-1
    if type(by_number_one)==str:
        for i in rez[0]:
            n1+=1
            if i==by_number_one:
                break
    else:
        n1=by_number_one
    n2 = -1
    if type(by_number_two) == str:
        for i in rez[0]:
            n2 += 1
            if i == by_number_two:
                break
    else:
        n2 = by_number_two
    for i in range(1,len(rez)):
        rez[i][n1]=tip(rez[i][n1])
        rez[i][n2]=tip(rez[i][n2])
        bool_list.append(rez[i][n1]<=rez[i][n2])
    print(bool_list)



def gr(FileName,by_number_one=0,by_number_two=0):
    rez = []
    bool_list=[]
    try:
        with open(FileName) as f:
            t = csv.reader(f, delimiter = ';')
            for i in t:
                rez.append(i)
            # return rez[start:stop]
    except IOError as err:
        print('Файла не существует')
    n1=-1
    if type(by_number_one)==str:
        for i in rez[0]:
            n1+=1
            if i==by_number_one:
                break
    else:
        n1=by_number_one
    n2 = -1
    if type(by_number_two) == str:
        for i in rez[0]:
            n2 += 1
            if i == by_number_two:
                break
    else:
        n2 = by_number_two
    for i in range(1,len(rez)):
        rez[i][n1]=tip(rez[i][n1])
        rez[i][n2]=tip(rez[i][n2])
        bool_list.append(rez[i][n1]>rez[i][n2])
    print(bool_list)

def ls(FileName,by_number_one=0,by_number_two=0):
    rez = []
    bool_list=[]
    try:
        with open(FileName) as f:
            t = csv.reader(f, delimiter = ';')
            for i in t:
                rez.append(i)
            # return rez[start:stop]
    except IOError as err:
        print('Файла не существует')
    n1=-1
    if type(by_number_one)==str:
        for i in rez[0]:
            n1+=1
            if i==by_number_one:
                break
    else:
        n1=by_number_one
    n2 = -1
    if type(by_number_two) == str:
        for i in rez[0]:
            n2 += 1
            if i == by_number_two:
                break
    else:
        n2 = by_number_two
    for i in range(1,len(rez)):
        rez[i][n1]=tip(rez[i][n1])
        rez[i][n2]=tip(rez[i][n2])
        bool_list.append(rez[i][n1]<rez[i][n2])
    print(bool_list)


def ge(FileName,by_number_one=0,by_number_two=0):
    rez = []
    bool_list=[]
    try:
        with open(FileName) as f:
            t = csv.reader(f, delimiter = ';')
            for i in t:
                rez.append(i)
            # return rez[start:stop]
    except IOError as err:
        print('Файла не существует')
    n1=-1
    if type(by_number_one)==str:
        for i in rez[0]:
            n1+=1
            if i==by_number_one:
                break
    else:
        n1=by_number_one
    n2 = -1
    if type(by_number_two) == str:
        for i in rez[0]:
            n2 += 1
            if i == by_number_two:
                break
    else:
        n2 = by_number_two
    for i in range(1,len(rez)):
        rez[i][n1]=tip(rez[i][n1])
        rez[i][n2]=tip(rez[i][n2])
        # print(rez[i][n1],rez[i][n2])
        bool_list.append(rez[i][n1]>=rez[i][n2])
    print(bool_list)



def filter_rows(FileName,bool_list,copy_table=False):
    rez = []
    try:
        with open(FileName) as f:
            t = csv.reader(f, delimiter = ';')
            for i in t:
                rez.append(i)
            # return rez[start:stop]
    except IOError as err:
        print('Файла не существует')
    res=[]
    for i in range(len(bool_list)):
        if bool_list[i]:
            res.append(rez[i])
    data=res[::]
    if copy_table:
        with open(copy_table, mode="w", encoding='utf-8') as w_file:
            names = data[0]
            file_writer = csv.DictWriter(w_file, delimiter=";",
                                         lineterminator="\r", fieldnames=names)
            file_writer.writeheader()
            stroki = len(data[1:])
            for g in range(1, stroki + 1):
                datat = data[g]
                rez = {}
                j = 0
                for i in names:
                    rez[i] = datat[j]
                    j += 1
                file_writer.writerow(rez)
                rez = {}
    else:
        with open(FileName, mode="w", encoding='utf-8') as w_file:
            names = data[0]
            file_writer = csv.DictWriter(w_file, delimiter=";",
                                         lineterminator="\r", fieldnames=names)
            file_writer.writeheader()
            stroki = len(data[1:])
            for g in range(1, stroki + 1):
                datat = data[g]
                rez = {}
                j = 0
                for i in names:
                    rez[i] = datat[j]
                    j += 1
                file_writer.writerow(rez)
                rez = {}
# def eq(FileName,by_number_one=0,by_number_two=0):
#     rez = []
#     try:
#         with open(FileName) as f:
#             t = csv.reader(f, delimiter = ';')
#             for i in t:
#                 rez.append(i)
#             # return rez[start:stop]
#     except IOError as err:
#         print('Файла не существует')
#     n1=-1
#     if type(by_number_one)==str:
#         for i in rez[0]:
#             n1+=1
#             if i==by_number_one:
#                 break
#     else:
#         n1=by_number_one
#     n2 = -1
#     if type(by_number_two) == str:
#         for i in rez[0]:
#             n2 += 1
#             if i == by_number_two:
#                 break
#     else:
#         n2 = by_number_two
#     for i in range(1,len(rez)):
#         rez[i][n]=type(rez[i][n])
#     with open('filesetcolumntypes.csv','w',newline='') as f:
#         writer=csv.writer(f,delimiter=';')
#         for i in range(len(rez)):
#             # print(rez[i])
#             writer.writerow(rez[i])

# print(tip('True'))