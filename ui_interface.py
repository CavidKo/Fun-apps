# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceYhRNzX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1459, 861)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color: #1f232a;\n"
"}\n"
"\n"
"#LeftMenuSubcontainer{\n"
"	background-color: #16191d;\n"
"}\n"
"\n"
"#LeftMenuSubcontainer QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#CenterMenuSubcontainer{\n"
"	background-color: #2c313c;\n"
"}\n"
"\n"
"#frame_6{\n"
"	background-color: 16191d;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#headerContainer{\n"
"	background-color: #2c313c;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.LeftMenuContainer.setObjectName(u"LeftMenuContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LeftMenuContainer.sizePolicy().hasHeightForWidth())
        self.LeftMenuContainer.setSizePolicy(sizePolicy)
        self.LeftMenuContainer.setMaximumSize(QSize(45, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.LeftMenuContainer)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuSubcontainer = QWidget(self.LeftMenuContainer)
        self.LeftMenuSubcontainer.setObjectName(u"LeftMenuSubcontainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LeftMenuSubcontainer.sizePolicy().hasHeightForWidth())
        self.LeftMenuSubcontainer.setSizePolicy(sizePolicy1)
        self.LeftMenuSubcontainer.setStyleSheet(u"QPushButton {\n"
"	background-color: #16191d;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #1f232a;\n"
"    }\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: #16191d;\n"
"    }")
        self.verticalLayout = QVBoxLayout(self.LeftMenuSubcontainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.LeftMenuSubcontainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.menuBtn.sizePolicy().hasHeightForWidth())
        self.menuBtn.setSizePolicy(sizePolicy2)
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(40, 40))
        self.menuBtn.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.menuBtn, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_2 = QFrame(self.LeftMenuSubcontainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 10, 0, 10)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        font = QFont()
        font.setPointSize(11)
        self.homeBtn.setFont(font)
        self.homeBtn.setStyleSheet(u"background-color: #1f232a;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(26, 26))

        self.verticalLayout_2.addWidget(self.homeBtn)

        self.calendarBtn = QPushButton(self.frame_2)
        self.calendarBtn.setObjectName(u"calendarBtn")
        self.calendarBtn.setFont(font)
#if QT_CONFIG(tooltip)
        self.calendarBtn.setToolTip(u"<html><head/><body><p><span style=\" color:#ffffff;\">calendar</span></p></body></html>")
#endif // QT_CONFIG(tooltip)
        self.calendarBtn.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/calendar.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.calendarBtn.setIcon(icon2)
        self.calendarBtn.setIconSize(QSize(26, 26))

        self.verticalLayout_2.addWidget(self.calendarBtn)

        self.binarySearchBtn = QPushButton(self.frame_2)
        self.binarySearchBtn.setObjectName(u"binarySearchBtn")
        self.binarySearchBtn.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.binarySearchBtn.setIcon(icon3)
        self.binarySearchBtn.setIconSize(QSize(26, 26))

        self.verticalLayout_2.addWidget(self.binarySearchBtn)

        self.wordGBtn = QPushButton(self.frame_2)
        self.wordGBtn.setObjectName(u"wordGBtn")
        self.wordGBtn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/book-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.wordGBtn.setIcon(icon4)
        self.wordGBtn.setIconSize(QSize(26, 26))

        self.verticalLayout_2.addWidget(self.wordGBtn)

        self.recorderBtn = QPushButton(self.frame_2)
        self.recorderBtn.setObjectName(u"recorderBtn")
        self.recorderBtn.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/volume-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.recorderBtn.setIcon(icon5)
        self.recorderBtn.setIconSize(QSize(26, 26))

        self.verticalLayout_2.addWidget(self.recorderBtn)

        self.colorGameBtn = QPushButton(self.frame_2)
        self.colorGameBtn.setObjectName(u"colorGameBtn")
        self.colorGameBtn.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/aperture.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.colorGameBtn.setIcon(icon6)
        self.colorGameBtn.setIconSize(QSize(26, 26))

        self.verticalLayout_2.addWidget(self.colorGameBtn)

        self.whatsappBtn = QPushButton(self.frame_2)
        self.whatsappBtn.setObjectName(u"whatsappBtn")
        self.whatsappBtn.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/twitch.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.whatsappBtn.setIcon(icon7)
        self.whatsappBtn.setIconSize(QSize(26, 26))

        self.verticalLayout_2.addWidget(self.whatsappBtn)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.LeftMenuSubcontainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.informationBtn = QPushButton(self.frame_3)
        self.informationBtn.setObjectName(u"informationBtn")
        self.informationBtn.setFont(font)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.informationBtn.setIcon(icon8)
        self.informationBtn.setIconSize(QSize(26, 26))

        self.verticalLayout_3.addWidget(self.informationBtn)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setFont(font)
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon9)
        self.helpBtn.setIconSize(QSize(26, 26))

        self.verticalLayout_3.addWidget(self.helpBtn)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.LeftMenuSubcontainer)


        self.horizontalLayout.addWidget(self.LeftMenuContainer)

        self.CenterMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.CenterMenuContainer.setObjectName(u"CenterMenuContainer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.CenterMenuContainer.sizePolicy().hasHeightForWidth())
        self.CenterMenuContainer.setSizePolicy(sizePolicy3)
        self.CenterMenuContainer.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.CenterMenuContainer)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.frame_6 = QFrame(self.CenterMenuContainer)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(30)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(15, 11, 15, 11)
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.closecentermenuBtn = QPushButton(self.frame_6)
        self.closecentermenuBtn.setObjectName(u"closecentermenuBtn")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closecentermenuBtn.setIcon(icon10)
        self.closecentermenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.closecentermenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.leftStackedWidget = QCustomStackedWidget(self.CenterMenuContainer)
        self.leftStackedWidget.setObjectName(u"leftStackedWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.leftStackedWidget.sizePolicy().hasHeightForWidth())
        self.leftStackedWidget.setSizePolicy(sizePolicy4)
        self.leftStackedWidget.setMaximumSize(QSize(200, 16777215))
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.horizontalLayout_8 = QHBoxLayout(self.page_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(self.page_6)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_2)

        self.leftStackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.horizontalLayout_5 = QHBoxLayout(self.page_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.page_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.leftStackedWidget.addWidget(self.page_7)

        self.verticalLayout_4.addWidget(self.leftStackedWidget)


        self.horizontalLayout.addWidget(self.CenterMenuContainer)

        self.MainBodyContainer = QWidget(self.centralwidget)
        self.MainBodyContainer.setObjectName(u"MainBodyContainer")
        sizePolicy1.setHeightForWidth(self.MainBodyContainer.sizePolicy().hasHeightForWidth())
        self.MainBodyContainer.setSizePolicy(sizePolicy1)
        self.MainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.MainBodyContainer)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.MainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        sizePolicy1.setHeightForWidth(self.headerContainer.sizePolicy().hasHeightForWidth())
        self.headerContainer.setSizePolicy(sizePolicy1)
        self.horizontalLayout_7 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.frame_5)
        self.pushButton_8.setObjectName(u"pushButton_8")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton_8.setFont(font2)

        self.horizontalLayout_9.addWidget(self.pushButton_8)


        self.horizontalLayout_7.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: hidden;\n"
