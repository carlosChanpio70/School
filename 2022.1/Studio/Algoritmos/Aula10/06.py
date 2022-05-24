def main(string,number):
    if number>len(string):
        number=len(string)
    return string[:number]

print(main("Test",2))