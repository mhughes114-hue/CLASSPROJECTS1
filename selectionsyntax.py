x = 5
y = 9
z = -13

if x > 7 or z < 0 and x-y == -4:
    print("true")
elif not(x < 10):
    print("true")
else:
    print("false")


result = "true" if x > 7 else "false"
print(result)

res = ("false", "true")[x < 0]
print(res)
# test
# test
x = int(input("put number: "))
match x:
    case 7:
        print("seven")
    case 12:
        print("twelve")
    case 5:
        print("FIVE")
    case _:
        print("DEFAULT")