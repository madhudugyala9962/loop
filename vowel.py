n=input("enter a character: ")
count=0
for x in n:

    if x in "aeiouAEIOU":
        count=count+1
print(count)