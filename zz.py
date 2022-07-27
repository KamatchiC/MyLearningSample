fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    count = count + 1
print('There are', count, 'lines in', fname)

str="ameyra"
s=str.upper()
print(s)

answer = input("What color is the sun? ")
if answer == "yellow":
  print("Correct!")
else:
  print("That is not the correct color!")