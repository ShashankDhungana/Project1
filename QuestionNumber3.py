'''3. N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains
in the basket. How many apples will each single student get? How many apples will remain in the basket?
The program reads the numbers N and K. It should print the two answers for the questions above.'''

n = int(input('number of students:'))
k = int(input('number of apples:'))
distribute = k // n
remaining = k%n
print(f'Each student will get {distribute} apples equally')
print(f' The remaining number of apple in the basket: {remaining}')