"	background-color: #2c313c;\n"
"    padding: 5px;\n"
"	border-radius:15px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #cfcf00;\n"
"	\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: hidden;	\n"
"	background-color: #bebe00;\n"
"    }")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon11)
        self.minimizeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_7)
        self.restoreBtn.setObjectName(u"restoreBtn")
        self.restoreBtn.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: hidden;\n"
"	background-color: #2c313c;\n"
"    padding: 5px;\n"
"	border-radius:15px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #009c72;\n"
"	\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: hidden;	\n"
"	background-color: #008861;\n"
"    }")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon12)
        self.restoreBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: hidden;\n"
"	background-color: #2c313c;\n"
"    padding: 5px;\n"
"	border-radius:15px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(197, 0, 0);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: hidden;	\n"
"	background-color: rgb(147, 0, 0);\n"
"    }")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon13)
        self.closeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.closeBtn)


        self.horizontalLayout_7.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.MainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy1.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy1)
        self.mainBodyContent.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout_5 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.mainStackWidget = QCustomStackedWidget(self.mainBodyContent)
        self.mainStackWidget.setObjectName(u"mainStackWidget")
        sizePolicy1.setHeightForWidth(self.mainStackWidget.sizePolicy().hasHeightForWidth())
        self.mainStackWidget.setSizePolicy(sizePolicy1)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"background-color: rgb(35, 62, 71);")
        self.verticalLayout_36 = QVBoxLayout(self.page)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.frame_8 = QFrame(self.page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(20, 35, 40);\n"
"border-radius: 20px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.mmStackedWidget = QStackedWidget(self.frame_8)
        self.mmStackedWidget.setObjectName(u"mmStackedWidget")
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.verticalLayout_37 = QVBoxLayout(self.page_9)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_23 = QLabel(self.page_9)
        self.label_23.setObjectName(u"label_23")
        font3 = QFont()
        font3.setFamily(u"Baskerville Old Face")
        font3.setPointSize(30)
        font3.setBold(True)
        font3.setUnderline(False)
        font3.setWeight(75)
        self.label_23.setFont(font3)
        self.label_23.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid rgb(35, 62, 71);;")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_23)

        self.label = QLabel(self.page_9)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamily(u"Bauhaus 93")
        font4.setPointSize(20)
        font4.setBold(False)
        font4.setWeight(50)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid rgb(35, 62, 71);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label)

        self.verticalLayout_37.setStretch(0, 1)
        self.verticalLayout_37.setStretch(1, 3)
        self.mmStackedWidget.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.verticalLayout_38 = QVBoxLayout(self.page_10)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_24 = QLabel(self.page_10)
        self.label_24.setObjectName(u"label_24")
        font5 = QFont()
        font5.setFamily(u"Baskerville Old Face")
        font5.setPointSize(30)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_24.setFont(font5)
        self.label_24.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid rgb(35, 62, 71);")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.label_24)

        self.label_25 = QLabel(self.page_10)
        self.label_25.setObjectName(u"label_25")
        font6 = QFont()
        font6.setFamily(u"Bauhaus 93")
        font6.setPointSize(20)
        self.label_25.setFont(font6)
        self.label_25.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid rgb(35, 62, 71);")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.label_25)

        self.verticalLayout_38.setStretch(0, 1)
        self.verticalLayout_38.setStretch(1, 3)
        self.mmStackedWidget.addWidget(self.page_10)
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.verticalLayout_42 = QVBoxLayout(self.page_14)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_32 = QLabel(self.page_14)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font5)
        self.label_32.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid rgb(35, 62, 71);")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout_42.addWidget(self.label_32)

        self.label_33 = QLabel(self.page_14)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font6)
        self.label_33.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid rgb(35, 62, 71);")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_42.addWidget(self.label_33)

        self.verticalLayout_42.setStretch(0, 1)
        self.verticalLayout_42.setStretch(1, 3)
        self.mmStackedWidget.addWidget(self.page_14)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.verticalLayout_39 = QVBoxLayout(self.page_11)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_26 = QLabel(self.page_11)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font5)
        self.label_26.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid rgb(35, 62, 71);")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_26)

        self.label_27 = QLabel(self.page_11)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font6)
        self.label_27.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid rgb(35, 62, 71);")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_39.addWidget(self.label_27)

        self.verticalLayout_39.setStretch(0, 1)
        self.verticalLayout_39.setStretch(1, 3)
        self.mmStackedWidget.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.verticalLayout_40 = QVBoxLayout(self.page_12)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_28 = QLabel(self.page_12)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font5)
        self.label_28.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid rgb(35, 62, 71);")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.label_28)

        self.label_29 = QLabel(self.page_12)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font6)
        self.label_29.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid rgb(35, 62, 71);")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.label_29)

        self.verticalLayout_40.setStretch(0, 1)
        self.verticalLayout_40.setStretch(1, 3)
        self.mmStackedWidget.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.verticalLayout_41 = QVBoxLayout(self.page_13)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_30 = QLabel(self.page_13)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font5)
        self.label_30.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid rgb(35, 62, 71);")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_41.addWidget(self.label_30)

        self.label_31 = QLabel(self.page_13)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font6)
        self.label_31.setStyleSheet(u"border-radius: 15px;\n"
"border: 1px solid rgb(35, 62, 71);")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_41.addWidget(self.label_31)

        self.verticalLayout_41.setStretch(0, 1)
        self.verticalLayout_41.setStretch(1, 3)
        self.mmStackedWidget.addWidget(self.page_13)

        self.horizontalLayout_11.addWidget(self.mmStackedWidget)


        self.verticalLayout_36.addWidget(self.frame_8)

        self.frame_23 = QFrame(self.page)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setStyleSheet(u"background-color: rgb(20, 35, 40);\n"
"border-radius: 20px;\n"
"/* border: 1px solid rgb(254, 23, 57); */\n"
"\n"
"\n"
"")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.previousNavBtn = QPushButton(self.frame_23)
        self.previousNavBtn.setObjectName(u"previousNavBtn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.previousNavBtn.sizePolicy().hasHeightForWidth())
        self.previousNavBtn.setSizePolicy(sizePolicy5)
        font7 = QFont()
        font7.setPointSize(8)
        self.previousNavBtn.setFont(font7)
        self.previousNavBtn.setStyleSheet(u"QPushButton {\n"
"   border-radius: 30px;\n"
"	border: 1px solid  rgb(0, 170, 255); \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 115, 172);\n"
"}\n"
"\n"
"\n"
"")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/arrow-left-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.previousNavBtn.setIcon(icon14)
        self.previousNavBtn.setIconSize(QSize(26, 26))

        self.horizontalLayout_10.addWidget(self.previousNavBtn)

        self.calendarAppBtn = QPushButton(self.frame_23)
        self.calendarAppBtn.setObjectName(u"calendarAppBtn")
        sizePolicy5.setHeightForWidth(self.calendarAppBtn.sizePolicy().hasHeightForWidth())
        self.calendarAppBtn.setSizePolicy(sizePolicy5)
        self.calendarAppBtn.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 115, 172);\n"
