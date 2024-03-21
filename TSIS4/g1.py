
try:
    N = int(input("Enter an integer for the upper limit: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

squares_list = [(i+1) * (i+1) for i in range(N)]

print("List of squares:")
print(squares_list)
