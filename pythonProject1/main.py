import csvuri


tz=csvuri.timezoneuri()
lg=csvuri.legaturi()
cheita=csvuri.chei()

class Tara:
    def __init__(self, nume):
        self.nume = nume
        self.time = tz[nume]
        legaturi = {}
        for i in cheita:
            if i!=nume:
                legaturi[i]=lg[i,nume]
        self.legaturi = legaturi


Tari={}

for i in cheita:
    Tari[i]=Tara(i)

for i in cheita:
    print(i,':',Tari[i].legaturi)
