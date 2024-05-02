import os,struct

path = os.path.join(os.path.dirname(__file__), 'vendas.bin')

def binary_to_venda(binary):
    return [struct.unpack('i',binary[:4])[0],struct.unpack('f', binary[4:8])[0], binary.decode('latin-1')[8:].strip()]

def venda_to_binary(venda):
    return (struct.pack('i', venda[0]) + struct.pack('f', venda[1]) + bytes(venda[2].ljust(10), 'latin-1'))

def criar_arquivo():
    f = open(path, 'wb')
    f.close()
    print('Arquivo criado')

def adicionar_venda(venda_in):
    j = locate_venda(venda_in,1)
    print(j)
    if j is not None:
        f = open(path, 'ab')
        f.seek(j*18)
        f.write(venda_to_binary(venda_in))
        f.close()
        print('Gravado')

def locate_venda(venda_in, type):
    f = open(path, 'rb')
    content = f.read()
    j = None
    if len(content) == 0 and type == 1:
        f.close()
        return 0
    def recursive_search(index):
        if index * 18 >= len(content):
            if type == 0:
                return None
            else:
                return index
        f.seek(index * 18)
        venda = binary_to_venda(f.read(18))
        if type == 0 and venda[0] == venda_in[0]:
            return index
        elif type == 1 and venda[0] == venda_in[0] and venda[2] == venda_in[2]:
            return index
        return recursive_search(index + 1)
    
    j = recursive_search(0)
    f.close()
    return j

def excluir_venda(vendedor):
    j = locate_venda([vendedor],0)
    print(j)
    if j is None:
        print('Nao existe')
    else:
        f = open(path, 'rb+')
        f.seek((j+1)*18)
        rd = f.read()
        f.seek(j*18)
        f.write(rd)
        f.seek(-18,os.SEEK_END)
        f.truncate()
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

def imprimir_vendas():
    f = open(path, 'rb')
    for i in range(len(f.read())//18):
        f.seek(i*18)
        venda = binary_to_venda(f.read(18))
        print(f'Vendedor: {venda[0]} Valor: {venda[1]} Data: {venda[2]}')
    f.close()

def vendedor_com_maior_valor():
    f = open(path, 'rb')
    maior = 0
    for i in range(len(f.read())//18):
        f.seek(i*18)
        venda = binary_to_venda(f.read(18))
        if venda[1] > maior:
            maior = venda[1]
            vendedor = venda[0]
    f.close()
    return vendedor

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
            criar_arquivo()
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
            imprimir_vendas()
        elif op == 6:
            print(f'Vendedor {vendedor_com_maior_valor()} tem o maior valor')
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