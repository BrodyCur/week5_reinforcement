nil = None

rows = [
  [None, "Pumpkin", None, None],
  ["Socks", nil, "Mimi", None],
  ["Gismo", "Shadow", None, None],
  ["Smokey","Toast","Pacha","Mau"]
]


def seat_picker():
  x = 0
  for row in rows:
    y = 0
    for seat in row:
      if seat == None:
        print(f"Row {x + 1}, seat {y + 1} is free. Do you want to sit there? (y/n)")
        sitter_input = input()
        if sitter_input == 'y':
          print("What is your name?")
          sitter_name = input()
          row[y] = sitter_name
          return
        elif sitter_input != 'n':
          print('Improper input')
          #How do I got back to the last if statement from here?
      y += 1
    x += 1      


seat_picker()

print(rows)