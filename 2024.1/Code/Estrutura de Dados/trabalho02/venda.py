import os
import struct

def binary_to_venda(binary):
    return (binary[0], binary[1], binary[2].decode('latin-1'))

def gravar_venda(venda):
    f = open(os.path.join(os.path.dirname(__file__), 'vendas.bin'), 'rb')
    j = 0
    for i in range(f.read()/18):
        f.seek(i*18)
        b = f.read(18)
        if binary_to_venda(b) == None:
            j = i
            break
        elif binary_to_venda(b)[0] == venda[0]:
            j = None
            break
        elif binary_to_venda(b)[2] > venda[2]:
            j = None
            break
    f.close()
    if j is None:
        print('ja existe')
        return
    f = open(os.path.join(os.path.dirname(__file__), 'vendas.bin'), 'ab')
    f.seek(j*18)
    f.write(struct.pack('i', venda[0]))
    f.write(struct.pack('f', venda[1]))
    f.write(bytes(venda[2].ljust(10), 'latin-1'))
    f.close()
    print('gravado')

def main():
    pass


f = open(os.path.join(os.path.dirname(__file__), 'vendas.bin'), 'wb+')
f.write(struct.pack('i', 23))
f.write(struct.pack('f', 8.5))
f.write(bytes('mm/aaaa'.ljust(10), 'latin-1'))
f.seek(0)
b = struct.unpack('i', f.read(4))[0]
print(b)
f.seek(4)
b = struct.unpack('f', f.read(4))[0]
print(b)
f.seek(8)
b = f.read(10).decode('latin-1')
print(b)
f.close()