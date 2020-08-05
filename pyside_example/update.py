# sunucudan versiyon bilgisi ceksin
# yeni ve eski dosyayi degistirir
# bir liste alsin, neler degisti ise icinde yazsin, ona gore yeni dosyalari indirsin, eski dosya isimlerini degistirsin ve indirdiklerini yeni dosya olarak kaydetsin

import os
import time

import requests


def dosya_indir():
    print("dosya_indir start")
    versiyon = "https://www.mesebilisim.com/media/v/pyside_example/ModulTest.py"
    r = requests.get(versiyon, allow_redirects=True)
    open('ModulTest.py', 'wb').write(r.content)

    # from subprocess import call
    # call(["python", "ModulTest.py"])

    print("dosya_indir end")
    return True

def eski_bak_sil():
    print("eski_bak_sil")
    if os.path.exists('bak_ModulTest.py'):
        os.remove("bak_ModulTest.py")
        return True
    return False

def eski_dosya_isim_degistir():
    print("eski_dosya_isim_degistir start")
    eski_bak_sil()
    os.rename("ModulTest.py", "bak_ModulTest.py")
    dosya_indir()
    print("eski_dosya_isim_degistir end")
    return True

def yeni_dosya():
    time.sleep(5)
    print("yeni_dosya start")
    eski_dosya_isim_degistir()
    print("yeni_dosya end")
    return True



