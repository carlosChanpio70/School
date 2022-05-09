def main():
    days = int(input("Digite a idade em dias: "))
    months = int(input("Digite a idade em meses: "))
    years = int(input("Digite a idade em anos: "))
    print(f"A idade da pessoa em dias é {get_age_days(days,months,years)}")

def get_age_days(days=0,months=0,years=0):
    days+=months*30
    days+=(years*12)*30
    return days

main()