def main():
    score = int(input("Insira a média final do aluno(0-100): "))
    print(f"O aluno teve nota {get_concept(score)}")

def get_concept(score):
    if 0<=score<50:
        return "D"
    if 50<=score<70:
        return "C"
    if 70<=score<90:
        return "B"
    if 90<=score<=100:
        return "A"

main()