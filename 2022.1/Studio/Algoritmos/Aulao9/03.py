def main():
    radius = float(input("Insira o raio da esfera: "))    
    print(f"Volume é {get_volume(radius)}")

def get_volume(radius=0):
    return (4*PI()*(radius**3))/3

def PI(): return 3.14159265359

main()