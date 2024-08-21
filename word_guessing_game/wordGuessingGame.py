import requests
# import random
# from appsGUI.main import UI
# from Custom_Widgets.Widgets import *


def get_word_list():
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

    response = requests.get(word_site)

    return [i for i in response.text.split() if len(i) > 7]


# class GuessingGameClass(UI):
#     def __init__(self):
#         self.ui = UI()
#
#     def get_word_list(self):
#         word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
#         response = requests.get(word_site)
#         words = [i for i in response.text.split() if len(i) >= 7]
#         return words
#
#     def wordGuessingGame(self):
#         self.secret_word = random.choice(self.get_word_list())
#
#         layout = self.ui.horizontalLayout_20
#         self.clearLayout(layout)
#
#         self.word_label = self.ui.label_7
#         self.word_label.setText(self.secret_word[0].upper() + ''.join(['-' for _ in range(1, len(self.secret_word))]))
#
#         self.guessings_list = []
#         for i in range(len(self.secret_word)):
#             if i == 0:
#                 lineEdit = QLineEdit(self.secret_word[i].upper())
#                 lineEdit.setDisabled(True)
#             else:
#                 lineEdit = QLineEdit()
#                 lineEdit.setValidator(QRegExpValidator(QRegExp("[a-zA-Z]")))
#             lineEdit.setFixedSize(QSize(80, 100))
#             lineEdit.setAlignment(Qt.AlignCenter)
#             lineEdit.setStyleSheet("background-color: black; border: 1px solid black; font-size: 30px;")
#             layout.addWidget(lineEdit, alignment=Qt.AlignCenter)
#
#             self.guessings_list.append(lineEdit)
#
#         for i in range(1, len(self.guessings_list) - 1):
#                 self.guessings_list[i].textChanged.connect(
#                     lambda _, next_lineEdit=self.guessings_list[i + 1]: next_lineEdit.setFocus())
#
#     def revealTheWord(self):
#         self.word_label.setText(self.secret_word.capitalize())
#
#     def checkTheGuessing(self):
#         self.userGuessing = ''.join([lineEdit.text() for lineEdit in self.guessings_list]).capitalize()
#
#         if len(self.userGuessing) == 1 or len(self.userGuessing) < len(self.secret_word):
#             self.alert('Attention', 'Please fill the cells correctly!', QMessageBox.Warning)
#         elif self.userGuessing.lower() == self.secret_word.lower():
#             for i in range(1, len(self.guessings_list)):
#                 self.guessings_list[i].setStyleSheet("background-color: green; border: 1px solid black; font-size: 30px;")
#                 self.guessings_list[i].setDisabled(True)
#             self.alert('Congratulations, You won!', "It was a great game. Let's play again...", QMessageBox.Information)
#             self.wordGuessingGame()
#         else:
#             for i in range(1, len(self.guessings_list)):
#                 if self.guessings_list[i].text().lower() == self.secret_word[i].lower():
#                     self.guessings_list[i].setStyleSheet("background-color: green; border: 1px solid black; font-size: 30px;")
#                     self.guessings_list[i].setDisabled(True)
#                 else:
#                     self.guessings_list[i].setText('')
#                     self.guessings_list[i].setStyleSheet("background-color: black; border: 1px solid black; font-size: 30px;")
#
#
#     def clearLayout(self, layout):
#         while layout.count():
#             item = layout.takeAt(0)
#             widget = item.widget()
#             if widget:
#                 widget.deleteLater()
#
#
#     def alert(self, title, message, icon):
#         message = str(message)
#         msg = QMessageBox()
#         msg.setWindowTitle(f"{title}")
#         msg.setText(message)
#         msg.setIcon(icon)
#         msg.exec_()
