import random, uuid, math
from typing import NamedTuple
from datetime import date

default_player_names = ("Meteor Heartfelt","Razor Defrost","Jasper Groove","Thalia Soliloque","Benedict Dicetower","Bingo Polaroid","Pumpernickel Fan","Baby Bop","Tantalus Chewed","Freddie Missouri","Load Bearing Coconut", "Frankle Knives", "Spooks McGee")
    


def random_player_emoji(rng):
    humanoid = ["👶","👧","🧒","👦","👩","🧑","👨","👩‍🦱","🧑‍🦱","👨‍🦱","👩‍🦰","🧑‍🦰","👨‍🦰","👱‍♀️",
"👱","👱‍♂️","👩‍🦳","🧑‍🦳","👨‍🦳","👩‍🦲","🧑‍🦲","👨‍🦲","🧔","👵","🧓","👴","👲","👳‍♀️",
"👳","👳‍♂️","🧕","👮‍♀️","👮","👮‍♂️","👷‍♀️","👷","👷‍♂️","💂‍♀️","💂","💂‍♂️","🕵️‍♀️","🕵️",
"🕵️‍♂️","👩‍⚕️","🧑‍⚕️","👨‍⚕️","👩‍🌾","🧑‍🌾","👨‍🌾","👩‍🍳","🧑‍🍳","👨‍🍳","👩‍🎓","🧑‍🎓","👨‍🎓","👩‍🎤",
"🧑‍🎤","👨‍🎤","👩‍🏫","🧑‍🏫","👨‍🏫","👩‍🏭","🧑‍🏭","👨‍🏭","👩‍💻","🧑‍💻","👨‍💻","👩‍💼","🧑‍💼","👨‍💼",
"👩‍🔧","🧑‍🔧","👨‍🔧","👩‍🔬","🧑‍🔬","👨‍🔬","👩‍🎨","🧑‍🎨","👨‍🎨","👩‍🚒","🧑‍🚒","👨‍🚒","👩‍✈️","🧑‍✈️",
"👨‍✈️","👩‍🚀","🧑‍🚀","👨‍🚀","👩‍⚖️","🧑‍⚖️","👨‍⚖️","👰","🏋️","🤵","🤸","👸","🤴","🦸‍♀️","🦸",
"🦸‍♂️","🦹‍♀️","🦹","🦹‍♂️","🤶","🚴","🎅","🧙‍♀️","🧙","🧙‍♂️","🧝‍♀️","🧝","🧝‍♂️","🧛‍♀️","🧛",
"🧛‍♂️","🧟‍♀️","🧟","🧟‍♂️","🧞‍♀️","🧞","🧞‍♂️","🧜‍♀️","🧜","🧜‍♂️","🧚‍♀️","🧚","🧚‍♂️","👼","🤰",
"🤱","🙇‍♀️","🙇","🙇‍♂️","💁‍♀️","💁","💁‍♂️","🙅‍♀️","🙅","🙅‍♂️","🙆‍♀️","🙆","🙆‍♂️","🙋‍♀️","🙋",
"🙋‍♂️","🧏‍♀️","🧏","🧏‍♂️","🤦‍♀️","🤦","🤦‍♂️","🤷‍♀️","🤷","🤷‍♂️","🙎‍♀️","🙎","🙎‍♂️","🙍‍♀️","🙍",
"🙍‍♂️","💇‍♀️","💇","💇‍♂️","💆‍♀️","💆","💆‍♂️","🧖‍♀️","🧖","🧖‍♂️","💅","🤳","💃","🕺","🕴","👩‍🦽",
"🧑‍🦽","👨‍🦽","👩‍🦼","🧑‍🦼","👨‍🦼","🚶‍♀️","🚶","🚶‍♂️","👩‍🦯","🧑‍🦯","👨‍🦯","🧎‍♀️","🧎","🧎‍♂️","🏃‍♀️","🏃",
"🏃‍♂️","🧍‍♀️","🧍","🧍‍♂️","👭","🧑‍🤝‍🧑","👬","👫","👩‍❤️‍👩","💑","👨‍❤️‍👨","👩‍❤️‍👨","👩‍❤️‍💋‍👩","💏","👨‍❤️‍💋‍👨","👩‍❤️‍💋‍👨",
"👪","👨‍👩‍👦","👨‍👩‍👧","👨‍👩‍👧‍👦","👨‍👩‍👦‍👦","👨‍👩‍👧‍👧","👨‍👨‍👦","👨‍👨‍👧","👨‍👨‍👧‍👦","👨‍👨‍👦‍👦","👨‍👨‍👧‍👧","👩‍👩‍👦","👩‍👩‍👧","👩‍👩‍👧‍👦","👩‍👩‍👦‍👦","👩‍👩‍👧‍👧",
"👨‍👦","👨‍👦‍👦","👨‍👧","👨‍👧‍👦","👨‍👧‍👧","👩‍👦","👩‍👦‍👦","👩‍👧","👩‍👧‍👦","👩‍👧‍👧","🗣","👤","👥"]

    nonhumanoid=[
"🐶","🐱","🐭","🐹","🐰","🦊","🐻","🐼","🐨","🐯","🦁","🐮","🐷","🐽","🐸","🐵",
"🙈","🙉","🙊","🐒","🐔","🐧","🐦","🐤","🐣","🐥","🦆","🦅","🦉","🦇","🐺","🐗","🐴","🦄",
"🐝","🐛","🦋","🐌","🐞","🐜","🦟","🦗","🕷️","🦂","🐢","🐍","🦎","🦖","🦕","🐙","🦑","🦐",
"🦞","🦀","🐡","🐠","🐟","🐬","🐳","🐋","🦈","🐊","🐅","🐆","🦓","🦍","🦧","🐘","🦛","🦏",
"🐪","🐫","🦒","🦘","🐃","🐂","🐄","🐎","🐖","🐏","🐑","🦙","🐐","🦌","🐕","🐩","🦮","🐕‍🦺",
"🐈","🐓","🦃","🦚","🦜","🦢","🦩","🕊️","🐇","🦝","🦨","🦡","🦦","🦥","🐁","🐀","🐿","🦔",
"🐉","🐲","🪐","💫","🌪","🌈","📠","📺"]

    if rng.random() > 0.5:
        return rng.choice(humanoid)
    else:
        return rng.choice(nonhumanoid)

