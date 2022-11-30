import copy
from random import randint

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
    #Seda saaks sõnastikuga palju lihtsamalt, kuid ma tol hetkel veel polnud seda õppinud ning tekstifailist lugemine ei tee seda oluliselt aegalsemaks.
    
    
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

def lisa_krunt(krunt, mängija): #Lisab mängijale krundi/kaardi jms
    mängija.append(krunt)
    return(mängija)
    
def pandi_krunt(krunt, mängija): #pandib mängija krundi. Selleks võtab tekstifailist pandi hinna, annab selle mängijale ning võtab talt krundi
    i = mängija.index(krunt) #võtab krundi indeksi
    if näita_krunti(krunt) != "Selle nimelist krunti pole":
        pant = (näita_krunti(krunt))[5]
        mängija[0] += int(pant) #lisab mängijale pandi hinna
        del mängija[i] #eemaldab krundi mängijalt
        return(mängija)
    else:
        return "Selle nimelist krunti pole"
            

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
    
    värvid = [["Jaama tänav","Soinaste tänav","pruun"], #krundid värvide järgi jaotatud. Neil on lisaks sees ka sõnena värvinimi, et proge ridu säästa.
["Ravila tänav","Ringtee tänav","Ilmatsalu tänav","helesinine"],
["Vabaduse pst","Sõbra tänav","Kesk kaar","roosa"],
["Kalevi tänav","F.R Kreutzvaldi tänav","Vaksali tänav","oranz"],
["Pikk tänav","Aardla tänav","Puussepa tänav","punane"],
["Puiestee tänav","Kalda tee","Võru tänav","kollane"],
["Turu tänav","Narva maantee","Riia tänav","roheline"], 
["Rüütli tänav","Raekoja plats","tumesinine"]]
    
    if type(järjend) == str: #kui krundi nimi sisestati valesti
        return("See pole krundi nimi")
    
    else:
        print("Selle krundi info on järgnev: \n")
        print("Krundinimi:", järjend[0])
        for rida in värvid:
            if järjend[0] in rida:
                print("Krundi värv:", rida[-1])
        print("Krundi hind:", järjend[1])
        print("Krundi rent:", järjend[2])
        print("Krundi rent, kui omanik omab kogu värvi:", järjend[3])
        print("Krundi rent hotelliga:", järjend[4])
        print("Krundi pant:", järjend[5])
        print("Hotelli hind:", järjend[6])
        
    return("") #et "none" lõpus vältida
    

    


def kas_värvid_on_koos(mängija): #selle funktsiooni eesmärk on näidata, kas mingil mängijal on kõik ühe värvi krundid.
    #Funktsiooni lõpuks on käes järjend, kus on mängijal koos olevad värvid, kui neid on.
    
    pruunid = ("Jaama tänav","Soinaste tänav") #krundid värvide järgi jaotatud
    helesinised = ("Ravila tänav","Ringtee tänav","Ilmatsalu tänav")
    roosad = ("Vabaduse pst","Sõbra tänav","Kesk kaar")
    oranzid = ("Kalevi tänav","F.R Kreutzvaldi tänav","Vaksali tänav")
    punased = ("Pikk tänav","Aardla tänav","Puussepa tänav")
    kollased = ("Puiestee tänav","Kalda tee","Võru tänav")
    rohelised = ("Turu tänav","Narva maantee","Riia tänav")
    tumesinised = ("Rüütli tänav","Raekoja plats")
    
    järjend1 = (helesinised, roosad, oranzid, punased, kollased, rohelised)#ennik kolmeliikmelistest ennikutest
    
    
    järjend2 = [0, 0, 0, 0, 0, 0]#0 märgib kolmeliikmelise värvi(helesin kuni roheline) kooslust mängija omanduses. Kui järjendis pole igat seda värvi krunti, siis jääb sinna kohta null.
    vastuse_järjend = []#See, mis lõpus
    pruun = 0
    tumesin = 0
    
    if pruunid[0] in mängija:
        if pruunid[1] in mängija:
            pruun = 1
        
    if tumesinised[0] in mängija:
        if tumesinised[1] in mängija:
            tumesin = 1
        
    for el in range(6): #kuus värvi on, kus on kolm krunti värvi kohta
        
        if järjend1[el][0] in mängija: #Ükshaaval, kas mängijal on kõik selle värvi krundid
            
            if järjend1[el][1] in mängija:
                
                if järjend1[el][2] in mängija:
                    järjend2[el] = 1
            
    

    if pruun == 1: #vaatab värvid ükshaaval üle, kui on koos, siis lisab järjendisse värvi nime
        vastuse_järjend.append("pruunid")
    if järjend2[0] == 1:
        vastuse_järjend.append("helesinised")
    if järjend2[1] == 1:
        vastuse_järjend.append("roosad")
    if järjend2[2] == 1:
        vastuse_järjend.append("oranzid")
    if järjend2[3] == 1:
        vastuse_järjend.append("punased")
    if järjend2[4] == 1:
        vastuse_järjend.append("kollased")
    if järjend2[5] == 1:
        vastuse_järjend.append("rohelised")
    if tumesin == 1:
        vastuse_järjend.append("tumesinised")
            
    if len(vastuse_järjend) == 0:
        return("Sel mängijal pole ühtki värvi koos.")
    
    return(vastuse_järjend)
    
