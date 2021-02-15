f=open("Pdata2_25.txt","r")
s=f.read()
print(s)
n=0
for c in s:
    if c in "aeiouAEIOU":n=n+1
print("元音个数为：",n)