# Modul Test
# 05.08.2020
# Sahin MERSIN
# Mese Bilisim
# https://www.mesebilisim.com
import os
import sys
import time
import tkinter as tk
from threading import Thread
from tkinter.filedialog import askopenfilename, asksaveasfilename

import psutil as psutil
import requests

version_info = (
    1,
    6
)


def restart_program():
    """Restarts the current program, with file objects and descriptors
       cleanup
    """

    try:
        p = psutil.Process(os.getpid())
        for handler in p.get_open_files() + p.connections():
            os.close(handler.fd)
    except:
        pass

    python = sys.executable
    os.execl(python, python, *sys.argv)


def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")


def versiyon_kontrol():
    """ Versiyon Kontrol """
    # Sunucudan versiyon.txt dosyasini oku
    versiyon = "https://www.mesebilisim.com/media/v/tkinter_example/versiyon.txt"
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

    if version_info[0] < v[0]:
        print("guncelle 1")
        return True
    elif version_info[0] == v[0]:
        if version_info[1] < v[1]:
            print("guncelle 2")
            return True

    return False


def cik():
    print("cikkkkkkkkkk")
    sys.exit()
    # th.join()
    # sys.exit(app.exec_())

    # return True


def guncelle():
    import update
    if update.yeni_dosya():
        print("update bittiiiiiiiiiiiiiii")

        restart_program()

        sys.exit()
        # cik()
        # sys.exit(app.exec_())
    else:
        print("ne olduuuuuuuuu")

    return True


def thread_function():
    global startTime
    global th_exit
    while True:
        executionTime = (time.time() - startTime)
        if executionTime > 10:
            startTime = time.time()
            print("guncelleme kontrol basliyor")
            if versiyon_kontrol():
                print("guncelle")
                time.sleep(1)
                guncelle()
                time.sleep(1)
                print("guncelleme bitti")
            else:
                print("devam et")
        time.sleep(1)

window = tk.Tk()
window.title("Simple Text Editor " + str(version_info))
window.rowconfigure(0, minsize=300, weight=1)
window.columnconfigure(1, minsize=300, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...")
btn_cik = tk.Button(fr_buttons, text="Cik", command=cik)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_cik.grid(row=4, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

startTime = time.time()

th = Thread(target=thread_function, daemon=True)
th.start()

window.mainloop()