def väljasta_tänavad(mängija): #Võtab mängija_vara järjendi ja väljastab järjendi ainult kruntidega.
    
    pruunid = ("Jaama tänav","Soinaste tänav") #krundid värvide järgi jaotatud
    helesinised = ("Ravila tänav","Ringtee tänav","Ilmatsalu tänav")
    roosad = ("Vabaduse pst","Sõbra tänav","Kesk kaar")
    oranzid = ("Kalevi tänav","F.R Kreutzvaldi tänav","Vaksali tänav")
    punased = ("Pikk tänav","Aardla tänav","Puussepa tänav")
    kollased = ("Puiestee tänav","Kalda tee","Võru tänav")
    rohelised = ("Turu tänav","Narva maantee","Riia tänav")
    tumesinised = ("Rüütli tänav","Raekoja plats")
    vaste = [] #tühi järjend
    
    for el in mängija: #käib ükshaaval kõik värvid läbi, et kaardid sorteeritaks värvide kaupa.
        if el in pruunid: #seda saaks lühemaks, kasutades maatrikseid, kuid siis peab hakkama kahekrundiseid värve eraldi kohtlema ja lõpuks on see segasem
            print(el)
            vaste.append(el)   
            
    for el in mängija:
        if el in helesinised:
            vaste.append(el)
            
    for el in mängija:
        if el in roosad:
            vaste.append(el)
            
    for el in mängija:
        if el in oranzid:
            vaste.append(el)            
    for el in mängija:
        if el in punased:
            vaste.append(el)
            
    for el in mängija:
        if el in kollased:
            vaste.append(el)
            
    for el in mängija:
        if el in rohelised:
            vaste.append(el)
            
    for el in mängija:
        if el in tumesinised:
            vaste.append(el)
    return(vaste)
                
                
    
