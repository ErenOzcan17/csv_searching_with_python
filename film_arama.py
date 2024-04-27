def film_arama(veri):
    arama = input("aranacak filmi giriniz: ")
    for film in veri:
        if arama in film['name'].lower():
            print(film)
