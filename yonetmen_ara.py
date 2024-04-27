def yonetmen_arama(veri):
    arama = input("aranacak yonetmeni giriniz: ")
    for film in veri:
        if arama in film['Director'].lower():
            print(film)
