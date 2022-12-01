import funktsioonid
f = funktsioonid
import random

def täringuvise():
    täring_1=random.randint(1,6)
    täring_2=random.randint(1,6)
    print(täring_1,täring_2)
    sammud=täring_1+täring_2
    return sammud

def vanglaFunk(i,mängija_asetus, vanglas, raha): #vanglas olemise funktsioon
    if i==3: #kui kolm korda pole mängija saanud duublit, siis  kolmas kord saab mängija vabaks
        i=0
        vanglas=False
        print("Vabanesid vanglast!")
        mängija_asetus=mängulaud[täringuvise()+mängulaud.index(mängija_asetus)]
        print("Mängija on ruudul "+str(mängija_asetus))
        return mängija_asetus, vanglas, i, raha

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
        return mängija_asetus, vanglas, i, raha
    else:
        i+=1 
        print("Mängija ei visanud duublit ja jääb vanglasse")
        return mängija_asetus, vanglas, i, raha
        
    

def liikumine(käik,mängija_asetus, mängija_nr,vanglas, mängija_vangla_käik, mängija_raha):
    print("Mängijal " +str(mängija_nr)+" on käik "+str(käik)) #loeb käike while-tsükli jaoks
    kontroll=0
    if vanglas==True:#kui mängija vangla staatus on True, käivitab vangla funktsiooni
        return vanglaFunk(mängija_vangla_käik,mängija_asetus, vanglas, mängija_raha)
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
            return mängija_asetus, vanglas, mängija_vangla_käik, mängija_raha

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
                return mängija_asetus, vanglas, mängija_vangla_käik, mängija_raha

            print("Veeretan täringuid")
            täring_1=random.randint(1,6)
            täring_2=random.randint(1,6)
            print(täring_1,täring_2)

            if täring_1==täring_2: #kolmas järjestikune duubli veeretamine tähendab vanglasse minemist
                print("Mängija viskas kolmanda järjestikuse duubli!")
                vanglas=True
                mängija_asetus="Vangla"
                print("Mängija "+str(mängija_nr)+ " läheb vangi!")
                return mängija_asetus, vanglas, mängija_vangla_käik, mängija_raha

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
            return mängija_asetus, vanglas, mängija_vangla_käik, mängija_raha
        return mängija_asetus, vanglas, mängija_vangla_käik, mängija_raha

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
        return mängija_asetus, vanglas, mängija_vangla_käik, mängija_raha
    return mängija_asetus, vanglas, mängija_vangla_käik, mängija_raha

mängija1_raha=1500 #Raha arvestamine mängija kohta
mängija2_raha=1500
mängija1_vangla_käik=0#kontrollib, mitu käiku on mängija vanglas olnud. Kui see on võrdne kolmega, siis mängija pääseb vanglast
mängija2_vangla_käik=0
käik=1 #Näitab üldist mängu käiku
mängulaud = ("Go","Jaama tänav" ,"kirst1","Soinaste tänav" ,"Tulumaks","Ülenurme rongijaam","Ravila tänav","Võimalus","Ringtee tänav" ,"Ilmatsalu tänav" ,"Vangla","Vabaduse pst" ,"Elektrivõrk","Sõbra tänav" ,"Kesk kaar" ,"Kirsi rongijaam","Kalevi tänav" ,"kirst2","F.R Kreutzvaldi tänav" ,"Vaksali tänav" ,"Tasuta parkimine","Pikk tänav" ,"võimalus2","Aardla tänav" ,"Puussepa tänav" ,"Aardla rongijaam","Puiestee tänav" ,"Kalda tee" ,"Veevärk","Võru tänav" ,"Lähed vangi","Turu tänav" ,"Narva maantee" ,"kirst3","Riia tänav" ,"Tartu rongijaam","võimalus3","Rüütli tänav" ,"Lisamaks","Raekoja plats")
#List, milles on elemendid mänguruutude nimed
mängija1_asetus="Go" #Mängija asetus. Algpositsioon on stardiruut "Go"
mängija2_asetus="Go"
mängija1_vanglas=False #Kui selle staatus on True, käivitub vangla funktsioon
mängija2_vanglas=False
hotelliteenindus = False

