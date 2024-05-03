# Program for administrasjon av droner og registrering av varer for utkjøring
# Når en ordre skal utføres legges varen inn, og hentes av en båt med ledig kapasitet
import json

#Testdata: vare,type,adresse
varer = [['Sykkel',1,'Lovund'],['traktordel',2,'Tomma'],['Noetungt',2,'Nesna'],['Storvare1',2,'Lovund'],['Storpakke',1,'Nesna']]
#Angi om båt er opptatt (True) eller ledig (False) og vektklasse
# vektklasse 1 er vare opptil 2-10kg, vektklasse 2 er vare opptil 10-50kg
bater =[[True,2],[False,1],[False,2],[True,1]]
antallBater = len(bater)

for vare in varer:
    for bat in bater: 
        if vare[type] == bat[vektklasse] + and not bat[0]:
            bat[0] = True
            # printer ut for debug
            print(json.dumps(bater, indent=4))
            print(f'båt på oppdrag til {vare[2]} med {vare[0]}')
            break
