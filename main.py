import random

deck = [11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]

    

    
def ddraw():
    i=deck[0]
    del deck[0]
    print(f'The dealer drew a {i}')
    return i
    
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
    if player.gethand() == 21 and dealer.gethand() == 21:
        print('draw')
    elif player.gethand()==21:
        print('Blackjack, you win.')
    elif dealer.gethand()==21:
        print('Blackjack, dealer wins.')
    elif player.gethand() > 21:
        print('Bust, dealer wins')
    elif dealer.gethand() >21:
        print('Bust, you win')
    else:
        inp=input('Hit or stand? ')
        while inp == 'hit' or 'Hit':
            player.draw()
            print('Your hand: ',player.gethand())
            print("Dealer's hand ",dealer.gethand())
            if player.gethand()==21:
                print('Blackjack, you win.')
                break
            elif player.gethand() > 21:
                print('Bust, dealer wins')
                break
            inp=input('Hit or stand? ')
        if inp == 'Stand' or 'stand':
            while dealer.gethand() < 17:
                dealer.draw()
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