from PyQt5 import QtWidgets
import sys,time


def on_stop_clicked():
    time.sleep(10)

def on_output_button_clicked():
    while True:
        print("*")


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Первая программа на PyQt")
window.resize(1000, 70)
label = QtWidgets.QLabel("<center>Hello world</center>")

stop_button = QtWidgets.QPushButton("Приостановить процесс")
stop_button.resize(200, 40)
stop_button.clicked.connect(on_stop_clicked)

output_button = QtWidgets.QPushButton("Запустисть процесс")
output_button.resize(200, 40)
output_button.clicked.connect(on_output_button_clicked)

exit_button = QtWidgets.QPushButton("Выйти")
exit_button.resize(200, 40)
exit_button.clicked.connect(app.quit)

vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(stop_button)
vbox.addWidget(output_button)
vbox.addWidget(exit_button)

window.setLayout(vbox)
window.show()
sys.exit(app.exec_())