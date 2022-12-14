import funktsioonid
f = funktsioonid        

mängija1_raha=1500 #Raha arvestamine mängija kohta
mängija2_raha=1500
mängija1_vangla_käik=0#kontrollib, mitu käiku on mängija vanglas olnud. Kui see on võrdne kolmega, siis mängija pääseb vanglast
mängija2_vangla_käik=0
käik=1 #Näitab üldist mängu käiku
mängija1_asetus="Go" #Mängija asetus. Algpositsioon on stardiruut "Go"
mängija2_asetus="Go"
mängija1_vanglas=False #Kui selle staatus on True, käivitub vangla funktsioon
mängija2_vanglas=False
hotelliteenindus = False

rongijaamad = ("Ülenurme rongijaam","Kirsi rongijaam","Aardla rongijaam","Tartu rongijaam")
vesi_ja_elekter = ("Elektrivõrk","Veevärk",)
maksud = ("Tulumaks","Lisamaks")
mängija1_vara = [mängija1_raha] #sellest saab list, kus sees on mängija raha, krundid ja vanglastpääsu kaart
mängija2_vara = [mängija2_raha]

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
    
    
        
    elif (käsk.split()[0]).lower() == "värvid":
        värv = input("Mis sorti kaartide kohta te teada tahate?\n")
        print(f.print_värv(f.näita_värvi(värv.lower()))) #rakendab kaks funktsiooni, millest sisemise argument on värvi nimi
        print("") #reavahe
        
        
    elif (käsk.split()[0]).lower() == "krunt":
        tänava_nim = input("Mis krundi kohta te infot tahate?\n")
        print(f.print_krunt(f.näita_krunti(tänava_nim.lower()))) #pmst sama, mis eelmine aga ühe krundi kohta
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
            mängija2_info=f.liikumine(käik,mängija2_asetus,2, mängija2_vanglas,mängija2_vangla_käik, mängija2_vara[0])#Saab enniku, kus esimene väärtus on mängija asetus ja teine on vangla staatus
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
                            if mängija2_vara[0] >= 150:
                                mängija2_vara[0] >= 200
                                mängija2_vara[0] -= 200
                                mängija2_vara.append(mängija2_asetus)
                                print("Kontolt eemaldatud 200 eurot.")
                                print("Teie kontol on " + str(mängija2_vara[0])+ " eurot.")
                            else:
                                print("Teil on selle ostmiseks puudu " + str(200 - mängija2_vara[0]) + " eurot.")
                                print('Te võite oma krunte pantida ettenähtud hinna eest ning siis uuesti osta proovida.\nRohkemaks infoks kirjutage "käsud".')
                        
                        elif mängija2_asetus in vesi_ja_elekter:
                            if mängija2_vara[0] >= 150:
                                mängija2_vara[0] >= 150
                                mängija2_vara[0] -= 150
                                mängija2_vara.append(mängija2_asetus)
                                print("Kontolt eemaldatud 150 eurot.")
                                print("Teie kontol on " + str(mängija2_vara[0])+ " eurot.")
                            else:
                                print("Teil on selle ostmiseks puudu " + str(150 - mängija2_vara[0]) + " eurot.")
                                print('Te võite oma krunte pantida ettenähtud hinna eest ning siis uuesti osta proovida.\nRohkemaks infoks kirjutage "käsud".')
                        
                            
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
                    
                    
                    elif käsk == "võit": #kui mäng kaotati
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
                if mängija2_vanglas == True:
                    print("Jääte vanglasse, käituge korralikult.")
                else:
                    print('''Külastades vanglat näete silti:
"Tulge üürnikuks! Rent on tasuta."''')
                
            else:
                print("Maandusite asukohale " + mängija2_asetus + ". Sellel kohal funktsiooni pole.")
                            
                            
                            
                            
                            
