posx = [10,20,22,26,50]
posx1 = [11,22,23,22,45]
posxf = []
mind = [0]
i=0
if len(posx) == len(posx1):
    for a in posx:
      
      posxf.append(abs(posx[i]-posx1[i]))
      print(i)
      i += 1
        #t=100
        ##for b in posx1:
        ##    if abs(a-b) < t and abs(a-b) < 4:
        ##     del mind[i]
        ##     mind.insert(i, b)
        #     t=abs(a-b)
        #    else:
        #     del mind[i]
        #     mind.insert(i, a)
        #     t=abs(a-b)
        # i += 1
        #print(mind)
    print(posxf)