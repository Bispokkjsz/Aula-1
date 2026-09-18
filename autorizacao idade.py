# escreva um programa em python que peça as seguintes informacoes:
# idade ( em numero inteiro)
# altura em centimetros (um numero inteiro)
# tem autoriacao dos pais? (uma string: "Sim" ou "Nao")
#
# o programa deve exibir "acesso LIberado!" se o visitante puder andar no brinquedo
#  ou "acesso negado!" caso o contrario
#
# regra
# o visitante pode entrar se:
# tiver idade maior ou igual a 12 e a altura maior ou igual a 140 cm
# ou tb se ele tiver a autorizacao

idade = int(input("Qual a sua idade? "))
altura = int(input("Qual a sua altura em cm "))
autorizacao = str(input("Voce tem uma autirizacao? "))

if idade >= 12 and altura >= 140:
    print("Acesso liberado!")
elif autorizacao == "sim":
    print("Acesso liberado!")
else:
    print("Acesso negado!")