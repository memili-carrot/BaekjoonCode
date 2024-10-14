croatian_alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

a = input()

for i in croatian_alphabets:
    a = a.replace(i,"*")
print(len(a))