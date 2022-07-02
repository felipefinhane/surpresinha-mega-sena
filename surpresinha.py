import random

def sortLuckNumber(arrList):
    lNumber = random.randint(1,60)
    if lNumber in arrList:
        return sortLuckNumber(arrList)
    return lNumber

question02 = eval(input('Quantidade de jogos: '))
question01 = eval(input('Quantidade de numeros: '))

indiceGames = 0
arrGames = []
while(indiceGames < (question02 * 12 * 100)):
    indiceGames += 1
    indiceNumbers = 0
    arrList = []
    while(indiceNumbers < question01):
        indiceNumbers += 1
        luckNumber = sortLuckNumber(arrList)
        arrList.append(luckNumber)
    arrList.sort()
    arrGames.append(arrList)

random.shuffle(arrGames)
contador = 0

for game in arrGames:
    if (contador >= question02):
        break
    contador += 1
    print(game)
