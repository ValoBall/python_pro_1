meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            "SHEESH": "lekka dezaprobata",
            "REL":"relatable - czyli coś z czym możesz się utożsamić, z zachowaniem, sytuacją"
            }




i=0
while i<4:
    word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("spróbuj jeszce raz")
    i+= 1
