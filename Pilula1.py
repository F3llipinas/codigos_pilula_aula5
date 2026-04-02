def validarSenha(s):
    if len(s) < 8:
        return 'Senha inválida, muito curta.'
    
    temNumero = False
    temMaiuscula = False
    
    for c in s:
        if c == ' ':
            return 'Senha Inválida, não pode conter espaços'
        if c >= '0' and c <= '9':
            temNumero = True
        if c >= 'A' and c <= 'Z':
            temMaiuscula = True
            
    if not temNumero == False:
        return 'Senha Inválida. Deve conter prlo menos um número'
    
    if not temMaiuscula == False:
        return 'Senha Inválida. Deve conter pelo menos ma letra maiúscula'
    return 'Senha válida'
    
#main
senha = input('Digite a senha: ')
r = validarSenha(senha)
print(r)