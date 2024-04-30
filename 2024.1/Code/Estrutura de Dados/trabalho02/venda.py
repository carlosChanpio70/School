import os,struct

def binary_to_venda(binary):
    return [struct.unpack('i',binary[:4])[0],struct.unpack('f', binary[4:8])[0], binary.decode('latin-1')[8:].strip()]

def venda_to_binary(venda):
    return (struct.pack('i', venda[0]) + struct.pack('f', venda[1]) + bytes(venda[2].ljust(10), 'latin-1'))

def check_if_exists(venda):
    f = open(os.path.join(os.path.dirname(__file__), 'vendas.bin'), 'rb')
    j = 0
    for i in range(len(f.read())//18):
        f.seek(i*18)
        b = f.read(18)
        venda2 = binary_to_venda(b)
        print(venda2)
        print(venda)
        if venda2 == None:
            j = i
            break
        elif venda2[0] == venda[0]:
            j = None
            break
        elif venda2[2][:2] > venda[2][:2]:
            j = None
            break
    f.close()
    return j

def adicionar_venda(venda):
    j = check_if_exists(venda)
    if j is None:
        print('Ja existe')
    else:
        f = open(os.path.join(os.path.dirname(__file__), 'vendas.bin'), 'ab')
        f.seek(j*18)
        f.write(venda_to_binary(venda))
        f.close()
        print('Gravado')

def ler_venda(vendedor):
    f = open(os.path.join(os.path.dirname(__file__), 'vendas.bin'), 'rb')
    j = None
    for i in range(len(f.read())//18):
        f.seek(i*18)
        venda = binary_to_venda(f.read(18))
        if venda[0] == vendedor:
            j = i
            break
    f.close()
    return j

def excluir_venda(vendedor):
    j = ler_venda(vendedor)
    if j is None:
        print('Nao existe')
    else:
        f = open(os.path.join(os.path.dirname(__file__), 'vendas.bin'), 'rb+')
        f.seek((j+1)*18)
        rd = f.read()
        f.seek(j*18)
        f.write(rd)
        f.close()
        print('Excluido')

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
            pass
        elif op == 4:
            pass
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