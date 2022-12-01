import funktsioonid
f = funktsioonid
from time import sleep
import random

def täringuvise():
    täring_1=random.randint(1,6)
    täring_2=random.randint(1,6)
    print(täring_1,täring_2)
    sammud=täring_1+täring_2
    return sammud

def vanglaFunk(i,mängija_asetus, vanglas): #vanglas olemise funktsioon
    if i==3: #kui kolm korda pole mängija saanud duublit, siis  kolmas kord saab mängija vabaks
        i=0
        vanglas=False
        print("Vabanesid vanglast!")
        mängija_asetus=mängulaud[täringuvise()+mängulaud.index(mängija_asetus)]
        print("Mängija on ruudul "+str(mängija_asetus))
        return mängija_asetus, vanglas, i

    print("Veeretan täringuid")
    täring_1=random.randint(1,6)
    täring_2=random.randint(1,6)
    print(täring_1,täring_2)
    if täring_1==täring_2: #Kui mängija viskab duubli, saab ta vanglast vabaks ja liigub silmade arvu võrra edasi
        i=0
        print("Vabanesid vanglast!")
        vanglas=False
        sammud=täring_1+täring_2
        mängija_asetus=mängulaud[sammud+mängulaud.index(mängija_asetus)]
        return mängija_asetus, vanglas, i
    else:
        i+=1 
        print("Mängija ei visanud duublit ja jääb vanglasse")
        return mängija_asetus, vanglas, i
        
    

def liikumine(käik,mängija_asetus, mängija_nr,vanglas, mängija_vangla_käik, mängija_raha):
    print("Mängijal " +str(mängija_nr)+" on käik "+str(käik)) #loeb käike while-tsükli jaoks
    kontroll=0
    if vanglas==True:#kui mängija vangla staatus on True, käivitab vangla funktsiooni
        return vanglaFunk(mängija_vangla_käik,mängija_asetus, vanglas)
    kontroll=0
    sammud=0 #näitab, mitu sammu mängija liigub ja kontrollib, kas mängija tegi tiiru lauale peale
    print("Veeretan täringuid")
    täring_1=random.randint(1,6)
    täring_2=random.randint(1,6)
    print(täring_1,täring_2)

    if täring_1==täring_2: #kontrollib, kas täringute silmad on võrdsed
        print("Mängija "+str(mängija_nr)+ " veeretas duubli")
        sammud=täring_1+täring_2
        kontroll=mängulaud.index(mängija_asetus)+sammud #kontrollile on vaja omistada mängu praeguse ruudu indeks ja sammude summa

        if kontroll>=40: #kui kontroll on võrde suurem 40, siis lahutab -40. Selleks, et saaks uut ringi alustada
            kontroll-=40
        mängija_asetus=mängulaud[kontroll] #Mängija asetuse võtab mängulaua indeksi järgi
        print("Mängija on ruudul "+str(mängija_asetus)) #prindib, mis ruudul mängija hetkel on

        if mängija_asetus=="Lähed vangi": #Kui mängija satub "lähed vangi" ruudule siis vangla staatus läheb Trueks
            print("Mängija "+str(mängija_nr)+ " läheb vangi!")
            vanglas=True
            mängija_asetus="Vangla"
            return mängija_asetus, vanglas, mängija_vangla_käik

        ("Veeretan täringuid")
        täring_1=random.randint(1,6)
        täring_2=random.randint(1,6)
        print(täring_1,täring_2)

        if täring_1==täring_2: #Kontrollib uuesti tuublit
            print("Mängija "+str(mängija_nr)+ " veeretas duubli uuesti")
            sammud=täring_1+täring_2
            kontroll=sammud+mängulaud.index(mängija_asetus)

            if kontroll>=40:
                kontroll-=40
            mängija_asetus=mängulaud[kontroll]
            print("Mängija on ruudul "+str(mängija_asetus))#Kontrollib uuesti kas sattus vangi

            if mängija_asetus=="Lähed vangi":
                vanglas=True
                mängija_asetus="Vangla"
                print("Mängija "+ str(mängija_nr)+ " läheb vangi!")
                return mängija_asetus, vanglas, mängija_vangla_käik

            print("Veeretan täringuid")
            täring_1=random.randint(1,6)
            täring_2=random.randint(1,6)
            print(täring_1,täring_2)

            if täring_1==täring_2: #kolmas järjestikune duubli veeretamine tähendab vanglasse minemist
                print("Mängija viskas kolmanda järjestikuse duubli!")
                vanglas=True
                mängija_asetus="Vangla"
                print("Mängija "+str(mängija_nr)+ " läheb vangi!")
                return mängija_asetus, vanglas, mängija_vangla_käik

        sammud=täring_1+täring_2 #Kui duublit kolmandat korda ei tule, käib tavapärane mängija asetuse arvutamine ja tingimuste täitmine
        kontroll=sammud+mängulaud.index(mängija_asetus) 

        if kontroll>=40:
            kontroll-=40
        mängija_asetus=mängulaud[kontroll]
        print("Mängija on ruudul "+str(mängija_asetus))

        if mängija_asetus=="Lähed vangi":
            vangla=True
            mängija_asetus="Vangla"
            print("Mängija "+str(mängija_nr)+ " läheb vangi!")
            return mängija_asetus, vanglas, mängija_vangla_käik
        return mängija_asetus, vanglas, mängija_vangla_käik

    sammud=täring_1+täring_2 #Kui duublit ei tule, käib mängija positsiooni arvutamine tavaapäraselt
    kontroll=sammud+mängulaud.index(mängija_asetus)
    if kontroll>=40:
            kontroll-=40
            print("Mängija tegi mängulauale tiiru peale")
            mängija_raha+=200
    mängija_asetus=mängulaud[kontroll]
    if mängija_asetus=="Lähed vangi":
        vanglas=True
        mängija_asetus="Vangla"
        print("Mängija "+ str(mängija_nr)+ " läheb vangi!")
        return mängija_asetus, vanglas, mängija_vangla_käik
    return mängija_asetus, vanglas, mängija_vangla_käik

