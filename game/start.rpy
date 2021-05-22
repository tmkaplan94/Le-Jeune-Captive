##################################################
# Images
##################################################

# backgrounds
image bg start Paris = "bg start Paris.jpg"

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


    return
