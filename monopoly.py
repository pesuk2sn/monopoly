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
    if täring_1==täring_2:
        print("Vabanesid vanglast!")
        sammud=täring_1+täring_2
        mängija_asetus=mängulaud[sammud+mängija_asetus]
    else:
        i+=1
        
    

def liikumine(mängija_asetus, käik): #kommenteerin, et mõista, mis täpsemalt toimub
    i=0
    sammud=0
    kinni = False
    
    while True:
        
        print("Veeretan täringuid") #täringumehhanism
        täring_1=random.randint(1,6)
        täring_2=random.randint(1,6)
        
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

while käik <20:
    if käik %2==0:
        mängija2_asetus=liikumine(mängija2_asetus)
        print("Mängija 2 on ruudul " +str(mängija2_asetus))
    else:
        mängija1_asetus=liikumine(mängija1_asetus)
        print("Mängija 1 on ruudul "+str(mängija1_asetus))
    käik+=1"""
    


    
