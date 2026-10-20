# from usuarios import validar_email


# def test_valido():
#     assert validar_email("ana@exemplo.com") is True


# def test_sem_arroba():
#     assert validar_email("ana.exemplo.com") is False


# def test_entrada_deve_ser_texto():
#     assert validar_email(123) is False


# def test_rejeita_none():
#     assert validar_email(None) is False


# def test_sem_espacos():
#     assert validar_email("ana silva@exemplo.com") is False


# def test_exatamente_um_arroba():
#     assert validar_email("ana@@exemplo.com") is False


# def test_parte_anterior_ao_arroba_nao_pode_ser_vazia():
#     assert validar_email("@exemplo.com") is False


# def test_parte_posterior_ao_arroba_nao_pode_ser_vazia():
#     assert validar_email("ana@") is False


# def test_dominio_nao_pode_terminar_em_ponto():
#     assert validar_email("ana@exemplo.") is False


# def test_dominio_deve_ter_duas_partes_nao_vazias():
#     assert validar_email("ana@exemplo.com") is True


# def test_dominio_nao_pode_ter_parte_vazia():
#     assert validar_email("ana@exemplo..com") is False

# def test_aceita_dominio_com_subdominio():
#     assert validar_email("ana@exemplo.teste.com") is True