"}")
        self.calendarAppBtn.setIcon(icon2)
        self.calendarAppBtn.setIconSize(QSize(26, 26))

        self.horizontalLayout_10.addWidget(self.calendarAppBtn)

        self.binarySearchAppBtn = QPushButton(self.frame_23)
        self.binarySearchAppBtn.setObjectName(u"binarySearchAppBtn")
        sizePolicy5.setHeightForWidth(self.binarySearchAppBtn.sizePolicy().hasHeightForWidth())
        self.binarySearchAppBtn.setSizePolicy(sizePolicy5)
        self.binarySearchAppBtn.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 115, 172);\n"
"}")
        self.binarySearchAppBtn.setIcon(icon3)
        self.binarySearchAppBtn.setIconSize(QSize(26, 26))

        self.horizontalLayout_10.addWidget(self.binarySearchAppBtn)

        self.whatsappBotApp = QPushButton(self.frame_23)
        self.whatsappBotApp.setObjectName(u"whatsappBotApp")
        sizePolicy5.setHeightForWidth(self.whatsappBotApp.sizePolicy().hasHeightForWidth())
        self.whatsappBotApp.setSizePolicy(sizePolicy5)
        self.whatsappBotApp.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 115, 172);\n"
"}")
        self.whatsappBotApp.setIcon(icon7)
        self.whatsappBotApp.setIconSize(QSize(26, 26))

        self.horizontalLayout_10.addWidget(self.whatsappBotApp)

        self.wordGuessingGameBtn = QPushButton(self.frame_23)
        self.wordGuessingGameBtn.setObjectName(u"wordGuessingGameBtn")
        sizePolicy5.setHeightForWidth(self.wordGuessingGameBtn.sizePolicy().hasHeightForWidth())
        self.wordGuessingGameBtn.setSizePolicy(sizePolicy5)
        self.wordGuessingGameBtn.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 115, 172);\n"
"}")
        self.wordGuessingGameBtn.setIcon(icon4)
        self.wordGuessingGameBtn.setIconSize(QSize(26, 26))

        self.horizontalLayout_10.addWidget(self.wordGuessingGameBtn)

        self.voiceRecorderApp = QPushButton(self.frame_23)
        self.voiceRecorderApp.setObjectName(u"voiceRecorderApp")
        sizePolicy5.setHeightForWidth(self.voiceRecorderApp.sizePolicy().hasHeightForWidth())
        self.voiceRecorderApp.setSizePolicy(sizePolicy5)
        self.voiceRecorderApp.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 115, 172);\n"
"}")
        self.voiceRecorderApp.setIcon(icon5)
        self.voiceRecorderApp.setIconSize(QSize(26, 26))

        self.horizontalLayout_10.addWidget(self.voiceRecorderApp)

        self.colorMatchingGameBtn = QPushButton(self.frame_23)
        self.colorMatchingGameBtn.setObjectName(u"colorMatchingGameBtn")
        sizePolicy5.setHeightForWidth(self.colorMatchingGameBtn.sizePolicy().hasHeightForWidth())
        self.colorMatchingGameBtn.setSizePolicy(sizePolicy5)
        self.colorMatchingGameBtn.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 115, 172);\n"
"}")
        self.colorMatchingGameBtn.setIcon(icon6)
        self.colorMatchingGameBtn.setIconSize(QSize(26, 26))

        self.horizontalLayout_10.addWidget(self.colorMatchingGameBtn)

        self.nextNavBtn = QPushButton(self.frame_23)
        self.nextNavBtn.setObjectName(u"nextNavBtn")
        sizePolicy5.setHeightForWidth(self.nextNavBtn.sizePolicy().hasHeightForWidth())
        self.nextNavBtn.setSizePolicy(sizePolicy5)
        self.nextNavBtn.setStyleSheet(u"QPushButton {\n"
"   border-radius: 30px;\n"
"	border: 1px solid  rgb(0, 170, 255); \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 115, 172);\n"
"}\n"
"\n"
"\n"
"")
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/arrow-right-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nextNavBtn.setIcon(icon15)
        self.nextNavBtn.setIconSize(QSize(26, 26))

        self.horizontalLayout_10.addWidget(self.nextNavBtn)


        self.verticalLayout_36.addWidget(self.frame_23)

        self.verticalLayout_36.setStretch(0, 8)
        self.verticalLayout_36.setStretch(1, 1)
        self.mainStackWidget.addWidget(self.page)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        sizePolicy.setHeightForWidth(self.page_4.sizePolicy().hasHeightForWidth())
        self.page_4.setSizePolicy(sizePolicy)
        self.verticalLayout_16 = QVBoxLayout(self.page_4)
        self.verticalLayout_16.setSpacing(7)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(11, 11, 11, 11)
        self.widget_4 = QWidget(self.page_4)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"background-color: rgb(70, 78, 95);\n"
