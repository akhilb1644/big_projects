from game import *
import json
from random import *
import inspect
import time

# This sets up the monopoly
property_deck = 'properties.json'
with open(property_deck) as deck:
    props = json.load(deck)

cc_spots = 'chance_and_chest_spots.json'
with open(cc_spots) as cc_s:
    cc_positions = json.load(cc_s)

chances = cc_positions["Chance"]
chests = cc_positions["Chest"]

cecs = chest_methods()
cacs = chance_methods()

chest_cards = []
chance_cards = []

def random_sort(c,d):
    for h in range(len(c)):
        e = choice(c)
        c.remove(e)
        d.append(e)

random_sort(cecs,chest_cards)
random_sort(cacs,chance_cards)

prop_cards = []
for prop in props:
    if prop["Type"] == "Title Deed":
        prop_cards.append(Title_Deed(prop["Position"],prop["Name"],prop["Color"],prop["Price"],prop["Per-House Price"],
                               prop["House Rent"],prop["Hotel Rent"],prop["Mortgage"],0,False,None,False))
    elif prop["Type"] == "Utility":
        prop_cards.append(Utility(prop["Position"],prop["Name"],prop["Price"],None,prop["Mortgage"],False))
    elif prop["Type"] == "Railroad":
        prop_cards.append(Railroad(prop["Position"],prop["Name"],prop["Price"],None,prop["Mortgage"],False))

players_num = int(input("Hello, this is monopoly. Could you please tell me how many people are playing\n"))
players = []
for i in range(players_num):
    name = input(f'Hello Player {i+1}, please tell me your name.')
    players.append(player(name,0,False,1500,[],[],[],[],[]))

order = dict()
for player in players:
    roll = randint(1,12)
    order[player] = roll

sorted_rolls = sorted(list(order.values()))
players = []

for i in range(-1,-1-len(sorted_rolls),-1): #Highest rolls to lowest rolls
    roll = sorted_rolls[i]
    for player in order:
        if order[player] == roll:
            players.append(player) # This is the order of the players

hotels,houses = 12,32

# All the functions in the program are below
def is_on_prop(position,deck=prop_cards):
    y = -3
    for prop in deck:
        if prop.position == position:
            y = prop
        else:
            continue
        return y
    return y

def color_find(property):
    if property.color == 'Brown' or property.color == 'Blue':
        return 2
    elif property.color == 'Cyan' or property.color == 'Pink' or property.color == 'Orange' or \
        property.color == 'Red' or property.color == 'Yellow' or property.color == 'Green':
        return 3

def mortgage_time(player,target = 0,houses = houses,hotels = hotels):
    while player.money < target:
        umps = [] # Collects unmortgaged properties
        for pr in player.properties:
            if pr.mortgage_state == True:
                pass
            else:
                umps.append(pr)
        for index2,u in enumerate(umps):
            if u.type == "Title Deed":
                q = color_find(u)
                if u.hotel_state == True:
                    print(f"{index2 + 1}) {u.name} comes for {(u.house_price * 5 * q * 0.5) + u.mortgage}")
                else:
                    print(f"{index2 + 1}) {u.name} comes for {(u.house_price * u.houses * q * 0.5) + u.mortgage}")
            elif u.type == "Raillroad" or "Utility":
                print(f"{index2 + 1}) {u.name} comes for {u.mortgage}")

        ind = int(input("Choose which property(with the number) to mortgage(houses or hotels for mortgaged properties are"
                        "sold for EACH PROPERTY OF THE SAME COLOR GROUP. Press 'q' to end the mortgaging session."))
        if ind == 'q':
            break
        ind -= 1 # Adjusting the number chosen to the actual index
        umps[ind].mortgage_state = True
        if umps[ind].type == "Title Deed":
            player.money += umps[ind].mortgage + (umps[ind].house_price * 0.5 * umps[ind].houses)
            if umps[ind].hotel_state == True:
                player.money += umps[ind].house_price * 0.5 * 5
                umps[ind].hotel_state = False
            for ump in umps:
                try:
                    if ump.color == umps[ind].color:
                        player.money += ump.houses * 0.5 * ump.house_price
                        ump.houses = 0
                        if ump.hotel_state == True:
                            player.money += ump.house_price * 0.5 * 5
                            ump.hotel_state = False
                        elif ump.hotel_state == False:
                            pass
                except AttributeError:
                    pass
        elif umps[ind].type == "Railroad" or umps[ind] == "Utility":
            player.money += umps[ind].mortgage
        umps.remove(umps[ind])
        print(f"Your balance is now ${player.money}")

