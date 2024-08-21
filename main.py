import random
import threading
import wave
from functools import partial

import pyaudio

from ui_interface import *
from Custom_Widgets.Widgets import *
import uuid

from word_guessing_game import wordGuessingGame
from colorGameApp import colorDictionary
from b_whatsapp import main as whatsappBot

time_limit = 30
correctScore = 0
wrongScore = 0
remainingTime = time_limit
currentColor = None


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.delete_button_to_note_frame = {}
        self.delete_contact_frame = {}

        self.frames = []

        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        self.recording_thread = None
        self.recording = None

        loadJsonStyle(self, self.ui)
        self.setWindowIcon(QtGui.QIcon('logopng.png'))  # logopng.png

        # self.ui.informationBtn.clicked.connect(self.ui.CenterMenuContainer.expandMenu)
        # self.ui.helpBtn.clicked.connect(lambda: self.ui.CenterMenuContainer.expandMenu())
        # self.ui.closecentermenuBtn.clicked.connect(lambda: self.ui.CenterMenuContainer.collapseMenu())

        self.ui.wordGBtn.clicked.connect(self.wordGuessingGame)
        self.ui.revealBtn.clicked.connect(self.revealTheWord)
        self.ui.checkGuessBtn.clicked.connect(self.checkTheGuessing)

        self.ui.lineEdit.setInputMask("D9999")
        self.ui.lineEdit_2.setInputMask("D9999")
        self.ui.lineEdit_3.setInputMask("D9999")
        self.ui.lineEdit_4.setInputMask("D9999")
        self.ui.generateArrayBtn.clicked.connect(self.generateArray)
        self.ui.binarySearchFindBtn.clicked.connect(self.findBinary)
        self.ui.binarySearchCleanBtn.clicked.connect(self.clearLayouts)

        self.ui.addNoteBtn.clicked.connect(self.addNote)
        self.ui.pushButton_2.clicked.connect(self.deleteNote)

        self.ui.pushButton.clicked.connect(self.startToRecord)
        self.ui.pushButton.setDisabled(False)
        self.ui.pushButton_3.clicked.connect(self.stopRecording)
        self.ui.pushButton_3.setDisabled(True)

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateProgress)

        self.ui.checkBox_4.setChecked(True)
        self.ui.checkBox_4.clicked.connect(self.check4Clicked)
        self.ui.checkBox_3.setChecked(False)
        self.ui.checkBox_3.clicked.connect(self.check3Clicked)
        self.checkBox4 = True
        self.checkBox3 = False

        self.correctColorLayout = self.ui.horizontalLayout_38
        self.selectedColorLayout = self.ui.horizontalLayout_37

        self.ui.pushButton_5.clicked.connect(self.createLayout)

        self.ui.previousNavBtn.clicked.connect(self.previousNavBtnClicked)
        self.ui.nextNavBtn.clicked.connect(self.nextNavBtnClicked)

        self.ui.addContactBtn.clicked.connect(self.createNewContact)
        self.ui.deleteTextBtn.clicked.connect(self.deleteTextMessage)
        self.ui.pushButton_7.setDisabled(True)
        self.ui.checkBox_2.setDisabled(True)
        self.ui.sendMessageBtn.clicked.connect(self.sendMessageToContacts)

        self.ui.lineEdit_7.setInputMask("D999999999999999999999999999")


    def sendMessageToContacts(self):
        message = self.ui.textEdit_3.toPlainText()
        if not message:
            self.alert('Warning', 'No message to send!', QMessageBox.Warning)
        else:
            for value, frame  in self.delete_contact_frame.items():
                qframe = frame.findChild(QFrame, value)
                checkbox = qframe.findChild(QCheckBox, value)

                if checkbox.isChecked():
                    number = '+' + value.split('/')[1]
                    dateTimeEdit = qframe.findChild(QDateTimeEdit)
                    dateTime = dateTimeEdit.dateTime().toString("dd/MM/yyyy HH:mm")

                    whatsappBot.sendMessage(number, message, dateTime)

    def deleteContact(self, button):
        custom_object_property = button.property("buttonType")
        for property_, frame_7  in self.delete_contact_frame.items():
            if property_ == custom_object_property:
                frame_7.setParent(None)
                frame_7.deleteLater()
                del self.delete_contact_frame[property_]
                break


    def deleteTextMessage(self):
        self.ui.textEdit_3.clear()

    def createNewContact(self):
        name = self.ui.lineEdit_6.text()
        number = self.ui.lineEdit_7.text()

        for value in self.delete_contact_frame.values():
            if name + number == value:
                self.alert('Warning', 'You have already created this contact.', QMessageBox.Warning)
                break

        else:
            contact_layout = self.ui.verticalLayout_48

            frame_27 = QFrame()
            frame_27.setObjectName(name + number)
            frame_27.setProperty("frameType", name + number)

            sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy8.setHorizontalStretch(0)
            sizePolicy8.setVerticalStretch(0)
            sizePolicy8.setHeightForWidth(frame_27.sizePolicy().hasHeightForWidth())

            frame_27.setSizePolicy(sizePolicy8)
            frame_27.setMinimumSize(QSize(250, 0))
            frame_27.setStyleSheet(u"background-color: rgb(35, 62, 71);")
            frame_27.setFrameShape(QFrame.StyledPanel)
            frame_27.setFrameShadow(QFrame.Raised)
            verticalLayout_46 = QVBoxLayout(frame_27)
            verticalLayout_46.setSpacing(0)
            verticalLayout_46.setContentsMargins(0, 0, 0, 0)
            frame_28 = QFrame(frame_27)

            sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
            sizePolicy9.setHorizontalStretch(0)
            sizePolicy9.setVerticalStretch(0)
            sizePolicy9.setHeightForWidth(frame_28.sizePolicy().hasHeightForWidth())

            frame_28.setSizePolicy(sizePolicy9)
            frame_28.setMinimumSize(QSize(0, 0))
            frame_28.setSizeIncrement(QSize(0, 0))
            frame_28.setStyleSheet(u"background-color: rgb(20, 35, 40);")
            frame_28.setFrameShape(QFrame.StyledPanel)
            frame_28.setFrameShadow(QFrame.Raised)
            horizontalLayout_44 = QHBoxLayout(frame_28)
            label_34 = QLabel(frame_28)
            sizePolicy8.setHeightForWidth(label_34.sizePolicy().hasHeightForWidth())
            label_34.setSizePolicy(sizePolicy8)
            font10 = QFont()
            font10.setPointSize(10)
            font10.setBold(True)
            font10.setWeight(75)
            label_34.setFont(font10)
            label_34.setText(name)
            label_34.setStyleSheet(u"border-color:transparent;")

            horizontalLayout_44.addWidget(label_34)

            sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            sizePolicy1.setHorizontalStretch(0)
            sizePolicy1.setVerticalStretch(0)
            sizePolicy1.setHeightForWidth(self.ui.LeftMenuSubcontainer.sizePolicy().hasHeightForWidth())

            horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            horizontalLayout_44.addItem(horizontalSpacer_12)

            pushButton_7 = QPushButton(frame_28)
            sizePolicy1.setHeightForWidth(pushButton_7.sizePolicy().hasHeightForWidth())
            pushButton_7.setSizePolicy(sizePolicy1)
            pushButton_7.setProperty("buttonType", name + '/' + number)
            pushButton_7.clicked.connect(lambda: self.deleteContact(pushButton_7))
            pushButton_7.setMinimumSize(QSize(50, 40))
            pushButton_7.setMaximumSize(QSize(50, 16777215))
            pushButton_7.setStyleSheet(u"QPushButton {\n"
                                            "   border: transparent;\n"
                                            "	border-radius: 15px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "   border: 2px solid white;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed {\n"
                                            "	background-color: rgb(35, 62, 71);\n"
                                            "}")
            icon16 = QIcon()
            icon16.addFile(u":/icons/icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
            pushButton_7.setIcon(icon16)
            pushButton_7.setIconSize(QSize(23, 23))

            horizontalLayout_44.addWidget(pushButton_7)

            verticalLayout_46.addWidget(frame_28)

            frame_29 = QFrame(frame_27)
            sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            sizePolicy10.setHorizontalStretch(0)
            sizePolicy10.setVerticalStretch(0)
            sizePolicy10.setHeightForWidth(frame_29.sizePolicy().hasHeightForWidth())

            # sizePolicy8.setHeightForWidth(frame_29.sizePolicy().hasHeightForWidth())
            frame_29.setSizePolicy(sizePolicy10)
            frame_29.setFrameShape(QFrame.StyledPanel)
            frame_29.setFrameShadow(QFrame.Raised)
            verticalLayout_47 = QVBoxLayout(frame_29)

            label_35 = QLabel(frame_29)
            # sizePolicy8.setHeightForWidth(label_35.sizePolicy().hasHeightForWidth())
            sizePolicy1.setHeightForWidth(label_35.sizePolicy().hasHeightForWidth())
            label_35.setSizePolicy(sizePolicy1)
            font11 = QFont()
            font11.setFamily(u"Bauhaus 93")
            font11.setPointSize(12)
            font11.setBold(False)
            font11.setWeight(50)
            label_35.setFont(font11)
            label_35.setText('+' + number)
            label_35.setAlignment(Qt.AlignCenter)

            verticalLayout_47.addWidget(label_35)

            verticalLayout_46.addWidget(frame_29)

            frame_30 = QFrame(frame_27)
            frame_30.setObjectName(name + '/' + number)
            sizePolicy8.setHeightForWidth(frame_30.sizePolicy().hasHeightForWidth())
            frame_30.setSizePolicy(sizePolicy8)
            frame_30.setLayoutDirection(Qt.LeftToRight)
            frame_30.setFrameShape(QFrame.StyledPanel)
            frame_30.setFrameShadow(QFrame.Raised)
            horizontalLayout_45 = QHBoxLayout(frame_30)
            checkBox_2 = QCheckBox(frame_30)
            checkBox_2.setObjectName(name + '/' + number)
            # checkBox_2

            horizontalLayout_45.addWidget(checkBox_2)

            dateTimeEdit = QDateTimeEdit(frame_30)
            dateTimeEdit.setDisplayFormat("dd/MM/yyyy HH:mm")
            font12 = QFont()
            font12.setPointSize(11)
            font12.setBold(False)
            font12.setWeight(50)
            dateTimeEdit.setFont(font12)
            horizontalLayout_45.addWidget(dateTimeEdit)

            verticalLayout_46.addWidget(frame_30)

            contact_layout.addWidget(frame_27)

            self.delete_contact_frame[name + '/' + number] = frame_27


    def previousNavBtnClicked(self):
        x = self.ui.mmStackedWidget.currentIndex()
        if int(x) > 0:
            x -= 1
            self.ui.mmStackedWidget.setCurrentIndex(x)


    def nextNavBtnClicked(self):
        x = self.ui.mmStackedWidget.currentIndex()
        if int(x) < 6:
            x += 1
            self.ui.mmStackedWidget.setCurrentIndex(x)

    def check4Clicked(self):
        if self.ui.checkBox_4.isChecked():
            self.ui.checkBox_3.setChecked(False)
            self.checkBox4 = True
            self.checkBox3 = False
        else:
            self.ui.checkBox_3.setChecked(True)
            self.checkBox4 = False
            self.checkBox3 = True

    def check3Clicked(self):
        if self.ui.checkBox_3.isChecked():
            self.ui.checkBox_4.setChecked(False)
            self.checkBox3 = True
            self.checkBox4 = False
        else:
            self.ui.checkBox_4.setChecked(True)
            self.checkBox3 = False
            self.checkBox4 = True


    def createLayout(self):
        self.ui.pushButton_5.setDisabled(True)
        self.clearLayout(self.correctColorLayout)
        self.clearLayout(self.selectedColorLayout)
        self.startColorGame()

    def startColorGame(self):
        global correctScore, wrongScore, currentColor, remainingTime
        correctScore = 0
        wrongScore = 0
        remainingTime = time_limit
        self.ui.checkBox_4.setDisabled(True)
        self.ui.checkBox_3.setDisabled(True)
        self.updateScores()
        self.updateTime()
        self.generateColor()
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.countDown)
        self.timer.start()


    def countDown(self):
        global remainingTime
        remainingTime -= 1
        self.updateTime()
        if remainingTime == 0:
            self.gameOver()

    def gameOver(self):
        self.timer.stop()
        self.ui.pushButton_5.setEnabled(True)
        self.ui.checkBox_4.setEnabled(True)
        self.ui.checkBox_3.setEnabled(True)

        for button in self.createdButtonsList:
            button.setDisabled(True)

        self.alert('Attention!', 'Game has ended. You can check your results.', QMessageBox.Information)


    def generateColor(self):
        global currentColor
        if self.checkBox4:
            color_list = list(colorDictionary.mainColorsDictionary.items())
        else:
            color_list = list(colorDictionary.allColorsDictionary.items())

        currentColor = random.sample(color_list, 5)

        self.updateColorLabel()
        self.createVariants()

    def checkColor(self, selectedColor):
        global correctScore, wrongScore
        if currentColor[0][1] == selectedColor:
            correctScore += 1
        else:
            wrongScore += 1
        currentColorLabel = QLabel()
        currentColorLabel.setFixedSize(QSize(20, 20))
        currentColorLabel.setStyleSheet(f"background-color: {currentColor[0][1]}")
        self.correctColorLayout.addWidget(currentColorLabel)

        selectedColorLabel = QLabel()
        selectedColorLabel.setFixedSize(QSize(20, 20))
        selectedColorLabel.setStyleSheet(f"background-color: {selectedColor}")
        self.selectedColorLayout.addWidget(selectedColorLabel)

        self.generateColor()
        self.updateScores()

    def createVariants(self):
        buttonFont = QFont()
        buttonFont.setPointSize(15)
        buttonFont.setBold(True)

        colorVariants = currentColor[:]
        random.shuffle(colorVariants)

        self.createdButtonsList = []

        button_layout = self.ui.horizontalLayout_39
        self.clearLayout(button_layout)
        for color in colorVariants:
            button = QPushButton(color[0])
            button.clicked.connect(partial(self.checkColor, color[1]))
            button.setFixedSize(QSize(150, 50))
            button.setFont(buttonFont)
            textColor = 'black'
            if color[0].lower() == 'black' or color[0].lower() == 'navy':
                textColor = 'white'

            button.setStyleSheet(f"background-color: {color[1]}; border: 1px solid black; font-size: 15px; color: {textColor}")

            self.createdButtonsList.append(button)
            button_layout.addWidget(button, alignment=Qt.AlignCenter)

    def updateColorLabel(self):
        self.ui.label_14.setText(currentColor[0][1])


    def updateTime(self):
        self.ui.label_15.setText(f"Time remaining: {remainingTime} s")

    def updateScores(self):
        self.ui.label_20.setText("Your Scores:")
        self.ui.label_18.setText(f"Correct: {correctScore}")
        self.ui.label_19.setText(f"Wrong: {wrongScore}")


    def updateProgress(self):
        current_value = self.ui.progressBar.value()
        max_value = self.ui.progressBar.maximum()
        new_value = min(current_value + 1, max_value)
        self.ui.progressBar.setValue(new_value)

    def startToRecord(self):
        self.ui.progressBar.setValue(0)
        self.timer.start(1000)
        self.recording = True
        self.ui.label_13.setText("Recording is in progress...")
        self.ui.pushButton.setDisabled(True)
        self.ui.pushButton_3.setDisabled(False)
        self.frames = []

        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/pause-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.pushButton.setIcon(icon5)
        self.ui.pushButton.setIconSize(QSize(30, 30))

        self.recording_thread = threading.Thread(target=self.record_audio)
        self.recording_thread.start()


    def record_audio(self):
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True,
                                      frames_per_buffer=1024)

        while self.recording:
            data = self.stream.read(1024)
            self.frames.append(list(map(int, data)))


    def stopRecording(self):
        print('in stop recording')
        self.timer.stop()
        self.recording = False
        if not self.frames:
            self.alert('Attention!', "Nothing's been recorded.", QMessageBox.Warning)

        self.ui.label_13.setText("Recording's been stopped. Your recording is saved.")
        self.ui.pushButton.setDisabled(False)
        self.ui.pushButton_3.setDisabled(True)

        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

        sound_file = wave.open(f'C:\\Users\\Cavid\\Desktop\\my_recording_{uuid.uuid4()}.wav', 'wb')
        sound_file.setnchannels(1)
        sound_file.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)

        self.ui.pushButton.setObjectName(u"pushButton")
        self.ui.pushButton.setStyleSheet(u"QPushButton {\n"
                                      "    color: #333;\n"
                                      "    border: 2px solid #555;\n"
                                      "    border-radius: 20px;\n"
                                      "    border-style: outset;\n"
                                      "    padding: 5px;\n"
                                      "    border-radius: 15px;\n"
                                      "    background-color: rgb(0, 115, 172);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(0, 170, 255);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    border-style: inset;\n"
                                      "    background-color: rgb(0, 115, 172);\n"
                                      "}")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/play-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.pushButton.setIcon(icon14)
        self.ui.pushButton.setIconSize(QSize(30, 30))

        for frame in self.frames:
            sound_file.writeframes(bytearray(frame))
        sound_file.close()

    def deleteNote(self, button):
        custom_object_property = button.property("buttonType")
        for frame_4, property_ in self.delete_button_to_note_frame.items():
            if property_ == custom_object_property:
                frame_4.setParent(None)
                frame_4.deleteLater()
                del self.delete_button_to_note_frame[frame_4]
                break


    def addNote(self):
        noteToAdd = self.ui.lineEdit_5.text()
        selectedDate = self.ui.calendarWidget.selectedDate().toString()

        if not noteToAdd:
            self.alert('Attention!', 'You must input the note!', QMessageBox.Warning)
        else:
            duplicated = self.ui.verticalFrame1.findChild(QFrame, noteToAdd + selectedDate)
            if duplicated:
                self.alert("Attention!", "This note has already been added.", QMessageBox.Warning)
            else:
                widget = self.ui.verticalFrame1.findChild(QFrame, 'frame_4')
                if widget:
                    widget.setParent(None)
                    widget.deleteLater()

                notesLayout = self.ui.verticalLayout_24

                frame_4 = QFrame()
                frame_4.setObjectName(noteToAdd + selectedDate)
                frame_4.setProperty("frameType", noteToAdd + selectedDate)
                frame_4.setMinimumSize(QSize(0, 100))
                frame_4.setMaximumSize(QSize(16777215, 100))
                frame_4.setStyleSheet(u"background-color: rgb(106, 106, 106);\n"
                                           "border: 1px solid white;\n"
                                           "border-radius: 10px;")
                frame_4.setFrameShape(QFrame.StyledPanel)
                frame_4.setFrameShadow(QFrame.Raised)
                verticalLayout_21 = QVBoxLayout(frame_4)
                verticalLayout_21.setSpacing(0)
                verticalLayout_21.setObjectName(u"verticalLayout_21")
                verticalLayout_21.setContentsMargins(0, 0, 0, 0)
                horizontalFrame_5 = QFrame(frame_4)
                horizontalFrame_5.setObjectName(u"horizontalFrame_5")
                horizontalFrame_5.setStyleSheet(u"border: transparent;")
                horizontalLayout_26 = QHBoxLayout(horizontalFrame_5)
                horizontalLayout_26.setSpacing(0)
                horizontalLayout_26.setObjectName(u"horizontalLayout_26")
                horizontalLayout_26.setContentsMargins(3, 0, 3, 0)
                label_16 = QLabel(horizontalFrame_5)
                label_16.setObjectName(u"label_16")
                label_16.setText(f"{selectedDate}")

                font5 = QFont()
                font5.setPointSize(10)
                font5.setBold(False)
                font5.setWeight(50)
                label_16.setFont(font5)

                horizontalLayout_26.addWidget(label_16)

                horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

                horizontalLayout_26.addItem(horizontalSpacer_2)

                pushButton_2 = QPushButton(horizontalFrame_5)

                pushButton_2.clicked.connect(lambda: self.deleteNote(pushButton_2))
                pushButton_2.setObjectName(u"pushButton_2")
                pushButton_2.setProperty("buttonType", noteToAdd + selectedDate)
                pushButton_2.setStyleSheet(u"QPushButton:hover{\n"
                                                " background-color: rgb(93, 93, 93);\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:pressed{\n"
                                                " background-color: transparent;\n"
                                                "}")
                icon11 = QIcon()
                icon11.addFile(u":/icons/icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)

                sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                sizePolicy1.setHorizontalStretch(0)
                sizePolicy1.setVerticalStretch(0)

                pushButton_2.setIcon(icon11)
                pushButton_2.setIconSize(QSize(25, 25))

                horizontalLayout_26.addWidget(pushButton_2)

                verticalLayout_21.addWidget(horizontalFrame_5)

                horizontalFrame_6 = QFrame(frame_4)
                horizontalFrame_6.setObjectName(u"horizontalFrame_6")
                sizePolicy1.setHeightForWidth(horizontalFrame_6.sizePolicy().hasHeightForWidth())
                horizontalFrame_6.setSizePolicy(sizePolicy1)
                horizontalLayout_27 = QHBoxLayout(horizontalFrame_6)
                horizontalLayout_27.setSpacing(0)
                horizontalLayout_27.setObjectName(u"horizontalLayout_27")
                horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
                label_17 = QLabel(horizontalFrame_6)
                label_17.setObjectName(u"label_17")
                label_17.setText(f"{noteToAdd}")

                font6 = QFont()
                font6.setFamily(u"Bauhaus 93")
                font6.setPointSize(10)
                label_17.setFont(font6)
                label_17.setStyleSheet(u"border: transparent;\n"
                                            "background-color: white;\n"
                                            "color: black;")
                label_17.setAlignment(Qt.AlignCenter)

                horizontalLayout_27.addWidget(label_17)

                verticalLayout_21.addWidget(horizontalFrame_6)

                notesLayout.addWidget(frame_4)

                self.delete_button_to_note_frame[frame_4] = noteToAdd + selectedDate

                with open("notesApp/notes.txt", 'a') as file:
                    file.write(f"{selectedDate}: {noteToAdd}\n")


    def findBinary(self):
        self.array = [int(i) for i in self.ui.textEdit_2.toPlainText().split(',')]
        self.wantedItem = int(self.ui.lineEdit_4.text())

        def binary_search(array, low, high, x):
            if high >= low:
                mid = (high + low) // 2

                if array[mid] == x:
                    self.ui.textEdit.append(f'🎯Found target item ({self.wantedItem}) in index {mid}.')
                    return mid
                elif array[mid] > x:
                    self.ui.textEdit.append(f'⬅️Mid item ({array[mid]}) is in index {mid}. Target item is in the left half.')
                    return binary_search(array, low, mid - 1, x)
                else:
                    self.ui.textEdit.append(f'➡️Mid item ({array[mid]}) is in index {mid}. Target item is in the right half.')
                    return binary_search(array, mid + 1, high, x)

            else:
                self.ui.textEdit.append(f'❗Target item ({self.wantedItem}) not found in array.')
                return -1

        self.ui.textEdit.clear()
        self.ui.textEdit.append(f'Binary searching for {self.wantedItem} is being started...')
        binary_search(self.array, 0, len(self.array) - 1, self.wantedItem)


    def clearLayouts(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.textEdit.clear()
        self.ui.textEdit_2.clear()

    def generateArray(self):
        self.lineEditTextFrom = self.ui.lineEdit_2.text()
        self.lineEditTextTo = self.ui.lineEdit.text()
        self.lineEditTextStepCount = self.ui.lineEdit_3.text() if self.ui.lineEdit_3.text() else '1'
        self.checkBoxChecked = self.ui.checkBox.isChecked()

        if self.lineEditTextFrom and self.lineEditTextTo:
            if not self.ui.checkBox.isChecked():
                self.generatedArray = [
                    str(i) for i in range(int(self.lineEditTextFrom.strip()), int(self.lineEditTextTo.strip()), int(self.lineEditTextStepCount.strip()))
                ]
                self.ui.textEdit_2.clear()
                self.ui.textEdit_2.append(', '.join(self.generatedArray))
            else:
                self.randomlyGenerated = random.sample(
                        range(int(self.lineEditTextFrom.strip()), int(self.lineEditTextTo.strip()),
                              int(self.lineEditTextStepCount.strip())),
                        int(self.lineEditTextTo.strip()) // (2 * int(self.lineEditTextStepCount.strip()))
                    )
                self.randomlyGenerated.sort()
                self.randomlyGenerated = [str(i) for i in self.randomlyGenerated]

                self.ui.textEdit_2.clear()
                self.ui.textEdit_2.append(', '.join(self.randomlyGenerated))
        else:
            self.alert('Attention!', 'Enter array generator parameters correctly!', QMessageBox.Warning)


    def wordGuessingGame(self):
        self.secret_word = random.choice(wordGuessingGame.get_word_list())

        layout = self.ui.horizontalLayout_20
        self.clearLayout(layout)

        self.word_label = self.ui.label_7
        self.word_label.setText(self.secret_word[0].upper() + ''.join(['-' for _ in range(1, len(self.secret_word))]))

        self.guessings_list = []
        for i in range(len(self.secret_word)):
            if i == 0:
                lineEdit = QLineEdit(self.secret_word[i].upper())
                lineEdit.setDisabled(True)
            else:
                lineEdit = QLineEdit()
                lineEdit.setValidator(QRegExpValidator(QRegExp("[a-zA-Z]")))
            lineEdit.setFixedSize(QSize(80, 100))
            lineEdit.setAlignment(Qt.AlignCenter)
            lineEdit.setStyleSheet("background-color: black; border: 1px solid black; font-size: 30px;")
            layout.addWidget(lineEdit, alignment=Qt.AlignCenter)

            self.guessings_list.append(lineEdit)

        for i in range(1, len(self.guessings_list) - 1):
                self.guessings_list[i].textChanged.connect(
                    lambda _, next_lineEdit=self.guessings_list[i + 1]: next_lineEdit.setFocus())

    def revealTheWord(self):
        self.word_label.setText(self.secret_word.capitalize())

    def checkTheGuessing(self):
        self.userGuessing = ''.join([lineEdit.text() for lineEdit in self.guessings_list]).capitalize()

        if len(self.userGuessing) == 1 or len(self.userGuessing) < len(self.secret_word):
            self.alert('Attention', 'Please fill the cells correctly!', QMessageBox.Warning)
        elif self.userGuessing.lower() == self.secret_word.lower():
            for i in range(1, len(self.guessings_list)):
                self.guessings_list[i].setStyleSheet("background-color: green; border: 1px solid black; font-size: 30px;")
                self.guessings_list[i].setDisabled(True)
            self.alert('Congratulations, You won!', "It was a great game. Let's play again...", QMessageBox.Information)
            self.wordGuessingGame()
        else:
            for i in range(1, len(self.guessings_list)):
                if self.guessings_list[i].text().lower() == self.secret_word[i].lower():
                    self.guessings_list[i].setStyleSheet("background-color: green; border: 1px solid black; font-size: 30px;")
                    self.guessings_list[i].setDisabled(True)
                else:
                    self.guessings_list[i].setText('')
                    self.guessings_list[i].setStyleSheet("background-color: black; border: 1px solid black; font-size: 30px;")


    def clearLayout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()


    def alert(self, title, message, icon):
        message = str(message)
        msg = QMessageBox()
        msg.setWindowTitle(f"{title}")
        msg.setText(message)
        msg.setIcon(icon)
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    UIWindow.show()
    sys.exit(app.exec_())