"border-radius: 15px;")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_9 = QFrame(self.widget_4)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy6)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        font8 = QFont()
        font8.setPointSize(20)
        self.label_5.setFont(font8)

        self.verticalLayout_17.addWidget(self.label_5, 0, Qt.AlignTop)


        self.horizontalLayout_16.addWidget(self.frame_9, 0, Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.widget_4, 0, Qt.AlignTop)

        self.widget_5 = QWidget(self.page_4)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy7)
        self.widget_5.setStyleSheet(u"background-color: rgb(53, 59, 72);\n"
"border-radius: 15px;")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalFrame = QFrame(self.widget_5)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(65, 74, 88);")
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_7 = QLabel(self.horizontalFrame)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setMinimumSize(QSize(0, 20))
        self.label_7.setMaximumSize(QSize(16777215, 50))
        font9 = QFont()
        font9.setFamily(u"Palatino Linotype")
        font9.setPointSize(20)
        self.label_7.setFont(font9)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_7)

        self.verticalFrame = QFrame(self.horizontalFrame)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    border-radius: 15px;\n"
"}")
        self.verticalLayout_19 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_19.setSpacing(10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.revealBtn = QPushButton(self.verticalFrame)
        self.revealBtn.setObjectName(u"revealBtn")
        self.revealBtn.setMaximumSize(QSize(150, 16777215))
        self.revealBtn.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    border-radius: 15px;\n"
"	background-color: rgb(170, 170, 127);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(170, 170, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background-color: rgb(170, 170, 127);\n"
"}")

        self.verticalLayout_19.addWidget(self.revealBtn)

        self.checkGuessBtn = QPushButton(self.verticalFrame)
        self.checkGuessBtn.setObjectName(u"checkGuessBtn")
        self.checkGuessBtn.setMaximumSize(QSize(150, 16777215))
        self.checkGuessBtn.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_19.addWidget(self.checkGuessBtn)


        self.horizontalLayout_17.addWidget(self.verticalFrame, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_18.addWidget(self.horizontalFrame)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")

        self.verticalLayout_18.addLayout(self.horizontalLayout_20)


        self.horizontalLayout_18.addLayout(self.verticalLayout_18)


        self.verticalLayout_16.addWidget(self.widget_5)

        self.mainStackWidget.addWidget(self.page_4)
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.verticalLayout_44 = QVBoxLayout(self.page_15)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.frame_24 = QFrame(self.page_15)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"background-color: rgb(20, 35, 40);\n"
"border-radius: 20px;\n"
"border: 3px solid rgb(35, 62, 71);")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.scrollArea_2 = QScrollArea(self.frame_24)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy4.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy4)
        self.scrollArea_2.setFrameShape(QFrame.StyledPanel)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 268, 186))
        sizePolicy4.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy4)
        self.verticalLayout_48 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.frame_27 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy8)
        self.frame_27.setMinimumSize(QSize(250, 0))
        self.frame_27.setStyleSheet(u"background-color: rgb(35, 62, 71);")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_27)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy9)
        self.frame_28.setMinimumSize(QSize(0, 0))
        self.frame_28.setSizeIncrement(QSize(0, 0))
        self.frame_28.setStyleSheet(u"background-color: rgb(20, 35, 40);")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_34 = QLabel(self.frame_28)
        self.label_34.setObjectName(u"label_34")
        sizePolicy1.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy1)
        font10 = QFont()
        font10.setPointSize(10)
        font10.setBold(True)
        font10.setWeight(75)
        self.label_34.setFont(font10)
        self.label_34.setStyleSheet(u"border-color:transparent;")

        self.horizontalLayout_44.addWidget(self.label_34)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_12)

        self.pushButton_7 = QPushButton(self.frame_28)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy1.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy1)
        self.pushButton_7.setMinimumSize(QSize(50, 40))
        self.pushButton_7.setMaximumSize(QSize(50, 16777215))
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"    border: transparent;\n"
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
        self.pushButton_7.setIcon(icon16)
        self.pushButton_7.setIconSize(QSize(23, 23))

        self.horizontalLayout_44.addWidget(self.pushButton_7)


        self.verticalLayout_46.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy10)
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_29)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label_35 = QLabel(self.frame_29)
        self.label_35.setObjectName(u"label_35")
        sizePolicy1.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy1)
        font11 = QFont()
        font11.setFamily(u"Bauhaus 93")
        font11.setPointSize(12)
        font11.setBold(False)
        font11.setWeight(50)
        self.label_35.setFont(font11)
        self.label_35.setAlignment(Qt.AlignCenter)

        self.verticalLayout_47.addWidget(self.label_35)


        self.verticalLayout_46.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_27)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy8.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy8)
        self.frame_30.setLayoutDirection(Qt.LeftToRight)
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.checkBox_2 = QCheckBox(self.frame_30)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_45.addWidget(self.checkBox_2)

        self.dateTimeEdit = QDateTimeEdit(self.frame_30)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        font12 = QFont()
        font12.setPointSize(11)
        font12.setBold(False)
        font12.setWeight(50)
        self.dateTimeEdit.setFont(font12)

        self.horizontalLayout_45.addWidget(self.dateTimeEdit)


        self.verticalLayout_46.addWidget(self.frame_30)


        self.verticalLayout_48.addWidget(self.frame_27)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_42.addWidget(self.scrollArea_2)

        self.frame_31 = QFrame(self.frame_24)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_31)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.textEdit_3 = QTextEdit(self.frame_31)
        self.textEdit_3.setObjectName(u"textEdit_3")
        font13 = QFont()
        font13.setPointSize(12)
        font13.setBold(True)
        font13.setWeight(75)
        self.textEdit_3.setFont(font13)
        self.textEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_49.addWidget(self.textEdit_3)

        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_8)

        self.sendMessageBtn = QPushButton(self.frame_32)
        self.sendMessageBtn.setObjectName(u"sendMessageBtn")
        self.sendMessageBtn.setStyleSheet(u"QPushButton {\n"
"    border: transparent;\n"
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
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/send.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sendMessageBtn.setIcon(icon17)
        self.sendMessageBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_43.addWidget(self.sendMessageBtn)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_10)

        self.deleteTextBtn = QPushButton(self.frame_32)
        self.deleteTextBtn.setObjectName(u"deleteTextBtn")
        self.deleteTextBtn.setStyleSheet(u"QPushButton {\n"
"    border: transparent;\n"
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
        self.deleteTextBtn.setIcon(icon10)
        self.deleteTextBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_43.addWidget(self.deleteTextBtn)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_9)


        self.verticalLayout_49.addWidget(self.frame_32)


        self.horizontalLayout_42.addWidget(self.frame_31)

        self.horizontalLayout_42.setStretch(0, 1)
        self.horizontalLayout_42.setStretch(1, 3)

        self.verticalLayout_43.addWidget(self.frame_24)


        self.verticalLayout_44.addLayout(self.verticalLayout_43)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.frame_25 = QFrame(self.page_15)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"background-color: rgb(20, 35, 40);\n"
