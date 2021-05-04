"""
Created on Tue May  4 10:35:52 2021

"""
# To print the occurence of numbers in a list

## Using Basic Method
n = input("Enter a number for length n of list : ")
while True:
    try:
        n = int(n)
        a = list(map(int, input("Enter numbers for list : ").strip().split()))[:n]
        break
    except:
        print("Try Again!!\nWrong Entry!!!!")
        
print(a)        
unique = []


for i in a:
    if i not in unique:
        unique.append(i)
unique.sort()
print("In the form of list\n",unique)     # This will print result in form of a list

for i in unique:
    print(i, ":", a.count(i))
    
    
## Using Set Function

unique1 = set(a)
print("In the form of set\n",unique1)     # This will print result in form of a set

for i in unique1:
    print(i, ":", a.count(i))