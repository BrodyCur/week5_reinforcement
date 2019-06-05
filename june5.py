import inflect
# pip install inflect if not already installed
# https://pypi.org/project/inflect/

def show_ordinal():
    p = inflect.engine()
    print('Please enter a number')
    user_number = int(input())
    print(p.ordinal(user_number))

show_ordinal()