try:
    result = 10/10
except:
    print("this is not devidion to zero, check this one again")

    fruit = {
        "appel":5,
        "banana":8,
        "orange":3
    }

    try:
        print(fruit("cherry"))
    except KeyError:
        print("the key does not exist in the dictonary")

