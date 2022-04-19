vote_loop=1;vote_1=0;vote_2=0;vote_3=0;vote_4=0;vote_null=0;vote_white=0
print("Vote 5(nulo) e 6(branco), use 0 para parar")

while vote_loop:
    vote = int(input(f"Coloque o voto {vote_loop}: "))
    vote_loop+=1
    if vote==0:
        vote_loop=0
    else:
        if 2>=vote>0:
            if vote == 1:
                vote_1+=1
            else:
                vote_2+=1
        else:
            if 4>=vote>2:
                if vote == 3:
                    vote_3+=1
                else:
                    vote_4+=1
            else:
                if vote==5:
                    vote_null+=1
                else:
                    vote_white+=1

print("O total de votos por candidato é:")
print(f"Candidato 1: {vote_1}\nCandidato 2: {vote_2}")
print(f"Candidato 3: {vote_3}\nCandidato 4: {vote_3}")
print(f"Votos nulos: {vote_null}\nVotos brancos: {vote_white}")