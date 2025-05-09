# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uwsift/ui/open_file_wizard.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_openFileWizard(object):
    def setupUi(self, openFileWizard):
        openFileWizard.setObjectName("openFileWizard")
        openFileWizard.resize(1100, 800)
        openFileWizard.setSizeGripEnabled(True)
        openFileWizard.setModal(True)
        openFileWizard.setWizardStyle(QtWidgets.QWizard.ModernStyle)
        openFileWizard.setOptions(QtWidgets.QWizard.CancelButtonOnLeft)
        openFileWizard.setTitleFormat(QtCore.Qt.AutoText)
        openFileWizard.setSubTitleFormat(QtCore.Qt.AutoText)
        self.fileSelectionPage = InitiallyIncompleteWizardPage()
        self.fileSelectionPage.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fileSelectionPage.setObjectName("fileSelectionPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fileSelectionPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.filterPatternLabel = QtWidgets.QLabel(self.fileSelectionPage)
        self.filterPatternLabel.setObjectName("filterPatternLabel")
        self.gridLayout.addWidget(self.filterPatternLabel, 1, 0, 1, 1)
        self.folderLabel = QtWidgets.QLabel(self.fileSelectionPage)
        self.folderLabel.setObjectName("folderLabel")
        self.gridLayout.addWidget(self.folderLabel, 2, 0, 1, 1)
        self.folderTextBox = QtWidgets.QLineEdit(self.fileSelectionPage)
        self.folderTextBox.setText("")
        self.folderTextBox.setObjectName("folderTextBox")
        self.gridLayout.addWidget(self.folderTextBox, 2, 1, 1, 1)
        self.filterPatternComboBox = QtWidgets.QComboBox(self.fileSelectionPage)
        self.filterPatternComboBox.setEditable(True)
        self.filterPatternComboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.filterPatternComboBox.setMinimumContentsLength(150)
        self.filterPatternComboBox.setObjectName("filterPatternComboBox")
        self.gridLayout.addWidget(self.filterPatternComboBox, 1, 1, 1, 2)
        self.readerLabel = QtWidgets.QLabel(self.fileSelectionPage)
        self.readerLabel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.readerLabel.setObjectName("readerLabel")
        self.gridLayout.addWidget(self.readerLabel, 0, 0, 1, 1)
        self.readerComboBox = QtWidgets.QComboBox(self.fileSelectionPage)
        self.readerComboBox.setObjectName("readerComboBox")
        self.gridLayout.addWidget(self.readerComboBox, 0, 1, 1, 2)
        self.selectFolderButton = QtWidgets.QPushButton(self.fileSelectionPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectFolderButton.sizePolicy().hasHeightForWidth())
        self.selectFolderButton.setSizePolicy(sizePolicy)
        self.selectFolderButton.setCheckable(False)
        self.selectFolderButton.setObjectName("selectFolderButton")
        self.gridLayout.addWidget(self.selectFolderButton, 2, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.fileTable = QtWidgets.QTableWidget(self.fileSelectionPage)
        self.fileTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.fileTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.fileTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.fileTable.setObjectName("fileTable")
        self.fileTable.setColumnCount(0)
        self.fileTable.setRowCount(0)
        self.fileTable.horizontalHeader().setMinimumSectionSize(20)
        self.fileTable.verticalHeader().setDefaultSectionSize(14)
        self.fileTable.verticalHeader().setMinimumSectionSize(14)
        self.verticalLayout_2.addWidget(self.fileTable)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.statusMessage = QtWidgets.QLabel(self.fileSelectionPage)
        self.statusMessage.setMinimumSize(QtCore.QSize(400, 0))
        self.statusMessage.setText("")
        self.statusMessage.setObjectName("statusMessage")
        self.horizontalLayout.addWidget(self.statusMessage)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.groupingModeLabel = QtWidgets.QLabel(self.fileSelectionPage)
        self.groupingModeLabel.setObjectName("groupingModeLabel")
        self.horizontalLayout.addWidget(self.groupingModeLabel)
        self.groupingModeComboBox = QtWidgets.QComboBox(self.fileSelectionPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupingModeComboBox.sizePolicy().hasHeightForWidth())
        self.groupingModeComboBox.setSizePolicy(sizePolicy)
        self.groupingModeComboBox.setObjectName("groupingModeComboBox")
        self.groupingModeComboBox.addItem("")
        self.groupingModeComboBox.addItem("")
        self.groupingModeComboBox.addItem("")
        self.horizontalLayout.addWidget(self.groupingModeComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        openFileWizard.addPage(self.fileSelectionPage)
        self.productSelectionPage = InitiallyIncompleteWizardPage()
        self.productSelectionPage.setObjectName("productSelectionPage")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.productSelectionPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.productSelectionButtonLayout = QtWidgets.QHBoxLayout()
        self.productSelectionButtonLayout.setObjectName("productSelectionButtonLayout")
        self.selectAllButton = QtWidgets.QPushButton(self.productSelectionPage)
        self.selectAllButton.setObjectName("selectAllButton")
        self.productSelectionButtonLayout.addWidget(self.selectAllButton)
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.productSelectionButtonLayout.addItem(spacerItem1)
        self.resamplingMethodLabel = QtWidgets.QLabel(self.productSelectionPage)
        self.resamplingMethodLabel.setObjectName("resamplingMethodLabel")
        self.productSelectionButtonLayout.addWidget(self.resamplingMethodLabel)
        self.resamplingMethodComboBox = QtWidgets.QComboBox(self.productSelectionPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resamplingMethodComboBox.sizePolicy().hasHeightForWidth())
        self.resamplingMethodComboBox.setSizePolicy(sizePolicy)
        self.resamplingMethodComboBox.setSizeIncrement(QtCore.QSize(1, 0))
        self.resamplingMethodComboBox.setObjectName("resamplingMethodComboBox")
        self.productSelectionButtonLayout.addWidget(self.resamplingMethodComboBox)
        self.radiusOfInfluenceLabel = QtWidgets.QLabel(self.productSelectionPage)
        self.radiusOfInfluenceLabel.setObjectName("radiusOfInfluenceLabel")
        self.productSelectionButtonLayout.addWidget(self.radiusOfInfluenceLabel)
        self.radiusOfInfluenceSpinBox = QtWidgets.QSpinBox(self.productSelectionPage)
        self.radiusOfInfluenceSpinBox.setMinimum(100)
        self.radiusOfInfluenceSpinBox.setMaximum(10000000)
        self.radiusOfInfluenceSpinBox.setSingleStep(100)
        self.radiusOfInfluenceSpinBox.setProperty("value", 5000)
        self.radiusOfInfluenceSpinBox.setObjectName("radiusOfInfluenceSpinBox")
        self.productSelectionButtonLayout.addWidget(self.radiusOfInfluenceSpinBox)
        self.projectionLabel = QtWidgets.QLabel(self.productSelectionPage)
        self.projectionLabel.setObjectName("projectionLabel")
        self.productSelectionButtonLayout.addWidget(self.projectionLabel)
        self.projectionComboBox = QtWidgets.QComboBox(self.productSelectionPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectionComboBox.sizePolicy().hasHeightForWidth())
        self.projectionComboBox.setSizePolicy(sizePolicy)
        self.projectionComboBox.setSizeIncrement(QtCore.QSize(1, 0))
        self.projectionComboBox.setObjectName("projectionComboBox")
        self.productSelectionButtonLayout.addWidget(self.projectionComboBox)
        self.resolutionLabel = QtWidgets.QLabel(self.productSelectionPage)
        self.resolutionLabel.setObjectName("resolutionLabel")
        self.productSelectionButtonLayout.addWidget(self.resolutionLabel)
        self.resolutionComboBox = QtWidgets.QComboBox(self.productSelectionPage)
        sizePolicy1 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.resolutionComboBox.sizePolicy().hasHeightForWidth())
        self.resolutionComboBox.setSizePolicy(sizePolicy1)
        self.resolutionComboBox.setSizeIncrement(QtCore.QSize(1, 0))
        self.resolutionComboBox.setObjectName("resolutionComboBox")
        self.productSelectionButtonLayout.addWidget(self.resolutionComboBox)

        #

        self.resamplingShapeLabel = QtWidgets.QLabel(self.productSelectionPage)
        self.resamplingShapeLabel.setObjectName("resamplingShapeLabel")
        self.productSelectionButtonLayout.addWidget(self.resamplingShapeLabel)
        self.resamplingShapeRowSpinBox = QtWidgets.QSpinBox(self.productSelectionPage)
        self.resamplingShapeRowSpinBox.setMinimum(1)
        self.resamplingShapeRowSpinBox.setMaximum(100000)
        self.resamplingShapeRowSpinBox.setProperty("value", 1000)
        self.resamplingShapeRowSpinBox.setObjectName("resamplingShapeRowSpinBox")
        self.productSelectionButtonLayout.addWidget(self.resamplingShapeRowSpinBox)
        self.resamplingShapeColumnSpinBox = QtWidgets.QSpinBox(self.productSelectionPage)
        self.resamplingShapeColumnSpinBox.setMinimum(1)
        self.resamplingShapeColumnSpinBox.setMaximum(100000)
        self.resamplingShapeColumnSpinBox.setProperty("value", 1000)
        self.resamplingShapeColumnSpinBox.setObjectName("resamplingShapeColumnSpinBox")
        self.productSelectionButtonLayout.addWidget(self.resamplingShapeColumnSpinBox)
        self.verticalLayout.addLayout(self.productSelectionButtonLayout)
        self.selectIDTable = QtWidgets.QTableWidget(self.productSelectionPage)
        self.selectIDTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.selectIDTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.selectIDTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.selectIDTable.setObjectName("selectIDTable")
        self.selectIDTable.setColumnCount(0)
        self.selectIDTable.setRowCount(0)
        self.selectIDTable.horizontalHeader().setMinimumSectionSize(20)
        self.selectIDTable.verticalHeader().setDefaultSectionSize(14)
        self.selectIDTable.verticalHeader().setMinimumSectionSize(14)
        self.verticalLayout.addWidget(self.selectIDTable)
        openFileWizard.addPage(self.productSelectionPage)

        self.retranslateUi(openFileWizard)
        QtCore.QMetaObject.connectSlotsByName(openFileWizard)
        openFileWizard.setTabOrder(self.readerComboBox, self.filterPatternComboBox)
        openFileWizard.setTabOrder(self.filterPatternComboBox, self.folderTextBox)
        openFileWizard.setTabOrder(self.folderTextBox, self.selectFolderButton)
        openFileWizard.setTabOrder(self.selectFolderButton, self.fileTable)
        openFileWizard.setTabOrder(self.fileTable, self.selectAllButton)
        openFileWizard.setTabOrder(self.selectAllButton, self.selectIDTable)

    def retranslateUi(self, openFileWizard):
        _translate = QtCore.QCoreApplication.translate
        openFileWizard.setWindowTitle(_translate("openFileWizard", "Open File Wizard"))
        self.fileSelectionPage.setTitle(_translate("openFileWizard", "Select Files to Open"))
        self.fileSelectionPage.setSubTitle(
            _translate(
                "openFileWizard",
                "Select reader & folder. Click column headers to sort files. Click'n'drag with mouse for easier row selection. Hold control key to extend selection. Use filter combo-box to choose from predefined patterns or write your own.",
            )
        )
        self.filterPatternLabel.setText(_translate("openFileWizard", "Filter:"))
        self.folderLabel.setText(_translate("openFileWizard", "Folder:"))
        self.readerLabel.setText(_translate("openFileWizard", "Reader:"))
        self.selectFolderButton.setToolTip(_translate("openFileWizard", "Add files/dirs to list"))
        self.selectFolderButton.setText(_translate("openFileWizard", "..."))
        self.fileTable.setSortingEnabled(True)
        self.groupingModeLabel.setText(_translate("openFileWizard", "Grouping:"))
        self.groupingModeComboBox.setItemText(0, _translate("openFileWizard", "By Group Keys"))
        self.groupingModeComboBox.setItemText(1, _translate("openFileWizard", "Keep Separate"))
        self.groupingModeComboBox.setItemText(2, _translate("openFileWizard", "Merge All"))
        self.productSelectionPage.setTitle(_translate("openFileWizard", "Select Products"))
        self.productSelectionPage.setSubTitle(_translate("openFileWizard", "Select products to add"))
        self.selectAllButton.setText(_translate("openFileWizard", "Select/Deselect All"))
        self.resamplingMethodLabel.setText(_translate("openFileWizard", "Resampling Method:"))
        self.radiusOfInfluenceLabel.setText(_translate("openFileWizard", "Radius of Influence:"))
        self.radiusOfInfluenceSpinBox.setSuffix(_translate("openFileWizard", " m"))
        self.projectionLabel.setText(_translate("openFileWizard", "Projection:"))
        self.resolutionLabel.setText(_translate("openFileWizard", "Resolution:"))
        self.resamplingShapeLabel.setText(_translate("openFileWizard", "Shape:"))
        self.selectIDTable.setSortingEnabled(True)


from uwsift.ui.custom_widgets import InitiallyIncompleteWizardPage
