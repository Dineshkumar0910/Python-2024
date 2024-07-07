a = 10
if a>10:
  print("a is greater than 10")
elif a==10:
  print("a is equal to 10")
  if (type(a)==float):
    print("a is float")
  else:
    print('a is int')
else:
  print('a is lesser')

#for
for i in range(1,a,2):
  print(i)
li = [2,34,3,64,8,36]
for i in li:
  print(i)
x = 0
while (x < 10):
  x = x+1
  if x==5:
    pass #continue #break
  print(x)

for i in range(a,0,-1):
  for j in range(1,i+1):
    print('*',end=' ')
  print()

for i in range(a):
  for j in range(1,i+1):
    print(i,end=' ')
  print()