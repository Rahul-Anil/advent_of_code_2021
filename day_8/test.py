# Program to check the list contains elements of another list

# List1
List1 = ["python", "javascript", "csharp", "go", "c", "c++"]

# List2
List2 = ["swift", "php", "python"]

check = all(item in List1 for item in List2)
# print(check)
# print([item in List1 for item in List2])


six = "cdfgeb"
nine = "cefabd"
zero = "cagedb"

three = "fbcad"
five = "cdfbe"
two = "gcdfa"

seven = "dab"
four = "eafb"
one = "ab"

print("five")
check_check = [char in six for char in two]
check = all(check_check)
print(check_check)
print(check)

three_1 = "fcadb"
three_2 = "cdbaf"

print("\n three check")
print(sorted(three))
print(sorted(three_1))
print(sorted(["a", "b"]) == sorted(three))
