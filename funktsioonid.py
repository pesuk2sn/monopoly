

def näita_värvi(värv): #See väljastab mingi värvi kõigi kruntide muutujad selles järjekorras:
                        #tänavanimi, hind, rent, rent kui ühel mängijal värv on koos, rent hotelliga, pant, hotelli hind
    
    pruunid = ("Jaama tänav","Soinaste tänav") #krundid värvide järgi jaotatud
    helesinised = ("Ravila tänav","Ringtee tänav","Ilmatsalu tänav")
    roosad = ("Vabaduse pst","Sõbra tänav","Kesk kaar")
    oranzid = ("Kalevi tänav","F.R Kreutzvaldi tänav","Vaksali tänav")
    punased = ("Pikk tänav","Aardla tänav","Puussepa tänav")
    kollased = ("Puiestee tänav","Kalda tee","Võru tänav")
    rohelised = ("Turu tänav","Narva maantee","Riia tänav")
    tumesinised = ("Rüütli tänav","Raekoja plats")
    
    #Eespool saab olema kaheksa korda pmst sama if lauset, teid on hoiatatud.
    #See on seepärast, et ma ei suutnud välja mõelda viisi, kuidas vaadata, kas mängija input on võrdne vastava ennikuga
    
    
    if värv == "pruunid":
        with open("Monopoli krundid.txt", "r", encoding="UTF-8") as f: #Avab faili lugemiseks
            rida = f.readline()
            kruntide_maatriks = [] #seda läheb hiljem vaja
            while rida: #kuni on ridu, mida lugeda
                rida = rida.replace("\n", "") #eemaldab reavahetuse

                
                if rida in pruunid: # Vaatab, kas sisestatud värv ühtib enniku nimega
                    
                    tänavanimi = rida
                    
                    rida = f.readline() #siin, kuni pmst if-lause lõpuni teeb järgnevat: loeb rea, omastab sellele muutuja ja loeb järgmise, kuni kõik ühe tänava kohta on loetud.
                    hind = rida
                    
                    rida = f.readline()
                    rent = rida
                    rida = rida.replace("\n", "")
                    rida = int(rida)*2
                    rent_kui_värv_on_koos = str(rida) + "\n"
                    
                    rida = f.readline()
                    rent_hotelliga = rida
                    
                    rida = f.readline()
                    pant = rida
                    
                    rida = f.readline()
                    hotelli_hind = rida
                    
                    
                    sõne = hind + rent + rent_kui_värv_on_koos + rent_hotelliga + pant + hotelli_hind
                    sõne = sõne.replace("\n", " ") #saab reavahetustest lahti
                    tänav = [tänavanimi] #kui tänavanimes on tühik sees, et siis ei looks mitut elementi sellest
                    krundi_list = tänav + sõne.split(" ") #loob järjendi, kus on saadud info salvestatud.
                    del krundi_list[7] #et tühi sõne ei tuleks järjendi elemendiks
                     
                    kruntide_maatriks += krundi_list #lisab järjendi suuremasse järjendisse, et krundi_list-i muutujaid saaks taaskord kasutada, kaotamata enne salvestatud infot.
                else:
                    rida = f.readline() #võtab uue rea, et igavest loopi ei jääks
                    
                    
                    
    elif värv == "helesinised":
        with open("Monopoli krundid.txt", "r", encoding="UTF-8") as f: #Avab faili lugemiseks
            rida = f.readline()
            kruntide_maatriks = [] #seda läheb hiljem vaja
            while rida: #kuni on ridu, mida lugeda
                rida = rida.replace("\n", "") #eemaldab reavahetuse

                
                if rida in helesinised: # Vaatab, kas sisestatud värv ühtib enniku nimega
                    
                    tänavanimi = rida
                    
                    rida = f.readline() #siin, kuni pmst if-lause lõpuni teeb järgnevat: loeb rea, omastab sellele muutuja ja loeb järgmise, kuni kõik ühe tänava kohta on loetud.
                    hind = rida
                    
                    rida = f.readline()
                    rent = rida
                    rida = rida.replace("\n", "")
                    rida = int(rida)*2
                    rent_kui_värv_on_koos = str(rida) + "\n"
                    
                    rida = f.readline()
                    rent_hotelliga = rida
                    
                    rida = f.readline()
                    pant = rida
                    
                    rida = f.readline()
                    hotelli_hind = rida
                    
                    
                    sõne =  hind + rent + rent_kui_värv_on_koos + rent_hotelliga + pant + hotelli_hind
                    sõne = sõne.replace("\n", " ") #saab reavahetustest lahti
                    tänav = [tänavanimi] #kui tänavanimes on tühik sees, et siis ei looks mitut elementi sellest
                    krundi_list = tänav + sõne.split(" ") #loob järjendi, kus on saadud info salvestatud.
                    del krundi_list[7] #et tühi sõne ei tuleks järjendi elemendiks
                    
                    kruntide_maatriks += krundi_list #lisab järjendi suuremasse järjendisse, et krundi_list-i muutujaid saaks taaskord kasutada, kaotamata enne salvestatud infot.
                else:
                    rida = f.readline() #võtab uue rea, et igavest loopi ei jääks
                    
                    
                    
    elif värv == "roosad":
        with open("Monopoli krundid.txt", "r", encoding="UTF-8") as f: #Avab faili lugemiseks
            rida = f.readline()
            kruntide_maatriks = [] #seda läheb hiljem vaja
            while rida: #kuni on ridu, mida lugeda
                rida = rida.replace("\n", "") #eemaldab reavahetuse

                
                if rida in roosad: # Vaatab, kas sisestatud värv ühtib enniku nimega
                    
                    tänavanimi = rida
                    
                    rida = f.readline() #siin, kuni pmst if-lause lõpuni teeb järgnevat: loeb rea, omastab sellele muutuja ja loeb järgmise, kuni kõik ühe tänava kohta on loetud.
                    hind = rida
                    
                    rida = f.readline()
                    rent = rida
                    rida = rida.replace("\n", "")
                    rida = int(rida)*2
                    rent_kui_värv_on_koos = str(rida) + "\n"
                    
                    rida = f.readline()
                    rent_hotelliga = rida
                    
                    rida = f.readline()
                    pant = rida
                    
                    rida = f.readline()
                    hotelli_hind = rida
                    
                    
                    sõne =  hind + rent + rent_kui_värv_on_koos + rent_hotelliga + pant + hotelli_hind
                    sõne = sõne.replace("\n", " ") #saab reavahetustest lahti
                    tänav = [tänavanimi] #kui tänavanimes on tühik sees, et siis ei looks mitut elementi sellest
                    krundi_list = tänav + sõne.split(" ") #loob järjendi, kus on saadud info salvestatud.
                    del krundi_list[7] #et tühi sõne ei tuleks järjendi elemendiks
                    
                    kruntide_maatriks += krundi_list #lisab järjendi suuremasse järjendisse, et krundi_list-i muutujaid saaks taaskord kasutada, kaotamata enne salvestatud infot.
                else:
                    rida = f.readline() #võtab uue rea, et igavest loopi ei jääks
                    
                    
    elif värv == "oranzid":
        with open("Monopoli krundid.txt", "r", encoding="UTF-8") as f: #Avab faili lugemiseks
            rida = f.readline()
            kruntide_maatriks = [] #seda läheb hiljem vaja
            while rida: #kuni on ridu, mida lugeda
                rida = rida.replace("\n", "") #eemaldab reavahetuse

                
                if rida in oranzid: # Vaatab, kas sisestatud värv ühtib enniku nimega
                    
                    tänavanimi = rida
                    
                    rida = f.readline() #siin, kuni pmst if-lause lõpuni teeb järgnevat: loeb rea, omastab sellele muutuja ja loeb järgmise, kuni kõik ühe tänava kohta on loetud.
                    hind = rida
                    
                    rida = f.readline()
                    rent = rida
                    rida = rida.replace("\n", "")
                    rida = int(rida)*2
                    rent_kui_värv_on_koos = str(rida) + "\n"
                    
                    rida = f.readline()
                    rent_hotelliga = rida
                    
                    rida = f.readline()
                    pant = rida
                    
                    rida = f.readline()
                    hotelli_hind = rida
                    
                    
                    sõne =  hind + rent + rent_kui_värv_on_koos + rent_hotelliga + pant + hotelli_hind
                    sõne = sõne.replace("\n", " ") #saab reavahetustest lahti
                    tänav = [tänavanimi] #kui tänavanimes on tühik sees, et siis ei looks mitut elementi sellest
                    krundi_list = tänav + sõne.split(" ") #loob järjendi, kus on saadud info salvestatud.
                    del krundi_list[7] #et tühi sõne ei tuleks järjendi elemendiks
                    
                    kruntide_maatriks += krundi_list #lisab järjendi suuremasse järjendisse, et krundi_list-i muutujaid saaks taaskord kasutada, kaotamata enne salvestatud infot.
                else:
                    rida = f.readline() #võtab uue rea, et igavest loopi ei jääks
                    
                    
                    
    elif värv == "punased":
        with open("Monopoli krundid.txt", "r", encoding="UTF-8") as f: #Avab faili lugemiseks
            rida = f.readline()
            kruntide_maatriks = [] #seda läheb hiljem vaja
            while rida: #kuni on ridu, mida lugeda
                rida = rida.replace("\n", "") #eemaldab reavahetuse

                
                if rida in punased: # Vaatab, kas sisestatud värv ühtib enniku nimega
                    
                    tänavanimi = rida
                    
                    rida = f.readline() #siin, kuni pmst if-lause lõpuni teeb järgnevat: loeb rea, omastab sellele muutuja ja loeb järgmise, kuni kõik ühe tänava kohta on loetud.
                    hind = rida
                    
                    rida = f.readline()
                    rent = rida
                    rida = rida.replace("\n", "")
                    rida = int(rida)*2
                    rent_kui_värv_on_koos = str(rida) + "\n"
                    
                    rida = f.readline()
                    rent_hotelliga = rida
                    
                    rida = f.readline()
                    pant = rida
                    
                    rida = f.readline()
                    hotelli_hind = rida
                    
                    
                    sõne =  hind + rent + rent_kui_värv_on_koos + rent_hotelliga + pant + hotelli_hind
                    sõne = sõne.replace("\n", " ") #saab reavahetustest lahti
                    tänav = [tänavanimi] #kui tänavanimes on tühik sees, et siis ei looks mitut elementi sellest
                    krundi_list = tänav + sõne.split(" ") #loob järjendi, kus on saadud info salvestatud.
                    del krundi_list[7] #et tühi sõne ei tuleks järjendi elemendiks
                    
                    kruntide_maatriks += krundi_list #lisab järjendi suuremasse järjendisse, et krundi_list-i muutujaid saaks taaskord kasutada, kaotamata enne salvestatud infot.
                else:
                    rida = f.readline() #võtab uue rea, et igavest loopi ei jääks
                    
                    
                    
    elif värv == "kollased":
        with open("Monopoli krundid.txt", "r", encoding="UTF-8") as f: #Avab faili lugemiseks
            rida = f.readline()
            kruntide_maatriks = [] #seda läheb hiljem vaja
            while rida: #kuni on ridu, mida lugeda
                rida = rida.replace("\n", "") #eemaldab reavahetuse

                
                if rida in kollased: # Vaatab, kas sisestatud värv ühtib enniku nimega
                    
                    tänavanimi = rida
                    
                    rida = f.readline() #siin, kuni pmst if-lause lõpuni teeb järgnevat: loeb rea, omastab sellele muutuja ja loeb järgmise, kuni kõik ühe tänava kohta on loetud.
                    hind = rida
                    
                    rida = f.readline()
                    rent = rida
                    rida = rida.replace("\n", "")
                    rida = int(rida)*2
                    rent_kui_värv_on_koos = str(rida) + "\n"
                    
                    rida = f.readline()
                    rent_hotelliga = rida
                    
                    rida = f.readline()
                    pant = rida
                    
                    rida = f.readline()
                    hotelli_hind = rida
                    
                    
                    sõne =  hind + rent + rent_kui_värv_on_koos + rent_hotelliga + pant + hotelli_hind
                    sõne = sõne.replace("\n", " ") #saab reavahetustest lahti
                    tänav = [tänavanimi] #kui tänavanimes on tühik sees, et siis ei looks mitut elementi sellest
                    krundi_list = tänav + sõne.split(" ") #loob järjendi, kus on saadud info salvestatud.
                    del krundi_list[7] #et tühi sõne ei tuleks järjendi elemendiks
                    
                    kruntide_maatriks += krundi_list #lisab järjendi suuremasse järjendisse, et krundi_list-i muutujaid saaks taaskord kasutada, kaotamata enne salvestatud infot.
                else:
                    rida = f.readline() #võtab uue rea, et igavest loopi ei jääks
                    
                    
    elif värv == "rohelised":
        with open("Monopoli krundid.txt", "r", encoding="UTF-8") as f: #Avab faili lugemiseks
            rida = f.readline()
            kruntide_maatriks = [] #seda läheb hiljem vaja
            while rida: #kuni on ridu, mida lugeda
                rida = rida.replace("\n", "") #eemaldab reavahetuse

                
                if rida in rohelised: # Vaatab, kas sisestatud värv ühtib enniku nimega
                    
                    tänavanimi = rida
                    
                    rida = f.readline() #siin, kuni pmst if-lause lõpuni teeb järgnevat: loeb rea, omastab sellele muutuja ja loeb järgmise, kuni kõik ühe tänava kohta on loetud.
                    hind = rida
                    
                    rida = f.readline()
                    rent = rida
                    rida = rida.replace("\n", "")
                    rida = int(rida)*2
                    rent_kui_värv_on_koos = str(rida) + "\n"
                    
                    rida = f.readline()
                    rent_hotelliga = rida
                    
                    rida = f.readline()
                    pant = rida
                    
                    rida = f.readline()
                    hotelli_hind = rida
                    
                    
                    sõne =  hind + rent + rent_kui_värv_on_koos + rent_hotelliga + pant + hotelli_hind
                    sõne = sõne.replace("\n", " ") #saab reavahetustest lahti
                    tänav = [tänavanimi] #kui tänavanimes on tühik sees, et siis ei looks mitut elementi sellest
                    krundi_list = tänav + sõne.split(" ") #loob järjendi, kus on saadud info salvestatud.
                    del krundi_list[7] #et tühi sõne ei tuleks järjendi elemendiks
                    
                    kruntide_maatriks += krundi_list #lisab järjendi suuremasse järjendisse, et krundi_list-i muutujaid saaks taaskord kasutada, kaotamata enne salvestatud infot.
                else:
                    rida = f.readline() #võtab uue rea, et igavest loopi ei jääks
                    
                    
                    
    elif värv == "tumesinised":
        with open("Monopoli krundid.txt", "r", encoding="UTF-8") as f: #Avab faili lugemiseks
            rida = f.readline()
            kruntide_maatriks = [] #seda läheb hiljem vaja
            while rida: #kuni on ridu, mida lugeda
                rida = rida.replace("\n", "") #eemaldab reavahetuse

                    
                if rida in tumesinised: # Vaatab, kas sisestatud värv ühtib enniku nimega
                        
                    tänavanimi = rida
                        
                    rida = f.readline() #siin, kuni pmst if-lause lõpuni teeb järgnevat: loeb rea, omastab sellele muutuja ja loeb järgmise, kuni kõik ühe tänava kohta on loetud.
                    hind = rida
                    
                    rida = f.readline()
                    rent = rida
                    rida = rida.replace("\n", "")
                    rida = int(rida)*2
                    rent_kui_värv_on_koos = str(rida) + "\n"
                    
                    rida = f.readline()
                    rent_hotelliga = rida
                    
                    rida = f.readline()
                    pant = rida
                    
                    rida = f.readline()
                    hotelli_hind = rida
                    
                    
                    sõne =  hind + rent + rent_kui_värv_on_koos + rent_hotelliga + pant + hotelli_hind
                    sõne = sõne.replace("\n", " ") #saab reavahetustest lahti
                    tänav = [tänavanimi] #kui tänavanimes on tühik sees, et siis ei looks mitut elementi sellest
                    krundi_list = tänav + sõne.split(" ") #loob järjendi, kus on saadud info salvestatud.
                    del krundi_list[7] #et tühi sõne ei tuleks järjendi elemendiks
                    
                    kruntide_maatriks += krundi_list #lisab järjendi suuremasse järjendisse, et krundi_list-i muutujaid saaks taaskord kasutada, kaotamata enne salvestatud infot.
                else:
                    rida = f.readline() #võtab uue rea, et igavest loopi ei jääks
                    
    else:
        kruntide_maatriks = "See pole krundinimi"
                      
                    
    return(kruntide_maatriks)#Okei, see pole sõna otseses mõttes maatriks, kuid ma ei viitsi seda siin selleks muuta, kui seda pole kindlusega nii vaja.
                
                    
                    
                    
                                  
                    
                    
                    #Uus funktsioon
                    
                    
                    
                    
