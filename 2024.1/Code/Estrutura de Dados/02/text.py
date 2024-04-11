import os
import struct

fp=open(os.path.join(os.path.dirname(__file__), "teste.bin"),"wb+")
fp.write(struct.pack('=i',23))
fp.write(bytes("Luiz".ljust(10),"latin-1"))
fp.write(struct.pack('f',8.5))
fp.write(struct.pack('i',15))
fp.write(bytes("Ana".ljust(10),"latin-1"))
fp.write(struct.pack('f',9.4))
print(fp.tell())
fp.seek(0)
mat=struct.unpack('i',fp.read(4))[0]
print(mat)
b=fp.read(10)
nome=b.decode("latin-1")
print(nome)
nota=struct.unpack('f',fp.read(4))[0]
print(nota)
print(fp.seek(0,os.SEEK_END))
fp.close()