class Pessoa:
    def __init__(self, nome):
        self.nome = nome

pessoas = [Pessoa("Ana"), Pessoa("Bruno"), Pessoa("Carla")]

nomes = extrair_nomes(pessoas)
print(nomes)
