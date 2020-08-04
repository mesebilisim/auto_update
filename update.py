# sunucudan versiyon bilgisi ceksin
# yeni ve eski dosyayi degistirir
# bir liste alsin, neler degisti ise icinde yazsin, ona gore yeni dosyalari indirsin, eski dosya isimlerini degistirsin ve indirdiklerini yeni dosya olarak kaydetsin

import os
import requests


def dosya_indir():
    versiyon = "https://www.mesebilisim.com/media/v/auto_update.py"
    r = requests.get(versiyon, allow_redirects=True)
    open('auto_update.py', 'wb').write(r.content)
    exec('auto_update.py')

def eski_dosya_isim_degistir():
    os.rename("auto_update.py", "bak_auto_update.py")
    dosya_indir()

def yeni_dosya():
    print("yeni_dosya")
    eski_dosya_isim_degistir()