def print_mängija(mängija_list, hotellid): #see funktsioon väljastab mängijale info mingi mängija raha ja kaartide kohta. Märgib ka kruntide värvid ning hotellid, kui on
    mängija = copy.deepcopy(mängija_list) #selleks, et siin elemente muutes päris järjend alles jääks
    print("Teil on " + str(mängija[0]) + " eurot")
    del mängija[0]
    
    pruunid = ("Jaama tänav","Soinaste tänav") #krundid värvide järgi jaotatud
    helesinised = ("Ravila tänav","Ringtee tänav","Ilmatsalu tänav")
    roosad = ("Vabaduse pst","Sõbra tänav","Kesk kaar")
    oranzid = ("Kalevi tänav","F.R Kreutzvaldi tänav","Vaksali tänav")
    punased = ("Pikk tänav","Aardla tänav","Puussepa tänav")
    kollased = ("Puiestee tänav","Kalda tee","Võru tänav")
    rohelised = ("Turu tänav","Narva maantee","Riia tänav")
    tumesinised = ("Rüütli tänav","Raekoja plats")
    
    if len(mängija) > 0:

        print("\nTeie kaardid on järgnevad: ")
        for el in mängija_list: #käib ükshaaval kõik värvid läbi, et kaardid sorteeritaks värvide kaupa.
            if el in pruunid and el not in hotellid: #seda saaks lühemaks, kasutades maatrikseid, kuid siis peab hakkama kahekrundiseid värve eraldi kohtlema ja lõpuks on see segasem.
                print(el, "(pruun)")
                del mängija[mängija.index(el)]
            elif el in pruunid and el in hotellid: #Kui mängijal on hotell, märgib selle ära
                print(el, "(pruun, hotelliga)")
                del mängija[mängija.index(el)]
                
        for el in mängija_list:
            if el in helesinised and el not in hotellid:
                print(el, "(helesinine)")
                del mängija[mängija.index(el)] 
            elif el in helesinised and el in hotellid: #Kui mängijal on hotell, märgib selle ära
                print(el, "(helesinine, hotelliga)")
                del mängija[mängija.index(el)]
                
        for el in mängija_list:
            if el in roosad and el not in hotellid:
                print(el, "(roosa)")
                del mängija[mängija.index(el)] 
            elif el in roosad and el in hotellid: #Kui mängijal on hotell, märgib selle ära
                print(el, "(roosa, hotelliga)")
                del mängija[mängija.index(el)]
                
        for el in mängija_list:
            if el in oranzid and el not in hotellid:
                print(el, "(oranz)")
                del mängija[mängija.index(el)] 
            elif el in oranzid and el in hotellid: #Kui mängijal on hotell, märgib selle ära
                print(el, "(oranz, hotelliga)")
                del mängija[mängija.index(el)]
                
        for el in mängija_list:
            if el in punased and el not in hotellid:
                print(el, "(punane)")
                del mängija[mängija.index(el)] 
            elif el in punased and el in hotellid: #Kui mängijal on hotell, märgib selle ära
                print(el, "(punane, hotelliga)")
                del mängija[mängija.index(el)]
                
                
        for el in mängija_list:
            if el in kollased and el not in hotellid:
                print(el, "(kollane)")
                del mängija[mängija.index(el)] 
            elif el in kollased and el in hotellid: #Kui mängijal on hotell, märgib selle ära
                print(el, "(kollane, hotelliga)")
                del mängija[mängija.index(el)]
                
        for el in mängija_list:
            if el in rohelised and el not in hotellid:
                print(el, "(roheline)")
                del mängija[mängija.index(el)] 
            elif el in rohelised and el in hotellid: #Kui mängijal on hotell, märgib selle ära
                print(el, "(roheline, hotelliga)")
                del mängija[mängija.index(el)]
                
                
        for el in mängija_list:
            if el in tumesinised and el not in hotellid:
                print(el, "(tumesinine)")
                del mängija[mängija.index(el)] 
            if el in tumesinised and el in hotellid: #Kui mängijal on hotell, märgib selle ära
                print(el, "(tumesinine, hotelliga)")
                del mängija[mängija.index(el)]
        
        if "vangla_vabastus" in mängija:
            indeks = mängija.index("vangla_vabastus") #eemaldab vanglast vabastuse kaardi
            del mängija[indeks]
            for i in range(len(mängija)): #väljastab kõik muud kaardid(raudteejaamad jms)
                print(mängija[i])
            
            print("\n" + "Teil on ka vanglast tasuta pääsemise kaart.")
            
        else:
            for i in range(len(mängija)): #väljastab kõik muud kaardid(raudteejaamad jms)
                print(mängija[i])
        
    
    return("")#et "none" lõpus vältida