def näita_krunti(krunt):#See väljastab mingi krundi kõik muutujad selles järjekorras:
                        #tänavanimi, hind, rent, rent kui ühel mängijal selle värv on koos, rent hotelliga, pant, hotelli hind
    

                    
        with open("Monopoli krundid.txt", "r", encoding="UTF-8") as f: #Avab faili lugemiseks
            rida = f.readline()

            while rida: #kuni on ridu, mida lugeda
                rida = rida.replace("\n", "") #eemaldab reavahetuse

                    
                if rida == krunt: # Vaatab, kas sisestatud värv ühtib enniku nimega
                        
                    tänavanimi = rida
                        
                    rida = f.readline() #siin, kuni pmst if-lause lõpuni teeb järgnevat: loeb rea, omastab sellele muutuja ja loeb järgmise, kuni kõik ühe tänava kohta on loetud.
                    hind = rida
                    
                    rida = f.readline()
                    rent = rida
                    rida = rida.replace("\n", "")
                    rida = int(rida)*2
                    rent_kui_värv_on_koos = str(rida) + "\n"
                    
                    rida = f.readline()
                    rent_hotelliga = rida
                    
                    rida = f.readline()
                    pant = rida
                    
                    rida = f.readline()
                    hotelli_hind = rida
                    
                    
                    sõne =  hind + rent + rent_kui_värv_on_koos + rent_hotelliga + pant + hotelli_hind
                    sõne = sõne.replace("\n", " ") #saab reavahetustest lahti
                    tänav = [tänavanimi] #kui tänavanimes on tühik sees, et siis ei looks mitut elementi sellest
                    krundi_list = tänav + sõne.split(" ") #loob järjendi, kus on saadud info salvestatud.
                    del krundi_list[7] #et tühi sõne ei tuleks järjendi elemendiks
                    return(krundi_list)
                else:
                    rida = f.readline()#võtab uue rea, et loopi ei jääks
                    
            return("Selle nimelist krunti pole")#Kui käis faili läbi ja ei leidnud tänavad