mängija1_raha=1500 #Raha arvestamine mängija kohta
mängija2_raha=1500
mängija1_vangla_käik=0#kontrollib, mitu käiku on mängija vanglas olnud. Kui see on võrdne kolmega, siis mängija pääseb vanglast
mängija2_vangla_käik=0
käik=1 #Näitab üldist mängu käiku
mängulaud = ["Go","Jaama tänav" ,"kirst1","Soinaste tänav" ,"maksud","rongijaam1","Ravila tänav" ,"Võimalus","Ringtee tänav" ,"Ilmatsalu tänav" ,"Vangla","Vabaduse pst" ,"Elekter","Sõbra tänav" ,"Kesk kaar" ,"rongijaam2","Kalevi tänav" ,"kirst2","F.R Kreutzvaldi tänav" ,"Vaksali tänav" ,"Tasuta parkimine","Pikk tänav" ,"võimalus2","Aardla tänav" ,"Puussepa tänav" ,"rongijaam3","Puiestee tänav" ,"Kalda tee" ,"Veevärk","Võru tänav" ,"Lähed vangi","Turu tänav" ,"Narva maantee" ,"kirst3","Riia tänav" ,"rongijaam4","võimalus3","Rüütli tänav" ,"maksud2","Raekoja plats"]
#List, milles on elemendid mänguruutude nimed
mängija1_asetus="Go" #Mängija asetus. Algpositsioon on stardiruut "Go"
mängija2_asetus="Go"
mängija1_vanglas=False #Kui selle staatus on True, käivitub vangla funktsioon
mängija2_vanglas=False
panditud = False

mängija1_vara = [mängija1_raha] #sellest saab list, kus sees on mängija raha, krundid ja vanglastpääsu kaart
mängija2_vara = [mängija2_raha]



#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#siit algab mäng
    
käsk = input('''===MONOPOL===
Tere tulemast maailmakuulsa lauamängu Monopol arvutimängu!
Leidke konkurent, võtke istet ja jätke empaatiaga hüvasti!
Alustamiseks kirjutage "start".
''')

while käsk != "start":
    käsk = input('''Kirjutage "start" ilma jutumärkideta.
''')
    
print('Mäng on alanud. Selleks, et teada, mis te teha saate kirjutage "käsud". \nEsimesena käib mängija_1, teisena mängija_2. Käigu alustamiseks kirjutage "käigu lõpp."')


