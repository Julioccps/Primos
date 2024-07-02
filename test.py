from primes.primes import Prime

prime_checker = Prime()

# Checar se um numero é primo

num = int(input("Digite um numero para saber se ele é primo: "))

primo = prime_checker.is_prime(num)

print(f"O número {num} é primo? {primo}")

# Determinar os numeros primos em um certo alcance

inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

primos = prime_checker.find_primes(inicio, fim)

print(f"Números primos entre {inicio} e {fim}: {primos}")

# Encontrar um certo número de primos apartir do tempo de calculo

tempo = int(input("Digite um tempo de funcionamento da função: "))
quantidade = int(input("Digite quantos numeros voce quer ao final dos calculos: "))

primos = prime_checker.prime_p_time(tempo, quantidade)

print(f"Ultimos {quantidade} números primos calculados em {tempo} segundos: {primos}")