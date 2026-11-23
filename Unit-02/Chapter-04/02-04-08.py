s1 = int(input("input the length of s1: "))
s2 = int(input("input the length of s2: " ))
s3 = int(input("input the length of s3: " ))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    if s1 == s2 == s3:
        print("equilateral")
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print("isosceles")
    else:
        print("scalene")
else:
    print("not a triangle")
