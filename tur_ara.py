def tur_arama(veri):
    arama = input("aranacak filmi giriniz: ")
    for film in veri:
        if arama in film['Genre'].lower():
            print(film)
