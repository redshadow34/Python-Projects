def tpi(nombres):
  p = []
  i = []
  for elem in nombres:
    if elem%2==0:
      p.append(elem)
    else:
      i.append(elem)
  return p, i
print(tpi((7, 55, 6, 23, 46, 88, 96, 13, 28, 33)))