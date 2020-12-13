a = int(input("Donner une valeur : "))
def listeNbePrem():
  p = []
  x = 2
  while x <= a:
    y = 2
    while y*y <= x:
        if x % y == 0:
            break
        y += 1
    else:
        p.append(x)
    x += 1
  return p
print(listeNbePrem())