from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(296, 392)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(296, 392))
        Dialog.setMaximumSize(QtCore.QSize(296, 9990))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(3, 0, 3, 3)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_3.setContentsMargins(0, 10, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame_6)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.gridLayout_3.addWidget(self.frame_3, 1, 1, 1, 1)
        # self.frame_2 = QtWidgets.QFrame(self.frame_6)
        # self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_2.setObjectName("frame_2")
        # self.verticalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        # self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        # self.verticalLayout.setSpacing(0)
        # self.verticalLayout.setObjectName("verticalLayout")
        # self.label = QtWidgets.QLabel(self.frame_2)
        # self.label.setObjectName("label")
        # self.verticalLayout.addWidget(self.label)
        # self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.gridLayout.addWidget(self.frame, 3, 0, 1, 1)
        self.frame_8 = QtWidgets.QFrame(Dialog)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_8.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.frame_8)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_8.addWidget(self.pushButton)
        self.gridLayout.addWidget(self.frame_8, 5, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(Dialog)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 2)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 5, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)
        # self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)

        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(70)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tableWidget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_2.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setTabKeyNavigation(False)
        self.tableWidget_2.setProperty("showDropIndicator", False)
        self.tableWidget_2.setDragDropOverwriteMode(False)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(0, 0, item)
        self.tableWidget_2.setDisabled(True)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(0, 2, item)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(70)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget_2, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sequential Auction"))
        self.pushButton_3.setText(_translate("Dialog", "New Game"))
        self.pushButton.setText(_translate("Dialog", "Start Game"))
        self.label_4.setText(_translate("Dialog", "Round Left: "))
        self.label_8.setText(_translate("Dialog", "0"))
        # self.label_6.setText(_translate("Dialog", "0"))
        # self.label_5.setText(_translate("Dialog", "Shares: "))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Player"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Score"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Budget"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Dialog", "You"))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Dialog", "0"))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Dialog", "0"))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Player"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Score"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Budget"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("Dialog", "You"))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item = self.tableWidget_2.item(0, 1)
        item.setText(_translate("Dialog", "0"))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item = self.tableWidget_2.item(0, 2)
        item.setText(_translate("Dialog", "0"))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)

        #disable start button
        self.pushButton.setEnabled(False)

        #disable lineEdit
        self.lineEdit_2.setEnabled(False)

        #set button to non-default
        self.pushButton.setDefault(False)
        self.pushButton_3.setDefault(False)

        #prevent the focus from being on the buttons
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.NoFocus)

        #prevent the focus from being on the table
        self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_2.setFocusPolicy(QtCore.Qt.NoFocus)
        
        #connect the buttons
        self.pushButton.clicked.connect(startGame)
        self.pushButton_3.clicked.connect(PopupBox)
        self.lineEdit_2.returnPressed.connect(lineEntered)

        #change the width of table cells
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 120)
        self.tableWidget.setColumnWidth(2, 120)
        self.tableWidget_2.setColumnWidth(0, 50)
        self.tableWidget_2.setColumnWidth(1, 120)
        self.tableWidget_2.setColumnWidth(2, 120)

        #set header to be unclickable
        self.tableWidget.horizontalHeader().setSectionsClickable(False)

        #set the width of the table to be unchangable
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)

        #double clicking the table cells edits the cell
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)

        #create second window
        self.popup = QtWidgets.QWidget()
        self.ui2 = Ui_Form2()
        self.ui2.setupUi(self.popup)
        
