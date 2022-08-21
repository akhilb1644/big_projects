from random import randint
import json
import inspect
import time

def search_list(list, item):
    for obj in list:
        if obj == item:
            return list.index(obj)
    return 0

def search_color_props(color):
    pass

class player:
    def __init__(self,name,position,jail_state,money,chest,chance,utils,rails,title_deeds):
        self.name = name
        self.position = position
        self.jail_state = jail_state
        self.money = money
        """
        Chest and chance variables are just for 'Get out of jail free' cards
        ...
        Or you could just pay $50(which in Monopoly isn't that much, can't even buy a single property),
        unless you used all your money for buying.rails or had to pay too much rent
        """
        self.chest = chest
        self.chance = chance
        self.utils = utils # Rent is based on dice number and number of utilities owned
        self.rails = rails # Rent is based on number of railways owned
        self.title_deeds = title_deeds
        try:
            self.properties = self.utils.extend + self.title_deeds + self.rails
        except TypeError:
            self.properties = []
        if len(self.title_deeds) > 0:
            self.colors = {'Brown':0,'Cyan':0,'Pink':0,'Orange':0,'Red':0,'Yellow':0,'Green':0,'Blue':0}
            for proper in self.title_deeds:
                self.colors[proper.color] += 1



    def move(self):
        while True:
            roll = 1
            d1,d2 = randint(1,6),randint(1,6) # Using 2 dice to check for doubles instead of 1 that is from 1-12
            time.sleep(1)
            print(f'Your roll is a {d1} and a {d2}')
            if d1 == d2:
                roll += 1
                time.sleep(0.5)
                print('You have to roll again because you got doubles')
                if roll > 3:
                    self.jail_state = True
                    print('You now have to go to jail because you got doubles 3 times in a row')
                    break
                continue

            self.position = self.position + d1 + d2
            time.sleep((d1+d2)*0.5)
            break

        if self.position > 39: # Pass Go and get 200
            self.money += 200
            print(f"{self.name} now has ${self.money} after earning $200 from passing GO.")
        self.position = self.position % 40

        if self.position == 30: # Go to jail block
            self.position = 10
            self.jail_state = True
        elif self.position == 10:
            print(f'Nothing to worry about {self.name}, you are just visiting jail.')
        elif self.position == 20:
            print(f'You are in free parking {self.name}, nothing happens here.')
        elif self.position == 38:
            self.money -= 100
            print(f'{self.name}, you just paid a luxury tax of $100, and now, your balance is ${self.money}')
        elif self.position == 4:
            self.money -= 200
            print(f'{self.name}, you had to pay an income tax of $200, your balance now is ${self.money}')

    def house_option(self):
        try:
            values = list(self.colors.values())
            colors = list(self.colors.keys())
            index = None
            q = 0
            if values[0] == 2:
                index = 0
                q = 2
            elif values[-1] == 2:
                index = len(values)-1
                q = 2

            for r in range(1,len(values)-1):
                if values[r] == 3:
                    index += r
                    q = 3
                    break
            if index != None:
                h = 200
                if index < 2:
                    h = 50
                elif index < 4:
                    h = 100
                elif index < 6:
                    h = 150
                print(f'{self.name}, you can now buy houses for your {colors[index]}, which will cost ${h*q}')
                return (h,colors[index])
            else:
                pass
        except AttributeError:
            pass

"""
There are 40 blocks between 'Go' and the block before 'Go' in the order that you are supposed to go in
...
But because indexes start from 0 and not 1, I am using 39 as the last block instead of 40. 40 is the same as 0 in this 
case.
"""
class Property:
    def __init__(self,position,name,price,owner,mortgage,mortgage_state,type):
        self.position = position
        self.name = name
        self.price = price
        self.owner = owner
        self.mortgage = mortgage
        self.mortgage_state = mortgage_state
        self.type = type

class Title_Deed(Property):
    def __init__(self,position,name,color,price,house_price,house_rent,hotel_rent,mortgage,houses,hotel_state,owner,mortgage_state,type='Title Deed'):
        super().__init__(position,name,price,owner,mortgage,mortgage_state,type)
        self.color = color
        self.house_price = house_price
        self.houses = houses
        self.hotel_state = hotel_state
        factor = 1
        count = 0
        if self.owner is not None:
            for p in self.owner.rails:
                if p.color == 'Blue' or p.color == 'Brown':
                    count += 1
                    if count == 2:
                        factor = 2
                elif p.color == 'Cyan' or p.color == 'Pink' or p.color == 'Orange' or p.color == 'Red' or \
                    p.color == 'Yellow' or p.color == 'Green':
                    count += 1
                    if count == 3:
                        factor = 2
        else:
            pass

        if not hotel_state:
            self.rent = house_rent[str(houses)] * factor
            if houses > 0:
                self.rent = self.rent / factor
        elif hotel_state:
            self.rent = hotel_rent * factor

class Railroad(Property):
    def __init__(self,position,name,price,owner,mortgage,mortgage_state,type='Railroad'):
        super().__init__(position,name,price,owner,mortgage,mortgage_state,type)
        self.rent = 25