"border-radius: 20px;\n"
"border: 3px solid rgb(35, 62, 71);")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_25)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_36 = QLabel(self.frame_26)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font13)
        self.label_36.setStyleSheet(u"border: transparent;")

        self.horizontalLayout_41.addWidget(self.label_36)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_11)

        self.addContactBtn = QPushButton(self.frame_26)
        self.addContactBtn.setObjectName(u"addContactBtn")
        self.addContactBtn.setStyleSheet(u"QPushButton {\n"
"    border: transparent;\n"
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
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addContactBtn.setIcon(icon18)
        self.addContactBtn.setIconSize(QSize(30, 30))

        self.horizontalLayout_41.addWidget(self.addContactBtn)


        self.verticalLayout_45.addWidget(self.frame_26)

        self.frame_33 = QFrame(self.frame_25)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"border: transparent;")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_37 = QLabel(self.frame_33)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(100, 0))
        self.label_37.setFont(font)
        self.label_37.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.label_37)

        self.lineEdit_6 = QLineEdit(self.frame_33)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"")

        self.horizontalLayout_47.addWidget(self.lineEdit_6)


        self.verticalLayout_45.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_25)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setStyleSheet(u"border: transparent;")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_38 = QLabel(self.frame_34)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(100, 0))
        self.label_38.setFont(font)
        self.label_38.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.label_38)

        self.lineEdit_7 = QLineEdit(self.frame_34)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: black;")

        self.horizontalLayout_48.addWidget(self.lineEdit_7)


        self.verticalLayout_45.addWidget(self.frame_34)


        self.horizontalLayout_40.addWidget(self.frame_25)


        self.verticalLayout_44.addLayout(self.horizontalLayout_40)

        self.verticalLayout_44.setStretch(0, 4)
        self.verticalLayout_44.setStretch(1, 1)
        self.mainStackWidget.addWidget(self.page_15)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_22 = QHBoxLayout(self.page_2)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.scrollArea = QScrollArea(self.page_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 145, 120))
        self.scrollAreaWidgetContents.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 15px;")
        self.horizontalLayout_24 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame1 = QFrame(self.scrollAreaWidgetContents)
        self.verticalFrame1.setObjectName(u"verticalFrame1")
        self.verticalLayout_24 = QVBoxLayout(self.verticalFrame1)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_4 = QFrame(self.verticalFrame1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 100))
        self.frame_4.setMaximumSize(QSize(16777215, 100))
        self.frame_4.setStyleSheet(u"background-color: rgb(106, 106, 106);\n"
"border: 1px solid white;\n"
"border-radius: 10px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_4)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalFrame_5 = QFrame(self.frame_4)
        self.horizontalFrame_5.setObjectName(u"horizontalFrame_5")
        self.horizontalFrame_5.setStyleSheet(u"border: transparent;")
        self.horizontalLayout_26 = QHBoxLayout(self.horizontalFrame_5)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(3, 0, 3, 0)
        self.label_16 = QLabel(self.horizontalFrame_5)
        self.label_16.setObjectName(u"label_16")
        font14 = QFont()
        font14.setPointSize(10)
        font14.setBold(False)
        font14.setWeight(50)
        self.label_16.setFont(font14)

        self.horizontalLayout_26.addWidget(self.label_16)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_2)

        self.pushButton_2 = QPushButton(self.horizontalFrame_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton:hover{\n"
" background-color: rgb(93, 93, 93);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
" background-color: transparent;\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons/alert-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon19)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.horizontalLayout_26.addWidget(self.pushButton_2)


        self.verticalLayout_21.addWidget(self.horizontalFrame_5)

        self.horizontalFrame_6 = QFrame(self.frame_4)
        self.horizontalFrame_6.setObjectName(u"horizontalFrame_6")
        sizePolicy1.setHeightForWidth(self.horizontalFrame_6.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_6.setSizePolicy(sizePolicy1)
        self.horizontalLayout_27 = QHBoxLayout(self.horizontalFrame_6)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.horizontalFrame_6)
        self.label_17.setObjectName(u"label_17")
        font15 = QFont()
        font15.setFamily(u"Bauhaus 93")
        font15.setPointSize(15)
        self.label_17.setFont(font15)
        self.label_17.setStyleSheet(u"border: transparent;\n"
"background-color: white;\n"
"color: black;")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_17)


        self.verticalLayout_21.addWidget(self.horizontalFrame_6)


        self.verticalLayout_24.addWidget(self.frame_4)


        self.horizontalLayout_24.addWidget(self.verticalFrame1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_14.addWidget(self.scrollArea)


        self.horizontalLayout_22.addLayout(self.verticalLayout_14)

        self.horizontalFrame_2 = QFrame(self.page_2)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.verticalLayout_15 = QVBoxLayout(self.horizontalFrame_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.calendarWidget = QCalendarWidget(self.horizontalFrame_2)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setStyleSheet(u"QCalendarWidget QWidget{\n"
"color: white;\n"
"background-color: black;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton{\n"
"background-color: black;\n"
"color: white;\n"
"icon-size: 30px;\n"
"}\n"
"\n"
"QCalendarWidget QMenu{\n"
"background-color: rgb(124, 124, 124);\n"
"color: white;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color: #4a4a4a;\n"
"color: black;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:disabled{\n"
"background-color: black;\n"
"color: white;\n"
"}\n"
"")

        self.verticalLayout_13.addWidget(self.calendarWidget)


        self.verticalLayout_15.addLayout(self.verticalLayout_13)

        self.verticalFrame_2 = QFrame(self.horizontalFrame_2)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalFrame_2.setStyleSheet(u"background-color: rgb(106, 106, 106);\n"
"border: 1px solid white;\n"
"border-radius: 10px;\n"
"\n"
"")
        self.horizontalLayout_15 = QHBoxLayout(self.verticalFrame_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.label_4 = QLabel(self.verticalFrame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"border: transparent;")

        self.horizontalLayout_15.addWidget(self.label_4)

        self.lineEdit_5 = QLineEdit(self.verticalFrame_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_15.addWidget(self.lineEdit_5)

        self.addNoteBtn = QPushButton(self.verticalFrame_2)
        self.addNoteBtn.setObjectName(u"addNoteBtn")
        self.addNoteBtn.setStyleSheet(u"QPushButton {\n"
"  border: transparent;\n"
"  background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
" background-color: rgb(93, 93, 93);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
" background-color: transparent;\n"
"}\n"
"\n"
"")
        self.addNoteBtn.setIcon(icon18)
        self.addNoteBtn.setIconSize(QSize(23, 23))

        self.horizontalLayout_15.addWidget(self.addNoteBtn)


        self.verticalLayout_15.addWidget(self.verticalFrame_2)

        self.verticalLayout_15.setStretch(0, 10)

        self.horizontalLayout_22.addWidget(self.horizontalFrame_2)

        self.horizontalLayout_22.setStretch(0, 2)
        self.horizontalLayout_22.setStretch(1, 10)
        self.mainStackWidget.addWidget(self.page_2)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_22 = QVBoxLayout(self.page_5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_10 = QFrame(self.page_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgb(56, 62, 76);\n"
"border: 1px solid white;\n"
"border-radius: 15px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_10)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_13 = QLabel(self.frame_10)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font13)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_13)


        self.verticalLayout_23.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_4)

        self.progressBar = QProgressBar(self.frame_10)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(100, 0))
        self.progressBar.setValue(0)

        self.horizontalLayout_28.addWidget(self.progressBar)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_5)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")

        self.horizontalLayout_28.addLayout(self.verticalLayout_25)


        self.verticalLayout_23.addLayout(self.horizontalLayout_28)


        self.verticalLayout_20.addWidget(self.frame_10)


        self.verticalLayout_22.addLayout(self.verticalLayout_20)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_11 = QFrame(self.page_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background-color: rgb(63, 70, 86);\n"
"border: 1px solid white;\n"
"border-radius: 30px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.frame_11)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
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
        icon20 = QIcon()
        icon20.addFile(u":/icons/icons/play-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon20)
        self.pushButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_23.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(self.frame_11)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
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
        icon21 = QIcon()
        icon21.addFile(u":/icons/icons/stop-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon21)
        self.pushButton_3.setIconSize(QSize(30, 30))

        self.horizontalLayout_23.addWidget(self.pushButton_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_14.addWidget(self.frame_11)


        self.verticalLayout_22.addLayout(self.horizontalLayout_14)

        self.verticalLayout_22.setStretch(0, 4)
        self.verticalLayout_22.setStretch(1, 1)
        self.mainStackWidget.addWidget(self.page_5)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.page_8.setStyleSheet(u"background-color: rgb(42, 57, 80);")
        self.verticalLayout_27 = QVBoxLayout(self.page_8)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.frame_12 = QFrame(self.page_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: rgb(197, 109, 134);\n"
"border-radius: 15px;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_13)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_13)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font12)
        self.label_14.setStyleSheet(u"background-color: rgb(143, 79, 98);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"border-radius: 15px;\n"
"color: rgb(0, 0, 0);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_15)


        self.verticalLayout_28.addWidget(self.frame_13)


        self.horizontalLayout_31.addLayout(self.verticalLayout_28)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"background-color: rgb(255, 117, 130);\n"
"border-radius: 15px;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_14)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.frame_14)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_20)

        self.frame_19 = QFrame(self.frame_14)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"background-color: rgb(143, 79, 98);")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_19)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_18 = QLabel(self.frame_19)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)
        self.label_18.setStyleSheet(u"border-radius: 15px;\n"
"background-color: rgb(143, 79, 98);")

        self.verticalLayout_33.addWidget(self.label_18)

        self.label_19 = QLabel(self.frame_19)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"background-color: rgb(143, 79, 98);")

        self.verticalLayout_33.addWidget(self.label_19)


        self.verticalLayout_31.addWidget(self.frame_19)


        self.verticalLayout_29.addWidget(self.frame_14)


        self.horizontalLayout_31.addLayout(self.verticalLayout_29)


        self.horizontalLayout_29.addWidget(self.frame_12)


        self.verticalLayout_27.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.frame_15 = QFrame(self.page_8)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"background-color: rgb(114, 90, 122);\n"
"\n"
"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.frame_20 = QFrame(self.frame_15)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 10px;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_20)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy3.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy3)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_21)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setSpacing(2)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")

        self.verticalLayout_35.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setSpacing(2)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")

        self.verticalLayout_35.addLayout(self.horizontalLayout_37)


        self.verticalLayout_34.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_21 = QLabel(self.frame_22)
        self.label_21.setObjectName(u"label_21")
        font16 = QFont()
        font16.setPointSize(12)
        font16.setBold(True)
        font16.setUnderline(True)
        font16.setWeight(75)
        font16.setStrikeOut(False)
        font16.setKerning(True)
        self.label_21.setFont(font16)
        self.label_21.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 10px;")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_21)


        self.verticalLayout_34.addWidget(self.frame_22)

        self.verticalLayout_34.setStretch(0, 1)
        self.verticalLayout_34.setStretch(1, 3)

        self.horizontalLayout_32.addWidget(self.frame_20)


        self.horizontalLayout_30.addWidget(self.frame_15)


        self.verticalLayout_27.addLayout(self.horizontalLayout_30)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_16 = QFrame(self.page_8)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_16)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"background-color: rgb(114, 90, 122);")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_22 = QLabel(self.frame_17)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_22)

        self.checkBox_4 = QCheckBox(self.frame_17)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout_35.addWidget(self.checkBox_4)

        self.checkBox_3 = QCheckBox(self.frame_17)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_35.addWidget(self.checkBox_3)

        self.horizontalLayout_35.setStretch(0, 3)
        self.horizontalLayout_35.setStretch(1, 1)
        self.horizontalLayout_35.setStretch(2, 1)

        self.horizontalLayout_33.addWidget(self.frame_17)


        self.verticalLayout_32.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"background-color: rgb(53, 92, 125);")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_6)

        self.pushButton_5 = QPushButton(self.frame_18)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 1px solid white;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    background-color: rgb(0, 115, 172);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 115, 172);\n"
