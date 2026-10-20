def validar_email(email: str) -> bool:
    if not isinstance(email, str):
        return False

    if " " in email or email.count("@") != 1:
        return False

    usuario, dominio = email.split("@")
    partes_dominio = dominio.split(".")

    return (
        usuario != ""
        and dominio != ""
        and len(partes_dominio) >= 2
        and all(partes_dominio)
    )