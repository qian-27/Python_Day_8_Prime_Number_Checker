def prime_number_checker(number):
  is_prime = True

  for i in range(2, number):
    if number % i == 0:
      is_prime = False

  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")


# Check this number
n = int(input("The number for checking: "))
# keyword arguments
prime_number_checker(number=n)