def check_syntax(str):
  openables = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
  }
  open = []
  opening_chars = openables.keys()
  closing_chars = openables.values()

  for char in list(str):

    if char in opening_chars: # opening bracket

      open.append(char)

    elif char in closing_chars: # closing bracket

      if open:
        required_char = openables[open[-1]]

        if char == required_char: # it's the right kind of closing bracket

          open.pop()

        else: # it's the wrong kind of closing bracket
          print("* You have a syntax error: there is an unexpected {} where there should be a {}.".format(char, required_char))
          return False

      else: # there's nothing to close
        print("* You have a syntax error: there is an unexpected {} where there is nothing to close.".format(char))

        return False



  if len(open) > 0:
    required_char = openables[open[-1]]
    print("* You have a syntax error: the string ended without a closing {}.".format(required_char))

  return not open

print(check_syntax("<html> (this)[] is some text</html>"))
print("*****")
print(check_syntax("<html> (this)] is some text</html>"))
print("*****")
print(check_syntax("<html> [(this] is some text</html>"))
print("*****")
print(check_syntax("<html> [this][ is some text</html>"))
print("*****")
print(check_syntax("<html> [this] is some text</html"))