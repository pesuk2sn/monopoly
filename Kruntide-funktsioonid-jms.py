

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
        kruntide_maatriks = "See pole tänavanimi"
        
                
                    
                    
                    
    return(kruntide_maatriks)#Okei, see pole sõna otseses mõttes maatriks, kuid ma ei viitsi seda siin selleks muuta, kui seda pole kindlusega nii vaja.
                
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    #Uus funktsioon
                    
                    
                    
                    
def näita_kaarti(krunt):#See väljastab mingi krundi kõik muutujad selles järjekorras:
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



def käsud():
    print("""Käsud, mida te saate kasutada oma käigu ajal on:

1. värvid (värvinimi):
    Kui soovite näha mingi värvi kruntide nimesi, hindu, rente jms. Värvinimed, rentidelt kasvavas järjekorras on järgnevad:
        pruunid, helesinised, roosad, oranzid, punased, kollased, rohelised, tumesinised
2. krunt (krundinimi):
    Kui soovite näha mingi krundi hinda, renti, hotelli maksuvust jms. Et teada saada mingi krundi nime,
    kasutage käsku "värvid (värvinimi)"
""")


        

    





    
    