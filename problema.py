line = input()
m,n = line.split(" ")
m = int(m)
n = int(n)
x = m*n 
l = x%2
answer = 0
if l == 0:
	answer = x/2
else:
	answer = x//2
print(int(answer))