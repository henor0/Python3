age = 25

int_as_str = str(age)

print(int_as_str, "of type", type(int_as_str))


print(bool("")) # Output: False
print(bool("50")) # Output: True

print(bool([""])) # Output: True
print(bool(None)) # Output: False

x = 85
y = 9.5
resultat = x+y
print(resultat, "of type",type(resultat))

age = 27
message = "i am" + str(age) + "year old"
a = 5
b= "3"
resultat = a+ int(b)
print(resultat)