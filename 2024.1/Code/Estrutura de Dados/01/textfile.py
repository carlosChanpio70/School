import os
tf=open(os.path.join(os.path.dirname(__file__), "teste.txt"), "w")
linha="Ainda que eu falasse a lingua dos homens\n"
tf.write(linha)
linha="Ainda que eu falasse a lingua dos anjos\n"
tf.write(linha)
linha="Sem amor eu nada seria\n"
tf.write(linha)
linha="É só o amor\n"
tf.write(linha)
tf.close()

tf=open(os.path.join(os.path.dirname(__file__), "teste.txt"), "r")
linha=tf.readline()
while(linha):
    print(linha)
    linha=tf.readline()
tf.close()