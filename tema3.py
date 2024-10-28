meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

#procesarea comenzilor
while studenti and comenzi and tavi:
    student=studenti.pop(0)
    comanda=comenzi.pop(0)
    tavi=tavi.pop()
    istoric_comenzi.append(comanda)
    print(f"{student}a comandat{comanda}")

#inventar
print(istoric_comenzi)
numar_papanasi=istoric_comenzi.count("papanasi")
numar_ceafa=istoric_comenzi.count("ceafa")
numar_guias=istoric_comenzi.count("guias")
#afisam rezultatele din inventar
print(f"S-au comandat {comenzi['guias']} guias, {comenzi['ceafa']} ceafa, {comenzi['papanasi']} papanasi.")
print(f"Mai sunt {len(tavi)} tavi.")
#verificam disponibilitatea produselor
print(f"mai este ceafa:{comenzi['ceafa']}")
print(f"mai este guias:{comenzi['guias']}")
print(f"mai este papanasi:{comenzi['papanasi']}")
#finante
#calculam castigurile
total_venit=0
for produs in preturi:
    total_venit+=produs[0]
print(f"cantina a facut: {total_venit} lei.")
#produs care costa cel mult 7 lei
 #pret_mic=[produs for produs in preturi if produs[1] <= 7]
#print(f"produse care costă cel mult 7 lei: {pret_mic}.")






