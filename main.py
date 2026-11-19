try:
    import random
    entrevista = input("diga por que você quer esse emprego:")
    o = random.choice(["esta contratado", "desculpe,não esta contratado"])
    print(o)
except Exception as u:
    print(u)