class Utility(Property):
    def __init__(self,position,name,price,owner,mortgage,mortgage_state,type='Utility'):
        super().__init__(position,name,price,owner,mortgage,mortgage_state,type)

    def find_rent(self,roll):
        try:
            if len(self.owner.utils) == 2:
                return 10 * roll
            elif len(self.owner.utils) == 1:
                return 4 * roll
        except AttributeError:
            pass


class Chance:
    def __init__(self):
        pass

    def boardwalk(self,player):
        print("Advance to Boardwalk")
        player.position = 39

    def illinois(self,player):
        print("Advance to Illinois Avenue.\nIf you pass GO, you get $200.")
        if player.position > 24:
            player.money += 200
            print(f"Your Balance is now ${player.money} after passing GO")
        player.position = 24

    def reading(self,player):
        print("Advance to Reading Railroad")
        if player.position > 5:
            player.money += 200
            print(f"Your Balance is now ${player.money} after passing GO")
        player.position = 5

    def speeding_fine(self,player):
        print("Speeding Fine $15")
        player.money -= 15
        print(f"Your Balance is now ${player.money}")

    def building_loan(self,player):
        print("Your Building Loan Matures, You Get $150")
        player.money += 150

    def go(self,player):
        print("Advance to Go")
        player.position = 0
        player.money += 200
        print(f"Your Balance is now {player.money}")

    def general_repairs(self,player):
        print("Make general repairs on all properties\n$115 per hotel and $40 per house")
        price = 0
        for property in player.title_deeds:
            price += property.houses * 25
            if property.hotel_state:
                price += 100
        print(f"This will cost ${price}.")
        player.money -= price

    def jail_free(self,player):
        print("You got a GET OUT OF JAIL FREE card")

    def go_jail(self,player):
        print("Go Directly To Jail")
        player.position = 10
        player.jail_state = True

    def nearest_rail(self,player):
        print("Advance to nearest railroad.")
        if player.position < 5:
            player.position = 5
        elif player.position < 15:
            player.position = 15
        elif player.position < 25:
            player.position = 25
        elif player.position < 35:
            player.position = 35
        else:
            player.position = 5

    def back_three(self,player):
        print("Go back 3 spaces")
        player.position -= 3

    def nearest_rail_2(self,player): # It is the same as nearest_rail, but only because there are 2 cards in chance like this
        print("Advance to nearest railroad.")
        if player.position < 5:
            player.position = 5
        elif player.position < 15:
            player.position = 15
        elif player.position < 25:
            player.position = 25
        elif player.position < 35:
            player.position = 35
        else:
            player.position = 5

    def st_charles_place(self,player):
        print("Advance to St. Charles Place")
        if player.position > 11:
            player.money += 200
            print(f"Your Balance is now ${player.money} after passing GO")
        player.position = 11

    def charman_board(self,player,players):
        print("You have been elected chairman of the board. Give each player $50.")
        players.remove(player)
        for p in players:
            p.money += 50
            player.money -= 50

    def dividend(self,player):
        print("Bank pays you dividend of $50!")
        player.money += 50

class Chest:
    def __init__(self):
        pass

    def street_repairs(self,player):
        amount = 0
        print("You are assesed for street repairs\n$115 per hotel and $40 per house")
        for p in player.title_deeds:
            amount += p.houses * 40
            if p.hotel_state == True:
                amount += 115
        print(f"You must pay ${amount} for street repairs.")
        player.money -= amount

    def stock_sale(self,player):
        print("You get $50 from sale of stock")
        player.money += 50

    def consultancy_fee(self,player):
        print("You Recieve $25 consultancy fee")
        player.money += 25

    def school_fees(self,player):
        print("Pay school fees of $50")
        player.money += 50

    def inherit(self,player):
        print("You inherit $100")
        player.money += 100

    def bank_error(self,player):
        print("Bank error in your favor\nyou collect $200")
        player.money += 200

    def go_jail(self,player):
        print("Go to jail. And crossing GO does not earn you $200")
        player.position = 10
        player.jail_state = True

    def beauty_contest(self,player):
        print("You've won second place in beauty contest, you get $10")
        player.money += 10

    def income_tax_refund(self,player):
        print("You get $20 from income tax refund")
        player.money += 20

    def matured_life_insurance(self,player):
        print("Life insurance mature, you get $100")
        player.money += 100

    def matured_holiday_fund(self,player):
        print("Holiday fund matures, you get $100")
        player.money += 100

    def birthday(self,player,players):
        print("It's your birthday, you get $10 from each player")
        players.remove(player)
        for p in players:
            p.money -= 10
            player.money += 10

    def doctors_fees(self,player):
        print("Pay doctors fees of $50")
        player.money -= 50

    def go(self,player):
        print("Advance to GO and get $200")
        player.position = 0
        player.money += 200

    def jail_free(self,player):
        print("You get a get out of jail free card!")

def chance_methods():
    chance_methods = inspect.getmembers(Chance)
    deck = []
    for c in chance_methods:
        if c[0].startswith('__') == False:
            deck.append(c)
    return deck

def chest_methods():
    chest_methods = inspect.getmembers(Chest)
    deck = []
    for c in chest_methods:
        if c[0].startswith('__') == False:
            deck.append(c)
    return deck
