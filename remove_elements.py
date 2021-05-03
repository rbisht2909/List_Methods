"""
Created on Mon May  3 15:17:04 2021

"""

# to remove the elements from a given list

n = input("Enter a no. for a length n of a list : ")
while True:
    try:
        n = int(n)
        a = list(map(int, input("Enter elements in  a list : ").strip().split()))[:n]
        break
    except:
        print("Try Again!!!\nWrong Entry")

print(a)
print("Choose elements to remove from list : ")
r_elements = list(map(int, input("Enter :").strip().split()))[:len(a)]


for k in r_elements:
    for i in range(len(a)):
        if k in a:
            a.remove(k)

print("List after removing elements : ", a)