import csv
import re
martica=['1.1.1','1.2.1','1.3.2','1.4.2','2.5.2','2.6.1','2.7.1']
martica = ['1.1.1', '1.2.1', '1.3.1', '1.4.1', '1.5.2', '1.6.2', '1.7.1', '1.8.1', '1.9.1', '1.10.1', '1.11.4', '1.12.4', '1.13.4', '1.14.4', '1.15.4', '2.16.1', '2.17.1', '2.18.1', '2.19.1', '2.20.2', '2.21.2', '2.22.1', '2.23.1', '2.24.1', '2.25.1', '2.26.4', '2.27.4', '2.28.4', '2.29.4', '2.30.4', '3.31.3', '3.32.3', '3.33.3', '3.34.3', '3.35.2', '3.36.2', '3.37.3', '3.38.3', '3.39.3', '3.40.3', '3.41.3', '3.42.3', '4.43.1', '4.44.1', '4.45.2', '4.46.4', '4.47.4', '4.48.4', '4.49.4', '5.50.1', '5.51.1', '5.52.1', '5.53.1', '5.54.4', '5.55.4', '5.56.4', '5.57.4', '5.58.4', '5.59.4', '5.60.2', '50.61.2']
a = [[0] * (len(martica)+6) for i in range(len(martica)+6)]
for i in range(len(a[0][::])):
    a[0][i]=None
    a[1][i] = None
    a[2][i] = None                        #заполнение таблицы пустыми значениями
    a[3][i] = None
    a[4][i] = None
    a[5][i] = None
for i in range(len(a[::][0])):
    a[i][0]=None
    a[i][1]=None
    a[i][2]=None
    a[i][3]=None
    a[i][len(martica)+5]=None
    a[i][len(martica)+4]=None
for i in range(6,len(martica)+6):
    result = re.findall(r'\d+', martica[i - 6])
    a[i][0]=int(result[0])
    a[i][1]=int(result[1])
    a[i][2] = int(result[2])                  #ВВЕДЕНИЕ В МАССИВ САМИ ДАННЫЕ ПО ВЕРТИКАЛИ
for i in range(4,len(martica)+4):
    result=re.findall(r'\d+',martica[i - 4])
    a[0][i]=int(result[0])
    a[1][i] = int(result[1])
    a[2][i] = int(result[2])
for i in range(6,len(a[::][0])):
    for p in range(4,len(a[0][::])):
        if a[2][p]==a[i][2] and a[0][p]!=a[i][0]:
            a[i][p]=0.5
        if a[2][p]==a[i][2] and a[0][p]==a[i][0] and a[1][p]==a[i][1]:
            a[i][p]=0                                                                 #ЗАПОЛНЕНИЕ МАТРИЦЫ -1,1,0.5
        if a[0][p]==a[i][0] and a[1][p]<a[i][1]:
            a[i][p] = -1
        elif a[0][p]==a[i][0] and a[1][p]>a[i][1]:
            a[i][p] = 1
for t in a:
    print(t)
with open('matrica.csv','w',newline='') as f:
    writer=csv.writer(f,delimiter=';')                               #запись матрицы в файл
    for i in range(len(a)):
        writer.writerow(a[i])

count=[]
stanok=[]
for i in range(6,len(a[::][0])):
    for p in range(4,len(a[0][::])):
        if a[i][p]==1:
            count.append((a[i][1],a[1][p],1.0))       #поиск из матрицы операций, совпадающих по станкам, или идущих друг за другом
            # stanok.append(a[i][2])
            # stanok.append(a[2][p])
        if a[i][p]==0.5:
            count.append((a[i][1], a[1][p], 0.5))
            count.append((a[1][p], a[i][1], 0.5))
            stanok.append([a[1][p], a[i][1]])
            # stanok.append([a[1][p],a[i][1],a[2][p]])
print('находящиеся на одном станке номера тактов',stanok)
copy_count=count
# print(count)
operat=[]
znak=True
f=True
vhod_chisla=[]
operations=[]
count_of_links=[[0] for i in range(100)]
c=0
while f==True:
    for p in range(1,len(martica)+1):
        for i in range(len(count)):
            if count[i][1]==p and count[i][2]==1.0 or p in operat:
                znak=False
        if znak:
            operat.append(p)
            vhod_chisla.append(p)
            for j in range(len(count)):
                #print(count[j])
                if count[j][0]==p and count[j][2]==1.0:
                    # print(count[j])
                    c+=1
        count_of_links[p].append(c)
        c=0
        if len(operat)==len(martica):
            f=False
        znak=True
    for j in range(len(count)):
        # print(count[j])
        if count[j][0] in operat and count[j][2] == 1.0:
            count[j] = (0, 0, 0)
    operations.append(vhod_chisla)
    vhod_chisla=[]
# print(operat)
print(operations)
# result=''
# i=0
# while i!=len(operations):
#     if operations[i] in stanok:
#         if count_of_links[operations[i][0]]>count_of_links[operations[i][1]]:
#             operations[i][0]=0
#             print(operations)
#             count_of_links[operations[i][0]]=0
#             i-=1
#         elif count_of_links[operations[i][0]]<count_of_links[operations[i][1]]:
#             operations[i][1] = 0
#             print(operations)
#             count_of_links[operations[i][0]]=0
#             i-=1
#     else:
#         operations[i]=0
#         print(operations)
#     i+=1