def rendimääraja(mängija_asetus, vastase_vara, hotellid): #See funktsioon määrab rendi hinna, olgu see krunt, rongijaam, elekter või vesi, output on int

    rent = 0
    kas_on_krunt = False
    värvid = [["Jaama tänav","Soinaste tänav","pruunid"], #krundid värvide järgi jaotatud. Neil on lisaks sees ka sõnena värvinimi, et proge ridu säästa.
["Ravila tänav","Ringtee tänav","Ilmatsalu tänav","helesinised"],
["Vabaduse pst","Sõbra tänav","Kesk kaar","roosad"],
["Kalevi tänav","F.R Kreutzvaldi tänav","Vaksali tänav","oranzid"],
["Pikk tänav","Aardla tänav","Puussepa tänav","punased"],
["Puiestee tänav","Kalda tee","Võru tänav","kollased"],
["Turu tänav","Narva maantee","Riia tänav","rohelised"], 
["Rüütli tänav","Raekoja plats","tumesinised"]]
     
    for rida in värvid: #Kui mängija asub mingil krundil
        if mängija_asetus in rida:
            kas_on_krunt = True
            rent = int((näita_krunti(mängija_asetus))[2])#võtab rendi tekstifailist
            
            for i in kas_värvid_on_koos(vastase_vara):#vaatab, kas vastasel on mingi värv koos
                
                for rida in värvid:
                    if mängija_asetus in rida and i in rida:
                        rent = rent*2 #kui värvid on koos, on rent kahekordne

                
            if mängija_asetus in hotellid: #Kui vastasel on seal kohas hotell, siis on rent kõrgem
                rent = int((näita_krunti(mängija_asetus))[4])
                
    if mängija_asetus == "Veevärk" or mängija_asetus == "Elektrivõrk": #Kui mängija on veevärgis või elektrivõrgus
        täring1 = randint(1, 6)
        täring2 = randint(1, 6)
        print("Veeretan täringuid\n"+ "Veeretasin " + str(täring1) + " ja " + str(täring2))
        
        if "Veevärk" in vastase_vara and "Elektrivõrk" in vastase_vara: #kui vastasel on mõlemad kaardid
            print("Kuna teie konkurendil on nii Veevärk, kui ka Elektrivõrk, on tasu " + str((täring1 + täring2) * 10) + " eurot.")
            rent = (täring1 + täring2) * 10
        
        else: #Kui vastasel on aint 1 kahest kaardist
            print("Tasu on " + str((täring1 + täring2) * 4) + " eurot.")
            rent = (täring1 + täring2) * 4
            
    elif mängija_asetus == "Tulumaks":
        rent = 200
        
    elif mängija_asetus == "Lisamaks":
        rent = 100
    
    elif kas_on_krunt == False: #Kui kaart pole krunt
        if len((mängija_asetus.split(" "))) == 2:
            if (mängija_asetus.split(" "))[1] == "rongijaam": #ehk kui mängija on kohal ... rongijaam
                vastase_vara[0] = str(vastase_vara[0])
                vastase_sõne = " ".join(vastase_vara)
                vastase_vara2 = vastase_sõne.split() #saab järjendi, kus on iga vastase vara elemendi sõna eraldi element
                if vastase_vara2.count("rongijaam") == 1:#Rongijaamade rendid
                    rent = 25
                if vastase_vara2.count("rongijaam") == 2:
                    rent = 50
                if vastase_vara2.count("rongijaam") == 3:
                    rent = 100
                if vastase_vara2.count("rongijaam") >= 4: #>= juhuks, kui kuidagipidi satub sama rongijaam mängijale korduvalt
                    rent = 200
                vastase_vara[0] = int(vastase_vara[0])
    
            
    
    return rent

def endgame(rent, mängija_vara, käsk): #See funktsioon rakendub siis, kui mängija peab maksma rohkem trahvi/renti, kui ta kontol on.
    #See on ainus viis mängu loomulikuks lõpuks.
        
    while rent > mängija_vara[0]: #kui mängijal pole piisavalt raha, et renti maksta 
        print("Pole piisavalt raha.")
        if len(väljasta_tänavad(mängija_vara)) < 1: #kui mängijal pole krunte
            print("Teil on krundid otsas, kaotasite mängu.")
            käsk = "võit" #tsükli lõppu jõudes väljub mängust
            break #väljub tsüklist
        else: #Kui mängijal on krunte
            
            while len(väljasta_tänavad(mängija_vara)) > 0:
                pandiotsus = input('''Teil pole piisavalt raha. Peate oma krunte pangale pantima.
Sisestage kas krundi nimi või "info", et teada saada oma kruntide pantide väärtused.
''')
                
                while pandiotsus not in väljasta_tänavad(mängija_vara) and pandiotsus != "info":
                    vale_valik = pandiotsus
                    pandiotsus = input("Teil puudub krunt nimega " + str(vale_valik) + '. Sisestage kas krundinimi või "info", et saada infot enda kruntide kohta.\n')
                
                
                if pandiotsus in väljasta_tänavad(mängija_vara):
                    mängija_vara = pandi_krunt(pandiotsus, mängija_vara) #pandib krundi, lisab hinna mängijale
                    print("Krunt panditud, teie kontol on nüüd " + str(mängija_vara[0]) + " eurot.")
                    break #läheb välimisse tsüklisse tagasi
                    
                else:
                    print("Teil on kontol " + str(mängija_vara[0]) + " eurot." )
                    print("Allpool on kirjas teie krundid.\n")
                    for u in väljasta_tänavad(mängija_vara):
                        print("Krundi " + u + " pant on " + str((näita_krunti(u))[5]))
    
    return mängija_vara
    
    