class PlayerStlats(NamedTuple):
    stance: str = "Incredibly boring"
    fav_tea: str = "Iced"
    nyoomability: float = 1.5           # movement speed

    # unused for now except for fun
    tofu: float = 4
    wiggle: float = 0.5 # chance someone about to bump into a swordfight holds back instead
    ritualism: float = 2

    unworthiness: float = 0.5
    splortsmanship: float = 1.0
    tankitude: float = 1.0
    pettiness: float = 0.0
    owlishness: float = 0.0
    disco: float = 0.0
    pettability: float = 0.0
    softness: float = 0.0
    improv: float = 0.0
    tentacles: int = 1
    capitalism: float = -0.5

    # shot power stats
    musclitude: float = 1.0             # how hard you swing
    finesse: float = 1.0                # how consistent your shots are hit with power, higher = better
    estimation: int = 0

    # swordfighting stlats
    churliness: float = 0.2 # how likely this player will go for offensive options in a swordfight
    earliness: float = 0.2 # how likely this player will go for defensive options in a swordfight
    twirliness: float = 0.2 # how likely this player will go for stylish options in a swordfight
    aceness: float = 0.3 # chance of resisting a kiss
    marbles: int = 3 # beginning-of-fight swordfighting hp

    polkadottedness: int = 0 # used for easter egg

    # shot angle stats
    needlethreadableness: float = 0.8   # how well you thread the needle (multiplier for how much angle variance your shots have), lower = better
    left_handedness: float = 0.0        # how biased your shots are to the left or right. can go negative, 0 = best