#Uus funktsioon

def lisa_krunt(krunt, mängija):
    mängija.append(krunt)
    return(mängija)
    
def pandi_krunt(krunt, mängija):
    i = mängija.index(krunt) #võtab krundi indeksi
    with open("Monopoli krundid.txt", "r", encoding="UTF-8") as f: #Avab faili lugemiseks
        rida = f.readline()
        while rida:
            rida = rida.replace("\n", "") #saab reavahetusest lahti
            if rida == krunt:
                for u in range(4): #Loeb ridu nimest alates, kuni jõuab pandini
                     rida = f.readline()
                pant = int(rida)
                mängija[0] += pant #lisab mängijale pandi hinna
                del mängija[i] #eemaldab krundi mängijalt
                return(mängija)
            

                    #See käsk on mõeldud mängijaga otse tegutsema. Täpsemalt see väljastab mängijale info mingit värvi kaardi kohta.
def print_värv(matrix):#See võib olla osa näita_värvi käsust, kuid arvutil on lihtsam leida infot järjendist, kui sõnest.
    
    if type(matrix) != list:
        return("See pole valikus olev värv.")
    
    print("Selle värvi kruntide info on järgnev:\n")
    
    if len(matrix) == 14: #Kui ühes värvis on 2 krunti
        for i in range(2):
            print("Krundinimi:", matrix[(i*7)])
            print("Krundi hind:", matrix[(i*7)+1])
            print("Krundi rent:", matrix[(i*7)+2])
            print("Krundi rent, kui omanik omab kogu värvi:", matrix[(i*7)+3])
            print("Krundi rent hotelliga:", matrix[(i*7)+4])
            print("Krundi pant:", matrix[(i*7)+5])
            print("Hotelli hind:", matrix[(i*7)+6])
            print("") #Üks rida vahele ilu pärast
            
    if len(matrix) == 21: #Kui ühes värvis on 3 krunti
        for i in range(3):
            print("Krundinimi:", matrix[(i*7)])
            print("Krundi hind:", matrix[(i*7)+1])
            print("Krundi rent:", matrix[(i*7)+2])
            print("Krundi rent, kui omanik omab kogu värvi:", matrix[(i*7)+3])
            print("Krundi rent hotelliga:", matrix[(i*7)+4])
            print("Krundi pant:", matrix[(i*7)+5])
            print("Hotelli hind:", matrix[(i*7)+6])
            print("") #Üks rida vahele ilu pärast
    return("")# et "none" lõpus vältida
            
