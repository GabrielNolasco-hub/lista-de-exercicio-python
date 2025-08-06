numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def segundoMaiorNumero(lista):
    numerosUnicos = list(set(lista))  
    numerosUnicos.sort(reverse=True) 
    if len(numerosUnicos) < 2:
        return None 
    return numerosUnicos[1]

print(segundoMaiorNumero(numeros))