"}")

        self.horizontalLayout_36.addWidget(self.pushButton_5)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_7)


        self.horizontalLayout_34.addWidget(self.frame_18)


        self.verticalLayout_32.addLayout(self.horizontalLayout_34)


        self.verticalLayout_26.addWidget(self.frame_16)


        self.verticalLayout_27.addLayout(self.verticalLayout_26)

        self.verticalLayout_27.setStretch(0, 1)
        self.verticalLayout_27.setStretch(1, 2)
        self.verticalLayout_27.setStretch(2, 1)
        self.mainStackWidget.addWidget(self.page_8)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_13 = QHBoxLayout(self.page_3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalFrame2 = QFrame(self.page_3)
        self.verticalFrame2.setObjectName(u"verticalFrame2")
        self.verticalLayout_9 = QVBoxLayout(self.verticalFrame2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_11 = QLabel(self.verticalFrame2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 25))
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 10px;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_11)

        self.lineEdit_4 = QLineEdit(self.verticalFrame2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy2.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy2)
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(99, 110, 135);")
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.lineEdit_4)

        self.binarySearchFindBtn = QPushButton(self.verticalFrame2)
        self.binarySearchFindBtn.setObjectName(u"binarySearchFindBtn")
        self.binarySearchFindBtn.setMaximumSize(QSize(50, 16777215))
        self.binarySearchFindBtn.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
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
"    background-color: rgb(0, 115, 172);\n"
"}")

        self.verticalLayout_9.addWidget(self.binarySearchFindBtn)

        self.label_8 = QLabel(self.verticalFrame2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QSize(16777215, 50))
        font17 = QFont()
        font17.setPointSize(13)
        font17.setBold(True)
        font17.setWeight(75)
        self.label_8.setFont(font17)
        self.label_8.setStyleSheet(u"border: 1px solid white;\n"
"border-radius: 10px;")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_8)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.verticalFrame_3 = QFrame(self.verticalFrame2)
        self.verticalFrame_3.setObjectName(u"verticalFrame_3")
        self.verticalLayout_11 = QVBoxLayout(self.verticalFrame_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_10 = QLabel(self.verticalFrame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 20))
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.label_10)

        self.label_9 = QLabel(self.verticalFrame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 20))
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.label_9)

        self.label_12 = QLabel(self.verticalFrame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.label_12)

        self.checkBox = QCheckBox(self.verticalFrame_3)
        self.checkBox.setObjectName(u"checkBox")
        font18 = QFont()
        font18.setPointSize(8)
        font18.setBold(True)
        font18.setWeight(75)
        font18.setStrikeOut(False)
        self.checkBox.setFont(font18)
        self.checkBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_11.addWidget(self.checkBox)

        self.generateArrayBtn = QPushButton(self.verticalFrame_3)
        self.generateArrayBtn.setObjectName(u"generateArrayBtn")
        self.generateArrayBtn.setMaximumSize(QSize(70, 16777215))
        font19 = QFont()
        font19.setBold(False)
        font19.setWeight(50)
        self.generateArrayBtn.setFont(font19)
        self.generateArrayBtn.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    padding: 5px;\n"
