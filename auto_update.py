""" calisan script
electrocoder
http://mesebilisim.com
"""

import requests
import sys


version_info = (
    1,
    4
)


def versiyon_kontrol():
    """ Versiyon Kontrol """
    # Sunucudan versiyon.txt dosyasini oku
    print("versiyon_kontrol start")
    versiyon = "https://www.mesebilisim.com/media/v/versiyon.txt"
    r = requests.get(versiyon, allow_redirects=True)
    open('versiyon.txt', 'wb').write(r.content)

    f = open('versiyon.txt')
    o = f.readline()
    o = o.split('.')

    v = []
    v.append(int(o[0]))
    v.append(int(o[1]))

    # resim = "https://www.mesebilisim.com/media/v/aaa.jpg"
    # r = requests.get(resim, allow_redirects=True)
    # print(r)
    # kaydet
    # open('D:\\Users\\elect\\Documents\\projects\\python\\auto_update\\aaa.jpg', 'wb').write(r.content)
    # print("ok")

    print("versiyon_kontrol end")

    if version_info[0] < v[0]:
        print("guncelle 1")
        return True
    elif version_info[0] == v[0]:
        if version_info[1] < v[1]:
            print("guncelle 2")
            return True
    else:
        return False


def guncelle():
    import update
    update.yeni_dosya()
    return True


if __name__ == "__main__":
    if versiyon_kontrol():
        print("guncelle")
        guncelle()
        print("guncelleme bitti")
        sys.exit()
    else:
        print("devam et")

    print("ex")