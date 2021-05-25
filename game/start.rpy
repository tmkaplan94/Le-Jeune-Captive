##################################################
# Characters
##################################################

# main cast and their variations
define Jean = Character("Jean")
define Moody_Medic = Character("Moody Medic")
define Ciel = Character("Ciel")
define Radiant_Redhead = Character("Radiant Redhead")
define Claude = Character("Claude")
define Rambunctious_Ragamuffin = Character("Rambunctious Ragamuffin")
define nvl_narrator = Character("", kind=nvl)

# side characters
define question_marks = Character("???")
define Worried_Protester = Character("Worried Protester")
define Dehydrated_Protester = Character("Dehydrated Protester")
define Agitated_Protester = Character("Agitated Protester")
define Frustrated_Youth = Character("Frustrated Youth")
define Downtrodden_Worker = Character("Downtrodden Worker")
define Disgruntled_Worker = Character("Disgruntled Worker")
define Young_Parisian_Lieutenant = Character("Young Parisian Lieutenant")
define Angry_Young_Parisian = Character("Angry Young Parisian")
define Frustrated_Young_Parisian = Character("Frustrated Young Parisian")
define Mousat = Character("Mousat")
define Wounded_Protester = Character("Wounded Protester")
define Frustrated_Protester = Character("Frustrated Protester")
define Helpful_Agitator = Character("Helpful Agitator")
define Newscaster = Character("Newscaster")


##################################################
# Images
##################################################

# backgrounds
image bg start Paris = "bg start Paris.jpg"
image bg champs_elysees = "champs-elysees.jpg"

# main characters and their variations
image Jean = "Jean Base.png"
image Moody_Medic = "Jean Base.png"
image Jean flip = im.Flip("Jean Base.png", horizontal="True")
image Ciel = "Ciel Base.png"
image Radiant_Redhead = "Ciel Base.png"
image Ciel_Dress = "Ciel Dress.png"
image Claude = "macaron.jpg"
image Rambunctious_Ragamuffin = "macaron.jpg"

# side characters
image Worried_Protester = "npc.png"
image Dehydrated_Protester = "npc.png"
image Agitated_Protester = "npc.png"
image Frustrated_Youth = "npc.png"
image Downtrodden_Worker = "npc.png"
image Disgruntled_Worker = "npc.png"
image Agitated_Protester = "npc.png"
image Frustrated_Youth = "npc.png"
image Downtrodden_Worker = "npc.png"
image Disgruntled_Worker = "npc.png"
image Young_Parisian_Lieutenant = "npc.png"


## Start of Game
label start:

    scene bg start Paris

    "Le Jeune Captive"

    menu:
        "Scene Selection"

        "New Game":
            jump scene1

        "Scene 1: First Aid":
            jump scene1

        "Scene 2: Take Back What is Ours":
            jump scene2

        "Scene 3: The Pigs Arrive":
            jump scene3

        "Scene 4: Beaten":
            jump scene4

        "Palais Bourbon Investigation":
            jump palais_bourbon


    return
