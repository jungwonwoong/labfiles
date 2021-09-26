posx = [10,20,22,26,50]
posx1 = [21,22,23]
posxf = []
mind = [0]
i=0
if len(posx) != len(posx1):
  if len(posx) > len(posx1):
    mind = posx
    for a in posx:
        t=100
        for b in posx1:
            if abs(a-b) < t and abs(a-b) < 4:
             del mind[i]
             mind.insert(i, b)
             t=abs(a-b)
            else:
             del mind[i]
             mind.insert(i, a)
             t=abs(a-b)
        i += 1
    print(mind)