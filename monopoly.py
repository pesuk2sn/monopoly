import random

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
        
    

def liikumine(mängija_asetus):
    käik=1
    i=0
    sammud=0
    while True:
        print("Veeretan täringuid")
        täring_1=random.randint(1,6)
        täring_2=random.randint(1,6)
        print(täring_1,täring_2)
        if täring_1==täring_2:
            i+=1
            if i==3:
                print("Lähed vangi!")
                i=0
                käik+=1
                kinni=True
                break
            else:
                sammud=täring_1+täring_2
                mängija_asetus=mängulaud[sammud+mängija_asetus]
                if mängija_asetus>41:
                    mängija_asetus-40
                return mängija_asetus
        sammud=täring_1+täring_2
        mängija_asetus=mängulaud[sammud+mängija_asetus]
        if mängija_asetus>41:
            mängija_asetus-40
        käik+=1
        return mängija_asetus


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
    käik+=1
    


    
