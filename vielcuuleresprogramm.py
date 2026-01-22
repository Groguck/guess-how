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
    "foto": "./ilder/chris.jpg"
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
    "foto": "./ilder/nick.jpg"
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
    "foto": "./ilder/kyle.jpg"
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
    "foto": "./ilder/daniel.jpg"
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
    "foto": "./ilder/rachael.jpg"
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
    "foto": "./ilder/jake.jpg"
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
    "foto": "./ilder/sarah.jpg"
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
    "foto": "./ilder/emily.jpg"
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
    "foto": "./ilder/andy.jpg"
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
    "foto": "./ilder/tyler.jpg"
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
    "foto": "./ilder/brandon.jpg"
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
    "foto": "./ilder/james.jpg"
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
    "foto": "./ilder/zachary.jpg"
    },
        {"name": "jon",
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
    "foto": "./ilder/jon.jpg"
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
    "foto": "./ilder/william.jpg"
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
    "foto": "./ilder/justin.jpg"
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
    "foto": "./ilder/joseph.jpg"
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
    "foto": "./ilder/connor.jpg"
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
    "foto": "./ilder/alex.jpg"
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
    "foto": "./ilder/ashley.jpg"
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
    "foto": "./ilder/joshua.jpg"
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
    "foto": "./ilder/matt.jpg"
        },
]

fotos = [
    "./ilder/chris.jpg",
    "./ilder/nick.jpg",
    "./ilder/kyle.jpg",
    "./ilder/daniel.jpg",
    "./ilder/rachael.jpg",
    "./ilder/jake.jpg",
    "./ilder/sarah.jpg",
    "./ilder/emily.jpg",
    "./ilder/andy.jpg",
    "./ilder/tyler.jpg",
    "./ilder/brandon.jpg",
    "./ilder/James.jpg",
    "./ilder/zachary.jpg",
    "./ilder/Jon.jpg",
    "./ilder/william.jpg",
    "./ilder/justin.jpg",
    "./ilder/joseph.jpg",
    "./ilder/connor.jpg",
    "./ilder/alex.jpg",
    "./ilder/ashley.jpg",
    "./ilder/joshua.jpg",
    "./ilder/matt.jpg",
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


ausschließen = "hihihi"

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


def antwort(fragenr_def):
    if fragenr_def == 0:
        return "ob sie blond ist und.."
    elif fragenr_def == 1:
        return "ob sie schwarze Haare hat und.."
    elif fragenr_def == 2:
        return "ob sie weisse haare hat und.. "
    elif fragenr_def == 3:
        return "ob sie eine glatze hat und.."
    elif fragenr_def == 4:
        return "ob sie braune haare hat und.."
    elif fragenr_def == 5:
        return "ob sie rote haare hat und.."
    elif fragenr_def == 6:
        return "ob sie einen bart hat und.."
    elif fragenr_def == 7:
        return "ob sie braune augen hat und.."
    elif fragenr_def == 8:
        return "ob sie blaue augen hat und.."
    elif fragenr_def == 9:
        return "ob sie weiss ist und.."
    elif fragenr_def == 10:
        return "ob sie eine grosse nase hat und.."
    elif fragenr_def == 11:
        return "ob sie einen hut traegt und.."
    elif fragenr_def == 12:
        return "ob sie eine brille traegt und.."
    elif fragenr_def == 13:
        return "ob sie ohrringe traegt und.."

namen_nichtexestents_counter=0
fragen_counter = 0

## Hauptprogramm
print ("#Willkommen zum 'Wer ist es?' Spiel!#")
character = random.choice(characters)
# Zeige das Bild mit allen Charakteren

img = Image.open("./ilder/ha.jpg")
img.show()

# Spielanleitung
print ("# Hier siehtst du ein bild mit allen Charackteren #")
print ("# Der bot hat einen von diesen charackteren ausgewählt und du musst versuchen ihn zu mithilfe von diesen fargen zu eraten #")
print (fragen_liste)
print ("# Gib bitte nur die Zahl von der frage ein, die du stellen möchtest#")
# Erste Frage

namen_nichtexestents_counter = 0
weiter="ja"


print ("# Was ist deine erste frage #")
fragenr=int(input("# Was ist deine erste frage #"))


# Weitere Fragen
while weiter == "ja":

    
    while fragenr < 1 or fragenr > 14:
        print ("# Ungültige Eingabe. Bitte gib eine Zahl zwischen 1 und 14 ein. #")
        fragenr=int(input("# Was ist deine frage #"))
    
    fragenr -= 1
    
    frage_stellen_antwort = frage_stellen(fragenr, character)
    if frage_stellen_antwort == True:
        print (f"# du hast gefragt {antwort(fragenr)} Ja, die Person ist #")
        fragen_counter = fragen_counter +1
    else:
        print (f"# du hast gefragt {antwort(fragenr)} Nein, die Person ist nicht #")
        fragen_counter = fragen_counter +1
    
    ausschließen = input("# Möchtest du einen Charakter ausschließen? Wenn ja dann schreibe den namen. Wenn nein schreibe 'nein' #")
    while ausschließen != "nein":
        for nameausschließen in range(len (characters)):
            if characters[nameausschließen]["name"] == ausschließen:
                characters.pop (nameausschließen)
                print (f"# Du hast {ausschließen} ausgeschlossen #")
                namen_nichtexestents_counter = 0
                break
            else:
                namen_nichtexestents_counter += 1
        if namen_nichtexestents_counter == len (characters):
            print ("# Dieser Name exestiert nicht. Bitte versuche es erneut. #")
        namen_nichtexestents_counter = 0
        
        ausschließen = input("# Möchtest du einen weiteren Charakter ausschließen? Wenn ja dann schreibe den namen, wenn nein schreibe 'nein' #")
    
    for foto_offnen in range(len(characters)):
        img = Image.open(characters[foto_offnen]["foto"])
        img.show()
    print ("# Das sind die Überbleibenden Charaktere #")
    
    
    weiter=input("# Möchtest du eine weitere Frage stellen? (ja/nein) (fallst du nochmal die fragen brauchst schrei 'fragen') #")
    if weiter == "nein":
        break
    if weiter == "fragen":
        print (fragen_liste)
        weiter=input("# Möchtest du eine weitere Frage stellen? (ja/nein) #")
    weiter = "ja"
    print ("# Was ist deine nächste frage #")
    fragenr=int(input("# Was ist deine nächste frage #"))


# Letzte Vermutung
print ("# Wer denkst du ist die Person? #")
guess=input("# Wer denkst du ist die Person? #")
if guess.lower() == character["name"]:
    print ("# Herzlichen Glückwunsch! Du hast richtig geraten! #")
else:
    print (f"# Leider falsch! Die richtige Antwort ist {character['name']}! #")
print (f"#du hast {fragen_counter} fragen gestellt#")