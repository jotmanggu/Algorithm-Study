data = list(map(int, input().split()))
left = 0
right = 0
for i in range(0, int(len(data)/2)):
    left = left + data[i]

for i in range(int(len(data)/2), int(len(data))):
    right = right + data[i]

if left == right:
    print("LUCKY")
else:
    print("READY")

