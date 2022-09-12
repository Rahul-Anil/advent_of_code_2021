# Program to check the list contains elements of another list

# List1
List1 = ["python", "javascript", "csharp", "go", "c", "c++"]

# List2
List2 = ["swift", "php", "python"]
List3 = List2.copy()

check = all(item in List1 for item in List2)
check2 = all(item in List3 for item in List2)
print(f"c1: {check} {[item in List1 for item in List2]}")
print(f"c2: {check2} {[item in List3 for item in List2]}")


six = "cdfgeb"
nine = "cefabd"
zero = "cagedb"

three = "fbcad"
five = "cdfbe"
two = "gcdfa"

seven = "dab"
four = "eafb"
one = "ab"

print([c in three for c in one])

print([c in two for c in one])
print([c in five for c in one])

print("abc" in "abcd")
