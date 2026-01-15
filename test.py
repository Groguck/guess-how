import random
from PIL import Image


characters = [
    {"name": "chris",
    "ist_blond": False , 
    "hat_schwarzehaare": False ,
    "hat_Weissehaare": False , 
    "hat_glatze": False , 
    "hat_braunehaare": True ,
    "hat_rotehaare": False ,
    "hat_bart": False ,
    "hat_brauneaugen": True ,
    "hat_blaueaugen": False ,
    "ist_weiss": True ,
    "hat_grosse_nase": True ,
    "hat_hut": True,
    "hat_brille": False,
    "hat_ohrringe": False ,
    },
        {"name": "nick",
    "ist_blond": False , 
    "hat_schwarzehaare": False ,
    "hat_Weissehaare": False , 
    "hat_glatze": False , 
    "hat_braunehaare": True ,
    "hat_rotehaare": False ,
    "hat_bart": False ,
    "hat_brauneaugen": False ,
    "hat_blaueaugen": True ,
    "ist_weiss": True ,
    "hat_grosse_nase": False ,
    "hat_hut": False,
    "hat_brille": True,
    "hat_ohrringe": False ,
    },
        {"name": "kyle",  
    "ist_blond": True , 
    "hat_schwarzehaare": False ,
    "hat_Weissehaare": False , 
    "hat_glatze": False , 
    "hat_braunehaare": False ,
    "hat_rotehaare": False ,
    "hat_bart": False ,
    "hat_brauneaugen": False ,
    "hat_blaueaugen": True ,
    "ist_weiss": True ,
    "hat_grosse_nase": True ,
    "hat_hut": False,
    "hat_brille": False,
    "hat_ohrringe": False ,
    },
        {"name": "daniel",
    "ist_blond": False , 
    "hat_schwarzehaare": False ,
    "hat_Weissehaare": False , 
    "hat_glatze": False , 
    "hat_braunehaare": True ,
    "hat_rotehaare": False ,
    "hat_bart": False ,
    "hat_brauneaugen": True ,
    "hat_blaueaugen": False ,
    "ist_weiss": False ,
    "hat_grosse_nase": True ,
    "hat_hut": True,
    "hat_brille": False,
    "hat_ohrringe": False ,
    },
        {"name": "rachael",
    "ist_blond": False , 
    "hat_schwarzehaare": False ,
    "hat_Weissehaare": False , 
    "hat_glatze": False , 
    "hat_braunehaare": True ,
    "hat_rotehaare": False ,
    "hat_bart": False ,
    "hat_brauneaugen": True ,
    "hat_blaueaugen": False ,
    "ist_weiss": True ,
    "hat_grosse_nase": False ,
    "hat_hut": True,
    "hat_brille": False,
    "hat_ohrringe": True ,
    },
        {"name": "jake",
    "ist_blond": True , 
    "hat_schwarzehaare": False ,
    "hat_Weissehaare": False , 
    "hat_glatze": False , 
    "hat_braunehaare": False ,
    "hat_rotehaare": False ,
    "hat_bart": True ,
    "hat_brauneaugen": True ,
    "hat_blaueaugen": False ,
    "ist_weiss": False ,
    "hat_grosse_nase": False ,
    "hat_hut": False,
    "hat_brille": False,
    "hat_ohrringe": False ,
     },
             {"name": "sarah",
    "ist_blond": False , 
    "hat_schwarzehaare": True ,
    "hat_Weissehaare": False , 
    "hat_glatze": False , 
    "hat_braunehaare": False ,
    "hat_rotehaare": False ,
    "hat_bart": False ,
    "hat_brauneaugen": True ,
    "hat_blaueaugen": False ,
    "ist_weiss": False ,
    "hat_grosse_nase": False ,
    "hat_hut": False,
    "hat_brille": True,
    "hat_ohrringe": True ,
     },
             {"name": "emily",
    "ist_blond": False , 
    "hat_schwarzehaare": False ,
    "hat_Weissehaare": True , 
    "hat_glatze": False , 
    "hat_braunehaare": False ,
    "hat_rotehaare": False ,
    "hat_bart": False ,
    "hat_brauneaugen": False ,
    "hat_blaueaugen": True ,
    "ist_weiss": True ,
    "hat_grosse_nase": False ,
    "hat_hut": False,
    "hat_brille": True,
    "hat_ohrringe": True ,
     },
             {"name": "andy",
    "ist_blond": False , 
    "hat_schwarzehaare": True ,
    "hat_Weissehaare": False , 
    "hat_glatze": False , 
    "hat_braunehaare": False ,
    "hat_rotehaare": False ,
    "hat_bart": False ,
    "hat_brauneaugen": True ,
    "hat_blaueaugen": False ,
    "ist_weiss": False ,
    "hat_grosse_nase": False ,
    "hat_hut": False,
    "hat_brille": False,
    "hat_ohrringe": False ,
     },
             {"name": "tyler",
    "ist_blond": False , 
    "hat_schwarzehaare": True ,
    "hat_Weissehaare": False , 
    "hat_glatze": False , 
    "hat_braunehaare": False ,
    "hat_rotehaare": False ,
    "hat_bart": True ,
    "hat_brauneaugen": True ,
    "hat_blaueaugen": False ,
    "ist_weiss": True ,
    "hat_grosse_nase": True ,
    "hat_hut": False,
    "hat_brille": False,
    "hat_ohrringe": False ,
     },
             {"name": "brandon",
    "ist_blond": True , 
    "hat_schwarzehaare": False ,
    "hat_Weissehaare": False , 
    "hat_glatze": False , 
    "hat_braunehaare": False ,
    "hat_rotehaare": False ,
    "hat_bart": True ,
    "hat_brauneaugen": True ,
    "hat_blaueaugen": False ,
    "ist_weiss": True ,
    "hat_grosse_nase": False ,
    "hat_hut": True,
    "hat_brille": False,
    "hat_ohrringe": False ,
     },
             {"name": "James",
    "ist_blond": False , 
    "hat_schwarzehaare": False ,
    "hat_Weissehaare": False , 
    "hat_glatze": True , 
    "hat_braunehaare": True ,
    "hat_rotehaare": False ,
    "hat_bart": True ,
    "hat_brauneaugen": True ,
    "hat_blaueaugen": False ,
    "ist_weiss": False ,
    "hat_grosse_nase": False ,
    "hat_hut": False,
    "hat_brille": False,
    "hat_ohrringe": False ,
     },
             {"name": "zachary",
    "ist_blond": False , 
    "hat_schwarzehaare": False ,
    "hat_Weissehaare": False , 
    "hat_glatze": True , 
    "hat_braunehaare": False ,
    "hat_rotehaare": True ,
    "hat_bart": False ,
    "hat_brauneaugen": True ,
    "hat_blaueaugen": False ,
    "ist_weiss": True ,
    "hat_grosse_nase": False ,
    "hat_hut": False,
    "hat_brille": False,
    "hat_ohrringe": False ,
     },
             {"name": "Jon",
    "ist_blond": False , 
    "hat_schwarzehaare": False ,
    "hat_Weissehaare": True , 
    "hat_glatze": False , 
    "hat_braunehaare": False ,
    "hat_rotehaare": False ,
    "hat_bart": True ,
    "hat_brauneaugen": True ,
    "hat_blaueaugen": False ,
    "ist_weiss": True ,
    "hat_grosse_nase": False ,
    "hat_hut": False,
    "hat_brille": False,
    "hat_ohrringe": False ,
     },
             {"name": "william",
    "ist_blond": True , 
    "hat_schwarzehaare": False ,
    "hat_Weissehaare": False , 
    "hat_glatze": False , 
    "hat_braunehaare": False ,
    "hat_rotehaare": False ,
    "hat_bart": True ,
    "hat_brauneaugen": True ,
    "hat_blaueaugen": False ,
    "ist_weiss": True ,
    "hat_grosse_nase": False ,
    "hat_hut": False,
    "hat_brille": False,
    "hat_ohrringe": False ,
     },
             {"name": "justin",
    "ist_blond": False , 
    "hat_schwarzehaare": False ,
    "hat_Weissehaare": False , 
    "hat_glatze": False , 
    "hat_braunehaare": True ,
    "hat_rotehaare": False ,
    "hat_bart": True ,
    "hat_brauneaugen": True ,
    "hat_blaueaugen": False ,
    "ist_weiss": True ,
    "hat_grosse_nase": False ,
    "hat_hut": False,
    "hat_brille": False,
    "hat_ohrringe": False ,
     },
             {"name": "joseph",
    "ist_blond": False , 
    "hat_schwarzehaare": False ,
    "hat_Weissehaare": False , 
    "hat_glatze": False , 
    "hat_braunehaare": False ,
    "hat_rotehaare": True ,
    "hat_bart": False ,
    "hat_brauneaugen": False ,
    "hat_blaueaugen": True ,
    "ist_weiss": True ,
    "hat_grosse_nase": False ,
    "hat_hut": False,
    "hat_brille": True,
    "hat_ohrringe": False ,
     },
             {"name": "connor",
    "ist_blond": False , 
    "hat_schwarzehaare": False ,
    "hat_Weissehaare": False , 
    "hat_glatze": False , 
    "hat_braunehaare": True ,
    "hat_rotehaare": False ,
    "hat_bart": True ,
    "hat_brauneaugen": True ,
    "hat_blaueaugen": False ,
    "ist_weiss": False ,
    "hat_grosse_nase": True ,
    "hat_hut": False,
    "hat_brille": False,
    "hat_ohrringe": False ,
     },
             {"name": "alex",
    "ist_blond": False , 
    "hat_schwarzehaare": False ,
    "hat_Weissehaare": True , 
    "hat_glatze": True , 
    "hat_braunehaare": False ,
    "hat_rotehaare": False ,
    "hat_bart": False ,
    "hat_brauneaugen": False ,
    "hat_blaueaugen": False ,
    "ist_weiss": True ,
    "hat_grosse_nase": True ,
    "hat_hut": False,
    "hat_brille": True,
    "hat_ohrringe": False ,
     },
             {"name": "ashley",
    "ist_blond": False , 
    "hat_schwarzehaare": False ,
    "hat_Weissehaare": False , 
    "hat_glatze": False , 
    "hat_braunehaare": False ,
    "hat_rotehaare": True ,
    "hat_bart": False ,
    "hat_brauneaugen": False ,
    "hat_blaueaugen": False ,
    "ist_weiss": True ,
    "hat_grosse_nase": False ,
    "hat_hut": True,
    "hat_brille": False,
    "hat_ohrringe": True ,
     },
             {"name": "joshua",
    "ist_blond": False , 
    "hat_schwarzehaare": False ,
    "hat_Weissehaare": True , 
    "hat_glatze": False , 
    "hat_braunehaare": False ,
    "hat_rotehaare": False ,
    "hat_bart": True ,
    "hat_brauneaugen": True ,
    "hat_blaueaugen": False ,
    "ist_weiss": True ,
    "hat_grosse_nase": True ,
    "hat_hut": False,
    "hat_brille": False,
    "hat_ohrringe": False ,
     },
             {"name": "matt",
    "ist_blond": False , 
    "hat_schwarzehaare": False ,
    "hat_Weissehaare": True , 
    "hat_glatze": False , 
    "hat_braunehaare": False ,
    "hat_rotehaare": False ,
    "hat_bart": False ,
    "hat_brauneaugen": True ,
    "hat_blaueaugen": False ,
    "ist_weiss": True ,
    "hat_grosse_nase": False ,
    "hat_hut": False,
    "hat_brille": False,
    "hat_ohrringe": False ,
        },
]

