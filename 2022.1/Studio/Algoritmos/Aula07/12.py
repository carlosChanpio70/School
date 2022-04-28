def main():
    interval = input_loop()
    print(f"Entre  0 e 25  há {interval[0]} valores.")
    print(f"Entre 26 e 50  há {interval[1]} valores.")
    print(f"Entre 51 e 75  há {interval[2]} valores.")
    print(f"Entre 76 e 100 há {interval[3]} valores.")

def input_loop():
    values=[]
    loop=1
    while loop:
        value = int(input(f"Insira o valor {loop}: "))
        if value>0:
            values.append(value)
            loop+=1
        else:
            loop=0
    return interval_check(values)

def interval_check(values):
    interval_25=0
    interval_50=0
    interval_75=0
    interval_100=0    
    for i in values:
        if 0<=i<=25:
            interval_25+=1
        elif 25<i<=50:
            interval_50+=1
        elif 51<i<=75:
            interval_75+=1
        elif 76<i<=100:
            interval_100+=1
    return [interval_25,interval_50,interval_75,interval_100]

main()