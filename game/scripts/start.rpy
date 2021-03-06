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
define Both = Character("Both")

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
define Politician = Character("Politician")
define Business_Person = Character("Business Person")
define Gaston = Character("Gaston")
define Guard = Character("Guard")
define Security_Guard = Character("Security Guard")
define Police_Chief = Character("Police Chief")
define Shady_Statesman = Character("Shady Statesman")


##################################################
# Images
##################################################

# backgrounds
image bg start Paris = "bg start Paris.jpg"
image bg first aid = "FirstAidTent.jpg"
image bg burning building = "BurningBuilding.jpg"
image bg frontline = "Frontline.jpg"
image bg safehouse = "Safehouse.jpg"
image bg office = "bg office.jpg"
image bg cafe = "bg cafe.jpg"
image bg cafe2 = "bg cafe2.jpg"
image bg university = "University.jpg"
image bg tresor_national = "bg tresor_national.jpg"
image bg tresor_door = "bg tresor_door.jpg"
image bg inside_tresor = "bg inside_tresor.jpg"
image bg transaction = "bg transaction.jpg"
image bg morse1 = "morse1.jpg"
image bg morse2 = "morse2.jpg"
image bg morse3 = "morse3.jpg"
image bg morse4 = "morse4.jpg"
image bg encrypted = "bg encrypted.jpg"
image bg car = "bg car.jpg"
image bg hangar = "bg hangar.jpg"
image bg tanks = "bg tanks.jpg"
image palais bourbon outside = "Daniel - Palais Bourbon Outside.jpg"
image palais bourbon hallway = "Daniel - Palais Bourbon Hallway.jpg"
image ciel office = "Daniel - Ciel Office.jpg"
image HotelLobby = "HotelLobby.JPG"
image HotelHallway = "HotelHallway.jpg"
image HotelOutside = "HotelOutside.jpg"
image HotelRoomMap = "HotelRoomMap.png"
image alley = "alley1.jpg"
image poll office = "pollOffice.jpg"
image bg LeGrandRoi sidewalk = "bg LeGrandRoi sidewalk.jpg"
image bg LeGrandRoi protest = "bg LeGrandRoi protest.jpg"
image bg LeGrandRoi front = "bg LeGrandRoi front.jpg"
image bg LeGrandRoi riot1 = "bg LeGrandRoi riot1.jpg"
image bg LeGrandRoi riot2 = "bg LeGrandRoi riot2.jpg"
image bg black = "bg black.jpg"

# main characters and their variations
image Jean = "Jean Base.png"
image Moody_Medic = "Jean Base.png"
image Jean flip = im.Flip("Jean Base.png", horizontal="True")
image Ciel = "Ciel Base.png"
image Ciel flip = im.Flip("Ciel Base.png", horizontal="True")
image Radiant_Redhead = "Ciel Base.png"
image Radiant_Redhead flip = im.Flip("Ciel Base.png", horizontal = "True")
image Ciel_Dress = "Ciel Dress.png"
image Ciel_Dress flip = im.Flip("Ciel Dress.png", horizontal="True")
image Claude = "Claude Base.png"
image Claude flip = im.Flip("Claude Base.png", horizontal="True")


# side characters
image Rambunctious_Ragamuffin = "npc.png"
image Worried_Protester = "npc.png"
image Dehydrated_Protester = "npc.png"
image Agitated_Protester = "fnpc.png"
image Frustrated_Youth = "npc.png"
image Downtrodden_Worker = "fnpc.png"
image Disgruntled_Worker = "npc.png"
image Young_Parisian_Lieutenant = "fnpc.png"
image Young_Parisian_Lieutenant flip = im.Flip("fnpc.png", horizontal="True")
image Gaston = "npc.png"
image Guard = "npc.png"
image Security_Guard = "fnpc.png"
image Police_Chief = "npc.png"
image Police_Chief flip = im.Flip("npc.png", horizontal="True")
image Shady_Statesman = "npc.png"
image Shady_Statesman flip = im.Flip("npc.png", horizontal="True")


label start:

    scene bg start Paris

    "Le Jeune Captive"

label scene_select:

    menu:
        "Scene Selection"

        "2019 - Prelude":
            jump scenes

        "2029 - Investigations":
            jump investigations

        "2029 - Ending":
            jump ending

label scenes:
    menu:
        "Scenes"

        "Scene 1: First Aid":
            jump scene1

        "Scene 2: Take Back What is Ours":
            jump scene2

        "Scene 3: The Pigs Arrive":
            jump scene3

        "Scene 4: Beaten":
            jump scene4

        "Scene 5: First Impressions":
            jump scene5

        "Scene 6: Mon Canari":
            jump scene6

        "Scene 7: Revolution Sans Revolution":
            jump scene7

        "Scene 8: A Hollow Victory":
            jump scene8

label investigations:

    menu:
        "Investigations"

        "Palais Bourbon Investigation":
            jump palais_bourbon

        "Tresor Nationale Investigation":
            jump tresor_nationale

        "Hotel de Luxe Investigation":
            jump hotel

        "Saint-Denis Election Investigation":
            jump saint_denis

return
