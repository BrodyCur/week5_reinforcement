def select_cards(possible_cards, hand):

  for current_card in possible_cards:
    print("Do you want to pick up {}?".format(current_card))
    answer = input()
    if answer.lower() == 'y':
      hand.append(current_card)
      continue
    elif answer.lower() == 'n':
      continue

    return hand

available_cards = ['queen of spades', '2 of clubs', '3 of diamonds', 'jack of spades', 'queen of hearts']

new_hand = []

select_cards(available_cards, new_hand)

display_hand = "\n".join(new_hand)

print("Your new hand is: \n{}".format(display_hand))