# Finding the second largest and second smallest number in a list


while True:
    n = input("Enter a no. for n length of list : ")
    try:
        n = int(n)
        a = list(map(int, input("Enter a list : ").strip().split()))[:n]
        break
    except:
        print("Wrong Entry: Try Again!! 'Enter a number' ")

print(a)
mx = max(a)
smx = 0

for i in a:
    if smx < i != mx:
        smx = i

print(f"Second largest number in list : {smx}")

mm = min(a)
ssm = mx
for i in a:
    if ssm > i != mm:
        ssm = i

print(f"Second smallest number in list : {ssm}")
