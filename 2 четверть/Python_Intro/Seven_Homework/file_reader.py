# data = open(f'data.{flag}')
def read_data(d):
    data = open(f'data.txt', 'r')
    s = data.read()
    st = s.split('\n')
    list = []
    for i in st:
        list.append(i.split())
    print(d)