def main(string, caracter):
    r_string = string
    i = 0
    if caracter in string:
        while r_string == string:
            if string[i] == caracter:
                r_string = string[:i]
            i += 1
    return r_string

print(main("Hello, World", "W"))