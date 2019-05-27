digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit','neuf']
jap = ['ichi', 'ni', 'san', 'shi', 'go', 'roku', 'shichi', 'hachi', 'ku']

numbers = {}

for num in range(0, len(digits)):
  numbers[digits[num]] = {
    'french': fr[num],
    'english': en[num],
    'japanese': jap[num]
  }

print(numbers)