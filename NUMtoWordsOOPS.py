from dictionary import  words
class num_to_words:
    _instance=None
    def __new__(cls, *args, **kwargs):
        '''Singleton method'''
        if not cls._instance:
            '''if there is no instance create one'''
            cls._instance = super().__new__(cls)
            '''assigning Dictionary'''
            cls._instance.words = words
        return cls._instance
    '''applying staticmethod for all methods so it cant be accessed outside class '''
    @staticmethod
    def convert(n):
        try:
            # n = int(n)
            if n == 0:
                return ' Zero '
            elif n < 100:
                return num_to_words._lessthanhundred(n)
            elif n >= 100 and n < 1000:
                return num_to_words._greaterthanhundred(n)
            elif n >= 1000 and n < 100000:
                return num_to_words._greaterthanthousand(n, 1000, 'Thousand')
            elif n >= 100000 and n < 10000000:
                return num_to_words._greaterthanthousand(n, 100000, 'Lakh')
            elif n >= 10000000:
                return num_to_words._greaterthanthousand(n, 10000000, 'Crore')
        except (ValueError, Exception) as e1:
            print('invalid Input Enter only Numbers', e1)

    @staticmethod
    def _lessthanhundred(n):
        if n in num_to_words._instance.words:
            return num_to_words._instance.words.get(n)
        else:
            quotient, remainder = divmod(n, 10)
            quotient1 = num_to_words._instance.words.get(quotient * 10)
            remainder1 = num_to_words._instance.words.get(remainder)
            return f'{quotient1} {remainder1}'

    @staticmethod
    def _greaterthanhundred(n):
        quotient, remainder = divmod(n, 100)
        quotient = num_to_words._instance.words.get(quotient)
        if remainder == 0:
            return f"{quotient} Hundred"
        else:
            remainder = num_to_words._lessthanhundred(remainder)
            return f"{quotient} Hundred {remainder}"
    @staticmethod
    def _greaterthanthousand(n, number, unit):
        quotient, remainder = divmod(n, number)
        quotient = num_to_words.convert(quotient)
        if remainder == 0:
            return f"{quotient}  {unit}"
        else:
            remainder = num_to_words.convert(remainder)
            return f"{quotient}  {unit}  {remainder}"

class fasade_numtowords:
    '''Fasade method'''
    def __init__(self):
        self.numtowords_instance=num_to_words()
    def converting_to_word(self,num):
        return self.numtowords_instance.convert(num)


if __name__=="__main__":
    '''Using dunder name function to check its running directly or imported '''
    Fasade = fasade_numtowords()
    while True:
        try:
            l = int(input('Enter a Number to convert to words:>>>>>'))
            result = Fasade.converting_to_word(l)
            print(f'{result} Rupees Only.')
            break
        except (ValueError, Exception) as ee:
            print(f'You have entered a wrong value')