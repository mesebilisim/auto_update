# Modul Test
# 11.11.2019
# Sahin MERSIN

import configparser
import sys
import time
import socket
import select
from threading import Thread

import requests
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton, QLineEdit, QDialog, QDialogButtonBox, \
    QVBoxLayout
from PySide2.QtCore import QFile, QObject


class CustomDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(CustomDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle("HELLO!")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class Form(QObject):

    def __init__(self, ui_file, parent=None):
        super(Form, self).__init__(parent)
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()

        self.version_info = (
            1,
            4
        )

        self.startTime = time.time()

        self.th_exit = False

        self.th = Thread(target=self.thread_function, daemon=True)
        self.th.start()

        self.window.setWindowTitle("Modül Test")

        self.cfg_file = "ModulTest.ini"

        self.modul_ip = self.window.findChild(QLineEdit, 'lineEdit_22')
        self.goz_1 = self.window.findChild(QLineEdit, 'lineEdit')
        self.goz_2 = self.window.findChild(QLineEdit, 'lineEdit_2')
        self.goz_3 = self.window.findChild(QLineEdit, 'lineEdit_4')
        self.goz_4 = self.window.findChild(QLineEdit, 'lineEdit_3')
        self.goz_5 = self.window.findChild(QLineEdit, 'lineEdit_8')
        self.goz_6 = self.window.findChild(QLineEdit, 'lineEdit_7')
        self.goz_7 = self.window.findChild(QLineEdit, 'lineEdit_5')
        self.goz_8 = self.window.findChild(QLineEdit, 'lineEdit_6')
        self.goz_9 = self.window.findChild(QLineEdit, 'lineEdit_16')
        self.goz_10 = self.window.findChild(QLineEdit, 'lineEdit_14')
        self.goz_11 = self.window.findChild(QLineEdit, 'lineEdit_11')
        self.goz_12 = self.window.findChild(QLineEdit, 'lineEdit_13')
        self.goz_13 = self.window.findChild(QLineEdit, 'lineEdit_15')
        self.goz_14 = self.window.findChild(QLineEdit, 'lineEdit_12')
        self.goz_15 = self.window.findChild(QLineEdit, 'lineEdit_9')

        self.gonder_1 = self.window.findChild(QLineEdit, 'lineEdit_10')
        self.gonder_2 = self.window.findChild(QLineEdit, 'lineEdit_17')
        self.gonder_3 = self.window.findChild(QLineEdit, 'lineEdit_18')
        self.gonder_4 = self.window.findChild(QLineEdit, 'lineEdit_20')
        self.gonder_5 = self.window.findChild(QLineEdit, 'lineEdit_19')
        self.gonder_6 = self.window.findChild(QLineEdit, 'lineEdit_21')

        self.alinan = self.window.findChild(QLineEdit, 'lineEdit_23')

        self.window.setTabOrder(self.modul_ip, self.goz_1)
        self.window.setTabOrder(self.goz_1, self.goz_2)
        self.window.setTabOrder(self.goz_2, self.goz_3)
        self.window.setTabOrder(self.goz_3, self.goz_4)
        self.window.setTabOrder(self.goz_4, self.goz_5)
        self.window.setTabOrder(self.goz_5, self.goz_6)
        self.window.setTabOrder(self.goz_6, self.goz_7)
        self.window.setTabOrder(self.goz_7, self.goz_8)
        self.window.setTabOrder(self.goz_8, self.goz_9)
        self.window.setTabOrder(self.goz_9, self.goz_10)
        self.window.setTabOrder(self.goz_10, self.goz_11)
        self.window.setTabOrder(self.goz_11, self.goz_12)
        self.window.setTabOrder(self.goz_12, self.goz_13)
        self.window.setTabOrder(self.goz_13, self.goz_14)
        self.window.setTabOrder(self.goz_14, self.goz_15)
        self.window.setTabOrder(self.goz_15, self.alinan)
        self.window.setTabOrder(self.alinan, self.gonder_1)
        self.window.setTabOrder(self.gonder_1, self.gonder_2)
        self.window.setTabOrder(self.gonder_2, self.gonder_3)
        self.window.setTabOrder(self.gonder_3, self.gonder_4)
        self.window.setTabOrder(self.gonder_4, self.gonder_5)
        self.window.setTabOrder(self.gonder_5, self.gonder_6)

        gorev_gonder = self.window.findChild(QPushButton, 'pushButton')
        gorev_gonder.clicked.connect(self.gorev_send)

        gorev_1_gonder = self.window.findChild(QPushButton, 'pushButton_2')
        gorev_1_gonder.clicked.connect(self.gorev_1_send)

        gorev_2_gonder = self.window.findChild(QPushButton, 'pushButton_3')
        gorev_2_gonder.clicked.connect(self.gorev_2_send)

        gorev_3_gonder = self.window.findChild(QPushButton, 'pushButton_4')
        gorev_3_gonder.clicked.connect(self.gorev_3_send)

        gorev_4_gonder = self.window.findChild(QPushButton, 'pushButton_5')
        gorev_4_gonder.clicked.connect(self.gorev_4_send)

        gorev_5_gonder = self.window.findChild(QPushButton, 'pushButton_6')
        gorev_5_gonder.clicked.connect(self.gorev_5_send)

        gorev_6_gonder = self.window.findChild(QPushButton, 'pushButton_7')
        gorev_6_gonder.clicked.connect(self.gorev_6_send)

        self.window.show()

        try:
            config = configparser.ConfigParser()
            config.read_file(open(self.cfg_file))

            self.modul_ip.setText(config['SETTINGS']['modul_ip'])
            self.goz_1.setText(config['SETTINGS']['goz_1'])
            self.goz_2.setText(config['SETTINGS']['goz_2'])
            self.goz_3.setText(config['SETTINGS']['goz_3'])
            self.goz_4.setText(config['SETTINGS']['goz_4'])
            self.goz_5.setText(config['SETTINGS']['goz_5'])
            self.goz_6.setText(config['SETTINGS']['goz_6'])
            self.goz_7.setText(config['SETTINGS']['goz_7'])
            self.goz_8.setText(config['SETTINGS']['goz_8'])
            self.goz_9.setText(config['SETTINGS']['goz_9'])
            self.goz_10.setText(config['SETTINGS']['goz_10'])
            self.goz_11.setText(config['SETTINGS']['goz_11'])
            self.goz_12.setText(config['SETTINGS']['goz_12'])
            self.goz_13.setText(config['SETTINGS']['goz_13'])
            self.goz_14.setText(config['SETTINGS']['goz_14'])
            self.goz_15.setText(config['SETTINGS']['goz_15'])

            self.gonder_1.setText(config['SETTINGS']['gonder_1'])
            self.gonder_2.setText(config['SETTINGS']['gonder_2'])
            self.gonder_3.setText(config['SETTINGS']['gonder_3'])
            self.gonder_4.setText(config['SETTINGS']['gonder_4'])
            self.gonder_5.setText(config['SETTINGS']['gonder_5'])
            self.gonder_6.setText(config['SETTINGS']['gonder_6'])
        except:
            self.goz_1.setText("0")
            self.goz_2.setText("0")
            self.goz_3.setText("0")
            self.goz_4.setText("0")
            self.goz_5.setText("0")
            self.goz_6.setText("0")
            self.goz_7.setText("0")
            self.goz_8.setText("0")
            self.goz_9.setText("0")
            self.goz_10.setText("0")
            self.goz_11.setText("0")
            self.goz_12.setText("0")
            self.goz_13.setText("0")
            self.goz_14.setText("0")
            self.goz_15.setText("0")

            self.modul_ip.setText("192.168.1.")

            self.gonder_1.setText("t,1")
            self.gonder_2.setText("t,2")
            self.gonder_3.setText("t,3")
            self.gonder_4.setText("t,4")
            self.gonder_5.setText("t,5")
            self.gonder_6.setText("t,6")


    def gorev_send(self):
        MESSAGE = "g,{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},".format(self.goz_1.text(), self.goz_2.text(),
                                                                          self.goz_3.text(), self.goz_4.text(),
                                                                          self.goz_5.text(), self.goz_6.text(),
                                                                          self.goz_7.text(), self.goz_8.text(),
                                                                          self.goz_9.text(), self.goz_10.text(),
                                                                          self.goz_11.text(), self.goz_12.text(),
                                                                          self.goz_13.text(), self.goz_14.text(),
                                                                          self.goz_15.text())
        print(MESSAGE)
        self.msg_gonder(MESSAGE)

    def gorev_1_send(self):
        sys.exit(app.exec_())
        # dlg = CustomDialog(self)
        # if dlg.exec_():
        #     print("Success!")
        # else:
        #     print("Cancel!")

    def gorev_2_send(self):
        MESSAGE = self.gonder_2.text()
        self.msg_gonder(MESSAGE)

    def gorev_3_send(self):
        MESSAGE = self.gonder_3.text()
        self.msg_gonder(MESSAGE)

    def gorev_4_send(self):
        MESSAGE = self.gonder_4.text()
        self.msg_gonder(MESSAGE)

    def gorev_5_send(self):
        MESSAGE = self.gonder_5.text()
        self.msg_gonder(MESSAGE)

    def gorev_6_send(self):
        MESSAGE = self.gonder_6.text()
        self.msg_gonder(MESSAGE)

    def msg_gonder(self, msg):
        self.save_cfg()

        UDP_IP_C = self.modul_ip.text()
        UDP_PORT_C = 333
        MESSAGE = msg

        UDP_IP_S = self.get_ip_x()
        UDP_PORT_S = 333

        sock_s = socket.socket(socket.AF_INET,  # Internet
                               socket.SOCK_DGRAM)  # UDP
        sock_s.bind((UDP_IP_S, UDP_PORT_S))

        sock_s.sendto(bytes(MESSAGE, encoding='utf-8'), (UDP_IP_C, UDP_PORT_C))

        sock_s.setblocking(0)
        ready = select.select([sock_s], [], [], 1)
        if ready[0]:
            data, addr = sock_s.recvfrom(1024)  # buffer size is 1024 bytes
            self.alinan.setText(str(data).replace("b", "").replace("'", ""))
            print(data)

    def save_cfg(self):
        config = configparser.ConfigParser()
        config['SETTINGS'] = {}
        config['SETTINGS']['modul_ip'] = str(self.modul_ip.text())
        config['SETTINGS']['goz_1'] = str(self.goz_1.text())
        config['SETTINGS']['goz_2'] = str(self.goz_2.text())
        config['SETTINGS']['goz_3'] = str(self.goz_3.text())
        config['SETTINGS']['goz_4'] = str(self.goz_4.text())
        config['SETTINGS']['goz_5'] = str(self.goz_5.text())
        config['SETTINGS']['goz_6'] = str(self.goz_6.text())
        config['SETTINGS']['goz_7'] = str(self.goz_7.text())
        config['SETTINGS']['goz_8'] = str(self.goz_8.text())
        config['SETTINGS']['goz_9'] = str(self.goz_9.text())
        config['SETTINGS']['goz_10'] = str(self.goz_10.text())
        config['SETTINGS']['goz_11'] = str(self.goz_11.text())
        config['SETTINGS']['goz_12'] = str(self.goz_12.text())
        config['SETTINGS']['goz_13'] = str(self.goz_13.text())
        config['SETTINGS']['goz_14'] = str(self.goz_14.text())
        config['SETTINGS']['goz_15'] = str(self.goz_15.text())

        config['SETTINGS']['gonder_1'] = str(self.gonder_1.text())
        config['SETTINGS']['gonder_2'] = str(self.gonder_2.text())
        config['SETTINGS']['gonder_3'] = str(self.gonder_3.text())
        config['SETTINGS']['gonder_4'] = str(self.gonder_4.text())
        config['SETTINGS']['gonder_5'] = str(self.gonder_5.text())
        config['SETTINGS']['gonder_6'] = str(self.gonder_6.text())

        with open(self.cfg_file, 'w') as configfile:
            config.write(configfile)

    def get_ip_x(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP


    def versiyon_kontrol(self):
        """ Versiyon Kontrol """
        # Sunucudan versiyon.txt dosyasini oku
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

        if self.version_info[0] < v[0]:
            print("guncelle 1")
            return True
        elif self.version_info[0] == v[0]:
            if self.version_info[1] < v[1]:
                print("guncelle 2")
                return True

        return False

    def cik(self):
        print("cikkkkkkkkkk")
        # sys.exit()
        # self.th.join()
        # sys.exit(app.exec_())

        return True

    def guncelle(self):
        from pyside_example import update
        if update.yeni_dosya():
            print("update bittiiiiiiiiiiiiiii")
            self.th_exit = True
            self.cik()
            # sys.exit(app.exec_())
        else:
            print("ne olduuuuuuuuu")

        return True

    def thread_function(self):
        while True:
            while True:
                if self.th_exit:
                    print("thread_function cik")
                    break
                executionTime = (time.time() - self.startTime)
                if executionTime > 10:
                    self.startTime = time.time()
                    print("guncelleme kontrol basliyor")
                    if self.versiyon_kontrol():
                        print("guncelle")
                        time.sleep(2)
                        self.guncelle()
                        time.sleep(2)
                        print("guncelleme bitti")
                        break
                    else:
                        print("devam et")
                time.sleep(1)

            print("while cikildi")
            self.gorev_1_send()
            time.sleep(1)
            sys.exit()


if __name__ == '__main__':
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    form = Form('ModulTest.ui')
    sys.exit(app.exec_())

