1.
r="Cat 2.5"
if(r.isdigit()):
  print("digit")
elif(r.isalpha()):
  print("Alpha")
else:
  print("Both")
o/p:
Both

2.
temp=float(input("Enter temp:"))
if(temp>37.5):
  print("above")
elif(temp==37.5):
  print("equal")
else:
  print("below")
o/p:
Enter temp:74.3
above

3.
bill=int(input())
if(bill>=2000):
  print("discount:",bill*(10/100))
else:
  print("not discount")
o/p:
2500
discount: 250.0

4.
mark=int(input("Enter your mark:"))
attendance=int(input("Enter your attendance percentage:"))
if mark>=90 and attendance>=85:
  print("Eligible for scholorship")
else:
  print("not eligible") 
o/p:
Enter your mark:89
Enter your attendance percentage:89
not eligible

5.
month=input()
m31=['Jan','Mar','May','Jul','Aug','Oct','Dec']
m30=['Apr','Jun','Sep','Nov']
if month in m31:
  print("31 days")
elif month in m30:
  print("30 days")
elif month==Feb:
  print("28 days")
else:
  print("invalid")
o/p:
May
31 days

6.
count=0
for i in range(1,51):
  if i%5==0:
    count+=1
print("count:",count)
o/p:
count: 10

7.
sum=0
for i in range(1,21):
  if(i%2!=0):
    sum+=i
print("sum of odd number:",sum)
o/p:
sum of odd number: 100

8.
for i in range(1,31):
  if i%3==0 and i%2!=0:
    print(i)
  else:
    pass
o/p:
3
9
15
21
27

9.
count_pos=0
count_neg=0
num=[1,-2,3,-4,5,-6,7,-8,9]
for i in num:
  if i>0:
    count_pos+=1
  elif i<0:
    count_neg+=1
  else:
    print("invalid")
print("count_pos:",count_pos)
print("count_neg:",count_neg)    
o/p:
count_pos: 5
count_neg: 4

10.
num=[1,20,3067,40,36,57]   
largest=num[0]
for i in num:
  if i>largest:
    largest=i
print("largest number:",largest)
o/p:
largest number: 3067

11.
n=int(input("Enter the number:"))
count=0
for i in range(1,n+1):
  if n%i==0:
    count+=1
if count==2:
  print("Prime")
else:
  print("not prime")
o/p:
Enter the number:5
Prime

12.
n=int(input())
s=n*n
if str(s).endswith(str(n)):
  print("Automarphic")
else:
  print("Not Automarphic")
o/p:
56
Not Automarphic

13.
n=int(input())
temp=n
reverse_num=0
while temp>0:
 digit=temp%10
 reverse_num=(reverse_num*10)+digit
 temp//=10
if reverse_num==n:
 print("Palindrome number")
else:
 print("Not Palindrome number")
o/p:
454
Palindrome number

14.
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
28
Perfect number

15.
n=int(input())
square=n**2
temp=square
total=0
while temp>0:
  digit=temp%10
  total+=digit
  temp//=10
if total==n:
  print("neon number")
else:
  print("not neon number")
o/p:
9
neon number

16.
n = int(input())
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")  
    for k in range(2 * i - 1):
        print("*", end="")  
    print()  
o/p:
5
*********
 *******
  *****
   ***
    *

17.
n=int(input("Enter a number:"))
temp=n
total=0
while temp>0:
  digit=temp%10
  fact=1
  for i in range(1,digit + 1):
    fact*=i
  total+=fact
  temp//=10
if total==n:
  print("Peterson number")
else:
  print("Not a peterson number")
o/p:
Enter a number:145
Peterson number

18.
n=input("Enetr a number:")
if n[0]!='0' and '0' in n:
  print("Duck number")
else:
  print("Not a Duck number")
o/p:
Enetr a number:0980
Not a Duck number

19.
n=int(input("Enetr a number:"))
temp=n
while temp!=1 and temp!=4:
  total=0
  while temp>0:
    digit=temp%10
    total+=digit*digit
    temp//=10
  temp=total
if temp==1:
  print("Happy number")
else:
  print("Not a Happy number")
o/p:
Enetr a number:7
Happy number