"    border-radius: 15px;\n"
"	background-color: rgb(147, 164, 200);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(99, 110, 135);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(147, 164, 200);\n"
"}")

        self.verticalLayout_11.addWidget(self.generateArrayBtn)

        self.binarySearchCleanBtn = QPushButton(self.verticalFrame_3)
        self.binarySearchCleanBtn.setObjectName(u"binarySearchCleanBtn")
        self.binarySearchCleanBtn.setMaximumSize(QSize(70, 16777215))
        self.binarySearchCleanBtn.setStyleSheet(u"QPushButton {\n"
"    color: #333;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    padding: 5px;\n"
"    border-radius: 15px;\n"
"	background-color: rgb(147, 164, 200);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(99, 110, 135);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(147, 164, 200);\n"
"}")

        self.verticalLayout_11.addWidget(self.binarySearchCleanBtn)


        self.horizontalLayout_21.addWidget(self.verticalFrame_3, 0, Qt.AlignTop)

        self.verticalFrame_4 = QFrame(self.verticalFrame2)
        self.verticalFrame_4.setObjectName(u"verticalFrame_4")
        self.verticalLayout_12 = QVBoxLayout(self.verticalFrame_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lineEdit_2 = QLineEdit(self.verticalFrame_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy8.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy8)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(99, 110, 135);\n"
"border-radius: 20px;")

        self.verticalLayout_12.addWidget(self.lineEdit_2)

        self.lineEdit = QLineEdit(self.verticalFrame_4)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy8.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy8)
        self.lineEdit.setStyleSheet(u"background-color: rgb(99, 110, 135);\n"
"border-radius: 20px;")

        self.verticalLayout_12.addWidget(self.lineEdit)

        self.lineEdit_3 = QLineEdit(self.verticalFrame_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy8.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy8)
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(99, 110, 135);\n"
"border-radius: 20px;")

        self.verticalLayout_12.addWidget(self.lineEdit_3)


        self.horizontalLayout_21.addWidget(self.verticalFrame_4, 0, Qt.AlignTop)


        self.verticalLayout_9.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_12.addWidget(self.verticalFrame2, 0, Qt.AlignLeft)

        self.verticalFrame_21 = QFrame(self.page_3)
        self.verticalFrame_21.setObjectName(u"verticalFrame_21")
        sizePolicy.setHeightForWidth(self.verticalFrame_21.sizePolicy().hasHeightForWidth())
        self.verticalFrame_21.setSizePolicy(sizePolicy)
        self.verticalFrame_21.setMaximumSize(QSize(1500, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.verticalFrame_21)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit_2 = QTextEdit(self.verticalFrame_21)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy3.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy3)
        self.textEdit_2.setMinimumSize(QSize(300, 0))
        self.textEdit_2.setMaximumSize(QSize(800, 16777215))
        self.textEdit_2.setStyleSheet(u"background-color: rgb(122, 122, 122);\n"
"border-radius: 20px;")

        self.verticalLayout_10.addWidget(self.textEdit_2)


        self.horizontalLayout_12.addWidget(self.verticalFrame_21)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.textEdit = QTextEdit(self.page_3)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QSize(1000, 0))
        self.textEdit.setMaximumSize(QSize(1500, 16777215))
        self.textEdit.setStyleSheet(u"background-color: rgb(122, 122, 122);\n"
"border-radius: 20px;")

        self.horizontalLayout_19.addWidget(self.textEdit)


        self.verticalLayout_8.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_13.addLayout(self.verticalLayout_8)

        self.mainStackWidget.addWidget(self.page_3)

        self.verticalLayout_5.addWidget(self.mainStackWidget)

        self.size_Grip = QFrame(self.mainBodyContent)
        self.size_Grip.setObjectName(u"size_Grip")
        sizePolicy1.setHeightForWidth(self.size_Grip.sizePolicy().hasHeightForWidth())
        self.size_Grip.setSizePolicy(sizePolicy1)
        self.size_Grip.setMinimumSize(QSize(30, 30))
        self.size_Grip.setMaximumSize(QSize(30, 30))
        self.size_Grip.setFrameShape(QFrame.StyledPanel)
        self.size_Grip.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.size_Grip)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.size_Grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_7.addWidget(self.mainBodyContent)


        self.horizontalLayout.addWidget(self.MainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.LeftMenuContainer.raise_()
        self.MainBodyContainer.raise_()
        self.CenterMenuContainer.raise_()

        self.retranslateUi(MainWindow)

        self.leftStackedWidget.setCurrentIndex(0)
        self.mainStackWidget.setCurrentIndex(0)
        self.mmStackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Menu</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Go to main menu</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.calendarBtn.setText(QCoreApplication.translate("MainWindow", u"Calendar", None))
#if QT_CONFIG(tooltip)
        self.binarySearchBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">binary search</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.binarySearchBtn.setText(QCoreApplication.translate("MainWindow", u"Binary search", None))
#if QT_CONFIG(shortcut)
        self.binarySearchBtn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.wordGBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">word guessing game</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.wordGBtn.setText(QCoreApplication.translate("MainWindow", u"Word GG", None))
#if QT_CONFIG(tooltip)
        self.recorderBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">record voice</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.recorderBtn.setText(QCoreApplication.translate("MainWindow", u"Voice recorder", None))
#if QT_CONFIG(tooltip)
        self.colorGameBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">match the colors</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.colorGameBtn.setText(QCoreApplication.translate("MainWindow", u"Color matching", None))
#if QT_CONFIG(tooltip)
        self.whatsappBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">send messages automatically</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.whatsappBtn.setText(QCoreApplication.translate("MainWindow", u"Whatsapp bot", None))
#if QT_CONFIG(tooltip)
        self.informationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">About the app</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.informationBtn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Get more help</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"More menu", None))
        self.closecentermenuBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Coming soon...", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Coming soon...", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Welcome to App Center", None))
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffff00;\">Minimize</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#53f900;\">Maximize-Restore</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ff0000;\">Close</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Notes App", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"This app is going to help you manage to manage your notes and events.", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Binary Search App", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"You can learn what is Binary Search and practise to know how does it work", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Whatsapp Bot App", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Create your contacts and send them messages you want", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Word Guessing Game App", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Guess the secret word and have fun", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Voice Recorder App", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"You can record your voice using this app. Your file will be appear on your desktop", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Color Matching App", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Match the colors and win the game", None))
        self.previousNavBtn.setText("")
        self.calendarAppBtn.setText("")
        self.binarySearchAppBtn.setText("")
        self.whatsappBotApp.setText("")
        self.wordGuessingGameBtn.setText("")
        self.voiceRecorderApp.setText("")
        self.colorMatchingGameBtn.setText("")
        self.nextNavBtn.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Find the secret word", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.revealBtn.setText(QCoreApplication.translate("MainWindow", u"Reveal the word", None))
        self.checkGuessBtn.setText(QCoreApplication.translate("MainWindow", u"Check the guess", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.pushButton_7.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"+99450xxxxxxx", None))
        self.checkBox_2.setText("")
        self.sendMessageBtn.setText("")
        self.deleteTextBtn.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Create new contact", None))
        self.addContactBtn.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Name: ", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Number: ", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Now", None))
        self.pushButton_2.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"No note here!", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Your note:", None))
        self.addNoteBtn.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Click start button to start recording.", None))
        self.pushButton.setText("")
        self.pushButton_3.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Secret color appears here.", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Remaining time appears here.", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Your scores appear here.", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Correct: 0", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Wrong: 0", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Available color variants appear here.", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"You can adjust difficulty level here:", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Easy", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Hard", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Start Game", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Number you want to find", None))
        self.binarySearchFindBtn.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Generate an array", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Step count", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Allow randomness", None))
        self.generateArrayBtn.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.binarySearchCleanBtn.setText(QCoreApplication.translate("MainWindow", u"Clean", None))
    # retranslateUi

