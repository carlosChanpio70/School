import os,struct

path = os.path.join(os.path.dirname(__file__), 'vendas.bin')

def binary_to_venda(binary):
    return [struct.unpack('i',binary[:4])[0],struct.unpack('f', binary[4:8])[0], binary.decode('latin-1')[8:].strip()]

def venda_to_binary(venda):
    return (struct.pack('i', venda[0]) + struct.pack('f', venda[1]) + bytes(venda[2].ljust(10), 'latin-1'))

def adicionar_venda(venda_in):
    f = open(path, 'rb')
    j = 0
    for i in range(len(f.read())//18):
        f.seek(i*18)
        b = f.read(18)
        venda = binary_to_venda(b)
        if venda == None:
            j = i
            break
        elif venda[0] == venda_in[0]:
            j = None
            break
        elif venda[2][:2] > venda_in[2][:2]:
            j = None
            break

    if j is None:
        print('Ja existe')
    else:
        f = open(path, 'ab')
        f.seek(j*18)
        f.write(venda_to_binary(venda_in))
        f.close()
        print('Gravado')

def locate_venda(venda_in,type):
    f = open(path, 'rb')
    j = None
    for i in range(len(f.read())//18):
        f.seek(i*18)
        venda = binary_to_venda(f.read(18))
        if venda == None:
            print('Nao existe')
            j = None
            break
        elif type == 0:
            if venda[0] == venda_in[0]:
                j = i
                break
        elif type == 1:
            if venda[0] == venda_in[0] and venda[2][:2] == venda_in[2][:2]:
                j = i
                break
    f.close()
    return j

def excluir_venda(vendedor):
    j = locate_venda(vendedor,0)
    if j is None:
        print('Nao existe')
    else:
        f = open(path, 'rb+')
        f.seek((j+1)*18)
        rd = f.read()
        f.seek(j*18)
        f.write(rd)
        f.close()
        print('Excluido')

def alterar_venda(venda_in):
    j = locate_venda(venda_in,1)
    if j is None:
        print('Nao existe')
    else:
        f = open(path, 'rb+')
        f.seek(j*18)
        f.write(venda_to_binary(venda_in))
        f.close()
        print('Alterado')

def main():
    venda = [None, None, None]
    while True:
        print('1 - Criar o arquivo de dados')
        print('2 - Incluir um determinado vendedor no arquivo')
        print('3 - Excluir um determinado vendedor no arquivo')
        print('4 - Alterar o valor total da venda de um determinado vendedor de um determinado mês')
        print('5 - Imprimir os registros na saída padrão')
        print('6 - Consultar o vendedor com maior valor da venda')
        print('7 - Finalizar o programa')
        op = int(input('Escolha uma opção: '))
        if op == 1:
            pass
        elif op == 2:
            venda[0] = int(input('Codigo do vendedor: '))
            venda[1] = float(input('Valor da venda: '))
            venda[2] = input('Mes/Ano: ')
            adicionar_venda(venda)
        elif op == 3:
            excluir_venda(int(input('Codigo do vendedor: ')))
        elif op == 4:
            venda[0] = int(input('Codigo do vendedor: '))
            venda[2] = input('Data da venda: ')
            venda[1] = float(input('Novo valor da venda: '))
            alterar_venda(venda)
        elif op == 5:
            pass
        elif op == 6:
            pass
        elif op == 7:
            break

main()

#* Fazer um programa denominado de venda.py que manipule um arquivo binário contendo registros descritos pelos seguintes campos:

#*   codigo_vendedor, valor_da_venda e mes_ano

#* Codigo_vendedor: integer
#* Valor_venda : float
#* mes_ano : string da forma (mm/aaaa)
#* Entrada de Dados

#* O programa vendas.py deverá apresentar uma tela com as opções disponíveis e executar cada opção.
#* A manipulação do arquivo em questão é feita através da execução das operações disponibilizadas pelo seguinte menu:

#* 1 Criar o arquivo de dados;
#* 2 Incluir um determinado vendedor no arquivo;
#* 3 Excluir um determinado vendedor no arquivo;
#* 4 Alterar o valor total da venda de um determinado vendedor de um determinado mês;
#* 5 Imprimir os registros na saída padrão;
#* 6 Consultar o vendedor com maior valor da venda
#* 7 Finalizar o programa.

#* Não deve existir mais de um registro no arquivo com mesmos valores nos campos código_vendedor e mes.