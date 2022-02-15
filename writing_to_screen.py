
person = "Homer Simpson"
city = "Springfield"
amount = 4.39023939

print(person, city, amount)
SEPARATOR = ' '
END_STRING = '\n'
print(str(person) + SEPARATOR + str(city) + SEPARATOR + str(amount) + END_STRING)

print("===")

print(person, city, amount, sep="/")
print(person, city, amount, sep="")
print(person, city, amount, sep=", ")

print(person, end=" ")
print(city, end='==')
print(amount)

my_value = 5
print(my_value)

print(amount)

print(person, "lives in", city)
print("{} lives in {}".format(person, city))
print(f"{person} lives in {city}")


print(f"amount is {amount}")
print(f"amount is {amount:.1f}")









