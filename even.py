# Count the number of Even Numbers between 1 to 10
# sum1=0
# for x in range(2,11,2):
#     sum1=sum1+1
# print(sum1)


# Reverse a String ("python" → "nohtyp") using a for loop
# n="python"
# s=""
# for x in n:
#     s=x+s
# print(s)

    
# Calculate the Shopping Cart Total for prices [100, 250, 75]

# sum1=0
# for x in (100,250,75):
#     sum1=sum1+x
# print(sum1)


# Simulate a Rocket Launch Countdown from 20 to 1 and print "Launch Successful!" at the end

# import time
# for x in range(20,0,-1):
#     time.sleep(1)
#     print(x)
# print("Launch Successfull")



# Count the number of Uppercase Letters in the string "PyThOnPrOgRaM"


# n="PyThOnPrOgRaM"
# count=0
# for x in n:
#     if x.isupper():
#         count=count+1
# print(count)



# Calculate the String Length Without using len() for the string "programming"

# n="programming"
# count=0
# for x in n:
#     count=count+1
# print(count)


# Check if a given string ("madam") is a Palindrome using a loop

# n="madam"
# c=""
# for x in n:
#     c=x+c
# print(c)



# Find the Second Largest Number from a list [10, 45, 23, 89, 67]
# list=[10, 45, 23, 89, 67]
# n=1
# for x in list:
#     if x>n:
#         n=x

# print(n)
# second_largest=1
# for x in list:
#     if x>second_largest and x<n:
#         second_largest=x
# print(second_largest)


# Create a Simple Interest Calculator that uses a loop to print interest for each year (Principal = 1000, Rate = 5%, Time = 5 years)

# Principal = 1000
# Rate = 5
# Time=5
# print("simple intrest: ", (Principal*Rate*Time)/100)

# principal=1000
# rate=0.05
# for i in range(1,6):
#     intrest=principal*rate*i
#     print(f"year {i}:Intrest={intrest}")



# harshad number

# n=18

# i=0
# for x in str(n):
  
#     i=i+int(x)
# if n%i==0:
#     print("harshad number")



# n=253
# s=0
# for x in str(n):
#    if int(x)>s:
#       s=int(x)
# print(s)



# num=12345
# n=0
# for x in str(num):
#     if int(x)%2==0:
#         n=n+int(x)
# print(n)


# Find the Sum of Odd Numbers from 1 to 50


# odd=0
# for x in range(1,50):
#     if x%2==1:
#         odd=odd+1
# print("odd",odd)
        

# Apply a 10% discount to prices [500, 1000, 1500] and print the new prices


# n=0
# for x in [500,1000,1500]:
#     n=x*10/100
#     print(x-n)

# Identify if a number is a Perfect Number using a for loop

# sum=0
# n=int(input("enter number"))
# for x in range(1,n):
#     if n%x==0:
#         sum=sum+x
# if sum==n:
#     print("perfect number")
# else:
#     print("not a perfect number")


# Check if a number is an Automorphic Number

# n=int(input("enter number"))
# x=len(str(n))
# automorphic=(n*n)%(10**x)
# if automorphic==n:
#     print("automorphic number")
# else:
#     print("not automorphic number")


#2)Find the Lucky Number (divisible by 7) using a loop
# n=int(input("enter number"))
# for i in range(1, n):
#     if i % 7 == 0:
#         print(i)

