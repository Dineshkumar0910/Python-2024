#variable, i/p, o/p
a = 20
print("a is:",a) #o/p
b = int(input()) #i/p #type conversion
print("b is:",b)
print(type(a),type(b))
#arithmetic operator
print(a+b,a-b,a*b,a/b,a%b,a//b,a**2)
#relational operator
print(a>b,a<b,a>=b,a<=b,a==b,a!=b)
#logical operator
print(a>b and a<b,a>b or a<b,not(a>b))
#bitwise operator
print(a&b,a|b,~a,a^b)
#assignment operator
a+=b #a=a+b
print(a)
a-=b
print(a)
#membership operator - in, not in
print("Atlas" in "Atlas is a variable")
print("las" not in "Atlas is a variable")
#identity operator - is, is not
print(a is 20)
print(a is not 20)
#precedence
print(((a+b)/10)*2**2)
#Practice
'''
Age Calculator: Write a program that asks for the user's birth year and calculates their age.'''