from basicCollections import stack

def parChecker(symbolString):
    s = stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def symbolChecker(symbolString):
    def matches(open,close):    
        opens = "([{"
        closers = ")]}"
        return opens.index(open) == closers.index(close)
    s = stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def decToBin(decNumber):
    rStack = stack()   # reminder stack 
    while decNumber > 0:
        rem = decNumber % 2
        rStack.push(rem)
        decNumber = decNumber // 2
    result = ""
    while not rStack.isEmpty():
        result += str(rStack.pop())
    return result

def dec2bin(n):
    return dec2bin(n // 2) + str(n % 2) if n > 1 else str(n)

def dec2base(n,base):
    convertString = "0123456789ABCDEF"
    return dec2base(n // base,base) + convertString[n%base] if n > base - 1 else convertString[n]

def infix(s):
    tr=[]    
    def body(s, i):
              if i >=len(s):
                   return   #  base case
              body(s, 2*i+1)  # recursive case
              body(s, 2*i+2) # recursive case
              tr.insert(0,s[i])
    body(s,0)
    return tr

def decToBase(n,base):
    rStack = stack() # reminder stack 
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base  # quocinte da divisão de n pela base
    result = ""
    while not rStack.isEmpty():
        result += str(rStack.pop())
    return result

if __name__ == '__main__':
    """
    print('parChecker :  ((()))')
    print(parChecker('((()))'))
    print(parChecker('(()'))
    print('symbolChecker : {{([][])}()}')
    print(symbolChecker('{{([][])}()}'))
    print('symbolChecker : [{()]')
    print(symbolChecker('[{()]'))
    """
    print('43 in binário ',decToBin(255))
    print('decimal 1453 to base 2 ',decToBase(255,2))
    print('decimal 1453 to base 8 ',decToBase(1453,8))
    print('decimal 1453 to base 10 ',decToBase(1453,10))
    print('decimal 1453 to base 16 ',decToBase(1453,16))
    print('recursive 43 in binário ',dec2bin(255))
    print('recursive decimal 1453 to base 2 ',dec2base(255,2))
    print('recursive decimal 1453 to base 8 ',dec2base(1453,8))
    print('recursive decimal 1453 to base 10 ',dec2base(1453,10))
    print('recursive decimal 1453 to base 16 ',dec2base(1453,16))


    


        