class Player:
    def __init__(self, name:str, stlats: PlayerStlats, emoji:str="🏌️", id:str="",modifications=None):
        self.name = name
        self.stlats = stlats
        self.emoji = emoji
        self.id = id

        self.modifications = []
        if modifications is not None:
            self.modifications = modifications
        

    def unpredictability(self): 
        # how much someone sticks to one swordfighting style. 0-1, 1 = better
        # if someone will always choose offensive, this is 0. if it's split evenly betwen churliness, earliness, and twirliness, it's 1
        weights = [self.stlats.churliness,self.stlats.earliness,self.stlats.twirliness]
        if self.stlats.stance in ("Aggro","Powerful","Hand to Hand","DPS","Explosive","Hardcore", "Wibble","Electric"): #offense-boosting stances
            weights[0] += 0.5
        # earliness-boosting stances
        elif self.stlats.stance in ("Tanky","Twitchy","Repose","Reverse","Softcore",  "Cottagecore","Pomegranate"): # defense-boosting stances
            weights[1] += 0.5
        #twirliness-boosting stances
        if self.stlats.stance in ("Feint","Tricky","Pop-Punk","Flashy","Spicy",       "Corecore","Wobble","Lefty"): # style-boosting stances
            weights[2] += 0.5

        weights = sorted(weights, reverse=True)

        chanceOfBiggest = weights[0]/sum(weights) #this ranges from highest = 1 to lowest = 1/len(weights)

        minChance = 1/len(weights)

        return 1-(chanceOfBiggest-minChance)/(1-minChance)


    def driving_rating(self): # "Driving": hitting, and driving a kart
        # +disco + tankitude
        rating_number = (self.stlats.musclitude + self.stlats.tofu)*5/2
        return format_stlat_display(rating_number)

    def precision_rating(self):
        # +pettability + splortsmanship +tentacles
        rating_number = ((1 - self.stlats.needlethreadableness)*0.5 + self.stlats.finesse + self.stlats.estimation*0.2) * 5/(1+0.2+0.5) - abs(self.stlats.left_handedness)
        return format_stlat_display(rating_number)

    def aerodynamics_rating(self):
        # +ritualism +softness +owlishness - unworthiness

        rating_number = (self.stlats.ritualism + self.stlats.owlishness + self.stlats.softness) * 5/3 #unused for now, need more stlats
        return format_stlat_display(rating_number)

    def self_awareness_rating(self):
        # - self.stlats.pettiness - capitalism + improv + tentacles
        rating_number = (self.stlats.wiggle*0.5 + (self.stlats.marbles-2)/2 + self.unpredictability()*0.8) * 5/(0.5+1+0.8) + self.stlats.polkadottedness * 5 #means nothing for now
        return format_stlat_display(rating_number)

    def modifications_string(self):
        if len(self.modifications) == 0:
            return ""
        else:
            return f"**Modifications**:\n{', '.join(self.modifications)}"

    def vk_stat_of_the_day(self):
        stlat_choices = list(self.stlats._fields)
        stlat_choices.remove("fav_tea")
        stlat_choices.remove("stance")
        stlat_choices.remove("polkadottedness")
        today = date.today()
        rng = random.Random(today) # seed rng with today's date

        stlatname = rng.choice(stlat_choices)
        stlat = getattr(self.stlats, stlatname, ':ghost:')

        fancystlatname = stlatname.replace("_"," ").title()
        return f"**Today's Verboten Knowledge Stlat:**\n||{fancystlatname}: {stlat:.2f}||"





def generate_random_player_from_name(name="Random Player", emoji="🏌️"):
    """
    Generate a completely random player.
    """

    seed = name.strip().title()

    rng = random.Random(seed)
    if seed:
        id_ = uuid.uuid3(uuid.NAMESPACE_X500, name=str(seed))
    else:
        id_ = uuid.uuid4()

    stlats = generate_random_stlats_from_name(name)

    if emoji is not None:
        emoji = random_player_emoji(rng)

    return Player(name=name, id=id_, stlats=stlats,emoji=emoji)
    


