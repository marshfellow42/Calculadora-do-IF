print('Calcule a sua nota para ver se está aprovado')
print('*' * 18)
x1 = float(input('Qual a sua nota da Primeira Prova: '))
if (x1 > 10):
  print('Essa nota não existe')
  exit('O programa acabou')
x2 = float(input('Qual a sua nota da Segunda Prova: '))
if (x2 > 10):
  print('Essa nota não existe')
  exit('O programa acabou')
x3 = float(input('Qual a sua nota da Terceira Prova: '))
if (x3 > 10):
  print('Essa nota não existe')
  exit('O programa acabou')
x4 = float(input('Qual a sua nota da Quarta Prova: '))
if (x4 > 10):
  print('Essa nota não existe')
  exit('O programa acabou')
print('*' * 18)  
N1 = (x1 + x2) / 2
N2 = (x3 + x4) / 2
media = 0.4 * N1 + 0.6 * N2
print ('Sua média parcial é', media)
if (media >= 6):
  print ('Você foi Aprovado')
if (media >= 3 and media <= 5.9):
  print ('Você vai para a Prova Final')
  print('*' * 18)
  x5 = float(input('Qual a sua nota da Prova Final: '))
  MF = (media + x5) / 2
  print('Sua média final é', MF)
  print('*' * 18)
  if (MF >= 5):
    print('Você foi Aprovado')
  else:
    print('Você foi Reprovado')
if (media < 3):
  print('Você foi Reprovado')