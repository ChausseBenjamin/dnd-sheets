dungeonsheets_version = "0.18.0"

xp = 0
level = 2
hp_max = 10

name = "Edowin Bloodthorne"
player_name = "Benjamin Chausse"

race = "drow"
classes = "warlock"
subclasses = "celestial"
background = "criminal"
alignment = "Chaotic Good"

age = 89
weight = 157
height = "5' 8\""
eyes = "Green"
skin = "Dust Grey"
hair = "White"

# portrait = True

# Ability Scores
strength = 10
dexterity = 16
constitution = 14
intelligence = 10
wisdom = 8
charisma = 16

# All lower case, underscores for spaces:
skill_proficiencies = [
    # From Criminal background:
    "deception",
    "stealth",
    # From Drow (Keen Senses):
    "perception",
    # From Warlock:
    # (choose two from Arcana, Deception, History, Intimidation,
    #  Investigation, Nature, and Religion)
    "intimidation",
    "investigation",
]

# Proficiencies and languages
languages = """Common, Undercommon, Elvish"""
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
proficiencies_text = ("Dice set", "Thieves' tools")

# Inventory
cp = 15  # Copper Pieces (+15 from Criminal background)
sp = 0  # Silver Pieces
ep = 0  # Electrum Pieces
gp = 0  # Gold Pieces
pp = 0  # Platinum Pieces

weapons = ()

magic_items = ()

equipment = (
    # From Criminal background:
    """
    - Crowbar\n
    - a set of dark common clothes including a hood\n
    - a belt pouch\n
    """
    # From the curse Campaign:
    """
    - 5 bear meat rations\n
    - Épine de ronces\n
    """
)


spells = (
    # What I picked on Level 1:
    "eldritch blast",  # Cantrip
    "create bonfire",  # Cantrip
    "hellish rebuke",  # Lvl 1 spell
    "guiding bolt",  # Lvl 1 spell (Celestial warlock spell)
    "sacred flame",  # Celestial warlock (free bonus cantrip)
    "light",  # Celestial warlock (free bonus cantrip)
    # What I picked on Level 2:
    "hex",  # Lvl 1 spell
    # Level 3:
    # "misty step",  # This is the spell I choose
    #  'faerie fire',    # Drow Magic (free spell): Uncomment when I get to level 3
    # Level 4:
    # Level 5:
    #  'darkness',       # Drow Magic (free spell): Uncomment when I get to level 5
)


# Which spells have been prepared (none for warlocks)
spells_prepared = (*spells,)

# Chosen eldritch invocations
features = (
    "agonizing blast",  # Level 2
    "repelling blast",  # Level 2
    # "pact of the chain",  # Uncomment when I get to level 3
)

personality_traits = "Slow to trust, yet expecting respect and trust from others."

ideals = """
    There should be honor among thieves.
    Thieves that betray their own are the worst kind of scum and deserve to die. (Good)
    If saving my sister requires throwing babies, how hard do I throw? (Chaotic)
"""

bonds = """
    Ithilda my sister, the ever-unchanging bonehead, perhaps the only person I
    find truly worth saving, became enslaved due to my own naivety. I will never
    let that happen again.
"""

flaws = """Short-tempered, narcissistic, & quick to anger."""

features_and_traits = """
**Criminal Specialty:** I was a burglar before I became an adventurer stealing
and looting the rich and the poor alike. I did not lack wealth. The exhiliration
of the sport was what drove me.

"""

backstory = """

    Edowin Bloodthorne, a Drow Warlock,  was once part of a tight-knit band of
    thieves, but in a fateful heist, his own comrades,  betrayed him by
    offering his sister up as bait to a rival drow faction, using her as a
    distraction to escape with the loot. As a result, his sister was kidnapped
    and condemned to a life of slavery and rape, with no intentions of rescue
    from her former comrades.

    Shocked by this turn of events, Edowin tried to slauther his own, attempting to
    avenge his sister. However, he was young and inexperienced. His act of heroism
    nearly cost him his very life.

    In this darkest hour, he encountered an Empyrean, a celestial being of
    unimaginable power. The Empyrean offered him a pact, a pact that would grant
    him abilities beyond his wildest dreams. Fueled by his deep disdain for the
    darkness that had consumed his drow kin, Edowin accepted the pact with the
    celestial, choosing the path of light and righteousness, the polar opposite of
    what a drow would normally prefer. Even though light targetting the Warlock is
    bound to hurt him, Edowin's hands were blessed with the power to cast spells
    of light and fire with no ill effects.
    """
