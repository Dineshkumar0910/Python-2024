unscrambled=[
    "hello:1",
    ["w","o","r","l","d"],
    "cde"	
]
def fn(unscrambled):
  ans=list()
  for i in unscrambled:
    if i is str(i) and ":" in i:
      tu=(i.split(":"))
      ans.append(tu)
      
    elif i is str(i) and ":" not in i:
      s=[x for x in i]
      ans.append(s) 
    else:
      l="".join(i)
      ans.append(l)
  return ans
print(fn(unscrambled))
