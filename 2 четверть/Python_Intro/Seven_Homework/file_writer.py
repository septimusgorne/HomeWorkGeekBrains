def write(flag, d):
    s = ' '.join(d)
    # if flag == 'txt':
    data = open(f'data.{flag}', 'a')
    data.write('\n' + s)
    # if flag == 'csv':
    #     data
        
