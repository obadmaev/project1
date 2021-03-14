import pickle
def save_table(FileName,data=''):
    with open(FileName,'wb') as f:
        pickle.dump(data,f)
def save_tables(*FileName):
    for p in FileName:
        print(p)
        with open(p, 'rb') as f:
            s=pickle.load(f)
        with open('SaveTables.pickle', 'ab') as f:
            pickle.dump(s, f)

def load_table(*FileName):
    for p in FileName:
        try:
            with open(p,'rb') as f:
                print(pickle.load(f))
        except IOError:
            print('Файла не существует')