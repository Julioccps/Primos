import time
from collections import deque

class Prime:
    def __init__(self):
        pass

    @staticmethod

    def is_prime(n):
        '''
        Define se um numero é primo ou não pelos seguintes metodos:
        se o numero for menor ou igual a 1, ele não é primo;
        se ele for igual a 2, ele é primo;
        se ele for divisivel por dois, não é primo.
        A outra parte determina se o valor fornecido é um primo 
        dividindo-o por todos os numeros até a raiz quadrada do 
        proprio
        '''
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False 
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        
        return True
    
    def find_primes(self, start, end):
        '''
        Encontra os numeros primos em um alcance determinado 
        usando a função anterior nos numeros dentre o alcance 
        definido
        '''
        primes = []
        for numero in range(start, end + 1):
            if self.is_prime(numero):
                primes.append(numero)
        return primes

    def prime_p_time(self, segundos, quantidade):  
        '''
        Encontra numeros primos em um determinado tempo de funcionamento
        '''
        primos = deque(maxlen=quantidade)
        numero = 2
        start_time = time.time()

        while time.time() - start_time < segundos:
            if self.is_prime(numero):
                primos.append(numero)
            numero += 1

        return list(primos)