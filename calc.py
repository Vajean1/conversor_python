from os import system

#calculadora de conversão de bases
print(f'{"Calculadora de conversão de bases":=^80}\n\n')
        
class menus():
    def menu_principal():
        print(f'{"DIGITE A OPÇÂO DESEJADA":=^80}')
        print('[ 1 ] - Conversão de bases\n[ 2 ] - Calculo com bases diferentes\n')
        escolha = int(input('Digite a opção desejada: '))
        if escolha == 1:
            system('cls')
            return menus.menu_conversao_bases()
        elif escolha == 2:
            system('cls')
            return menus.menu_calculo_bases_diferentes()

    def menu_conversao_bases():
        print('Você escolheu a opção de conversão de bases.\nAqui teremos várias opções, inclusive a que você quiser colocar.')
        print('Escolha: \n[ d ] - Para decimal.\n[ b ] - Para binário.\n[ o ] - Para Octal.\n[ h ] - Para Hexagonal. \nCaso queira converter de uma base de escolha sua, sendo de binário ao decimal, escolha a opção [ m ] - Mais.')
        escolha = str(input('Qual a opção desejada: '))


    def menu_calculo_bases_diferentes():
        print('Você escolheu a opção de calculo com bases diferentes. \nAqui você selecionará o tipo de conversão que deseja fazer e calculo será realizado entre essas bases.')
        print('Escolha: \n[ d ] - Para decimal.\n[ b ] - Para binário.\n[ o ] - Para Octal.\n[ h ] - Para Hexagonal. \nCaso queira converter de uma base de escolha sua, sendo de binário ao decimal, escolha a opção [ m ] - Mais.')
        print('Você vai escolher as bases para qual quer fazer o calculo e irá retornar o valor.')