def generate_random_stlats_from_name(name="Random Player"):
    # Generate stlats for a player using their name
    name = name.strip().title() # case insensitive

    rng = random.Random(name) #seed with name

    return PlayerStlats(
        nyoomability = max(rng.gauss(0,0.3),1.4),
        tofu=           rng.random(), # unused
        wiggle=         rng.random(), # unused
        ritualism=   rng.random(), # unused
        musclitude=     rng.random(),
        finesse=        rng.random(),
        needlethreadableness=   rng.random(), 
        left_handedness=        rng.gauss(0,0.3), #how often shots are biased to the left or right of what you want
        stance= rng.choice(["Tricky","Flashy","Aggro","Tanky","Twitchy","Powerful",
            "Wibble","Wobble","Reverse","Feint","Electric","Spicy","Pomegranate",
            "Explosive","Cottagecore","Corecore","Hardcore","Softcore",
            "Hand to Hand","Lefty","Pop-Punk","DPS","Repose"]),
        fav_tea= rng.choice(["Iced","Boba","White","Green","Oolong",
            "Pu'erh","Chai","Milk","Neon","Sweet","Void","Tea?","Caramel",
            "Lightspeed","Time-traveling","Bloody","Black","Miso","Concrete",
                "Hard-boiled egg","Hot Chocolate","Bubble"]),
        estimation= rng.random(),

        earliness= rng.random(),
        twirliness= rng.random(),
        churliness= rng.random(),
        aceness=rng.random(),
        marbles= rng.randrange(2,4),

        unworthiness=rng.random(),
        splortsmanship=rng.random(),
        tankitude=rng.random(),
        pettiness=rng.random(),
        owlishness=rng.random(),
        disco=rng.random(),
        pettability=rng.random(),
        softness=rng.random(),
        improv=rng.random(),
        tentacles= rng.randrange(0,10),
        capitalism= -rng.random() # always negative

    )

def player_with_mods_but_random_stats(name, mods):
    player = generate_random_player_from_name(name)
    player.modifications = mods
    return player


# Easter egg: polkadot has max stats
known_players = {
    "Polkadot Patterson": Player(name="Polkadot Patterson", id=1, stlats=PlayerStlats(
        stance="Squiddish",
        fav_tea= "Iced",
        nyoomability = 1.5,
        musclitude=1,
        finesse=1,
        needlethreadableness=0,
        polkadottedness=1,  
        left_handedness= 0,
        estimation=1,
        twirliness=0.3,
        churliness=0.3,
        earliness=0.3,
        marbles=4,

        tofu=1, # unused
        wiggle=1, # unused
        ritualism=1, # unused
        owlishness=1,
        softness=1,
        unworthiness=0,
        tentacles=4,
        ),emoji="😅"),
    "Simulacrum": player_with_mods_but_random_stats("Simulacrum",["Ǫ̷͍̺̘͕̼̣͔̮̤̮̫͓̜͊͆̈́̈̉͌́̈̌͠ͅŭ̷̟̦̹͇̮͚̦̱̹̖̲̟̻͈̳͚̰̀̎͆̌̀t̴̨̨̹͇̬̠̤̳̘̟̩̜̻̳͓́̀͌̍̌","😈"]),
    "Solar Dies": player_with_mods_but_random_stats("Solar Dies",["Ǫ̷͍̺̘͕̼̣͔̮̤̮̫͓̜͊͆̈́̈̉͌́̈̌͠ͅŭ̷̟̦̹͇̮͚̦̱̹̖̲̟̻͈̳͚̰̀̎͆̌̀t̴̨̨̹͇̬̠̤̳̘̟̩̜̻̳͓́̀͌̍̌","😈"]),
    "Load Bearing Coconut": player_with_mods_but_random_stats("Load Bearing Coconut",["🧥"]),
    "Frankle Knives": player_with_mods_but_random_stats("Frankle Knives",["🧥"]),
    "Spooks Mcgee": player_with_mods_but_random_stats("Spooks McGee",["🧥"]),
    "1": player_with_mods_but_random_stats("1",["🤝💖"]),
}
known_players["Alto"] = known_players["Polkadot Patterson"]

def get_player_from_name(name):
    # generate a player from their name with random stats
    # ...or if they're polkadot, return a maxed person
    if name.title() in known_players:
        return known_players[name.title()]
    else:
        return generate_random_player_from_name(name)

def format_stlat_display(starcount: float):
    if starcount > 0:
        num_stars = math.floor(starcount)
        return_string = "🌕" * num_stars
        remainder = starcount - num_stars
        if remainder > 0.75:
            return return_string + "🌖"
        elif remainder > 0.5:
            return return_string + "🌗"
        elif remainder > 0.25:
            return return_string + "🌘"
        else: #remainder <= 0.25
            return return_string
    else:
        num_stars = -math.ceil(starcount)
        return_string = "🌕" * num_stars
        remainder = starcount + num_stars
        if remainder > -0.25:
            return "🌒" + return_string
        elif remainder > -0.5:
            return "🌓" + return_string
        elif remainder > -0.75:
            return "🌔" + return_string
        else:
            return "🌝" + return_string

