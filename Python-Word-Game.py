
# Ad         : Okan
# Soyad      : YORUK
# Ogrenci No : 22100011067

#ODEV-2 | KELIME TAHMIN OYUNU

import random                                   # Rastgele Sayilar Uretmek Icin Kullaniliyor.

print("Kelime Tahmin Oyununa Hosgeldiniz...")

# Liste Bilgisi Veriliyor.
Kelime_listesi=["system", "data", "algorithm", "such", "base", "node", "model", "case", "program",
                "information", "set", "code", "function", "process", "application", "software", "class",
                "point", "type", "network", "tree", "object", "element", "input", "operation", "level",
                "memory", "table", "order", "file", "variable", "language", "write", "list", "structure",
                "compute", "sequence", "computer", "bit", "probability", "machine", "array", "page", "error",
                "step", "search", "most", "path", "graph", "web", "length", "several", "security", "proof",
                "access", "obtain", "matrix", "task", "image", "form", "return", "interface", "resource",
                "address", "implementation", "loop", "first", "read", "location", "hardware", "behavior",
                "programming", "field", "key", "parameter", "distribution", "definition", "instance",
                "interaction", "internet", "representation", "edge", "stack", "return", "procedure", "link",
                "output", "block", "domain", "store", "call", "device", "server", "static", "dataset",
                "detection", "write", "execute", "least", "key"]

onceki_kelimeler=[]

# ANA UYGULAMA KISMI
while True:

    kelime_no = random.randint(0, len(Kelime_listesi) - 1)   # Listeden Rastgele Kelime Aliniyor .
    kelime=Kelime_listesi[kelime_no]

    # Kelimenin Daha Once Sorulup Sorulmadigi Kontrol Ediliyor.
    if kelime in onceki_kelimeler:
        continue

    ipucu = len(kelime) // 3
    puan = 0

    tahmin_hak = len(kelime) ** (1 / 2)                           # Tahmin Hakki Hesaplaniyor.
    tahmin_hak = int(tahmin_hak)

    if tahmin_hak ** 2 == len(kelime):                            # Tahmin Hakki Kontrol Ediliyor.
        tahmin_hak += 0
        kontrol_hak=tahmin_hak
    else:
        tahmin_hak += 1
        kontrol_hak=tahmin_hak

    print("------------------------")
    print("Kelimedeki Harf Sayisi: ",len(kelime))

    dogru_harf = ""
    yanlis_harf = ""
    ipucu_harf = ""
    sesli_harf = "aeıioöuü"

    while tahmin_hak>0:

        print("------------------------")
        print("Tahmin Hakki :",tahmin_hak)
        print("Puan :",puan)                                            # Uygulama Icin Bilgiler Yazdiriliyor.
        print("Tahmin Edilen Harfler :",dogru_harf,yanlis_harf)
        print("------------------------")

        # Ipucu Verilecek Harfler Aliniyor.
        while ipucu>0:
            random_harf=kelime[random.randint(0,len(kelime)-1)]
            if random_harf not in ipucu_harf:
                ipucu_harf+=random_harf
                ipucu-=1

        kelime_durumu=""
        for i in kelime:
            # Gerekli Yerlere Harfler Yerlestiriliyor.
            if i in ipucu_harf or i in dogru_harf:
                kelime_durumu+=i+" "
            # Harf Olmayan Yerlere "_" Yerlestiriliyor.
            else:
                kelime_durumu+="_ "

        # Kelimenin Son Durumu Yazdiriliyor.
        print("Kelime Durumu :",kelime_durumu)
        print("------------------------")


        # Harf Tahmin Kismi
        while True:
            tahmin_harf=input("Bir Harf Tahmin Ediniz :")
            tahmin_harf=tahmin_harf.lower()

            # Yazilan Harf Ipucu Olarak Verildiyse Tekrar Isteniyor.
            if tahmin_harf in ipucu_harf:
                    print("Bu Harf Ipucu Olarak Verilmistir!.\n")
                    continue
            else:
                break

        # Yazilan Harften Birden Fazla Varsa Sayim Yapiliyor.
        sayac=0
        for i in kelime:
            if i==tahmin_harf:
                sayac+=1

        # Yazilan Harfin Daha Once Girip Girilmedigi Kontrol Ediliyor.
        if tahmin_harf in dogru_harf or tahmin_harf in yanlis_harf:
            print("------------------------")
            print("Lutfen Daha Onceden Girilmemis Bir Harf Giriniz!.")
            continue

        # Dogru Tahmin Edilen Harfler Icin Gerekli Puanlama Yapiliyor.
        if tahmin_harf in kelime:
            dogru_harf+=tahmin_harf+", "
            if tahmin_harf not in sesli_harf:
                puan+=3*sayac
            else:
                puan+=4*sayac

            # Kelime Dogrulugu Kontrol Ediliyor.
            kontrol=1
            for i in kelime:
                if i not in dogru_harf and i not in ipucu_harf:
                    kontrol=0
                    break

            # Kelime Bilindigi Icin Gerekli Bilgilendirme Yapiliyor.
            if kontrol==1:
                if tahmin_hak==kontrol_hak:
                    puan+=5
                print("------------------------")
                print("Oyundaki Kelime :",kelime)
                print("Tebrik Ederiz :)")
                print("Kelimeyi Dogru Tahmin Ettiniz.")
                print("Aldiginiz Puan:",puan)
                print("------------------------")
                break

        # Yanlis Tahmin Edilen Harfler Icin Gerekli Hesaplama Yapiliyor.
        else:
            yanlis_harf+=tahmin_harf+", "
            tahmin_hak-=1
            puan-=5
        # Kelime Bilinemedigi Icin Gerekli Bilgilendirme Yapiliyor.
        if tahmin_hak==0:
            print("------------------------")
            print("Kaybettiniz :(")
            print("Tahmin Hakkiniz Kalmadi.")
            print("Aldiginiz Puan :",puan)
            print("------------------------")
            print("Oyundaki Kelime :",kelime)
            print("------------------------")
            break

    onceki_kelimeler+=[kelime]                   # Onceki Kelimenin Tekrar Sorulmamasi Icin Bu Listeye Ekleniyor.

# Tekrar Baslatma ve Cikis Secenekleri
    print(" | Yeni Kelime (1) |")
    print(" |     CIKIS (2)   |")
    secim=input("Yapmak Istediginiz Islem Icin Yanindaki Tusa Basiniz :")
    secim=int(secim)

    if secim==1:
        print("Yeni Kelimeye Geciliyor!.")
        continue
    elif secim==2:
        print("Uygulamadan Cikis Yapiliyor!.")
        break
    else:
        print("Yanlis Secim Yaptiniz!.")
        print("Uygulamadan Cikis Yapildi!.")
        break

