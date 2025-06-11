#Jacob Sexton Chapter 2 - Lab 1 6/11/2025
MARBLE_COST = 1.2
user_first = input('Enter your first name: ')
user_last = input('Enter your last name: ')
number_marbles = int(input('Enter the number of marbles you wish to purchase: '))

print("\n\nOrder prepared for", user_first, user_last)

total_cost = number_marbles * MARBLE_COST

print("\n", number_marbles, "marbles ordered @", MARBLE_COST)

print(f"\nTotal cost is ${total_cost:.2f}")
