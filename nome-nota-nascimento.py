ano_nascimento = int(input("qual a sua data de nascimento? "))
nome = input("qual o seu nome? ")
nota1 = float(input("qual a sua nota? "))
nota2 = float(input("qual a sua segunda nota? "))

media = (nota1 + nota2) / 2

if media >= 7:
    situacao = "aprovado"
elif media >= 5:
    situacao = "recuperacao"
else:
    situacao = "reprovado"

ano_atual = 2026
idade = ano_atual - ano_nascimento

print (f"Aluno {nome}")
print (f'Sua idade é {idade}')
print (f"Sua media é {media}")
print (f"situacao: {situacao}")