class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(174, 91)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(174, 91))
        Form.setMaximumSize(QtCore.QSize(174, 91))
        Form.setWindowTitle(".")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(20, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.spinBox_2 = QtWidgets.QSpinBox(self.frame)
        self.spinBox_2.setMinimumSize(QtCore.QSize(60, 0))
        self.spinBox_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout.addWidget(self.spinBox_2)
        self.spinBox_5 = QtWidgets.QSpinBox(self.frame)
        self.spinBox_5.setMinimumSize(QtCore.QSize(60, 0))
        self.spinBox_5.setMaximumSize(QtCore.QSize(60, 16777215))
        self.spinBox_5.setObjectName("spinBox_5")
        self.verticalLayout.addWidget(self.spinBox_5)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Rounds:"))
        self.label_2.setText(_translate("Form", "Players:"))

        self.spinBox_2.setValue(10)
        self.spinBox_5.setValue(5)

        self.buttonBox.accepted.connect(popup_accept)
        self.buttonBox.rejected.connect(popup_reject)
        
def popup_accept():
    # get the values from the spinboxes
    _rounds = ui.ui2.spinBox_2.value()
    _players = ui.ui2.spinBox_5.value()

    # if the values are invalid, display error message
    if (_rounds < 0 or _players < 0):
        setErrorMessage("Negative values are not allowed.")
    elif(_rounds < 1):
        setErrorMessage("There must be at least one round.")
    elif (_players < 2):
        setErrorMessage("There must be at least two players.")
    else:
        ui.popup.close()
        setErrorMessage("")
        newGame(_rounds, _players)

def popup_reject():
    ui.popup.close()

def PopupBox():
    ui.popup.show()

def setRoundsLeft(rounds):
    ui.label_8.setText(QtCore.QCoreApplication.translate("Dialog", str(rounds)))

def setErrorMessage(message):
    ui.label_7.setStyleSheet("color: rgb(255, 85, 0);")
    ui.label_7.setText(QtCore.QCoreApplication.translate("Dialog", message))

def setMessage(message):
    ui.label_7.setStyleSheet("color: rgb(0, 0, 0);")
    ui.label_7.setText(QtCore.QCoreApplication.translate("Dialog", message))

#------------------------------------------------------------------------------

import random

class Game:
    def __init__(self, _rounds, _players):
        self.total_rounds = _rounds
        self.rounds = _rounds
        # sorted every round, from highest score to the lowest score
        self.rank = [Player(i) for i in range(_players)]
        # simply sorted from lowest index to highest index
        self.players = [Player(i) for i in range(_players)]
        self.you_index = 0
        
    def start(self):
        # create a list of integers from 0 to len(rank) - 1, and shuffle it
        index_list = [i for i in range(len(self.players))]
        random.shuffle(index_list)
        self.you_index = index_list[0]
        count = 0
        for i in index_list:
            _player = self.players[i]
            _player.index = i
            _player.score = float(ui.tableWidget.item(count, 1).text())
            _player.balance = float(ui.tableWidget.item(count, 2).text())
            _player.initial_balance = _player.balance
            count += 1
        self.rank = self.players.copy()
        self.rank.sort(reverse=True)
        self.updateDisplay()

    def play_round(self, _your_bid):
        round_winner_index = -1
        round_winner_bid = -1
        for _player in self.players:
            player_bid = _player.bid()
            if _player.index == self.you_index:
                player_bid = _your_bid
            if player_bid > round_winner_bid:
                round_winner_index = _player.index
                round_winner_bid = player_bid
            print("Player {} bid {}".format(_player.index, player_bid))
            
        self.players[round_winner_index].add_score()
        self.players[round_winner_index].deduct_money(round_winner_bid)
        self.rank.sort(reverse=True)
        self.updateDisplay()
        if round_winner_index == self.you_index:
            setMessage(f"You won this round!")
        else:
            setMessage("You got nothing this round.")

        self.rounds -= 1
        setRoundsLeft(self.rounds)
        if self.rounds == 0:
            self.end_game()
            return
        
    def end_game(self):
        # get the indices of the players with the highest score
        highest_score = self.rank[0].score
        highest_score_indices = []
        for _player in self.rank:
            if _player.score == highest_score:
                highest_score_indices.append(_player.index)
            else:
                break
        indices = [str(i + 1) for i in highest_score_indices]
        indices.sort()
        if len(highest_score_indices) == 1 and game.you_index in highest_score_indices:
            setMessage("You won!")
        elif game.you_index in highest_score_indices and len(highest_score_indices) > 1:
            setMessage("You tied with player " + ", ".join(indices))
        else:
            setMessage("You lost to player " + ", ".join(indices))

        #disable lineEdit
        ui.lineEdit_2.setEnabled(False)
        ui.label_2.setText("")
        ui.label_2.setEnabled(False)

    def get_score_sum(self):
        return sum([_player.score for _player in self.players])

    def get_balance_sum(self):
        return sum([_player.balance for _player in self.players])

    # requirements: rank list must be ordered before calling this function
    def updateDisplay(self):
        your_index = self.you_index
        count = 0
        for _player in self.rank:
            i = _player.index
            if i == your_index:
                
                ui.tableWidget.item(count, 0).setText("You")
                # make the text bold
                font = QtGui.QFont()
                font.setBold(True)
                ui.tableWidget.item(count, 0).setFont(font)
                ui.tableWidget.item(count, 1).setText(str(_player.score))
                ui.tableWidget.item(count, 2).setText(str(_player.balance))
                ui.tableWidget_2.item(0, 1).setText(str(_player.score))
                ui.tableWidget_2.item(0, 2).setText(str(_player.balance))
            else:
                ui.tableWidget.item(count, 0).setText("Player " + str(i + 1))
                font = QtGui.QFont()
                font.setBold(False)
                ui.tableWidget.item(count, 0).setFont(font)
                ui.tableWidget.item(count, 1).setText(str(_player.score))
                ui.tableWidget.item(count, 2).setText(str(_player.balance))
            count += 1


class Player:
    def __init__(self, index, _strategy = 'N'):
        self.initial_balance = 0
        self.balance = 0
        self.score = 0
        self.index = index
        self.strategy = _strategy

    def bid(self):
        if self.strategy == 'Y':
            return strategy_YOLO(self.balance, self.initial_balance)
        elif self.strategy == 'N':
            return strategy_Nash(self.balance, self.initial_balance)

    def deduct_money(self, _cost):
        self.balance -= _cost

    def set_player_score(self, _amount):
        self.score = _amount

    def add_score(self):
        self.score += 1

    def __repr__(self):
        return f'Player {self.index} has {self.balance} dollars and has {self.score} candies'
    
    # create a comparison function between player with the following order: score, balance, index
    def __lt__(self, other):
        if self.score != other.score:
            return self.score < other.score
        elif self.balance != other.balance:
            return self.balance < other.balance
        else:
            return self.index > other.index
    
    def __sort__(self, other):
        if self.score != other.score:
            return self.score > other.score
        elif self.balance != other.balance:
            return self.balance > other.balance
        else:
            return self.index < other.index

def lineEntered():
    #get the text from the lineEdit, clear the line. If the text is not a number or empty, display error message.
    bid = -1
    try:
        text2 = ui.lineEdit_2.text()
        if(text2 == ""):
            raise Exception
        bid = eval(text2)
        if(bid < 0):
            raise Exception
        ui.lineEdit_2.clear()
        setErrorMessage("")
    except:
        setErrorMessage("Invalid Input")
        return

    if bid > game.players[game.you_index].balance:
        setErrorMessage("You cannot spend more than your balance")
        return
    
    game.play_round(bid)
    


def strategy_YOLO(current_balance, initial_balance):
    _bid = current_balance
    return _bid

def strategy_Nash(current_balance, initial_balance):
    player_num = len(game.players)
    total_rounds = game.total_rounds
    _bid = initial_balance * (player_num / total_rounds)
    if _bid > current_balance:
        _bid = current_balance
    return _bid


global game

def checkTableValid():
    for i in range(ui.tableWidget.rowCount()):
        score_text = ui.tableWidget.item(i, 1).text()
        balance_text = ui.tableWidget.item(i, 2).text()
        if score_text == "" or balance_text == "":
            return False
        try:
            _dummy_score = float(score_text)
            _dummy_balance = float(balance_text)
            if _dummy_score < 0 or _dummy_balance < 0:
                return False
        except:
            return False
    return True

# newGame Button is clicked
def newGame(_rounds, _players):

    setRoundsLeft(_rounds)

    global game 
    game = Game(_rounds, _players)

    #set the table to have the correct number of rows
    ui.tableWidget.setRowCount(_players)
    for i in range(_players):
        if i == 0:
            ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem("You"))
        else:
            ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem("Bot"))
        # set the items to be uneditable
        ui.tableWidget.item(i, 0).setFlags(QtCore.Qt.ItemIsEnabled)
        ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem("0"))
        ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem("60"))

        #set text align to center
        ui.tableWidget.item(i, 0).setTextAlignment(QtCore.Qt.AlignCenter)
        ui.tableWidget.item(i, 1).setTextAlignment(QtCore.Qt.AlignCenter)
        ui.tableWidget.item(i, 2).setTextAlignment(QtCore.Qt.AlignCenter)

    ui.tableWidget_2.item(0, 1).setText("0")
    ui.tableWidget_2.item(0, 2).setText("60")

    # enable start button
    ui.pushButton.setEnabled(True)
    # disable lineEdit
    ui.lineEdit_2.setEnabled(False)
    ui.label_2.setText("")


    
def startGame():

    # check if the table is valid
    if not checkTableValid():
        setErrorMessage("Invalid Table")
        return
    game.start()
    #disable start button
    ui.pushButton.setEnabled(False)
    #enable lineEdit
    ui.lineEdit_2.setEnabled(True)
    ui.label_2.setText("Enter your bid: ")

    setMessage("Your index is " + str(game.you_index + 1) + ". Enter your bid and amount to buy.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
