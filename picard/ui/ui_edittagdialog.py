# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/edittagdialog.ui'
#
# Created: Fri Nov  8 17:04:27 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_EditTagDialog(object):
    def setupUi(self, EditTagDialog):
        EditTagDialog.setObjectName(_fromUtf8("EditTagDialog"))
        EditTagDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        EditTagDialog.resize(400, 250)
        EditTagDialog.setFocusPolicy(QtCore.Qt.StrongFocus)
        EditTagDialog.setModal(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(EditTagDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tag_names = QtGui.QComboBox(EditTagDialog)
        self.tag_names.setEditable(True)
        self.tag_names.setObjectName(_fromUtf8("tag_names"))
        self.verticalLayout_2.addWidget(self.tag_names)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.value_list = QtGui.QListWidget(EditTagDialog)
        self.value_list.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.value_list.setTabKeyNavigation(False)
        self.value_list.setProperty("showDropIndicator", False)
        self.value_list.setObjectName(_fromUtf8("value_list"))
        self.horizontalLayout.addWidget(self.value_list)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.edit_value = QtGui.QPushButton(EditTagDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_value.sizePolicy().hasHeightForWidth())
        self.edit_value.setSizePolicy(sizePolicy)
        self.edit_value.setMinimumSize(QtCore.QSize(100, 0))
        self.edit_value.setAutoDefault(False)
        self.edit_value.setObjectName(_fromUtf8("edit_value"))
        self.verticalLayout.addWidget(self.edit_value)
        self.add_value = QtGui.QPushButton(EditTagDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_value.sizePolicy().hasHeightForWidth())
        self.add_value.setSizePolicy(sizePolicy)
        self.add_value.setMinimumSize(QtCore.QSize(100, 0))
        self.add_value.setAutoDefault(False)
        self.add_value.setObjectName(_fromUtf8("add_value"))
        self.verticalLayout.addWidget(self.add_value)
        self.remove_value = QtGui.QPushButton(EditTagDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(120)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_value.sizePolicy().hasHeightForWidth())
        self.remove_value.setSizePolicy(sizePolicy)
        self.remove_value.setMinimumSize(QtCore.QSize(120, 0))
        self.remove_value.setAutoDefault(False)
        self.remove_value.setObjectName(_fromUtf8("remove_value"))
        self.verticalLayout.addWidget(self.remove_value)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.buttonbox = QtGui.QDialogButtonBox(EditTagDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonbox.sizePolicy().hasHeightForWidth())
        self.buttonbox.setSizePolicy(sizePolicy)
        self.buttonbox.setMinimumSize(QtCore.QSize(150, 0))
        self.buttonbox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonbox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonbox.setObjectName(_fromUtf8("buttonbox"))
        self.verticalLayout_2.addWidget(self.buttonbox)

        self.retranslateUi(EditTagDialog)
        QtCore.QObject.connect(self.buttonbox, QtCore.SIGNAL(_fromUtf8("accepted()")), EditTagDialog.accept)
        QtCore.QObject.connect(self.buttonbox, QtCore.SIGNAL(_fromUtf8("rejected()")), EditTagDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditTagDialog)

    def retranslateUi(self, EditTagDialog):
        EditTagDialog.setWindowTitle(_("Edit Tag"))
        self.edit_value.setText(_("Edit value"))
        self.add_value.setText(_("Add value"))
        self.remove_value.setText(_("Remove value"))

