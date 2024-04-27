import csv
import os
def veri_okuma():
    veri = []

    with open('imdb_top_1000.csv', newline='', encoding='utf-8') as csvfile:
        okuyucu = csv.reader(csvfile, delimiter=',')
        for satir in okuyucu:
            film = {
                'url': satir[0],
                'name': satir[1],
                'release_date': satir[2],
                'Certificate': satir[3],
                'Runtime': satir[4],
                'Genre': satir[5],
                'IMDB_Rating': satir[6],
                'Overview': satir[7],
                'Meta_score': satir[8],
                'Director': satir[9],
                'Star1': satir[10],
                'Star2': satir[11],
                'Star3': satir[12],
                'Star4': satir[13],
                'No_of_Votes': satir[14],
                'Gross': satir[15]
            }
            veri.append(film)

    return veri
