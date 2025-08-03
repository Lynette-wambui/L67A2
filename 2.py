# Division Formula: Dividend = Divisor x Quotient + Remainder

# Input from user
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

# Calculate Quotient and Remainder
quotient = dividend // divisor
remainder = dividend % divisor

# Show the result
print(f"\nQuotient = {quotient}")
print(f"Remainder = {remainder}")


# Check the formula
print(f"\n {dividend} = {divisor} x {quotient} + {remainder}")