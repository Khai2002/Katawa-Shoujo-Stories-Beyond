# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Shizune = Character("Shizune", color="#72ADEE", what_suffix='"', what_prefix='"')
define Misha = Character("Misha", color="#FF809F", what_suffix='"', what_prefix='"')
define Hisao = Character("Hisao", color="#629276", what_suffix='"', what_prefix='"')
define Lilly = Character("Lilly", color="#ddb640",  what_suffix='"', what_prefix='"')
define Emi = Character("Emi", color="#FF8E7F", what_suffix='"', what_prefix='"')
define Meiko = Character("Meiko", color="#9C5051",  what_suffix='"', what_prefix='"')
define Saki = DynamicCharacter("saki_name", color="#b77029",  what_suffix='"', what_prefix='"')
define Chi = Character("Chisato", color="#cd4b34",  what_suffix='"', what_prefix='"')
define other = DynamicCharacter("other_name", color="#69b129",  what_suffix='"', what_prefix='"')
define Nori = Character("Noriko", color="#b849ab",  what_suffix='"', what_prefix='"')
define Saka = Character("Ms. Sakamoto", color="#9339c7",  what_suffix='"', what_prefix='"')


image start_menu_bus_ride = "event/busride_ni.jpg"

# The game starts here.

label start:     

    scene start_menu_bus_ride
    with dissolve

    $ saki_name = "???"

    " "

    menu:
        "Where do you want to go?"

        "Ascent":
            jump emi
        "Learning to Fly":
            jump saki_sc1
        "Dev":
            $saki_name = "Saki"
            jump saki_sc4
        "Test":
            jump emi

    return

