numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def segundoMaiorNumero(lista):
  numerosUnicos = liste(set(lista));
  numerosUnicos.sort(reverse=true);
  if len(numerosUnicos) < 2:
    return none;
  return numerosUnicos[1];


segundoMaiorNumero(numeros);
