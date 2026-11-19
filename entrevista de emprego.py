import random as rd

print("Bem Vindo a sua Entrevista!")
print("Irei te fazer algumas questões e dependendo do seu desempenho, você será contratado ou rejeitado,")
print("Vamos Começar!")

perguntas = [
        "Você está realmente interessado no emprego",
        "Você tem experiência na área?",
        "Quais são suas Expectativas?",
        "Como você se vê daqui a 3/4 anos?",
]

for pergunta in perguntas:
    respostas = input(f"{pergunta}   ")
    valor = rd.randint(1,10)
    
print("Questionário finalizado, Obrigado!")
if valor <= 30:
    print(f"Você foi Aprovado para a Equipe!\nSua nota foi: {valor}")
else:
    print(f"Infelizmente você foi reprovado..\nSua Nota Foi: {valor}")