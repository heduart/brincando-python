from envio_email.enviar_email import EnviarEmail


def test_criar_envio_de_email():
    enviar_email = EnviarEmail()
    assert enviar_email is not None


def test_remetente():
    enviar_email = EnviarEmail()
    destinatarios = ['felipe@terra.com.br', 'carlos_gonzales@hotmail.com', 'heduarte2003@yahoo.com.br']

    remetente = ['lucia_firmino@yahoo.com.br']
    assunto = 'Aprendendo Python com Testes'
    descricao = 'Primeiros Testes em Deselvolvimento'

    for destinatario in destinatarios:
        resultado = enviar_email.enviar(
            destinatario,
            remetente,
            assunto,
            descricao
        )
        assert destinatario in destinatarios


