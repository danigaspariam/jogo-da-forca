secreto = 'perfume'
digitada = []

while True:
  letra = input('Digite uma letra: ')
  if len(letra) > 1:
    print('Você digitou mais de uma letra. Está errado.')
    continue

  digitada.append(letra)

  if letra in secreto:
    print(f'Uhuuullll!!! a letra {letra} está na palavra secreta!')
  else:
    print(f'Sinto muito, a letra {letra} não está na palavra secreta')
    digitada.pop()

  secreto_temporario = ''
  for letra_secreta in secreto:
    if letra_secreta in digitada:
      secreto_temporario += letra_secreta
    else:
      secreto_temporario += '*'

  if secreto_temporario == secreto:
    print(f'Parabéns, você conseguiu! A palavra secreta é: {secreto}.')
    break
  else:
    print(f'A palavra secreta, está assim: {secreto_temporario}.')

        


