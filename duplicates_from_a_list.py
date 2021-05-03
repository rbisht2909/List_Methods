"""
Created on Mon May  3 20:30:39 2021


"""
# Program to print duplicates from a list of integers

n = input("Enter a no. for length n of list : ")
while True:
    try:
        n = int(n)
        a = list(map(int, input("Enter no.s to a list: ").strip().split()))[:n]
        break
    except:
        print("Wrong entry!!!\nTry Again")

print(a)


# Using function
def duplicate_elements(ls):
    se_list = []
    for i in ls:
        if ls.count(i)>1 and i not in se_list:
            se_list.append(i)
    
    return se_list
r = duplicate_elements(a)
print(r)
 