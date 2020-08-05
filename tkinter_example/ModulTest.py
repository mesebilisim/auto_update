# Modul Test
# 11.11.2019
# Sahin MERSIN
import sys
import time
import tkinter as tk
from threading import Thread
from tkinter.filedialog import askopenfilename, asksaveasfilename

import requests

version_info = (
    1,
    5
)


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
    global th_exit
    import update
    if update.yeni_dosya():
        print("update bittiiiiiiiiiiiiiii")
        th_exit = True

        # from subprocess import call
        # call(["python", "ModulTest.py"])

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
        if th_exit:
            print("thread_function cik")
            break
        executionTime = (time.time() - startTime)
        if executionTime > 10:
            startTime = time.time()
            print("guncelleme kontrol basliyor")
            if versiyon_kontrol():
                print("guncelle")
                time.sleep(2)
                guncelle()
                time.sleep(2)
                print("guncelleme bitti")
                break
            else:
                print("devam et")
        time.sleep(1)

    print("while cikildi")
    time.sleep(1)
    sys.exit()


def test():
    th = Thread(target=thread_function, daemon=True)
    th.start()


def test2():
    if versiyon_kontrol():
        print("guncelle")
        time.sleep(2)
        guncelle()
        time.sleep(2)
        print("guncelleme bitti")
        sys.exit()


window = tk.Tk()
window.title("Simple Text Editor " + str(version_info))
window.rowconfigure(0, minsize=300, weight=1)
window.columnconfigure(1, minsize=300, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...")
btn_test = tk.Button(fr_buttons, text="Test", command=test)
btn_test2 = tk.Button(fr_buttons, text="Test 2", command=test2)
btn_cik = tk.Button(fr_buttons, text="Cik", command=cik)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_test.grid(row=2, column=0, sticky="ew", padx=5)
btn_test2.grid(row=3, column=0, sticky="ew", padx=5)
btn_cik.grid(row=4, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

startTime = time.time()

th_exit = False

window.mainloop()

