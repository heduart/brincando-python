from envio_email.enviar_email import EnviarEmail


def test_criar_envio_de_email():
    enviar_email = EnviarEmail()
    assert enviar_email is not None


def test_remetente():
    enviar_email = EnviarEmail()
    resultado = enviar_email.enviar(
        'felipe@terra.com.br',
        'lucia_firmino@yahoo.com.br',
        'Aprendendo Python com Testes',
        'Primeiros Testes em Deselvolvimento'
    )

    assert 'felipe@terra.com.br' in resultado
