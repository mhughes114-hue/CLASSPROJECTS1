# prompt enter a price
# set price = input
# set total = price * 1.07
# ECHO total

price = float(input("How much does item cost? "))
while price < 0:
    print("Please enter a non-negative price.")
    price = float(input("How much does item cost? "))

total = price * 1.07
print(f"The total in Indiana would be ${total:.2f}.")
