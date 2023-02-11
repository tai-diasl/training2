print('''
   .
  .
 . .
  ...
\~~~~~/
 \   /
  \ /
   V
   |
   |
  ---
''')

print("Welcome to the Tip Calculator!\n")

bill = float(input("What was the total bill? €"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

total = bill * (1 + tip / 100)

each = round(total / people, 2)

print(f"\nEach person should pay €{each}")