def print_krunt(järjend): #pmst sama, mis print_värv, kuid ühe krundi jaoks
    
    if type(järjend) == str: #kui krundi nimi sisestati valesti
        return("See pole krundi nimi")
    
    else:
        print("Selle krundi info on järgnev: \n")
        print("Krundinimi:", järjend[0])
        print("Krundi hind:", järjend[1])
        print("Krundi rent:", järjend[2])
        print("Krundi rent, kui omanik omab kogu värvi:", järjend[3])
        print("Krundi rent hotelliga:", järjend[4])
        print("Krundi pant:", järjend[5])
        print("Hotelli hind:", järjend[6])
    return("") #et "none" lõpus vältida
    

    
    
def tulumaks(mängija): #kui maandub tulumaksule
    mängija[0] -= 200
    return(mängija)

def lisamaks(mängija): #kui maandub lisamaksule
    mängija[0] -= 100
    return(mängija)

def kas_värvid_on_koos(mängija): #selle funktsiooni eesmärk on näidata, kas mingil mängijal on kõik ühe värvi krundid.
    #Funktsiooni lõpuks on käes järjend, kus 1. element on tõeväärtus ja ülejäänud koos olevad värvid, kui neid on.
    
    
    #POOLELI
    
    pruunid = ("Jaama tänav","Soinaste tänav") #krundid värvide järgi jaotatud
    helesinised = ("Ravila tänav","Ringtee tänav","Ilmatsalu tänav")
    roosad = ("Vabaduse pst","Sõbra tänav","Kesk kaar")
    oranzid = ("Kalevi tänav","F.R Kreutzvaldi tänav","Vaksali tänav")
    punased = ("Pikk tänav","Aardla tänav","Puussepa tänav")
    kollased = ("Puiestee tänav","Kalda tee","Võru tänav")
    rohelised = ("Turu tänav","Narva maantee","Riia tänav")
    tumesinised = ("Rüütli tänav","Raekoja plats")
    
    järjend1 = (helesinised, roosad, oranzid, punased, kollased, rohelised)#ennik kolmeliikmelistest ennikutest
    
    on_vä = 0 #märgib, kas mingi värv on koos. 0 märgib eitust, 1 jaatust
    pruun = 0
    helesin = 0
    roosa = 0
    oranz = 0
    punane = 0
    kollane = 0
    roheline = 0
    tumesin = 0
    
    järjend2 = (helesin, roosa, oranz, punane, kollane, roheline)#ennik kolmeliikmeliste ennikute väärtustest
    vastuse_järjend = []#See, mis lõpus tagastatakse
    
    if pruunid[0] in mängija and pruunid[1] in mängija:
        pruun = 1
        on_vä = 1
        
    if tumesinised[0] in mängija and tumesinised[1] in mängija:
        pruun = 1
        on_vä = 1
        
    for el in range(6): #kuus värvi on, kus on kolm krunti värvi kohta
        if järjend1[el][1] in mängija and järjend1[el][2] in mängija and järjend1[el][1] in mängija:
            järjend2[el] = 1
            on_vä = 1
    
    if on_vä == 1:#kui on mingi värv koos
        vastuse_järjend.append(1)
        
        if pruun == 1: #vaatab värvid ükshaaval üle, kui on koos, siis lisab järjendisse värvi nime
            vastuse_järjend.append("pruunid")
        if helesin == 1:
            vastuse_järjend.append("helesinised")
        if roosa == 1:
            vastuse_järjend.append("roosad")
        if oranz == 1:
            vastuse_järjend.append("oranzid")
        if punane == 1:
            vastuse_järjend.append("punased")
        if kollane == 1:
            vastuse_järjend.append("kollased")
        if roheline == 1:
            vastuse_järjend.append("rohelised")
        if tumesin == 1:
            vastuse_järjend.append("helesinised")
            
    else:
        return("Sel mängijal pole ühtki värvi koos.")
    
    return(vastuse_järjend)
    
    
    
