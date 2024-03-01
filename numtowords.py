from dictionary import words

def convert(n):
    try:
        #n = int(n)
        if n == 0:
            return ' Zero '
        elif n <= 100:
            return lessthanhundred(n)
        elif n > 100 and n < 1000:
            return greaterthanhundred(n)
        elif n>=1000 and n < 100000:
            return greaterthanthousand(n,1000,'Thousand')
        elif n >= 100000 and n<10000000:
            return greaterthanthousand(n,100000,'Lakh')
        elif n >=10000000:
            return greaterthanthousand(n,10000000,'Crore')
    except (ValueError, Exception) as e1:
        print('invalid Input Enter only Numbers',e1)

def lessthanhundred(n):
    if n in words:
        return words.get(n)
    else:
        quotient, remainder = divmod(n, 10)
        return words.get(quotient*10) + ' ' + words.get(remainder) 

def greaterthanhundred(n):
    quotient, remainder = divmod(n,100)
    quotient = words.get(quotient)
    if remainder == 0:
        return quotient +' '+ ' Hundred '
    else:
        remainder = lessthanhundred(remainder)
        return quotient +' '+ ' Hundred ' +' '+ remainder 

def greaterthanthousand(n,number,unit):
    quotient,remainder = divmod(n,number)
    quotient = convert(quotient)
    if remainder == 0:
        return quotient +' '+ unit
    else:
        remainder = convert(remainder)
        return quotient +' '+ unit +' '+ remainder

while True:
    try:
        l = int(input('Enter a Number to convert to words:>>>>>'))
        print(convert(l),'Rupees Only')
        break
    except (ValueError,Exception) as ee:
        print('You have entered a wrong value ')
        