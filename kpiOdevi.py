print('''Menu:
1.Karlilik
2.Ekipman Etkililik Orani (OEE)
3.Adambasi Ciro''')

secim=int(input("Menuden hesaplamak istediginiz islem numarasini giriniz: "))

if secim==1:

    #Soru 1:Karlilik

    def gelir():
        finGelir=int(input("Finansman gelirinizi giriniz: "))
        pazGelir=int(input("Pazar gelirinizi giriniz: "))
        kiraGelir=int(input("Kira gelirinizi giriniz: "))
        topGelir=finGelir+pazGelir+kiraGelir
        print("Toplam geliriniz:",topGelir,"TL")
        return topGelir

    def gider():
        ucret=int(input("Ücret giderinizi giriniz: "))
        finGider=int(input("Finansman giderlerini giriniz: "))
        pazGider=int(input("Pazar giderlerinizi giriniz: "))
        kiraGider=int(input("Kira giderlerinizi giriniz: "))
        muhaGider=int(input("Muhasebe giderlerinizi giriniz: "))
        topGider=ucret+finGider+pazGider+kiraGider+muhaGider
        print("Toplam gideriniz:",topGider,"TL")
        return topGider

    def karlilik():
        kar=gelir()-gider()
        if kar>1000:
            print("İşletmeniz karlıdır.")
        elif kar<1000:
            print("İşletmeniz malesef karlı değildir.")
        else:
            print("İşletmeniz başabaş noktasındadır.")

    karlilik()

elif secim==2:

    #Soru 2:Ekipman Etkililik Orani(OEE)

    def kullan():
        planUreSure=int(input("Planlanmış üretim süresini giriniz: "))
        plansizDurus=int(input("Plansız duruşu giriniz: "))
        kBilirlik=(planUreSure-plansizDurus)/planUreSure
        print("Kullanılabilirlik oranınız:",kBilirlik)
        return kBilirlik

    def perf():
        stanCevZamani=int(input("Standart çevrim zamanını giriniz: "))
        ureMiktari=int(input("Üretim miktarını giriniz: "))
        planUreSure=int(input("Planlanmış üretim süresiniz giriniz: "))
        plansizDurus=int(input("Plansız duruşu giriniz: "))
        performans=(stanCevZamani*ureMiktari)/(planUreSure-plansizDurus)
        print("Performans oranınız:",performans)
        return performans

    def kalite():
        sagUrun=int(input("Sağlam ürün miktarını giriniz: "))
        topUreMik=int(input("Toplam üretim miktarını giriniz: "))
        kaliteOrani=sagUrun/topUreMik
        print("Kalite oranınız:",kaliteOrani)
        return kaliteOrani

    def oee():
        ekipEtki=kullan()*perf()*kalite()*1
        print("Ekipman etkililik oranınız: ",ekipEtki)

    oee()

elif secim==3:

    #Soru 3:Adambasi Ciro

    def ciro():
        satMiktari=int(input("Satış miktarını giriniz: "))
        birimFiyat=int(input("Birim satış fiyatını giriniz: "))
        cirom=satMiktari*birimFiyat
        print("Cironuz:",cirom)
        return cirom

    def adamCiro():
        topCalisan=25
        aBasiCiro=ciro()/topCalisan
        print("Adambaşı cironuz:",aBasiCiro)

    adamCiro()

else:
    print("Hatalı seçim yaptınız. Lütfen sadece 1, 2 veya 3 seçeneklerinden birini seçiniz.")
