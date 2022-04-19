month = int(input("Informar o número do mês: "))
if 0 < month <= 6:
    if month == 1:
        month = "janeiro"
    else: 
        if month == 2:
            month = "fevereiro"
        else:
            if month == 3:
                month = "março"
            else:
                if month == 4:
                    month = "abril"
                else:
                    if month == 5:
                        month = "maio"
                    else:
                        month = "junho"
else:
    if 6 < month <= 12:
        if month == 7:
            month = "julho"
        else:
            if month == 8:
                month = "agosto"
            else:
                if month == 9:
                    month = "setembro"
                else:
                    if month == 10:
                        month = "outubro"
                    else:
                        if month == 11:
                            month = "novembro"
                        else:
                            month = "dezembro"
        print(f"O mês é {month}")
    else:
        print("Mês inválido")