def selling_time(player,target = 0):
    while player.money < target:
        hps = [] # Collects properties with houses
        for pr in player.title_deeds:
            if pr.houses > 0:
                hps.append(pr)
        if len(hps) > 0:
            choice = int(input(f"Do you want to sell buildings(0) or properties(1), choose the number next to the option"
                               f" you want to pick. Press 'q' to end the selling session. "))
            if choice == 0:
                for i,hp in enumerate(hps):
                    q = color_find(hp)
                    print(f'{i+1}. {hp.houses} houses from {hp.name} for ${hp.house_price * hp.houses * q}')
                ind = int(input(
                    "Choose which property(with the number) to mortgage(houses or hotels for mortgaged properties are"
                    "sold for EACH PROPERTY OF THE SAME COLOR GROUP. Press 5 to end the mortgaging session."))
                ind -= 1
                hp = hps[ind]
                player.money += hp.house_price * hp.houses * color_find(hp)
                for pro in hps:
                    if pro.color == hp.color:
                        pro.houses = 0
                        pro.hotel_state = False
                        hps.remove(pro)

        else:
            choice = int(input(f"Do you want to sell properties(1)? Choose the number next to the option. To end the "
                               f"selling session, press 5."))
        if choice == 1:
            for index2,pt in enumerate(player.properties):
                if pt.type == 'Title Deed':
                    if pt.hotel_state == False:
                        print(f"{index2 + 1}. {pt.name} comes for {pt.price * 0.5 + (pt.houses * 0.5 * pt.house_price * color_find(pt))}")
                    elif pt.hotel_state == True:
                        print(f"{index2 + 1}. {pt.name} comes for {pt.price * 0.5 + pt.house_price * 0.5 * 5}")
                elif pt.type == 'Utility' or 'Railroad':
                    print(f"{index2 + 1}. {pt.name} comes for {pt.price * 0.5}")
            index3 = int(input("Choose the property you would like to sell"))
            i = player.properties[index3 - 1]
            if i.type == "Title Deed":
                if i.hotel_state == True:
                    player.money += i.house_price * 5 * 0.5 + i.price * 0.5
                elif i.hotel_state == False:
                    player.money += i.house_price * i.houses * 0.5 + i.price * 0.5
                for prop in player.properties:
                    try:
                        if prop.color == i.color:
                            player.money += prop.houses * 0.5 * prop.hosue_price + prop.price * 0.5
                        else:
                            pass
                    except AttributeError:
                        pass
            elif i.type == "Utility" or i.type == "Railroad":
                player.money += i.price * 0.5

        elif choice == 5:
            break
        if player.money < 0:
            print(f'{player.name}, you still have to get ${player.money * -1}.')
        elif target > player.money:
            key= input(f'{player.name}, press \'q\' to end the selling session. To go on, press any other letter.')
        try:
            if key == 'q':
                break
        except NameError:
            pass


