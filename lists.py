li1 = [1,2,3,4,5,6,7,8,9,10]
print(li1[0])
print(li1[-5])
print(li1[0:7])
li2 = [34,547,324,87,['Kohli','Rohit','Ronaldo']]
print(li2[4][2])
li2.append(500)
print(li2)
li2.insert(4,250)
print(li2)
li2.extend(['Pant','Bumra'])
print(li2)
li2[5] = ['Kohli','Rohit','Ronaldo','Rahul']
print(li2)
li2.remove(500)
print(li2)
li2.pop(1)
print(li2)
li2.pop()
print(li2)
for i in li2:
  if i == 250:
    print(i)
    break
  print(i)