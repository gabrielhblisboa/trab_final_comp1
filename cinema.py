import random as rnd

def menuprincipal():
    print('1 - Ver sala/Reservar assento')
    print('2 - Apagar reservas')
    print('3 - Carregar salas salvas')
    print('4 - Sortear assentos promocionais')
    print('5 - Sair')


def mostrarSalas(nomeArq):
    '''
    A função lê o arquivo e imprime as salas disponíveis.
    '''
    salas = open(nomeArq, 'r')
    sala = salas.readline()
    i = 1
    print('Salas disponiveis:')
    while sala != '':
        print(i, end='; ')
        i += 1
        sala = salas.readline()
    print()
    salas.close()
    
    # Número de salas é igual a i - 1 pois o i é
    # contado mais uma vez antes de sair do while
    
    nSalas = i - 1
    return nSalas


def escolherSala(nomeArq):
    '''
    Função que interage com o usuário para que ele escolha
    a sala. Após a escolha da sala, ela é transformada de
    string para lista de listas.
    '''
    # nSalas = número de salas
    
    nSalas = mostrarSalas(nomeArq)
    while True:
        s = input('Digite o numero da sala: ')
        try:
            s = int(s)
            if s < 0 or s > nSalas:
                raise ValueError 
        except ValueError:
            print('Valor invalido. Tente novamente.')
        else:
            break
    salas = open(nomeArq, 'r')
    sala = salas.readline()
    i = 1
    while sala != '':
        if i == s:
            sala = eval(sala)
            print(sala)
            break
        i += 1
        sala = salas.readline()
    print('1 = assento reservado')
    print('2 = assento promocional')
    salas.close()
    
    # i -> indica o número da sala e a posição da
    # sala dentro do arquivo
    
    return sala, i


def reservarAssento(nomeArq):
    '''
    A função interage com o usuário para que ele digite o
    número da fileira e do assento que ele deseja
    reservar. O valor do assento passa de 0
    (assento livre) para 1 (assento reservado). A sala 
    (lista de listas) é modificada e salva no arquivo.
    '''
    sala, i = escolherSala(nomeArq)
    op = input('Deseja reservar um assento? s/n: ')
    while op != 'n':
        if op == 's':
            while True:
                fileira = input('Digite o numero da fileira: ')
                try:
                    fileira = int(fileira)
                    if fileira <= 0 or fileira > len(sala):
                        raise ValueError
                except ValueError:
                    print('Valor invalido. Tente novamente.')
                else:
                    break
            while True:
                assento = input('Digite o numero do assento: ')
                try:
                    assento = int(assento)
                    if assento <= 0 or assento > len(sala[fileira-1]):
                        raise ValueError
                except ValueError:
                    print('Valor invalido. Tente novamente.')
                else:
                    break
            if sala[fileira-1][assento-1] != 0:
                print('Assento já reservado.')
            else:
                sala[fileira-1][assento-1] = 1
                salvarSalas(nomeArq, sala, i)
                print('Assento reservado com sucesso!')
                print(sala)
        else:
            print('Opcao invalida. Tente novamente.')
        op = input('Deseja reservar outro assento? s/n: ')


def carregarSalas():
    '''
    Função que carrega um determinado arquivo salvo
    '''
    nomeArq = input('Digite o nome do arquivo'+\
                    '(ex: salas.txt): ')
    try:
        salas = open(nomeArq, 'r')
    except FileNotFoundError:
        print('Arquivo nao encontrado.')
    else:
        for sala in salas:
            print(sala)
        salas.close()
        return nomeArq


def salvarSalas(nomeArq, sala, linha):
    '''
    Função que salva no arquivo as salas modificadas 
    sala -> lista de listas que representa uma sala
    linha -> indica em qual linha está a sala que tem
             que ser modificada
    '''
    salas = open(nomeArq, 'r+')
    n = 1
    l = salas.readline()
    pos = 0
    while l != '':
        if n == linha:
            salas.seek(pos)
            salas.write(str(sala))
            salas.write('\n')
            break
        n += 1
        pos = salas.tell()
        l = salas.readline()
    salas.close()


def apagarReservas(nomeArq):
    '''
    Função que apaga todas as reservas de todas
    as salas
    '''
    salas = open(nomeArq, 'r')
    salas_w = open(nomeArq, 'r+')
    
    # pos -> vai servir para mover o cursor pro início de
    # cada linha na hora de sobrescrevê-la
    
    pos = salas.tell()
    sala = salas.readline()
    while sala != '':
        sala = eval(sala)
        for f_pos in range(len(sala)):
            fileira = sala[f_pos]
            for a_pos in range(len(fileira)):
                assento = fileira[a_pos]
                if assento != 0:
                    sala[f_pos][a_pos] = 0         
        salas_w.seek(pos)
        salas_w.write(str(sala))
        pos = salas.tell()
        sala = salas.readline()
    print('Reservas apagadas com sucesso!')
    print()
    salas.close()
    salas_w.close()


def sortearAssento(nomeArq):
    '''
    Função que sorteia um determinado número de assentos
    promocionais. A função interage com o usuário para
    determinar quantos assentos serão sorteados, e verifica
    se há assentos disponíveis para fazer o sorteio. Os
    assentos promocionais são marcados com o numero 2.
    '''
    sala, linha = escolherSala(nomeArq)
    op = 's'
    while op != 'n': 
        while True:
            numSort = input('Digite o numero de assentos que deseja sortear: ')
            try:
                numSort = int(numSort)
                if numSort <= 0:
                    raise ValueError
            except ValueError:
                print('Valor invalido. Tente novamente.')
            else:
                break   
        somaTotal = 0
        for f in sala:
            somaFileira = 0
            for assento in f:
                if assento == 0:
                    somaFileira += 1
            somaTotal += somaFileira
        if somaTotal < numSort:
            print('Esta sala possui %d assentos disponiveis.'%(somaTotal))
            print('Nao foi possivel fazer o sorteio.')
            while True:
                op = input('Deseja realizar um novo sorteio? (s/n): ')
                if op == 'n':
                    return None
                elif op != 's' and op != 'n':
                    print('Opcao invalida. Tente novamente.')
                else:
                    break
        else:
            break        
    n = 1
    while n <= numSort:
        
        # A cada iteração é sorteada uma fileira e um
        # assento, e o sorteio só é considerado se o assento
        # estiver livre.
        
        fileira = rnd.randint(0, len(sala)-1)
        assento = rnd.randint(0, len(sala[fileira])-1)
        if sala[fileira][assento] == 0:
            sala[fileira][assento] = 2
        else:
            continue
        n += 1
    print(sala)
    salvarSalas(nomeArq, sala, linha)


def main():
    while True:
    
        # A função carregarSalas fica em loop até o
        # usuário digitar um nome de arquivo válido.
        
        salas = carregarSalas()
        if salas is not None:
            break
    while True:
        menuprincipal()
        op = input('Digite uma das opcoes acima: ')
        if op == '1':
            reservarAssento(salas)
        elif op == '2':
            apagarReservas(salas)
        elif op == '3':

            # Caso o nome do arquivo digitado não seja
            # encontrado, o arquivo que já estava sendo
            # utilizado é mantido
            
            tmpSala = carregarSalas()
            if tmpSala is not None:
                salas = tmpSala
        elif op == '4':
            sortearAssento(salas)
        elif op == '5':
            break
        else:
            print('Opcao invalida. Tente novamente.')


if __name__ == '__main__':

    main()