rongijaamad = ("Ülenurme rongijaam","Kirsi rongijaam","Aardla rongijaam","Tartu rongijaam")
vesi_ja_elekter = ("Elektrivõrk","Veevärk",)
maksud = ("Tulumaks","Lisamaks")
mängija1_vara = [mängija1_raha] #sellest saab list, kus sees on mängija raha, krundid ja vanglastpääsu kaart
mängija2_vara = [mängija1_raha]

hotellid = [] # Ehk ühelgi krundil pole hotelli. Selles järjendis on kõik hotellidega krundid.


#################################################################################################################################################
#################################################################################################################################################
#################################################################################################################################################
#siit algab mäng
    
käsk = input('''===MONOPOL===
Teretulemast maailmakuulsa lauamängu Monopol arvutimängu!
Leidke konkurent, võtke istet ja jätke empaatiaga hüvasti!
Alustamiseks kirjutage "start".
''').lower()


while käsk != "start":
    käsk = input('''Kirjutage "start" ilma jutumärkideta.
''').lower()
    

print('Mäng on alanud. Selleks, et teada, mis te teha saate kirjutage "käsud". \nEsimesena käib mängija 1, teisena mängija 2. Käigu alustamiseks kirjutage "algus" või "lõpp".')



while käsk != "mängu lõpp" and käsk != "võit":
    
    
    käsk = input("Valige, mida teha: ")

    if käsk == "":
        print('See pole konsoolile tuntud käsk. Et näha käske, kirjutage "käsud".')
        
    elif (käsk.split()[0]).lower() == "käsud":
        print(f.käsud())
    
    
        
    elif (käsk.split()[0]).lower() == "värv":
        print(f.print_värv(f.näita_värvi(käsk.split()[1]))) #rakendab kaks funktsiooni, millest sisemise argument on värvi nimi
        print("") #reavahe
        
        
    elif (käsk.split()[0]).lower() == "krunt":
        tänava_nim_järjend = käsk.split()
        del tänava_nim_järjend[0]
        tänava_nim = " ".join(tänava_nim_järjend) #selleks, et krundinimed on mitme sõnalised
        print(f.print_krunt(f.näita_krunti(tänava_nim))) #pmst sama, mis eelmine aga ühe krundi kohta
        print("") #reavahe
        
    elif (käsk.split()[0]).lower() == "info": #info mängija... See väljastab kõik mängija vara
        
        isik = käsk.split()[1] + käsk.split()[2]
        if isik == "mängija1":
            print(f.print_mängija(mängija1_vara, hotellid))
            
        elif isik == "mängija2":
            print(f.print_mängija(mängija2_vara, hotellid))
            
        else:
            print("See pole mängija nimi.\n")
    
    elif (käsk.split()[0]).lower() == "lõpp" or (käsk.split()[0]).lower() == "algus": #See käsk on selline, et initsiatiiv vahetub ning uue mängija eest veeretatakse ning maandutakse kuskil.
        if käik %2==0:
            mängija2_info=liikumine(käik,mängija2_asetus,2, mängija2_vanglas,mängija2_vangla_käik, mängija2_vara[0])#Saab enniku, kus esimene väärtus on mängija asetus ja teine on vangla staatus
            mängija2_asetus = mängija2_info[0]
            mängija2_vanglas = mängija2_info[1]
            mängija2_vangla_käik=mängija2_info[2]
            mängija2_vara[0] = mängija2_info[3]
            print("Mängija 2 on ruudul " +str(mängija2_asetus)+"\n")
            
            if f.näita_krunti(mängija2_asetus) != "Selle nimelist krunti pole" or mängija2_asetus in rongijaamad or mängija2_asetus in vesi_ja_elekter: #kui tegu on krundi, jaama või kommunaaliga
                
                if mängija2_asetus not in mängija1_vara and mängija2_asetus not in mängija2_vara:#kui keegi seda ei oma.
                    
                    if f.näita_krunti(mängija2_asetus) != "Selle nimelist krunti pole":
                        print(f.print_krunt(f.näita_krunti(mängija2_asetus))) #annab ostmata krundi info
                        print("")
                    
                    if mängija2_asetus in rongijaamad:
                        print("""Rongijaamad töötavad järgmiselt:
Ühe rongijaamaga on tasu 25 eurot.
Kahega on tasu 50 eurot.
Kolmega on tasu 100 eurot.
Neljaga on tasu 200 eurot.
Rongijaamad maksavad 200 eurot.
""")
                    if mängija2_asetus in vesi_ja_elekter:
                        print("""Veevärk ja elektrivõrk töötavad järgmiselt:
Mängija veeretab kaks täringut.
Kui tema konkurendil on vaid üks neist, on tasu veeretusest neli korda suurem.
Kui tema konkurendil on mõlemad, on tasu veeretusest kümnekordne.
Elektrivõrgu ja veevärgi hind on 150 eurot.
""")
                    ostuotsus = input('Kaart on ostmata. Kui soovite osta, sisestage "jah".\nKui hetkel mitte, siis kirjutage "ei" ja krunt jääb vabaks.\n')
                    
                    while ostuotsus != "jah" and ostuotsus != "ei":#kui esitati vale sõne
                        ostuotsus = input('Sisestage "jah" või "ei" jutumärkideta \n')
                        
                    if ostuotsus == "ei":
                        print("See kaart jääb järgmist ostjat ootama.")
                        
                    if ostuotsus == "jah":
                        if f.näita_krunti(mängija2_asetus) != "Selle nimelist krunti pole":
                            if int((f.näita_krunti(mängija2_asetus))[1]) <= mängija2_vara[0]: #kui mängijal on piisavalt raha
                                mängija2_vara[0] -= int((f.näita_krunti(mängija2_asetus))[1]) #lahutab mängijalt krundi hinna
                                mängija2_vara = f.lisa_krunt(mängija2_asetus, mängija2_vara) #lisab krundi mängijale
                                print("Kontolt eemaldatud " + str(((f.näita_krunti(mängija2_asetus))[1])) + " eurot.")
                                print("Teie kontol on " + str(mängija2_vara[0])+ " eurot.")
                            
                            else:
                                print("Teil on selle ostmiseks puudu " + str(int((f.näita_krunti(mängija2_asetus))[1]) - mängija2_vara[0]) + " eurot.")
                                print('Te võite oma krunte pantida ettenähtud hinna eest ning siis uuesti osta proovida.\nRohkemaks infoks kirjutage "käsud".')
                        
                        elif mängija2_asetus in rongijaamad:
                            mängija2_vara[0] >= 200
                            mängija2_vara[0] -= 200
                            mängija2_vara.append(mängija2_asetus)
                            print("Kontolt eemaldatud 200 eurot.")
                            print("Teie kontol on " + str(mängija2_vara[0])+ " eurot.")
                        
                        elif mängija2_asetus in vesi_ja_elekter:
                            mängija2_vara[0] >= 150
                            mängija2_vara[0] -= 150
                            mängija2_vara.append(mängija2_asetus)
                            print("Kontolt eemaldatud 150 eurot.")
                            print("Teie kontol on " + str(mängija2_vara[0])+ " eurot.")
                        
                            
                elif mängija2_asetus in mängija2_vara:
                    print("Te olete selle koha omanik. Nautige tasuta!")
                    
                else:
                    rent = f.rendimääraja(mängija2_asetus, mängija1_vara, hotellid)
                    
                    if f.näita_krunti(mängija2_asetus) != "Selle nimelist krunti pole":
                        print("Maandusite konkurendi krundile, rent on " + str(rent) + " eurot.")
                    elif mängija2_asetus in rongijaamad:
                        print("Maandusite konkurendi rongijaamale, tasu on " + str(rent) + " eurot.")

                    
                    if rent > mängija2_vara[0]: #Kui mängijal pole piisavalt raha
                        mängija2_vara[0] = (f.endgame(rent, mängija2_vara, käsk))[0]
                        mängija2_vara[0] -= rent
                        if mängija2_vara[0] < 0:
                            käsk = "võit"
                    
                    
                    if käsk == "võit": #kui mäng kaotati
                        break
                    
                    else:
                        mängija2_vara[0] -= rent #toimub rahavahetus
                        mängija1_vara[0] += rent
                        print("Teie kontole jäi " + str(mängija2_vara[0]) + " eurot.")
            

            elif mängija2_asetus in maksud:
                rent = f.rendimääraja(mängija2_asetus, mängija1_vara, hotellid)
                print("Peate maksma " + str(rent) + " eurot makse.")
                if rent > mängija2_vara[0]: #Kui mängijal pole piisavalt raha
                    mängija2_vara[0] = (f.endgame(rent, mängija2_vara, käsk))[0]
                    mängija2_vara[0] -= rent
                    if mängija2_vara[0] < 0:
                        käsk = "võit"
                    
                    
                else:
                    mängija2_vara[0] -= rent
                    print("Teie kontole jäi " + str(mängija2_vara[0]) + " eurot.")
                    
            elif mängija2_asetus == "Vangla":
                print("Saabusite vanglasse, käituge korralikult.")
                
            else:
                print("Maandusite asukohale " + mängija2_asetus + ". Sellel kohal funktsiooni pole.")
                            
                            
                            
                            
                            
     #############################################################################################################################                       
    
                            
                            
        else:
            mängija1_info=liikumine(käik,mängija1_asetus,1, mängija1_vanglas,mängija1_vangla_käik, mängija1_vara[0])
            mängija1_asetus = mängija1_info[0]
            mängija1_vanglas = mängija1_info[1]
            mängija1_vangla_käik = mängija1_info[2]
            mängija1_vara[0] = mängija1_info[3]
            print("Mängija 1 on ruudul " +str(mängija1_asetus)+"\n")
            
            if f.näita_krunti(mängija1_asetus) != "Selle nimelist krunti pole" or mängija1_asetus in rongijaamad or mängija1_asetus in vesi_ja_elekter: #kui tegu on krundi, jaama või kommunaaliga
                
                if mängija1_asetus not in mängija2_vara and mängija1_asetus not in mängija1_vara:#kui keegi seda ei oma.
                    
                    if f.näita_krunti(mängija1_asetus) != "Selle nimelist krunti pole":
                        print(f.print_krunt(f.näita_krunti(mängija1_asetus))) #annab ostmata krundi info
                        print("")
                    
                    if mängija1_asetus in rongijaamad:
                        print("""Rongijaamad töötavad järgmiselt:
Ühe rongijaamaga on tasu 25 eurot.
Kahega on tasu 50 eurot.
Kolmega on tasu 100 eurot.
Neljaga on tasu 200 eurot.
Rongijaamad maksavad 200 eurot.
""")
                    if mängija1_asetus in vesi_ja_elekter:
                        print("""Veevärk ja elektrivõrk töötavad järgmiselt:
Mängija veeretab kaks täringut.
Kui tema konkurendil on vaid üks neist, on tasu veeretusest neli korda suurem.
Kui tema konkurendil on mõlemad, on tasu veeretusest kümnekordne.
Elektrivõrgu ja veevärgi hind on 150 eurot.
""")
                    ostuotsus = input('Kaart on ostmata. Kui soovite osta, sisestage "jah".\nKui hetkel mitte, siis kirjutage "ei" ja krunt jääb vabaks.\n')
                    
                    while ostuotsus != "jah" and ostuotsus != "ei":#kui esitati vale sõne
                        ostuotsus = input('Sisestage "jah" või "ei" jutumärkideta \n')
                        
                    if ostuotsus == "ei":
                        print("See kaart jääb järgmist ostjat ootama.")
                        
                    if ostuotsus == "jah":
                        if f.näita_krunti(mängija1_asetus) != "Selle nimelist krunti pole":
                            if int((f.näita_krunti(mängija1_asetus))[1]) <= mängija1_vara[0]: #kui mängijal on piisavalt raha
                                mängija1_vara[0] -= int((f.näita_krunti(mängija1_asetus))[1]) #lahutab mängijalt krundi hinna
                                mängija1_vara = f.lisa_krunt(mängija1_asetus, mängija1_vara) #lisab krundi mängijale
                                print("Kontolt eemaldatud " + str(((f.näita_krunti(mängija1_asetus))[1])) + " eurot.")
                                print("Teie kontol on " + str(mängija1_vara[0])+ " eurot.")
                            
                            else:
                                print("Teil on selle ostmiseks puudu " + str(int((f.näita_krunti(mängija1_asetus))[1]) - mängija1_vara[0]) + " eurot.")
                                print('Te võite oma krunte pantida ettenähtud hinna eest ning siis uuesti osta proovida.\nRohkemaks infoks kirjutage "käsud".')
                        
                        elif mängija1_asetus in rongijaamad:
                            mängija1_vara[0] >= 200
                            mängija1_vara[0] -= 200
                            mängija1_vara.append(mängija1_asetus)
                            print("Kontolt eemaldatud 200 eurot.")
                            print("Teie kontol on " + str(mängija1_vara[0])+ " eurot.")
                        
                        elif mängija1_asetus in vesi_ja_elekter:
                            mängija1_vara[0] >= 150
                            mängija1_vara[0] -= 150
                            mängija1_vara.append(mängija1_asetus)
                            print("Kontolt eemaldatud 150 eurot.")
                            print("Teie kontol on " + str(mängija1_vara[0])+ " eurot.")
                        
                            
                elif mängija1_asetus in mängija1_vara:
                    print("Te olete selle koha omanik. Nautige tasuta!")
                    
                else:
                    rent = f.rendimääraja(mängija1_asetus, mängija2_vara, hotellid)
                    
                    if f.näita_krunti(mängija1_asetus) != "Selle nimelist krunti pole":
                        print("Maandusite konkurendi krundile, rent on " + str(rent) + " eurot.")
                    elif mängija1_asetus in rongijaamad:
                        print("Maandusite konkurendi rongijaamale, tasu on " + str(rent) + " eurot.")
                    elif mängija1_asetus in vesi_ja_elekter:
                        print("Sattusite konkurendi kommunaalile, tasu on " + str(rent) + " eurot.")
                    
                    if rent > mängija1_vara[0]: #Kui mängijal pole piisavalt raha
                        mängija1_vara[0] = (f.endgame(rent, mängija1_vara, käsk))[0]
                        mängija1_vara[0] -= rent
                        if mängija1_vara[0] < 0:
                            käsk = "võit"                                                            
                    
                    
                    if käsk == "võit": #kui mäng kaotati
                        break
                    
                    else:
                        mängija1_vara[0] -= rent #toimub rahavahetus
                        mängija2_vara[0] += rent
                        print("Teie kontole jäi " + str(mängija1_vara[0]) + " eurot.")
            

            elif mängija1_asetus in maksud:
                rent = f.rendimääraja(mängija1_asetus, mängija2_vara, hotellid)
                print("Peate maksma " + str(rent) + " eurot makse.")
                if rent > mängija1_vara[0]: #Kui mängijal pole piisavalt raha
                    mängija1_vara[0] = (f.endgame(rent, mängija2_vara, käsk))[0]
                    mängija1_vara[0] -= rent
                    if mängija2_vara[0] < 0:
                        käsk = "võit"
                    
                else:
                    mängija1_vara[0] -= rent
                    print("Teie kontole jäi " + str(mängija1_vara[0]) + " eurot.")
                    
            elif mängija1_asetus == "Vangla":
                print("Saabusite vanglasse, käituge korralikult.")
                
            else:
                print("Maandusite asukohale " + mängija1_asetus + ". Sellel kohal siin versioonis veel funktsiooni pole.")
            
            
            
        käik+=1
    
    
    elif käsk.lower() == "osta":
        if käik % 2 == 0: #ehk  kui äsja käis mängija 1(sest käik += 1 oli lõpus)
            if mängija1_asetus in mängija1_vara or mängija1_asetus in mängija2_vara:
                print("See kaart pole müügiks.")
                
            elif mängija1_asetus not in rongijaamad and mängija1_asetus not in vesi_ja_elekter and  f.näita_krunti(mängija1_asetus) == "Selle nimelist krunti pole":
                print("Seda kohta ei saa osta.")
                
            else:
                if mängija1_vara[0] >= int((f.näita_krunti(mängija1_asetus))[1]): #kui mängijal on ostuks raha
                    mängija1_vara[0] -= int((f.näita_krunti(mängija1_asetus))[1])
                    mängija1_vara.append(mängija1_asetus)
                    print(mängija1_asetus, "ostetud.")
                    print("Teie kontol on", str(mängija1_vara[0]), "eurot.")
                    
                else:
                    print("Teil jääb puudu", str(int((f.näita_krunti(mängija1_asetus))[1]) - mängija1_vara[0]), "eurot.")
                
            
            
        else:
            if mängija2_asetus in mängija1_vara or mängija2_asetus in mängija2_vara:
                print("See kaart pole müügiks.")
                
            elif mängija2_asetus not in rongijaamad and mängija2_asetus not in vesi_ja_elekter and  f.näita_krunti(mängija2_asetus) == "Selle nimelist krunti pole":
                print("Seda kohta ei saa osta.")
                
            else:
                if mängija2_vara[0] >= int((f.näita_krunti(mängija2_asetus))[1]): #kui mängijal on ostuks raha
                    mängija2_vara[0] -= int((f.näita_krunti(mängija2_asetus))[1])
                    mängija2_vara.append(mängija2_asetus)
                    print(mängija2_asetus, "ostetud.")
                    print("Teie kontol on", str(mängija2_vara[0]), "eurot.")
                    
                else:
                    print("Teil jääb puudu", str(((f.näita_krunti(mängija2_asetus))[1]) - mängija2_vara[0]), "eurot.")
            
    
    elif (käsk.split()[0]).lower() == "pandi":
        panditav = käsk.split() #saab järjendi
        del panditav[0] #eemaldab "pandi" osa
        panditav = " ".join(panditav) #saab krundinime
        print(panditav)
        if käik %2==0: #kui on 1. mängija käik
            if panditav in mängija1_vara:
                if panditav in väljasta_tänavad(mängija1_vara):
                    mängija1_vara = f.pandi_krunt(panditav, mängija1_vara) #pandib
                    print("Teie kontol on nüüd " + str(mängija1_vara[0]) + " eurot.")
                else:
                    print("Te ei saa kaarti " + panditav + "pantida")
                
            else:
                print("Teil pole seda krunti.")
                
        else:
            if panditav in mängija2_vara:#kui on 2. mängija käik
                if panditav in väljasta_tänavad(mängija2_vara):
                    mängija2_vara = f.pandi_krunt(panditav, mängija2_vara) #pandib
                    print("Teie kontol on nüüd " + str(mängija2_vara[0]) + " eurot.")
                else:
                    print("Te ei saa kaarti " + panditav + "pantida")
            else:
                print("Teil pole seda krunti.")
                
    elif käsk.lower() == "osta hotell":
        if käik % 2 == 0: #ehk kui äsja käis mängija 1(sest käik += 1 oli "lõpp" lõpus)
            if mängija1_asetus not in mängija1_vara:
                print("See pole teie krunt.")
            
            elif mängija1_asetus in hotellid:
                print("Siin krundil on juba hotell.")
            
            else:
                if f.näita_krunti(mängija1_asetus) != "Selle nimelist krunti pole": #Et tegu oleks krundiga, mitte näiteks raudteejaamaga.
                    värvide_järjend = f.kas_värvid_on_koos(mängija1_vara) #järjend värvidest, mis mängijal on koos
                    if mängija1_vara[0] >= int((f.näita_krunti(mängija1_asetus))[6]): #Kui mängijal on hotelli ostmiseks piisavalt raha
                        if värvide_järjend != "Sel mängijal pole ühtki värvi koos.": #Kui mängijal on koos mingi värv
                            
                            for i in värvide_järjend: # mingi värv, mis on koos
                
                                if len(f.näita_värvi(i)) == 14: #kui on kahekrundine värv
                                    vajalikud_krundid = (f.näita_värvi(i)[0], f.näita_värvi(i)[7])#see on ühe värvi kõigi kruntide järjend.
                                     
                                    if vajalikud_krundid[0] == mängija1_asetus or vajalikud_krundid[1] == mängija1_asetus: #kui mängija asub ühel kahest koos oleva värvi kruntidest.
                                        if vajalikud_krundid[0] in mängija1_vara and vajalikud_krundid[1] in mängija1_vara:
                                            mängija1_vara[0] -= int((f.näita_krunti(mängija1_asetus))[6]) #Võtab raha
                                            hotellid.append(mängija1_asetus) #Lisab krundi hotellidega kruntide järjendisse.
                                            print("Hotell ostetud.\nTeie kontol on", str(mängija1_vara[0]), "eurot.")
                                            hotelliteenindus = True #ehk hotell osteti
                                            
                                if len(f.näita_värvi(i)) == 21: #kui on kahekrundine värv
                                    vajalikud_krundid = (f.näita_värvi(i)[0], f.näita_värvi(i)[7], f.näita_värvi(i)[14])#see on ühe värvi kõigi kruntide järjend.
                                     
                                    if vajalikud_krundid[0] == mängija1_asetus or vajalikud_krundid[1] == mängija1_asetus or vajalikud_krundid[2] == mängija1_asetus: #kui mängija asub ühel kolmest koos oleva värvi kruntidest.
                                        if vajalikud_krundid[0] in mängija1_vara and vajalikud_krundid[1] in mängija1_vara and vajalikud_krundid[2] in mängija1_vara: #Kui mängijal on kõik krundid selles värvis
                                            mängija1_vara[0] -= int((f.näita_krunti(mängija1_asetus))[6]) #Võtab raha
                                            hotellid.append(mängija1_asetus) #Lisab krundi hotellidega kruntide järjendisse.
                                            print("Hotell ostetud.\nTeie kontol on", str(mängija1_vara[0]), "eurot.")
                                            hotelliteenindus = True #ehk hotell osteti    
                       
                            if hotelliteenindus == False: #kui ei ostetud hotelli
                                print("Teil pole selle krundi värvi koos.")
                            hotelliteenindus = False # et eelmine if-lause töötaks ka järgmine kord.
                       
                        else:
                            print("Teil pole selle krundi värvi koos")
                       
                    else:
                        print("Teil on hotelli ostmiseks puudu", str(int((f.näita_krunti(mängija1_asetus))[6])-mängija1_vara[0]), "eurot.")
                    
                else:
                    print("Te ei saa asukohale", mängija1_asetus, "hotelli osta.")
                    
        else:
            if mängija2_asetus not in mängija2_vara:
                print("See pole teie krunt.")
            
            elif mängija2_asetus in hotellid:
                print("Siin krundil on juba hotell.")
            
            else:
                if f.näita_krunti(mängija2_asetus) != "Selle nimelist krunti pole": #Et tegu oleks krundiga, mitte näiteks raudteejaamaga.
                    värvide_järjend = f.kas_värvid_on_koos(mängija2_vara) #järjend värvidest, mis mängijal on koos
                    if mängija2_vara[0] >= int((f.näita_krunti(mängija2_asetus))[6]): #Kui mängijal on hotelli ostmiseks piisavalt raha
                        if värvide_järjend != "Sel mängijal pole ühtki värvi koos.": #Kui mängijal on koos mingi värv
                            
                            for i in värvide_järjend: # mingi värv, mis on koos
                                
                                if len(f.näita_värvi(i)) == 14: #kui on kahekrundine värv
                                    vajalikud_krundid = (f.näita_värvi(i)[0], f.näita_värvi(i)[7])#see on ühe värvi kõigi kruntide järjend.
                                    
                                    if vajalikud_krundid[0] == mängija2_asetus or vajalikud_krundid[1] == mängija2_asetus: #kui mängija asub ühel kahest koos oleva värvi kruntidest.
                                        if vajalikud_krundid[0] in mängija2_vara and vajalikud_krundid[1] in mängija2_vara:
                                            mängija2_vara[0] -= int((f.näita_krunti(mängija2_asetus))[6]) #Võtab raha
                                            hotellid.append(mängija2_asetus) #Lisab krundi hotellidega kruntide järjendisse.
                                            print("Hotell ostetud.\nTeie kontol on", str(mängija2_vara[0]), "eurot.")
                                            hotelliteenindus = True #ehk hotell osteti
                                            
                                if len(f.näita_värvi(i)) == 21: #kui on kahekrundine värv
                                    vajalikud_krundid = (f.näita_värvi(i)[0], f.näita_värvi(i)[7], f.näita_värvi(i)[14])#see on ühe värvi kõigi kruntide järjend.
                                    
                                     
                                    if vajalikud_krundid[0] == mängija2_asetus or vajalikud_krundid[1] == mängija2_asetus or vajalikud_krundid[2] == mängija2_asetus: #kui mängija asub ühel kolmest koos oleva värvi kruntidest.
                                        if vajalikud_krundid[0] in mängija2_vara and vajalikud_krundid[1] in mängija2_vara and vajalikud_krundid[2] in mängija2_vara: #Kui mängijal on kõik krundid selles värvis
                                            mängija2_vara[0] -= int((f.näita_krunti(mängija2_asetus))[6]) #Võtab raha
                                            hotellid.append(mängija2_asetus) #Lisab krundi hotellidega kruntide järjendisse.
                                            print("Hotell ostetud.\nTeie kontol on", str(mängija2_vara[0]), "eurot.")
                                            hotelliteenindus = True #ehk hotell osteti    
                       
                            if hotelliteenindus == False: #kui ei ostetud hotelli
                                print("Teil pole selle krundi värvi koos.")
                            hotelliteenindus = False # et eelmine if-lause töötaks ka järgmine kord.
                       
                       
                       
                    else:
                        print("Teil on hotelli ostmiseks puudu", str(int((f.näita_krunti(mängija2_asetus))[6])-mängija2_vara[0]), "eurot.")
                    
                else:
                    print("Te ei saa asukohale", mängija2_asetus, "hotelli osta.")
                    
                    
                    
    elif käsk.lower() == "müü": #Kui mängija soovib mingit oma kaarti müüa
        if käik % 2 == 0: #ehk kui äsja käis mängija 1(sest käik += 1 oli "lõpp" lõpus)
            varad = f.müük(mängija1_vara, mängija2_vara, käik)
            mängija1_vara = varad[0] #uued varad
            mängija2_vara = varad[1]
        else:
            varad = f.müük(mängija2_vara, mängija1_vara, käik)
            mängija2_vara = varad[0]
            mängija1_vara = varad[1]
        
    
    elif käsk.lower() == "mängu lõpp":#et else: ei rakendaks
        ...
        
        
        
    else:
        print('See pole konsoolile tuntud käsk. Et näha käske, kirjutage "käsud".')


            

if mängija1_vara[0] < 0: #kui keegi võitis mängu
    print("Palju õnne mängija 2! Te olete rivaalitu äriparun. Teie varad on järgnevad:")
    print_mängija(mängija2_vara, hotellid)
    
elif mängija2_vara[0] < 0:
    print("Palju õnne mängija 1! Te olete rivaalitu äriparun. Teie varad on järgnevad:")
    print_mängija(mängija1_vara, hotellid)
    
print("Mängu lõpp.")
