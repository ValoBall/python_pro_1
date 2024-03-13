import random
import string

# Poproś użytkownika o podanie długości hasła
length = int(input("Podaj długość hasła(min 8 znakow): "))
if length <8:
    print("Długość hasła nie może być mniejsza niż 8. Proszę podać inną liczbę.")
    exit()
elif length>=50:
    print("Hasło jest za długie") 
    exit()  
    

# Zmienna przechowująca wygenerowane hasło
password = ''

# Pętla generująca hasło
for _ in range(length):
    password += random.choice(string.ascii_uppercase)
        
        # Dodanie przynajmniej jednej cyfry
password += random.choice(string.digits)
        
        # Dodanie przynajmniej jednego znaku specjalnego
password += random.choice(string.punctuation)
    # Losowo wybierz znak ze zbioru znaków alfanumerycznych
password += random.choice(string.ascii_letters + string.digits + string.punctuation)

# Wyświetl wygenerowane hasło
print("Wygenerowane hasło:", password)