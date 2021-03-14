# import csv
# import re
# spisok=['1.1.1','1.2.1','1.3.2','1.4.2','2.5.2','2.6.1','2.7.1']
# martica = ['1.1.1', '1.2.1', '1.3.1', '1.4.1', '1.5.2', '1.6.2', '1.7.1', '1.8.1', '1.9.1', '1.10.1', '1.11.4', '1.12.4', '1.13.4', '1.14.4', '1.15.4', '2.16.1', '2.17.1', '2.18.1', '2.19.1', '2.20.2', '2.21.2', '2.22.1', '2.23.1', '2.24.1', '2.25.1', '2.26.4', '2.27.4', '2.28.4', '2.29.4', '2.30.4', '3.31.3', '3.32.3', '3.33.3', '3.34.3', '3.35.2', '3.36.2', '3.37.3', '3.38.3', '3.39.3', '3.40.3', '3.41.3', '3.42.3', '4.43.1', '4.44.1', '4.45.2', '4.46.4', '4.47.4', '4.48.4', '4.49.4', '5.50.1', '5.51.1', '5.52.1', '5.53.1', '5.54.4', '5.55.4', '5.56.4', '5.57.4', '5.58.4', '5.59.4', '5.60.2', '5.61.2']
# a = [[0] * (len(martica)+6) for i in range(len(martica)+6)]
# for i in range(len(a[0][::])):
#     a[0][i]=None
#     a[1][i] = None
#     a[2][i] = None
#     a[3][i] = None
#     a[4][i] = None
#     a[5][i] = None
# for i in range(len(a[::][0])):
#     a[i][0]=None
#     a[i][1]=None
#     a[i][2]=None
#     a[i][3]=None
#     a[i][len(martica)+5]=None
#     a[i][len(martica)+4]=None
# for i in range(6,len(martica)+6):
#     result = re.findall(r'\d+', martica[i - 6])
#     print(result)
#     a[i][0] = int(result[0])
#     a[i][1] = int(result[1])
#     a[i][2] = int(result[2])                  #ВВЕДЕНИЕ В МАССИВ САМИ ДАННЫЕ ПО ВЕРТИКАЛИ
# for i in range(4,len(martica)+4):
#     result=re.findall(r'\d+',martica[i - 4])
#     print(result)
#     a[0][i] = int(result[0])
#     a[1][i] = int(result[1])
#     a[2][i] = int(result[2])
#     a[4][i] = int(result[1])
# for i in range(6,len(a[::][0])):
#     for p in range(4,len(a[0][::])):
#         if a[2][p]==a[i][2] and a[0][p]!=a[i][0]:
#             a[i][p]=0.5
#         if a[2][p]==a[i][2] and a[0][p]==a[i][0] and a[1][p]==a[i][1]:
#             a[i][p]=0                                                                 #ЗАПОЛНЕНИЕ МАТРИЦЫ -1,1,0.5
#         if a[0][p]==a[i][0] and a[1][p]<a[i][1]:
#             a[i][p] = -1
#         elif a[0][p]==a[i][0] and a[1][p]>a[i][1]:
#             a[i][p] = 1
# for t in a:
#     print(t)
# with open('matrica.csv','w',newline='') as f:
#     writer=csv.writer(f,delimiter=';')
#     for i in range(len(a)):
#         writer.writerow(a[i])
stash = ['1.1.1','1.2.1','1.3.2','1.4.2', '1.2.3', '1.6.1', '1.8.3', '1.6.4']
stash_oven={}
import re
for operarion in stash: # создание словаря стэша для печей (сколько на печь идет деталей)
        result = re.findall(r'\d+', operarion)
        if result[2] in stash_oven:
            stash_oven[result[2]] += 1
        else:
            stash_oven.update({result[2] : 1})
k=1

values_view = stash_oven.values()
value_iterator = iter(values_view)
first_value = next(value_iterator)
if len(stash_oven) > 1:
        for i in stash_oven.values():
            k *= i
        m = [[] for  i in range(k)]
        schet=0
        for i, j in stash_oven.items():
           try:
               schett=j_last//2
               print(schet)
           except:
               pass
           for t in range(len(stash)):
               result = re.findall(r'\d+', stash[t])
               print(stash[t])
               j_last=j
               print(schet)
               if result[2]==i:
                   for z in range(k // j):
                       
                       m[schet].append(stash[t])
                       schet += 1


for i in m:
    print(i)
