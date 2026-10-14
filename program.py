1.
x = int(input('x='))
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")
o/p:
x=56
positive

2.
a=int(input("Enter a number:"))
if a%2==0:
  print("The number is even")
else:
  print("The number is odd")
o/p:
Enter a number:34
The number is even

3.
x=int(input('x:'))
y=int(input('y:'))
if x > y:
  print("x is the max")
else:
  print("y is the max")
o/p:
x:46
y:97
y is the max

4.
age=int(input('Enter your age:'))
if age>=18:
  print("Eligible for vote")
else:
  print("Not eligible for vote")
o/p:
Enter your age:19
Eligible for vote

5.
mark=int(input('Enter your total mark:'))
if mark>=35:
  print("Pass")
else:
  print("Fail")
o/p:
Enter your total mark:45
Pass

6.
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
  print("a is largest number")
elif b>a and b>c:
  print("b is largest number")
else:
  print("c is largest number")
o/p:
67
98
34
b is largest number

7.
x=int(input('x:'))
if x%4==0:
  print("Leap Year")
else:
  print("Not Leap Year")
o/p:
x:2012
Leap Year

8.
a=int(input())
b=int(input())
c=int(input())
d=a+b
e=b-c
print(d)
print(e)
o/p:
12
4
6
16
-2

9.
x=int(input('Enter your number:'))
if x%5==0:
  print("x is divisible by 5")
else:
  print("Not divisible by 5")
o/p:
Enter your number:45
x is divisible by 5

10.
age=int(input('Enter your age:'))
r='eligible' if age>18 else 'Not'
print(r)
o/p:
Enter your age:19
eligible

11.
a=int(input())
b=int(input())
c=int(input())
if a<b and a<c:
 print("a is smaller")
elif b<a and b<c:
 print("b is smaller")
else:
 print("c is smaller")
o/p:
54
34
24
c is smaller

12.
x=int(input())
if x%5==0 and x%3==0:
 print("x is divisible by 5 and 3")
else:
 print("not divisible by 5 and 3")
o/p:
56
not divisible by 5 and 3

13.
x=int(input())
if x>=10 and x<100:
 print("x is 2 digit number")
else:
 print("x is not 2 digit number")
o/p:
765
x is not 2 digit number

14.
num=int(input())
if(num%10==5):
 print("True")
else:
 print("False")
o/p:
765
True

15.
a="Apple is Redcolor"
if a.isupper():
 print("a is upper")
elif a.islower():
 print("a is lower")
else:
  print("a is mixed")
o/p:
a is mixed

16.
n=int(input())
temp=n
power=len(str(n))
total=0
while temp>0:
 digit=temp%10
 total+=digit**power
 temp//=10
if total==n:
 print("armstrong")
else:
 print("not armstrong")
o/p:
564
not armstrong

17.
n=int(input())
s=n*n
if str(s).endswith(str(n)):
 print("Automarphic")
else:
 print("Not Automarphic")
o/p:
25
Automarphic

18.
n = int(input())
square = n ** 2  
temp = square
total = 0
while temp > 0:
    digit = temp % 10
    total += digit
    temp //= 10  
if total == n:
    print("neon number")
else:
    print("not neon number")
o/p:
9
neon number

19.
n=int(input())
total=0
for i in range(1,n):
 if n%i==0:
  total+=i
if total==n and n>0:
 print("Perfect number")
else:
 print("Not Perfect number")
o/p:
65
Not Perfect number