def print_mängija(mängija): #see funktsioon väljastab mängijale info mingi mängija raha ja kaartide kohta
    print("Sul on " + str(mängija[0]) + " eurot")
    
    if len(mängija) > 1:
        if "vangla_vabastus" not in mängija:
            print("Teie krundid on järgnevad: ")
            for el in range(len(mängija)-1): #käib ükshaaval kõik krundid läbi
                print(mängija[el+1]) #el+1, et raha krundiks ei peaks
        else:
            indeks = mängija.index("vangla_vabastus") #eemaldab vanglast vabastuse kaardi
            del mängija[indeks]
            print("Teie krundid on järgnevad: ")
            for el in range(len(mängija)-1): #käib ükshaaval kõik krundid läbi
                print(mängija[el+1]) #el+1, et raha krundiks ei peaks
                
            mängija.append("vangla_vabastus")#lisab vangistpääsemise kaardi tagasi
            print("\n" + "Teil on ka vanglast tasuta pääsemise kaart.")
    
    return("")#et "none" lõpus vältida



    
def käsud():
    return("""Käsud, mida te saate kasutada oma käigu ajal on:
    
1. värv (värvinimi):
    Kui soovite näha mingi värvi kruntide nimesi, hindu, rente jms. Värvinimed, rentidelt kasvavas järjekorras on järgnevad:
        pruunid, helesinised, roosad, oranzid, punased, kollased, rohelised, tumesinised
        
2. krunt (krundinimi):
    Kui soovite näha mingi krundi hinda, renti, hotelli maksuvust jms. Et teada saada mingi krundi nime,
    kasutage käsku "värvid (värvinimi)"
    
3. isik (mängija nimi):
    Kui soovite teada, kui palju raha on mingil mängijal ning mis kaardid neil on.
""")


        



    
    