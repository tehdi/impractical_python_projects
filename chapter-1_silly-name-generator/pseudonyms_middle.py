#!/usr/local/bin/python3

"""Generate nicknames in the style of Psych.

Variation: The Middle

Rewrite the funny name generator code to include middle names. First,
create a new middle_name tuple, then split apart existing first name–middle
name pairs (such as “Joe ‘Pottin Soil’” or “Sid ‘The Squirts’”) and add
them to the tuple. You should also move some obvious nicknames (like
“Oil Can”) to your middle_name tuple. Finally, add some new middle names
(such as “The Big News,” or “Grunts,” or “Tinkie Winkie”). Use Python’s
random module so that a middle name is chosen only one-half or one-third
of the time.
"""

import random

MIDDLE_NAME_PERCENT_CHANCE = 40


def main():
    """Generate and print a sidekick name.

    Randomly choose a first name and a last name from the tuples of names,
    sometimes throw in a middle name for extra funsies,
    then print the result to stdout.
    """
    print('Welcome to the Pysch Sidekick Name Picker')
    print("where we build names just like Sean does for his pal Gus")
    print('or should we say...')
    first_names = (
        'Bill', 'Bob', 'Boxelder', 'Bud', 'Butterbean', 'Buttermilk',
        'Buttocks', 'Chad', 'Chesterfield', 'Chewy', 'Chigger', 'Cinnabuns',
        'Cleet', 'Cornbread', 'Crapps', 'Dennis', 'Dicman', 'Elphonso',
        'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Huckleberry', 'Huggy',
        'Ignatious', 'Joe', 'Johnny', 'Lemongrass', 'Lil Debil', 'Longbranch',
        'Mergatroid', 'Oinks', 'Ovaltine', 'Pennywhistle', 'Pitchfork Ben',
        'Pushmeet', 'Schlomo', 'Scratchensniff', 'Scut', 'Sid', 'Skidmark',
        'Slaps', 'Snakes', 'Snoobs', 'Snorki', 'Soupcan Sam', 'Spitzitout',
        'Squids', 'Stinky', 'Storyboard', 'TeeTee', 'Wheezy Joe', 'Winston',
        'Worms')

    middle_names = (
        'Bowel Noises', 'Big Burps', 'Rock Candy', 'Sweet Tea', 'Bad News',
        'Baby Oil', 'Beenie-Weenie', 'Stinkbug', 'Lite', 'Clawhammer',
        'Lunch Money', 'Potato Bug', 'Old Scratch', 'Greasy Jim', 'Grunts',
        'Mr Peabody', 'Oil-Can', 'Jimbo', 'Dark Skies', 'Crab Meat',
        'Pottin Soil', 'The Squirts', 'Jazz Hands', 'The Big News',
        'Tinkie Winkie')

    last_names = (
        'Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
        'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
        'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
        'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
        'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
        'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
        'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
        'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
        'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
        'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
        'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
        'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
        'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
        'Woolysocks')

    while True:
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)

        if random.randrange(0, 100) < MIDDLE_NAME_PERCENT_CHANCE:
            middle_name = random.choice(middle_names)
            print('{} "{}" {}'.format(first_name, middle_name, last_name))
        else:
            print('{} {}'.format(first_name, last_name))
        print()

        again = input('Another? (y/n) ')
        if again.lower() == 'n':
            break


if __name__ == "__main__":
    main()