fragen_liste = [
    "1. Ist die Person blond?",
    "2. Hat die Person schwarze Haare?",
    "3. Hat die Person weisse Haare?",
    "4. Hat die Person eine Glatze?",
    "5. Hat die Person braune Haare?",
    "6. Hat die Person rote Haare?",
    "7. Hat die Person einen Bart?",
    "8. Hat die Person braune Augen?",
    "9. Hat die Person blaue Augen?",
    "10. Ist die Person weiss?",
    "11. Hat die Person eine grosse Nase?",
    "12. Traegt die Person einen Hut?",
    "13. Traegt die Person eine Brille?",
    "14. Traegt die Person Ohrringe?"]

def frage_stellen(fragenr_def, character_def):
    if fragenr_def == 0:
        return character_def["ist_blond"]
    elif fragenr_def == 1:
        return character_def["hat_schwarzehaare"]
    elif fragenr_def == 2:
        return character_def["hat_Weissehaare"]
    elif fragenr_def == 3:
        return character_def["hat_glatze"]
    elif fragenr_def == 4:
        return character_def["hat_braunehaare"]
    elif fragenr_def == 5:
        return character_def["hat_rotehaare"]
    elif fragenr_def == 6:
        return character_def["hat_bart"]
    elif fragenr_def == 7:
        return character_def["hat_brauneaugen"]
    elif fragenr_def == 8:
        return character_def["hat_blaueaugen"]
    elif fragenr_def == 9:
        return character_def["ist_weiss"]
    elif fragenr_def == 10:
        return character_def["hat_grosse_nase"]
    elif fragenr_def == 11:
        return character_def["hat_hut"]
    elif fragenr_def == 12:
        return character_def["hat_brille"]
    elif fragenr_def == 13:
        return character_def["hat_ohrringe"]
    








