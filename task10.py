# . Two strings of equal length will be given. Print all the adjacent pairs which are not equal.

# Input: asdfghij and adsfgijh

# Output: sd-ds, hij-ijh
a="asdfghij" 
b="adsfgijh"
a1=""
b1=""

for i in range(len(a)):
    if a[i]==b[i]:
        pass
    else:
        a1+=a[i]
        b1+=b[i]
    
print(f"{a1[0:2]}-{b1[0:2]}",f"{a1[2:]}-{b1[2:]}")