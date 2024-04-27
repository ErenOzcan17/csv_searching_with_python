def basrol_arama(veri):
    arama = input("aranacak filmi giriniz: ")
    for film in veri:
        if arama in film['Star1'].lower():
            print(film)
