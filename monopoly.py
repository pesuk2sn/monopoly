from time import sleep
import random
import funktsioonid
f = funktsioonid
#tp märgib tasuta parkimist, ehk ühegi mõjuta kohti.
mängulaud = ("tp","Jaama tänav" ,"tp","Soinaste tänav" ,"tp","tp","Ravila tänav" ,"tp","Ringtee tänav" ,"Ilmatsalu tänav" ,"vangla","Vabaduse pst" ,"tp","Sõbra tänav" ,"Kesk kaar" ,"tp","Kalevi tänav" ,"tp","F.R Kreutzvaldi tänav" ,"Vaksali tänav" ,"tp","Pikk tänav" ,"tp","Aardla tänav" ,"Puussepa tänav" ,"tp","Puiestee tänav" ,"Kalda tee" ,"tp","Võru tänav" ,"tp","Turu tänav" ,"Narva maantee" ,"tp","Riia tänav" ,"tp","tp","Rüütli tänav" ,"tp","Raekoja plats" ,)



def vangla(kinni):
    i=1
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
def liikumine(mängija_asetus, käik): #kommenteerin, et mõista, mis täpsemalt toimub
    i=0
    sammud=0
    kinni = False
    
    while True:
        
        print("Veeretan täringuid") #täringumehhanism
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
        
        print("Veeretasid 1. täringul numbri " + str(täring_1))
        sleep(0.3)
        print("Veeretasid 2. täringul numbri " + str(täring_2))
        sleep(0.5)
        
        
        if int(täring_1) == int(täring_2): #duublimehhanism
            i+=1
            
            sammud=täring_1+täring_2 #uptate'b mängija asetust
            mängija_asetus += sammud
            
            print("Veeretasid duubli, veeretab uuesti.")
            
            for u in range(2):#veeretab uuesti
                
                täring_1=random.randint(1,6)
                täring_2=random.randint(1,6)
                
                print("Veeretasid 1. täringul numbri " + str(täring_1))
                sleep(0.3)
                print("Veeretasid 2. täringul numbri " + str(täring_2))
                sleep(0.5)
                
                sammud=täring_1+täring_2
                mängija_asetus += sammud
                
                if int(täring_1) != int(täring_2):
                    i += 1
                    break
                
                else:
                    print("Veeretasid duubli, veeretab uuesti.")
                    i += 1
                    
            if i >= 4:
                print("Lähed vangi!")
                i=0
                käik+=1
                kinni=True
                [mängija_asetus, käik, kinni]
            
            else:
                
                if mängija_asetus>41:
                    mängija_asetus-40
                
                käik+=1
                return [mängija_asetus, käik, kinni]
            

        else:
            if mängija_asetus>41:
                mängija_asetus-40
                sammud = täring_1+täring_2
                mängija_asetus += sammud
                käik+=1
                return [mängija_asetus, käik, kinni]
        
        sammud = täring_1+täring_2
        mängija_asetus += sammud
        
        if mängija_asetus>41:
            mängija_asetus-40
        käik+=1
        return [mängija_asetus, käik, kinni]

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#siit algab mäng
    
käsk = input('''===MONOPOL===
Teretulemast maailmakuulsa lauamängu Monopol arvutimängu!
Leidke konkurent, võtke istet ja jätke empaatiaga hüvasti!
Alustamiseks kirjutage "start".
''')

while käsk != "start":
    käsk = input('''Kirjutage "start" ilma jutumärkideta.
''')
    
print('Mäng on alanud. Selleks, et teada, mis te teha saate kirjutage "käsud". Esimesena käib mängija_1, teisena mängija_2.')
mängija_1 = [750] #jagab mängijatele raha ära
mängija_2 = [750]
asetus_1 = 1
asetus_2 = 1


while käsk != "lõpp":
    
    käsk = input("Valige, mida teha: ")
    
    if käsk == "käsud":
        print(f.käsud())
        
    elif käsk.split()[0] == "värv":
        print(f.print_värv(f.näita_värvi(käsk.split()[1]))) #rakendab kaksfunktsiooni, millest sisemise argument on värvi nimi
        print("") #reavahe
        
    elif käsk.split()[0] == "krunt":
        tänava_nim_järjend = käsk.split()
        del tänava_nim_järjend[0]
        tänava_nim = " ".join(tänava_nim_järjend)
        print(f.print_krunt(f.näita_krunti(tänava_nim))) #pmst sama, mis eelmine aga ühe krundi kohta
        print("") #reavahe
        
    elif käsk.split()[0] == "isik":
        
        if käsk.split()[1] == "mängija_1":
            print(f.print_mängija(mängija_1))
        elif käsk.split()[1] == "mängija_2":
            print(f.print_mängija(mängija_2))
            
        else:
            print("See pole mängija nimi.\n")
    
    #elif käsk == "käigu lõpp": #See käsk on selline, et initsiatiiv vahetub ning uue mängija eest veeretatakse ning maandutakse kuskil.
        
            
            
            
            
"""
käik=1
#sammud=0
mängulaud=list(range(0,40))
mängija1_asetus=0
mängija2_asetus=0

while käik <30:
    kontroll=0
    if käik %2==0:
        mängija2_info=liikumine(käik,mängija2_asetus,2, mängija2_vanglas,mängija2_vangla_käik, mängija2_raha)#Saab enniku, kus esimene väärtus on mängija asetus ja teine on vangla staatus
        mängija2_asetus = mängija2_info[0]
        mängija2_vanglas = mängija2_info[1]
        mängija2_vangla_käik=mängija2_info[2]
        print("Mängija 2 on ruudul " +str(mängija2_asetus)+"\n")
    else:
        mängija1_info=liikumine(käik,mängija1_asetus,1, mängija1_vanglas,mängija1_vangla_käik, mängija1_raha)
        mängija1_asetus = mängija1_info[0]
        mängija1_vanglas = mängija1_info[1]
        mängija1_vangla_käik = mängija1_info[2]
        print("Mängija 1 on ruudul "+str(mängija1_asetus)+"\n")
    käik+=1
        mängija1_asetus=liikumine(mängija1_asetus)
        print("Mängija 1 on ruudul "+str(mängija1_asetus))
    käik+=1"""
    


    
