l1 = [5,1,3,2,4,6,1,7,3,2,8]
l2 = []

m = 3

while len(l1) >= m:
  l2.append(min(l1[:m]))
  print l1[:m], '= ', l2[-1]
  del l1[0]

print l2