def müük(mängija_vara, vastase_vara, käik): #See on käsk, mis rakendub siis, kui üks mängija tahab teisele oma kaarti müüa.
    #See tõstab elemendi ühest järjendist teise ja saadab valitud hulga raha teisest järjendist esimesse. See tagastab mängija vara ja ta konkurendi vara järjendid.

        kaart = input("Mis kaarti te müüa tahate?\n")
        hind = input("Mis hinna eest te selle kaardi müüte?\n")
        try:
            int(hind)
        except ValueError:
            print(str(hind), "pole arv. Tehing ei läinud läbi.")
            return (mängija_vara, vastase_vara)
        
        hind = int(hind)
        
        if hind < 0:
            print("Te mängite monopoli, mitte heategevust. Tehing ei läinud läbi.")
            return (mängija_vara, vastase_vara)
            
        if kaart in mängija_vara:
            try: #kui hind pole int
                if vastase_vara[0] >= hind:
                    print("Teie, mängija "+ str((käik%2) + 1) +" müüte oma kaardi " + kaart + " oma konkurendile " + str(hind) + " euro eest.")
                    vastus = input('Kui olete selles kindlad, kirjutage "jah". Tahtes katkestada kirjutage "ei".\n')
                    
                    while vastus.lower() != "jah" and vastus.lower() != "ei":
                        vastus = input('Kirjutage "jah" või "ei" jutumärkideta.\n')
                    if vastus.lower() == "jah": #teeb vahetuse
                        mängija_vara[0] += hind
                        vastase_vara[0] -= hind
                        vastase_vara.append(kaart)
                        del mängija_vara[mängija_vara.index(kaart)]
                        print("Kaart on müüdud, hind on makstud.")
                        return (mängija_vara, vastase_vara)
                        
                    else:
                        print("Tehing ei läinud läbi.")
                        return (mängija_vara, vastase_vara)
            
                else:
                    print("Ostjal jääb " + str(hind - vastase_vara[0]) + " eurot puudu. Võite ümber kaubelda, kui soovite.")
                    return (mängija_vara, vastase_vara)
                    
            except TypeError:
                print(str(hind), "pole arv. Tehing ei läinud läbi.")
                return (mängija_vara, vastase_vara)
        else:
            print("Müüal puudub kaart " + kaart + '. veenduge, kasutades käsku "info mängija ' + str((käik%2) + 1) + '" et te sisestasite kaardi nime õigesti.')
            return (mängija_vara, vastase_vara)
    
def käsud(): #See tagastab lihtsalt alloleva sõne
    return("""Käsud, mida te saate kasutada oma käigu ajal on:
    
1. värv (värvinimi):
    Kui soovite näha mingi värvi kruntide nimesi, hindu, rente jms. Värvinimed, rentidelt kasvavas järjekorras on järgnevad:
        pruunid, helesinised, roosad, oranzid, punased, kollased, rohelised, tumesinised
        
2. krunt (krundinimi):
    Kui soovite näha mingi krundi hinda, renti, hotelli maksuvust jms. Et teada saada mingi krundi nime,
    kasutage käsku "värvid (värvinimi)"
    
3. info (mängija nimi):
    Kui soovite teada, kui palju raha on mingil mängijal ning mis kaardid neil on.
    
4. lõpp:
    Kui soovite oma käigu üle anda. Võite ka algus kirjutada.
    
5. pandi (krundinimi):
    Kui soovite oma krundi pangale pantida. Saate selle eest pool ostuhinnast.
    Täpsemaks infoks kasutage käsku "krunt (krundinimi)"
    
6. osta:
    Kui soovite osta kaarti, millel maandusite. Eeldades, et see on ostetav.

7. osta hotell:
    Kui tahate osta hotelli krundile, mille peal olete. Teil peab selleks olema kõik selle värvi krundid.

8. müü:
    Kui soovite mingit oma kaarti konkurendile müüa.

9. mängu lõpp:
    Kui soovite mängu enneaegselt lõpetada.
""")



    
    