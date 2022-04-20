def main():
    vote_loop=1;vote_1=vote_2=vote_3=vote_4=vote_null=vote_white=0
    print("Vote 5(nulo) e 6(branco), use 0 para parar")

    while vote_loop:
        vote = int(input(f"Coloque o voto {vote_loop}: "))
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
        vote_loop = vote_loop_logic(vote)

    print("O total de votos por candidato é:")
    print(f"Candidato 1: {vote_1}\nCandidato 2: {vote_2}")
    print(f"Candidato 3: {vote_3}\nCandidato 4: {vote_3}")
    print(f"Votos nulos: {vote_null}\nVotos brancos: {vote_white}")

def vote_loop_logic(vote):
    if vote==0:
        return 0
    else:
        return 1

main()

variable.sub = 1