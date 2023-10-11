cards: str = "5682"
card_idx: int = 0
low_card: int = int(cards[0])
while card_idx < 4:
    #check if current card is less than low card
    current_card: int = int(cards[card_idx])
    if current_card < low_card:
        low_card = current_card
    card_idx += 1
print(low_card)