while käsk != "lõpp" and käsk != "võit":
    
    käsk = input("Valige, mida teha: ")
    
    if käsk == "käsud":
        print(f.käsud())
        
    elif käsk.split()[0] == "värv":
        print(f.print_värv(f.näita_värvi(käsk.split()[1]))) #rakendab kaks funktsiooni, millest sisemise argument on värvi nimi
        print("") #reavahe
        
    elif käsk.split()[0] == "krunt":
        tänava_nim_järjend = käsk.split()
        del tänava_nim_järjend[0]
        tänava_nim = " ".join(tänava_nim_järjend) #selleks, et krundinimed on mitme sõnalised
        print(f.print_krunt(f.näita_krunti(tänava_nim))) #pmst sama, mis eelmine aga ühe krundi kohta
        print("") #reavahe
        
    elif käsk.split()[0] == "isik":
        
        if käsk.split()[1] == "mängija_1":
            print(f.print_mängija(mängija1_vara))
        elif käsk.split()[1] == "mängija_2":
            print(f.print_mängija(mängija2_vara))
            
        else:
            print("See pole mängija nimi.\n")
    
    elif käsk == "käigu lõpp": #See käsk on selline, et initsiatiiv vahetub ning uue mängija eest veeretatakse ning maandutakse kuskil.
        if käik %2==0:
            mängija2_info=liikumine(käik,mängija2_asetus,2, mängija2_vanglas,mängija2_vangla_käik, mängija2_raha)#Saab enniku, kus esimene väärtus on mängija asetus ja teine on vangla staatus
            mängija2_asetus = mängija2_info[0]
            mängija2_vanglas = mängija2_info[1]
            mängija2_vangla_käik=mängija2_info[2]
            print("Mängija 2 on ruudul " +str(mängija2_asetus)+"\n")
            
            if f.näita_krunti(mängija2_asetus) != "Selle nimelist krunti pole": #kui tegu on krundiga
                
                if mängija2_asetus not in mängija1_vara and mängija2_asetus not in mängija2_vara:#kui keegi seda ei oma.
                    
                    print(f.print_krunt(f.näita_krunti(mängija2_asetus))) #annab ostmata krundi info
                    print("")
                    ostuotsus = input('Krunt on ostmata. Kui soovite osta, sisestage "jah".\nKui mitte, siis kirjutage "ei" ja krunt jääb vabaks.\n')
                    
                    while ostuotsus != "jah" and ostuotsus != "ei":#kui esitati vale sõne
                        ostuotsus = input('Sisestage "jah" või "ei" jutumärkideta \n')
                        
                    if ostuotsus == "ei":
                        print("See krunt jääb järgmist ostjat ootama.")
                        
                    if ostuotsus == "jah":
                        
                        if int((f.näita_krunti(mängija2_asetus))[1]) <= mängija2_vara[0]: #kui mängijal on piisavalt raha
                            mängija2_vara[0] -= int((f.näita_krunti(mängija2_asetus))[1]) #lahutab mängijalt krundi hinna
                            mängija2_vara = f.lisa_krunt(mängija2_asetus, mängija2_vara) #lisab krundi mängijale
                            print("Kontolt eemaldatud " + str(((f.näita_krunti(mängija2_asetus))[1])) + " eurot.")
                            print("Teie kontol on " + str(mängija2_vara[0])+ " eurot.")
                            
                        else:
                            print("Teil on selle ostmiseks puudu " + str(int((f.näita_krunti(mängija2_asetus))[1]) - mängija2_vara[0]) + " eurot.")
                            print('Te võite oma krunte pantida ettenähtud hinna eest ning siis uuesti osta proovida.\nRohkemaks infoks kirjutage "käsud".')
                
                
                elif mängija2_asetus in mängija2_vara:
                    print("Maandusite enda krundile. Nautige tasuta!")
                    
                else:
                    print("Maandusite konkurendi krundile, rent on " + str((f.näita_krunti(mängija2_asetus))[2]))
                    while int((f.näita_krunti(mängija2_asetus))[2]) > mängija2_vara[0]: #kui mängijal pole piisavalt raha, et renti maksta 
                        print("Pole piisavalt raha.")
                        if len(mängija2_vara) < 2: #kui mängijal pole krunte
                            print("Teil on krundid otsas, kaotasite mängu.")
                            käsk = "võit" #tsükli lõppu jõudes väljub mängust
                            
                        else:
                            
                            while len(mängija2_vara) > 2:
                                pandiotsus = input('''Teil pole piisavalt raha. Peate oma krunte pangale pantima.
Sisestage kas krundinimi või "info", et teada saada oma kruntide pantide väärtused.
''')
                                
                                while pandiotsus not in mängija2_vara and pandiotsus != "info":
                                    pandiotsus = vale_valik
                                    pandiotsus = input("Teil puudub krunt nimega " + str(vale_valik) + '. Sisestage kas krundinimi või "info", et saada infot enda kruntide kohta.')
                                
                                
                                if pandiotsus in mängija2_vara:
                                    mängija2_vara = f.pandi_krunt(pandiotsus, mängija2_vara) #pandib krundi, lisab hinna mängijale
                                    print("Krunt panditud, teie kontol on nüüd " + str(mängija2_vara[0]) + " eurot.")
                                    panditud = True
                                    
                                else:
                                    print("Allpool onkirjas teie krundid.\n")
                                    if "vangla_vabastus" not in mängija: #kui vanglast pääsemise kaarti mängijal pole
                                        u = 1
                                        for u in range(len(mängija2_vara)):
                                            print("Krundi " + mängija2_vara[u] + " pant on " + str((näita_krunti(pandiotsus))[5]))
                                    
                                    else:
                                        indeks = mängija.index("vangla_vabastus") #eemaldab vanglast vabastuse kaardi
                                        del mängija[indeks] #eemaldab vanglast pääsemise kaardi
                                        u = 1
                                        for u in range(len(mängija2_vara)):
                                            print("Krundi " + mängija2_vara[u] + " pant on " + str((näita_krunti(pandiotsus))[5]))
                                            
                                        mängija.append("vangla_vabastus") #lisab selle tagasi
                    
                    
                    if int((f.näita_krunti(mängija2_asetus))[2]) > mängija2_vara[0]: #kui mäng kaotati
                        break
                    
                    else:
                        mängija2_vara[0] -= int((f.näita_krunti(mängija2_asetus))[2]) #toimub rahavahetus
                        mängija2_vara[0] += int((f.näita_krunti(mängija2_asetus))[2])
                        print("Teie kontole jäi " + str(mängija2_vara[0]) + " eurot.")
            else:
                print("Maandusite asukohale " + mängija2_asetus + ". Sellel kohal siin versioonis veel funktsiooni pole.")
                            
                            
                            
                            
                            
        else:
            mängija1_info=liikumine(käik,mängija1_asetus,1, mängija1_vanglas,mängija1_vangla_käik, mängija1_raha)
            mängija1_asetus = mängija1_info[0]
            mängija1_vanglas = mängija1_info[1]
            mängija1_vangla_käik = mängija1_info[2]
            print("Mängija 1 on ruudul "+str(mängija1_asetus)+"\n")
            
            
            
            if f.näita_krunti(mängija1_asetus) != "Selle nimelist krunti pole": #kui tegu on krundiga
                
                if mängija1_asetus not in mängija1_vara and mängija1_asetus not in mängija2_vara:#kui keegi seda ei oma.
                    
                    print(f.print_krunt(f.näita_krunti(mängija1_asetus))) #annab ostmata krundi info
                    print("")
                    ostuotsus = input('Krunt on ostmata. Kui soovite osta, sisestage "jah".\nKui mitte, siis kirjutage "ei" ja krunt jääb vabaks.\n')
                    
                    while ostuotsus != "jah" and ostuotsus != "ei":#kui esitati vale sõne
                        ostuotsus = input('Sisestage "jah" või "ei" jutumärkideta \n')
                        
                    if ostuotsus == "ei":
                        print("See krunt jääb järgmist ostjat ootama.")
                        
                    if ostuotsus == "jah":
                        
                        if int((f.näita_krunti(mängija1_asetus))[1]) <= mängija1_vara[0]: #kui mängijal on piisavalt raha
                            mängija1_vara[0] -= int((f.näita_krunti(mängija1_asetus))[1]) #lahutab mängijalt krundi hinna
                            mängija1_vara = f.lisa_krunt(mängija1_asetus, mängija1_vara) #lisab krundi mängijale
                            print("Kontolt eemaldatud " + str(((f.näita_krunti(mängija1_asetus))[1])) + " eurot.")
                            print("Teie kontol on " + str(mängija1_vara[0])+ " eurot.")
                            
                        else:
                            print("Teil on selle ostmiseks puudu " + str(int((f.näita_krunti(mängija1_asetus))[1]) - mängija1_vara[0]) + " eurot.")
                            print('Te võite oma krunte pantida ettenähtud hinna eest ning siis uuesti osta proovida.\nRohkemaks infoks kirjutage "käsud".')
                
                
                elif mängija1_asetus in mängija1_vara:
                    print("Maandusite enda krundile. Nautige tasuta!")
                    
                else:
                    print("Maandusite konkurendi krundile, rent on " + str((f.näita_krunti(mängija1_asetus))[2]))
                    while int((f.näita_krunti(mängija1_asetus))[2]) > mängija1_vara[0]: #kui mängijal pole piisavalt raha, et renti maksta 
                        print("Pole piisavalt raha.")
                        if len(mängija1_vara) < 2: #kui mängijal pole krunte
                            print("Teil on krundid otsas, kaotasite mängu.")
                            käsk = "võit" #tsükli lõppu jõudes väljub mängust
                            
                        else:
                            
                            while len(mängija1_vara) > 2:
                                pandiotsus = input('''Teil pole piisavalt raha. Peate oma krunte pangale pantima.
Sisestage kas krundinimi või "info", et teada saada oma kruntide pantide väärtused.
''')
                                
                                while pandiotsus not in mängija1_vara and pandiotsus != "info":
                                    pandiotsus = vale_valik
                                    pandiotsus = input("Teil puudub krunt nimega " + str(vale_valik) + '. Sisestage kas krundinimi või "info", et saada infot enda kruntide kohta.')
                                
                                
                                if pandiotsus in mängija1_vara:
                                    mängija1_vara = f.pandi_krunt(pandiotsus, mängija1_vara) #pandib krundi, lisab hinna mängijale
                                    print("Krunt panditud, teie kontol on nüüd " + str(mängija1_vara[0]) + " eurot.")
                                    panditud = True
                                    
                                else:
                                    print("Allpool onkirjas teie krundid.\n")
                                    if "vangla_vabastus" not in mängija1_vara: #kui vanglast pääsemise kaarti mängijal pole
                                        u = 1
                                        for u in range(len(mängija1_vara)):
                                            print("Krundi " + mängija1_vara[u] + " pant on " + str((näita_krunti(pandiotsus))[5]))
                                    
                                    else:
                                        indeks = mängija.index("vangla_vabastus") #eemaldab vanglast vabastuse kaardi
                                        del mängija[indeks] #eemaldab vanglast pääsemise kaardi
                                        u = 1
                                        for u in range(len(mängija1_vara)):
                                            print("Krundi " + mängija1_vara[u] + " pant on " + str((näita_krunti(pandiotsus))[5]))
                                            
                                        mängija.append("vangla_vabastus") #lisab selle tagasi
                    
                    
                    if int((f.näita_krunti(mängija1_asetus))[2]) > mängija1_vara[0]: #kui mäng kaotati
                        break
                    
                    else:
                        mängija1_vara[0] -= int((f.näita_krunti(mängija1_asetus))[2])#rendi maksmine
                        mängija2_vara[0] += int((f.näita_krunti(mängija1_asetus))[2])
                        print("Teie kontole jäi " + str(mängija1_vara[0]) + " eurot.")
        

            
            else:
                print("Maandusite asukohale " + mängija1_asetus + ". Sellel kohal siin versioonis veel funktsiooni pole.")
            
            
            
        käik+=1
    
    elif käsk.split()[0] == "pandi":
        panditav = käsk.split() #saab järjendi
        del panditav[0] #eemaldab "pandi" osa
        panditav = " ".join(panditav) #saab krundinime
        if käik %2==0: #kui on 1. mängija käik
            if panditav in mängija1_vara:
                mängija1_vara = f.pandi_krunt(panditav, mängija1_vara) #pandib
                print("Su kontol on nüüd " + str(mängija1_vara[0]) + " eurot.")
                
            else:
                print("Sul pole seda krunti")
                
        else:
            if panditav in mängija2_vara:#kui on 2. mängija käik
                mängija2_vara = f.pandi_krunt(panditav, mängija2_vara) #pandib
                print("Su kontol on nüüd " + str(mängija2_vara[0]) + " eurot.")
                
            else:
                print("Sul pole seda krunti")
                
    elif käsk == "lõpp":#et järgmist rida ei rakendaks
        ...
        
    else:
        print('See pole konsoolile tuntud käsk. Et näha käske, kirjutage "käsud".')

            


print("Mängu lõpp.")    
