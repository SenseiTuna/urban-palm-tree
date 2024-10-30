sonmetin="\nİşleminizin sonucu: {}"
while True:
    islem=input("\nHangi işlemi yapmak istiyorusunuz \n(Toplama/Çıkarma/Çarpma/Bölme/Üs/Mod/Çıkış)\n").lower()
    if islem=="cikis" or islem=="çıkış" or islem=="quit":
        print("Çıkış yaptınız.")
        break
    else:
        sayi1=float(input("İlk sayıyı giriniz: "))
        sayi2=float(input("ikinci sayıyı giriniz: "))
        if islem=="toplama": 
            sonuc=sayi1+sayi2
            gerceksonuc=sonuc
        
            if gerceksonuc!=int(sonuc):
                print(sonmetin.format(gerceksonuc))
            else:
                print(sonmetin.format(int(sonuc)))
        elif islem=="cikarma" or islem=="çıkarma" or islem=="cıkarma" or islem=="çikarma":
            sonuc=sayi1-sayi2
            gerceksonuc=sonuc
        
            if gerceksonuc!=int(sonuc):
                print(sonmetin.format(gerceksonuc))
            else:
                print(sonmetin.format(int(sonuc)))
        elif islem=="carpma" or islem=="çarpma":
            sonuc=sayi1*sayi2
            gerceksonuc=sonuc
        
            if gerceksonuc!=int(sonuc):
                print(sonmetin.format(gerceksonuc))
            else:
                print(sonmetin.format(int(sonuc)))
        elif islem=="bolme" or islem=="bölme":
            if sayi2!=0:
                sonuc=sayi1/sayi2
                gerceksonuc=sonuc
        
                if gerceksonuc!=int(sonuc):
                    print(sonmetin.format(gerceksonuc))
                else:
                    print(sonmetin.format(int(sonuc)))
            else:
                print("Böleniniz(ikinci sayı) 0 olamaz!")
        elif islem=="us" or islem=="üs" or islem=="üsalma" or islem=="usalma":
            sonuc=sayi1**sayi2
            gerceksonuc=sonuc

            if gerceksonuc!=int(sonuc):
                print(sonmetin.format(gerceksonuc))
            else:
                print(sonmetin.format(int(sonuc)))
        elif islem=="mod" or islem=="modalma":
            sonuc=sayi1%sayi2
            gerceksonuc=sonuc

            if gerceksonuc!=int(sonuc):
                print(sonmetin.format(gerceksonuc))
            else:
                print(sonmetin.format(int(sonuc)))
        else:
            print("Lütfen geçerli bir işlem giriniz.")