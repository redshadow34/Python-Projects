from random import randint
justePrix=randint(1,500)


def essayer():
  NbEssai = 10
  a = ('prix proposé par le joueur')
  while justePrix != a and NbEssai > 0:
    NbEssai = NbEssai-1
    a = int(input('essaiPrix : '))
    print('Il vous reste', NbEssai, 'tentatives')
    if justePrix == a:
      print('win')
    elif NbEssai == 0:
        print('game over')
        print('justePrix est égale à', justePrix)
    elif a < justePrix:
        print('le justePrix est plus grand')
    else:
        print('le justePrix est plus petit')


essayer()