def is_prime(n):
    """Helper function to check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Step 1: Get user input
name = input("Enter your name: ")
print(f"Hello, {name}! Let's explore your favorite numbers.")
numbers = []

# Step 2: Get the three favorite numbers from the user
for i in range(1, 4):
    num = int(input(f"Enter favorite number {i}: "))
    numbers.append(num)

# Step 3: Check if the numbers are even or odd
even_odd_info = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]

# Step 4: Display whether each number is even or odd
print("\nEven/Odd Analysis:")
for num, info in even_odd_info:
    print(f"The number {num} is {info}.")

# Step 5: Create a list of tuples with numbers and their squares
squares = [(num, num**2) for num in numbers]

# Step 6: Print the numbers and their squares in a creative format
print("\nNumber Squaring Adventure:")
for num, square in squares:
    print(f"The square of {num} is {square}. That's a powerful number!")

# Step 7: Calculate the sum of the three numbers
sum_numbers = sum(numbers)

# Step 8: Display the sum with an encouraging message
print(f"\nThe sum of your favorite numbers is: {sum_numbers}. That's an interesting total!")

# Step 9: Check if the sum is a prime number
if is_prime(sum_numbers):
    print(f"Wow, {sum_numbers} is a prime number! You're working with special numbers!")
else:
    print(f"{sum_numbers} is not a prime number, but it's still great to work with!")

# Final message
print(f"\n{name}, I hope you enjoyed exploring your favorite numbers!")