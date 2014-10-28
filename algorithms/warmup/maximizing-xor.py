maxXor=0
l = input()
r = input()

for iL in range(l,r+1):
    for iR in range(iL, r+1):
        if iL ^ iR > maxXor:
            maxXor = iL ^ iR

print maxXor
