#from blackjack import *

# _deal_card  is not imported with * as it is protected member(as you can see it's missing from globals())
# g = sorted(globals())
#
# for x in g:
#     print(x)

#
import blackjack
blackjack._deal_card(blackjack.dealer_card_frame) #blackjack is explicitly imported (would give protected warning)
blackjack.play()
print(blackjack.cards)
