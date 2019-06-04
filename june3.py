numbers = range(1, 51)

new_numbers = {}

for num in numbers:
  if num % 2 == 0 and num % 7 == 0:
    new_numbers.update( {num: num * 2} )
  elif num % 7 == 0:
    new_numbers.update( {num: num - 1 } )
  elif num % 2 == 0:
    new_numbers.update( {num: num + 1} )
  else:
    new_numbers.update( {num: num} )

print(new_numbers)