def play(player,players=players,houses=houses):
    response = input(f'Hello {player.name}. Press any letter(except q) and \'enter\' to move. Press \'q\' to quit.\n')
    if response.lower() == 'q':
        return -1
    else:
        player.move()
        road = 0
        try:
            area = chests.index(player.position)
            road = 1
            card = None
        except ValueError:
            try:
                area = chances.index(player.position)
                road = 2
                card = None
            except ValueError:
                pass

        if road == 1:
            card = chest_cards[0]
            chest_cards.remove(card)
            print("Community Chest:")
            try:
                card[1](player,player)
            except TypeError:
                card[1](player,player,players)
            if card[0] == 'jail_free':
                player.chest.append(card)

        elif road == 2:
            card = chance_cards[1]
            chance_cards.remove(card)
            print("Chance:")
            try:
                card[1](player,player)
            except TypeError:
                card[1](player,player,players)
            if card[0] == 'jail_free':
                player.chance.append(card)

        if road > 0:
            chest_cards.append(card)


        if player.jail_state == True:
            return -6
        result = is_on_prop(player.position)
        if type(result) != int:
            print(f"{player.name}, you landed on {result.name}")
        if type(result) == int:
            return result
        elif result.owner == None:
            choice = int(input(f"Would you like to buy {result.name} for ${result.price} (0 for no and 1 for yes)."))
            if (result.price > player.money and choice == 1):
                print("You cannot buy this property as you do not have enough money")
            if (result.price > player.money and choice == 1) or choice == 0:
                print("It's auction time!")
                return -4
            if choice == 1:
                if result.type == 'Railroad':
                    player.rails.append(result)
                    for rail in player.rails:
                        rail.rent = 25 * (2 ** (len(player.rails)-1))
                elif result.type == 'Utility':
                    result.owner = player
                    player.utils.append(result)

                else:
                    player.title_deeds.append(result)
                player.money -= result.price
                result.owner = player
        elif result.owner == player:
            pass
        else:
            return (result,7)

