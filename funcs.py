def validar_cpf(cpf: str):
    cpf = ''.join(filter(str.isdigit, cpf))  # remove não numéricos
    if len(cpf) != 11:
        raise ValueError("O CPF deve ter exatamente 11 dígitos.")
    return cpf