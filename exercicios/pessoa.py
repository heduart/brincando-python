"""
Cria uma classe pessoa para testes.
"""


class Pessoa:
    def id_do_objeto(self):
        # Retornando o Id para um objeto qualquer criado.
        return id(self)


if __name__ == '__main__':
    pessoa1 = Pessoa()
    print(f'Retonando o id criado para o objeto: \033[4;33;40m{pessoa1.id_do_objeto()}\033[m')
