import random

deck = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]

    

class Player:
    def __init__(self):
        self.hand=[]
    def draw(self):
        i=deck[0]
        del deck[0]
        print(f'You drew a {i}')
        self.hand.append(i)
    def gethand(self):
        return sum(self.hand)
    
class Dealer:
    def __init__(self):
        self.hand=[]
    def draw(self):
        i=deck[0]
        del deck[0]
        print(f'The dealer drew a {i}')
        self.hand.append(i)    
    def gethand(self):
        return sum(self.hand)
    
def main():
    #code
    random.shuffle(deck)
    player=Player()
    dealer=Dealer()
    player.draw()
    player.draw()
    dealer.draw()
    dealer.draw()
    print('Your hand: ',player.gethand())
    print("Dealer's hand ",dealer.gethand())
    inp=input('Hit or stand? ')
    while inp !='hit' and inp != 'Hit' and inp != 'stand' and inp != 'Stand':
            print("invalid input")
            inp=input('Hit or stand? ')
    while inp == 'hit' or inp =='Hit':
        player.draw()
        print('Your hand: ',player.gethand())
        print("Dealer's hand ",dealer.gethand())
        if player.gethand()==21:
            print('Blackjack, you win.')
            exit()
        elif player.gethand() > 21:
            print('Bust, dealer wins')
            exit()
        inp=input('Hit or stand? ')
        while inp !='hit' and inp != 'Hit' and inp != 'stand' and inp != 'Stand':
            print("invalid input")
            inp=input('Hit or stand? ')
        if inp == 'stand' or inp=='Stand':
            break
        
    while dealer.gethand() < 17:
        dealer.draw()
    print('Your hand: ',player.gethand())
    print("Dealer's hand ",dealer.gethand())
    if dealer.gethand() >21:
        print('Bust, you win')
    elif dealer.gethand()==21:
        print('Blackjack, dealer wins.')
    elif dealer.gethand() > player.gethand():
        print('Dealer wins')
    elif dealer.gethand() < player.gethand():
        print('you win')
    elif dealer.gethand() == player.gethand():
        print('draw')
    
    return


if __name__ == '__main__':
    main()