jail_count = 0
pl_ind = 0
jail_help = 0
code = 0
# Main program is below
while True:
    val = -2  # Makes the variable local to the while loop, not just the for loop
    while True:
        player = players[pl_ind % len(players)]

        if player.jail_state == True:
            if jail_count != 0:
                print(f"A dice will be rolled to determine whether you can get out of jail {player.name}. You get out of jail if you get doubles.")
                d1,d2 = randint(1,6),randint(1,6)
                print(f"Your roll was {d1} and {d2}")
                if d1 == d2:
                    print(f"{player.name}, you got doubles, and can get out of jail")
                    player.jail_state = False
                    jail_count = 0
                    continue
                elif jail_count == 3:
                    print(f'{player.name}, you have finished your stint(3 turns) in jail, so you get to come out')
                    player.jail_state = False
                    jail_count = 0
                    continue
                else:
                    jail_count += 1
            else:
                tide = 0
                try:
                    if player.chance[0] == 'jail_free':
                        tide = int(input('Would you like to use your get out of jail free card to get out of jail? (0 for no, 1 for yes)?'))
                except IndexError:
                    pass
                if len(player.chance) == 0 or tide == 0:
                    c = int(input("Would you pay $50 to get out of jail(1 for yes, 0 for no)"))
                    if c == 1:
                        player.jail_state = False
                        player.money -= 50
                    else:
                        jail_count += 1
                        pass

        else:
            pre = player.position + 0
            val = play(player)
            post = player.position + 0
            dice_roll = post - pre
            r = 0
            if type(val) == tuple:
                val = val[0]
                if val.type != 'Utility':
                    player.money -= val.rent
                    val.owner.money += val.rent
                else:
                    player.money -= val.find_rent(dice_roll)
                    val.owner.money += val.find_rent(dice_roll)
                if player.money < 0:
                    print(f"You don't have enough money, you still need to pay ${player.money * -1} more.")
                    path = int(input("Would you like to mortgage(1), sell property(2), type the numbers in the "
                                     "parentheses and ENtER to choose that path."))
                    if path == 1:
                        while player.money < 0:
                            mortgage_time(player)
                            selling_time(player)

                else:
                    if val.type != 'Utility':
                        print(f'{player.name} had to pay {val.owner.name} ${val.rent} for landing on {val.name}')
                    else:
                        print(f'{player.name} had to pay {val.owner.name} ${val.find_rent(dice_roll)} for landing on {val.name}')

                print(f'Player {player.name} balance is ${player.money}.')
                print(f'Player {val.owner.name} balance is now ${val.owner.money}.\n')
            if val == -1: # Breaks out of for loop
                break
            elif val == -6:
                continue
            else:
                if val == None or val == -3:
                    pass
                elif type(val) != int:
                    if val.mortgage_state == True:
                        pass
                elif val == -4:
                    pass

            option = player.house_option()

            if option == None:
                pass
            elif type(option) == tuple:
                fork = int(input("Type 1 for yes, and 0 for no. Type ENTER after whichever one you choose"))
                if fork == 1:
                    print(f"Your current balance is ${player.money}\n")
                    quantity = int(input("How many houses do you want(1, 2, 3, or 4). Or do you want hotel(5). You buy houses for 1, buy it"
                                         " for the others."))
                    player.money -= option[0] * quantity
                    yn = 0
                    if quantity == 4:
                        yn = int(input(f"Do you want to replace your 4 houses with a hotel(0=no, 1=yes,"
                                   f" ENTER after whichever option.) You get more rent(check json file if needed)."
                                       f" But you have to pay ${option[0]} extra"))
                    elif quantity == 5:
                        yn = 1

                    for td in player.properties:
                        try:
                            if td.color == option[1]:
                                if yn == 0:
                                    td.houses += quantity
                                elif yn == 1:
                                    td.hotel_state = True
                                    td.houses += quantity
                        except AttributeError:
                            pass

                elif fork == 0:
                    pass

            if val == -4:
                index1 = players.index(player) - 1
                mgold = 0
                for proper in prop_cards:
                    if player.position == proper.position:
                        mgold = proper
                        break
                bid = 0
                bid0 = 0
                bidders = players.copy()
                while True:
                    index1 = (index1 + 1) % len(bidders)
                    bidder = bidders[index1]
                    if bid == 0:
                        bid0 = int(input(f"{bidder.name}, how much do you bid for {mgold.name} worth ${mgold.price}, "
                                     f"bid starts at ${bid}\n (Enter 0 to drop from the bid)? "))
                        bid = bid0
                    else:
                        bid0 = int(input(f"{bidder.name}, how much do you bid for {mgold.name}, the bid has reached ${bid}"
                                     f". Value of property is ${mgold.price}\n"
                                     f"(Enter 0 or a value lower than the bid to drop form the bid)? "))
                        if bid < bid0:
                            bid = bid0
                    if bid0 == 0 or bid > bid0:
                        bidders.remove(bidder)
                    if len(bidders) == 1:
                        bidder = bidders[0]
                        if bid > bidder.money:
                            plan = int(input(f"Because you need ${bid - bidder.money}, would you like to mortgage any of your"
                                         f" properties(0), sell any properties(1)"))
                            if plan == 0:
                                mortgage_time(bidder)
                            if plan == 1:
                                selling_time(bidder)
                        print(f"The bid has ended. {mgold.name} will go to {bidder.name} for ${bid}")
                        bidder.money -= bid
                        print(f'{bidder.name}, you now have ${bidder.money}')
                        if mgold.type == 'Title Deed':
                            bidder.title_deeds.append(mgold)
                        elif mgold.type == 'Utility':
                            bidder.utils.append(mgold)
                        elif mgold.type == 'Railroad':
                            bidder.rails.append(mgold)
                        break

            elif val == -6:
                continue

            while player.money < 0:
                plan = int(input(f"Because you need {-1 * player.money}, would you like to mortgage any of your"
                                 f" properties(0), sell any properties(1)"))
                if plan == 0:
                    mortgage_time(player)
                if plan == 1:
                    selling_time(player)

            player.properties = player.rails + player.utils + player.title_deeds
            if len(player.properties) != 0:
                print(f"{player.name}, you have ${player.money}, and your properties are: ")
                for p in player.properties:
                    if p.type == 'Title Deed' or p.type == 'Railroad':
                        print(f" - {p.name} is a {p.type} with rent value of ${p.rent}")
                    elif p.type == 'Utility':
                        if len(player.utils) == 1:
                            print(f" - {p.name} is a {p.type} with rent as 4 times dice roll.")
                        elif len(player.utils) == 2:
                            print(f" - {p.name} is a {p.type} with rent as 10 times dice roll.")
                    time.sleep(0.4)
            else:
                print(f"{player.name}, you have ${player.money}")

            print("\n")

        pl_ind += 1

        if val == -1: # Breaks out of the while loop
            code -= 1
            break

    if code == -1:
        break
