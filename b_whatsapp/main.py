import pywhatkit
# from PySide2.QtCore import QSize, Qt, QTime, QLocale
#
# from PySide2.QtGui import QFont, QIcon
#
# from PySide2.QtWidgets import QDialog, QVBoxLayout, QLabel, QFrame, QSizePolicy, QHBoxLayout, QPushButton, QCheckBox, \
#     QTimeEdit, QLineEdit


def sendMessage(mobile_no: str, message: str, dateTime: str): # hour: int, minute: int
    # date = dateTime.split()[0]
    time = dateTime.split()[1]
    hour = int(time.split(':')[0])
    minute = int(time.split(':')[1])

    pywhatkit.sendwhatmsg(mobile_no, message, hour, minute, 10, True, 3)


# class CreateContact(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#         self.main_layout = QVBoxLayout(self)
#
#         self.top_frame = QFrame()
#         self.top_layout = QHBoxLayout(self.top_frame)
#         self.top_label = QLabel("Create Contact")
#         self.top_label.setFont(QFont("Arial", 12, weight=QFont.Bold))
#
#         self.top_layout.addWidget(self.top_label)
#         self.top_frame.setLayout(self.top_layout)
#
#         self.details_frame = QFrame()
#         self.details_layout = QVBoxLayout(self.details_frame)
#         self.name_label = QLabel("Name:")
#         self.name_input = QLineEdit()
#         self.phone_label = QLabel("Phone:")
#         self.phone_input = QLineEdit()
#         self.details_layout.addWidget(self.name_label)
#         self.details_layout.addWidget(self.name_input)
#         self.details_layout.addWidget(self.phone_label)
#         self.details_layout.addWidget(self.phone_input)
#         self.details_frame.setLayout(self.details_layout)
#
#         self.reminder_frame = QFrame()
#         self.reminder_layout = QHBoxLayout(self.reminder_frame)
#         self.addBtn = QPushButton("add contact")
#         self.reminder_layout.addWidget(self.addBtn)
#         self.reminder_frame.setLayout(self.reminder_layout)
#
#         self.main_layout.addWidget(self.top_frame)
#         self.main_layout.addWidget(self.details_frame)
#         self.main_layout.addWidget(self.reminder_frame)
#
#         self.setLayout(self.main_layout)