print ("#Willkommen zum 'Wer ist es?' Spiel!#")
character = random.choice(characters)

img = Image.open("./ilder/ha.jpg")
img.show()

print ("# Hier siehtst du ein bild mit allen Charackteren #")
print ("# Der bot wird einen von diesen charackteren ausgewählt haben und du musst versuchen ihn zu eraten mithilfe von diesen fargen #")
print (fragen_liste)
print ("# Gib bitte nur die zahlen vor den fragen ein um diese zu stallen #")

print ("# Was ist deine erste frage #")
fragenr=int(input("# Was ist deine erste frage #"))
fragenr -= 1

frage_stellen(fragenr, character)

if frage_stellen==True:
    print ("# Ja, Sie ist #")
else:
    print ("# Nein, Sie ist nicht #")
print ("# Möchtest du eine weitere Frage stellen? (ja/nein) #")
weiter=input("# Möchtest du eine weitere Frage stellen? (ja/nein) #")

while weiter == "ja":
    print ("# Was ist deine nächste frage #")
    fragenr=int(input("# Was ist deine nächste frage #"))
    fragenr -= 1

    frage_stellen(fragenr, character)

    if frage_stellen==True:
        print ("# Ja, Sie ist #")
    else:
        print ("# Nein, Sie ist nicht #")
    print ("# Möchtest du eine weitere Frage stellen? (ja/nein) #")
    weiter=input("# Möchtest du eine weitere Frage stellen? (ja/nein) #")

print ("# Wer denkst du ist die Person? #")
guess=input("# Wer denkst du ist die Person? #")
if guess.lower() == character["name"]:
    print ("# Herzlichen Glückwunsch! Du hast richtig geraten! #")
else:
    print (f"# Leider falsch! Die richtige Antwort ist {character['name']}! #")