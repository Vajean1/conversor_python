def meu_switch(escolha):
    opcoes = {
        'd': 'Decimal',
        'b': 'Binário',
        'o': 'Octal',
        'h': 'Hexadecimal',
        'm': 'Mais'
        
    }
    retornar = 'error'
    for x in opcoes:
        if escolha[0] in x:
            retornar = opcoes[x]
            break
    return retornar
