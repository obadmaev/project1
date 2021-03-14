import ForCsvFile
# def get_column_types(by_number=True):
#     with open(FileName,encoding='utf-8',):
# def get_rows_by_number(start, stop, copy_table=False):
#     with open('NewTablByNumber.csv',mode='w',encoding='utf-8') as f:
#         for i in range(start,stop):
def get_column(FileName):
    z, f = ForCsvFile.load_table(FileName)
    n = 0
    NameColumn = 'First Name'
    while z[n] != NameColumn:
        n += 1
    rez = []
    for i in f:
        rez.append(i[n])
    return rez