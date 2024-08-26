example=input().strip()
# example='Топинамбур'
print(example[0])
print(example[-1])

half=int(len(example)/2)
if len(example[half:])%2 == 0:
    print(example[half+1:])
else:
    print(example[half:])

print(example[::-1])
print(example[1::2])

