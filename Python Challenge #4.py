#convert numbers from base 10 to others
rem = []
num = int(input("Base 10 number: "))
target_base = int(input("Output base: "))

n = target_base
X = num

if X > n:
    rem.append(X%n)
    print(" ")
    print(f"{n} | {X}")
    print(f"{n} | {X//n} r {X%n}")
    X = X//n
    while X >= 1:
        rem.append(X%n)
        print(f"{n} | {X//n} r {X%n}")
        X = X//n
else:
    rem.append(X)

rem.reverse()
output = "".join(str(e) for e in rem)
print(f"""
:. {num} in base 10 = {output} in base {n}"""
)