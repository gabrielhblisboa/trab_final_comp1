def menuprincipal():
    print('1 - Ver sala')
    print('2 - Apagar reservas')
    print('3 - Carregar salas salvas')
    print('4 - Sortear assentos promocionais')
    print('5 - Sair')

def mostrarSalas(nomeArq):
    salas = open(nomeArq, 'r')
    sala = salas.readline()
    i = 1
    print('Salas disponiveis:')
    while sala != '':
        print(i, end='; ')
        i += 1
        sala = salas.readline()
    print()


def verSala(nomeArq):
    s = input('Digite o numero da sala: ')
    s = int(s)
    salas = open(nomeArq, 'r')
    sala = salas.readline()
    i = 1
    while sala != '':
        if i == s:
            print(sala)
            sala = eval(sala)
            break
        i += 1
        sala = salas.readline()
    print(sala)
    print('* = assento reservado')
    op = input('Deseja reservar um assento? s/n: ')
    while op != 'n':
        if op == 's':
            fileira = input('Digite o numero da fileira: ')
            try:
                fileira = int(fileira)
                if fileira <= 0:
                    raise ValueError
            except ValueError:
                print('Valor invalido. Tente novamente.')
                continue
            assento = input('Digite o numero do assento: ')
            try:
                assento = int(assento)
                if assento <= 0:
                    raise ValueError
            except ValueError:
                print('Valor invalido. Tente novamente.')
            else:
                if sala[fileira-1][assento-1] == '*':
                    print('Assento já reservado.')
                else:
                    sala[fileira-1][assento-1] = '*'
                    print(i)
                    salvarSalas(nomeArq, sala, i)
                    print('Assento reservado com sucesso!')
                    print(sala)
        else:
            print('Opcao invalida. Tente novamente.')
        op = input('Deseja reservar outro assento? s/n: ')



def carregarSalas():
    nomeArq = input('Digite o nome do arquivo'+\
                    '(ex: salas.txt): ')
    try:
        salas = open(nomeArq, 'r')
    except FileNotFoundError:
        print('Arquivo nao encontrado.')
    else:
        for sala in salas:
            print(sala)
        return nomeArq

def salvarSalas(nomeArq, sala, linha):
    salas = open(nomeArq, 'r+')
    n = 1
    l = salas.readline()
    while l != '':
        if n == linha:
            print('Entrei no if')
            print(linha)
            print(l)
            salas.seek(0)
            salas.write(str(sala))
            salas.write('\n')
            break
        n += 1
        l = salas.readline()
    salas.close()


def apagarReservas(nomeArq):
    salas = open(nomeArq, 'r+')
    salas.seek(0)
    for sala in salas:
        sala = eval(sala)
        print(sala)
        for fileira in sala:
            print(fileira)
            for p in range(len(fileira)):
                assento = fileira[p]
                print(assento)
                if assento == '*':
                    assento = p+1
        salas.write(str(sala))


def main():
    salas = 'salas.txt'
    while True:
        menuprincipal()
        op = input('Digite uma das opcoes acima: ')
        if op == '1':
            mostrarSalas(salas)
            verSala(salas)
        elif op == '2':
            apagarReservas(salas)
        elif op == '3':
            tmpSala = carregarSalas()
            if tmpSala is not None:
                salas = tmpSala
        elif op == '4':
            pass
        elif op == '5':
            break
        else:
            print('Opcao invalida. Tente novamente.')


if __name__ == '__main__':

    main()
