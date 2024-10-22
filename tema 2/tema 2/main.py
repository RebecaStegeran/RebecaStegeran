import string
# Declaratia unui sir copiat de pe internet
sir_articol ="""Romanii au luat mai multe credite pentru case,masini sau afaceri.Suma uriasa oferita de banci in doar 8 luni"""
# Impartirea sirurului in 2 parti egale
jumatate=len(sir_articol)//2
prima_parte=sir_articol[:jumatate]
a_doua_parte=sir_articol[jumatate:]
# In prima parte
#  Transforma toate literele in majusule
prima_parte=prima_parte.upper
# Elimina toate spatiile goale de la inceputul si finalul sirului
prima_parte=prima_parte.stripp
# In a doua parte
# Inversează ordinea caracterelor
a_doua_parte=a_doua_parte[::-1]
# Transformă prima literă în majusculă
a_doua_parte=a_doua_parte.capitalize()
# Elimină toate caracterele de punctuație (., ,, !, ?) din această parte
a_doua_parte=a_doua_parte.translate(str.maketrans('', '', string.punctuation))
# Combină cele două părți și afișează rezultatul
rezultat=prima_parte+a_doua_parte
print(rezultat)
