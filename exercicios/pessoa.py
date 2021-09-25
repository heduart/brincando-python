"""
Cria uma classe pessoa para testes.
"""


class Pessoa:
    """Criando algumas funções e objetos para a classe pessoa."""

    def __init__(self, nome: str = None, sobrenome: str = None, idade: int = None):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def id_do_objeto(self):
        """Apresentando o ID do objeto criado."""
        return id(self)


if __name__ == '__main__':
    """Testando objetos."""
    pessoa1 = Pessoa()
    print(f'Retornando o id criado para o objeto: \033[4;31;40m{pessoa1.id_do_objeto()}\033[m')
