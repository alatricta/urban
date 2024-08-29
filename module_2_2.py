first = input().strip()
second = input().strip()
third = input().strip()

if first==second and second==third:
    print(3)
elif first==second or second==third or first==third:
    print(2)
else:
    print(0)
