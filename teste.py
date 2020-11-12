
filepath = 'arquivo_teste.txt'
with open(filepath, 'w') as fp:
    fp.write('teste1\n')
    fp.write('teste2\n')
    fp.write('teste3\n')

with open(filepath, 'r+') as fp:
    # fp.write('teste4')
    print(fp.readline())
    print(fp.tell())
    # fp.seek(fp.tell())
    fp.write('teste4')
