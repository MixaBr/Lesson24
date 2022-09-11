def famil(surname):
    surname = surname.capitalize()
    s = ""
    for i in surname:
        if i.isupper():
            s += i
        else:
            s += "*"
    return s


print(famil("огурцова"))