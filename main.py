from dictionary import veri_okuma
veri = veri_okuma()

def genel_fonskiyon(value):
    arama = input("aranacak parametreyi giriniz: ")
    if value == 1:
        for film in veri:
            if arama in film[value].lower():
                print(film)

while True:
    print(
        """--------------------------------------------------------------------------------------------------
          |******** MENÜ **********|
          -------------------------
          |    1...FİLM ARA        |"
          |    2...YONETMEN ARA    |
          |    3...IMDB ARA        |
          |    4...TÜRLER          |
          |    5...BAŞROL ARA      |
          |    6...ÇIKIŞ           |""")

    x = int(input("lütfen seçim yapınız: "))
    if x == 1:
        genel_fonskiyon(value='name')
    if x == 2:
        genel_fonskiyon(value='Director')
    if x == 3:
        genel_fonskiyon(value='IMDB_Rating')
    if x == 4:
        genel_fonskiyon(value='Genre')
    if x == 5:
        genel_fonskiyon(value='Star1')
    if x == 6:
        break