################################################################################################################################                       
    
                            
                            
        else:
            mängija1_info=f.liikumine(käik,mängija1_asetus,1, mängija1_vanglas,mängija1_vangla_käik, mängija1_vara[0])
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

                    
                    if rent > mängija1_vara[0]: #Kui mängijal pole piisavalt raha
                        mängija1_vara[0] = (f.endgame(rent, mängija1_vara, käsk))[0]
                        mängija1_vara[0] -= rent
                        if mängija1_vara[0] < 0:
                            käsk = "võit"                                                            
                    
                    
                    elif käsk == "võit": #kui mäng kaotati
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
                if mängija1_vanglas == True:
                    print("Jääte vanglasse, käituge korralikult.")
                else:
                    print('''Külastades vanglat näete silti:
"Tulge üürnikuks! Rent on tasuta."''')
                    
            else:
                print("Maandusite asukohale " + mängija1_asetus + ". Sellel kohal funktsiooni pole.")
            
            
            
        käik+=1
    
    
    elif käsk.lower() == "osta":
        if käik % 2 == 0: #ehk  kui äsja käis mängija 1(sest käik += 1 oli lõpus)
            if mängija1_asetus in mängija1_vara or mängija1_asetus in mängija2_vara:
                print("See kaart pole müügiks.")
                
            elif mängija1_asetus not in rongijaamad and mängija1_asetus not in vesi_ja_elekter and  f.näita_krunti(mängija1_asetus) == "Selle nimelist krunti pole":
                print("Seda kohta ei saa osta.")
                
            else:
                if f.näita_krunti(mängija1_asetus) != "Selle nimelist krunti pole":
                    if mängija1_vara[0] >= int((f.näita_krunti(mängija1_asetus))[1]): #kui mängijal on ostuks raha
                        mängija1_vara[0] -= int((f.näita_krunti(mängija1_asetus))[1])
                        mängija1_vara.append(mängija1_asetus)
                        print(mängija1_asetus, "ostetud.")
                        print("Teie kontol on", str(mängija1_vara[0]), "eurot.")
                        
                    else:
                        print("Teil jääb puudu", str(int((f.näita_krunti(mängija1_asetus))[1]) - mängija1_vara[0]), "eurot.")
                        
                elif mängija1_asetus in rongijaamad:
                    if mängija1_vara[0] >= 200: #kui mängijal on ostuks raha
                        mängija1_vara[0] -= 200
                        mängija1_vara.append(mängija1_asetus)
                        print(mängija1_asetus, "ostetud.")
                        print("Teie kontol on", str(mängija1_vara[0]), "eurot.")
                        
                    else:
                        print("Teil jääb puudu", str(200 - mängija1_vara[0]), "eurot.")
                        
                else:
                    if mängija1_vara[0] >= 150: #kui mängijal on ostuks raha
                        mängija1_vara[0] -= 150
                        mängija1_vara.append(mängija1_asetus)
                        print(mängija1_asetus, "ostetud.")
                        print("Teie kontol on", str(mängija1_vara[0]), "eurot.")
                    
                    else:
                        print("Teil jääb puudu", str(150 - mängija1_vara[0]), "eurot.")
            
            
        else:
            if mängija2_asetus in mängija1_vara or mängija2_asetus in mängija2_vara:
                print("See kaart pole müügiks.")
                
            elif mängija2_asetus not in rongijaamad and mängija2_asetus not in vesi_ja_elekter and  f.näita_krunti(mängija2_asetus) == "Selle nimelist krunti pole":
                print("Seda kohta ei saa osta.")
                
            else:
                if f.näita_krunti(mängija2_asetus) != "Selle nimelist krunti pole":
                    if mängija2_vara[0] >= int((f.näita_krunti(mängija2_asetus))[1]): #kui mängijal on ostuks raha
                        mängija2_vara[0] -= int((f.näita_krunti(mängija2_asetus))[1])
                        mängija2_vara.append(mängija2_asetus)
                        print(mängija2_asetus, "ostetud.")
                        print("Teie kontol on", str(mängija2_vara[0]), "eurot.")
                        
                    else:
                        print("Teil jääb puudu", str(int((f.näita_krunti(mängija2_asetus))[1]) - mängija2_vara[0]), "eurot.")
                        
                elif mängija2_asetus in rongijaamad:
                    if mängija2_vara[0] >= 200: #kui mängijal on ostuks raha
                        mängija2_vara[0] -= 200
                        mängija2_vara.append(mängija2_asetus)
                        print(mängija2_asetus, "ostetud.")
                        print("Teie kontol on", str(mängija2_vara[0]), "eurot.")
                        
                else:
                    if mängija2_vara[0] >= 150: #kui mängijal on ostuks raha
                        mängija2_vara[0] -= 150
                        mängija2_vara.append(mängija2_asetus)
                        print(mängija2_asetus, "ostetud.")
                        print("Teie kontol on", str(mängija2_vara[0]), "eurot.")
            
            
            
    
    elif (käsk.split()[0]).lower() == "pandi": #Kui mängija soovib oma krunti pangale pantida
        
        krunt = input("Mis krunti te pantida tahate?\n")
        
        kas_on_krunt = False
        kas_mängijal_on_kaart = False
        i = 1
                
        if käik %2==0: #kui on 1. mängija käik
            
            while i in range(len(mängija1_vara)):
                if mängija1_vara[i].lower() == krunt.lower():
                    kas_mängijal_on_kaart = True
                i += 1
                  
            for el in f.väljasta_tänavad(mängija1_vara):
                if el.lower() == krunt.lower():
                    kas_on_krunt = True
                    panditav = el
                
                
            if kas_mängijal_on_kaart == True:
                if kas_on_krunt == True:
                    mängija1_vara = f.pandi_krunt(panditav, mängija1_vara) #pandib
                    print("Teie kontol on nüüd " + str(mängija1_vara[0]) + " eurot.")
                else:
                    print("Te ei saa kaarti " + panditav + "pantida")
                
            else:
                print("Teil pole seda krunti.")
                
        else: #kui on 2. mängija käik
            
            while i in range(len(mängija2_vara)):
                if mängija2_vara[i].lower() == krunt.lower():
                    kas_mängijal_on_kaart = True
                i += 1  
                  
            for el in f.väljasta_tänavad(mängija2_vara):
                if el.lower() == krunt.lower():
                    kas_on_krunt = True
                    panditav = el
                
            if kas_mängijal_on_kaart == True:
                if kas_on_krunt == True:
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
    print("\nPalju õnne mängija 2! Te olete rivaalitu äriparun. Teie varad on järgnevad:")
    f.print_mängija(mängija2_vara, hotellid)
    
elif mängija2_vara[0] < 0:
    print("\nPalju õnne mängija 1! Te olete rivaalitu äriparun. Teie varad on järgnevad:")
    f.print_mängija(mängija1_vara, hotellid)
    
    

print("""
Mängu lõpp.
===MONOPOL===""")