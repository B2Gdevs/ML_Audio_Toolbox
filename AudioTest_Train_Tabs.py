# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AudioTest_Train_Tabs.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from pyAudioAnalysis import audioTrainTest as aT
from pyAudioAnalysis import audioFeatureExtraction
from pyAudioAnalysis import audioBasicIO
#import matplotlib.pyplot as plt
import numpy

import os

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(812, 547)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Frame)
        self.tabWidget.setObjectName("tabWidget")
        self.TensorFlow_Audio = QtWidgets.QWidget()
        self.TensorFlow_Audio.setObjectName("TensorFlow_Audio")
        self.tabWidget.addTab(self.TensorFlow_Audio, "")
        self.Kit_Test_Audio = QtWidgets.QWidget()
        self.Kit_Test_Audio.setObjectName("Kit_Test_Audio")
        self.tabWidget.addTab(self.Kit_Test_Audio, "")
        self.QuickAudio = QtWidgets.QWidget()
        self.QuickAudio.setObjectName("QuickAudio")
        self.gridLayout = QtWidgets.QGridLayout(self.QuickAudio)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(self.QuickAudio)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.QuickAudio)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_6)
        self.Quick_Train_Train_RootFolderButton = QtWidgets.QToolButton(self.frame_2)
        self.Quick_Train_Train_RootFolderButton.setObjectName("Quick_Train_Train_RootFolderButton")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Quick_Train_Train_RootFolderButton)
        self.Quick_Train_RootFolderName = QtWidgets.QLineEdit(self.frame_2)
        self.Quick_Train_RootFolderName.setObjectName("Quick_Train_RootFolderName")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Quick_Train_RootFolderName)
        self.Quick_Train_TrainButton = QtWidgets.QPushButton(self.frame_2)
        self.Quick_Train_TrainButton.setObjectName("Quick_Train_TrainButton")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Quick_Train_TrainButton)
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_14)
        self.gridLayout.addWidget(self.frame_2, 2, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.QuickAudio)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame_4)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_9)
        self.Quick_Train_TestFolderButton = QtWidgets.QToolButton(self.frame_4)
        self.Quick_Train_TestFolderButton.setObjectName("Quick_Train_TestFolderButton")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Quick_Train_TestFolderButton)
        self.Quick_Train_TestFolder = QtWidgets.QLineEdit(self.frame_4)
        self.Quick_Train_TestFolder.setObjectName("Quick_Train_TestFolder")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Quick_Train_TestFolder)
        self.Quick_Train_TestButton = QtWidgets.QPushButton(self.frame_4)
        self.Quick_Train_TestButton.setObjectName("Quick_Train_TestButton")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Quick_Train_TestButton)
        self.gridLayout.addWidget(self.frame_4, 4, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.QuickAudio)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.QuickAudio)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.formLayout = QtWidgets.QFormLayout(self.frame_3)
        self.formLayout.setObjectName("formLayout")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.Quick_Train_ModelFileButton = QtWidgets.QToolButton(self.frame_3)
        self.Quick_Train_ModelFileButton.setObjectName("Quick_Train_ModelFileButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Quick_Train_ModelFileButton)
        self.Quick_Train_TestClassifier = QtWidgets.QComboBox(self.frame_3)
        self.Quick_Train_TestClassifier.setObjectName("Quick_Train_TestClassifier")
        self.Quick_Train_TestClassifier.addItem("")
        self.Quick_Train_TestClassifier.addItem("")
        self.Quick_Train_TestClassifier.addItem("")
        self.Quick_Train_TestClassifier.addItem("")
        self.Quick_Train_TestClassifier.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Quick_Train_TestClassifier)
        self.Quick_Train_TestModelPath = QtWidgets.QLineEdit(self.frame_3)
        self.Quick_Train_TestModelPath.setObjectName("Quick_Train_TestModelPath")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Quick_Train_TestModelPath)
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_8)
        self.gridLayout.addWidget(self.frame_3, 4, 0, 1, 1, QtCore.Qt.AlignTop)
        self.label_7 = QtWidgets.QLabel(self.QuickAudio)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.QuickAudio)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.Quick_Train_Window = QtWidgets.QLineEdit(self.frame)
        self.Quick_Train_Window.setObjectName("Quick_Train_Window")
        self.gridLayout_2.addWidget(self.Quick_Train_Window, 2, 1, 1, 1)
        self.Quick_Train_ModelName = QtWidgets.QLineEdit(self.frame)
        self.Quick_Train_ModelName.setObjectName("Quick_Train_ModelName")
        self.gridLayout_2.addWidget(self.Quick_Train_ModelName, 5, 1, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 6, 0, 1, 1)
        self.Quick_Train_BeatBoolean = QtWidgets.QCheckBox(self.frame)
        self.Quick_Train_BeatBoolean.setText("")
        self.Quick_Train_BeatBoolean.setObjectName("Quick_Train_BeatBoolean")
        self.gridLayout_2.addWidget(self.Quick_Train_BeatBoolean, 6, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 2)
        self.Quick_Train_Step = QtWidgets.QLineEdit(self.frame)
        self.Quick_Train_Step.setObjectName("Quick_Train_Step")
        self.gridLayout_2.addWidget(self.Quick_Train_Step, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.Quick_Train_TrainClassifier = QtWidgets.QComboBox(self.frame)
        self.Quick_Train_TrainClassifier.setObjectName("Quick_Train_TrainClassifier")
        self.Quick_Train_TrainClassifier.addItem("")
        self.Quick_Train_TrainClassifier.addItem("")
        self.Quick_Train_TrainClassifier.addItem("")
        self.Quick_Train_TrainClassifier.addItem("")
        self.Quick_Train_TrainClassifier.addItem("")
        self.gridLayout_2.addWidget(self.Quick_Train_TrainClassifier, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)
        self.tabWidget.addTab(self.QuickAudio, "")
        self.Audio_Feature_Extraction = QtWidgets.QWidget()
        self.Audio_Feature_Extraction.setObjectName("Audio_Feature_Extraction")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Audio_Feature_Extraction)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.Audio_Feature_Extraction)
        self.frame_5.setMaximumSize(QtCore.QSize(353, 481))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.formLayout_4 = QtWidgets.QFormLayout(self.frame_5)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_18 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_18)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_4.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.label_16 = QtWidgets.QLabel(self.frame_5)
        self.label_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.Audio_Feature_Extraction_SingleFileWindowTerm = QtWidgets.QComboBox(self.frame_5)
        self.Audio_Feature_Extraction_SingleFileWindowTerm.setObjectName("Audio_Feature_Extraction_SingleFileWindowTerm")
        self.Audio_Feature_Extraction_SingleFileWindowTerm.addItem("")
        self.Audio_Feature_Extraction_SingleFileWindowTerm.addItem("")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.Audio_Feature_Extraction_SingleFileWindowTerm)
        self.label_20 = QtWidgets.QLabel(self.frame_5)
        self.label_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_20.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_20.setObjectName("label_20")
        self.formLayout_4.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.Audio_Feature_Extraction_SingleFileWindowSize = QtWidgets.QLineEdit(self.frame_5)
        self.Audio_Feature_Extraction_SingleFileWindowSize.setObjectName("Audio_Feature_Extraction_SingleFileWindowSize")
        self.formLayout_4.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.Audio_Feature_Extraction_SingleFileWindowSize)
        self.label_21 = QtWidgets.QLabel(self.frame_5)
        self.label_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_21.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_21.setObjectName("label_21")
        self.formLayout_4.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.Audio_Feature_Extraction_SingleFileStepSize = QtWidgets.QLineEdit(self.frame_5)
        self.Audio_Feature_Extraction_SingleFileStepSize.setObjectName("Audio_Feature_Extraction_SingleFileStepSize")
        self.formLayout_4.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.Audio_Feature_Extraction_SingleFileStepSize)
        self.label_24 = QtWidgets.QLabel(self.frame_5)
        self.label_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_24.setObjectName("label_24")
        self.formLayout_4.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.Audio_Feature_Extraction_SingleFileDataVisualisation = QtWidgets.QCheckBox(self.frame_5)
        self.Audio_Feature_Extraction_SingleFileDataVisualisation.setText("")
        self.Audio_Feature_Extraction_SingleFileDataVisualisation.setObjectName("Audio_Feature_Extraction_SingleFileDataVisualisation")
        self.formLayout_4.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.Audio_Feature_Extraction_SingleFileDataVisualisation)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_4.setItem(18, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.label_26 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.formLayout_4.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.Audio_Feature_Extraction_SingleFileBrowserButton = QtWidgets.QToolButton(self.frame_5)
        self.Audio_Feature_Extraction_SingleFileBrowserButton.setObjectName("Audio_Feature_Extraction_SingleFileBrowserButton")
        self.formLayout_4.setWidget(21, QtWidgets.QFormLayout.LabelRole, self.Audio_Feature_Extraction_SingleFileBrowserButton)
        self.Audio_Feature_Extraction_SingleFilePath = QtWidgets.QLineEdit(self.frame_5)
        self.Audio_Feature_Extraction_SingleFilePath.setObjectName("Audio_Feature_Extraction_SingleFilePath")
        self.formLayout_4.setWidget(21, QtWidgets.QFormLayout.FieldRole, self.Audio_Feature_Extraction_SingleFilePath)
        self.Audio_Feature_Extraction_SingleFileExtractButton = QtWidgets.QPushButton(self.frame_5)
        self.Audio_Feature_Extraction_SingleFileExtractButton.setObjectName("Audio_Feature_Extraction_SingleFileExtractButton")
        self.formLayout_4.setWidget(22, QtWidgets.QFormLayout.LabelRole, self.Audio_Feature_Extraction_SingleFileExtractButton)
        self.label_28 = QtWidgets.QLabel(self.frame_5)
        self.label_28.setWordWrap(True)
        self.label_28.setObjectName("label_28")
        self.formLayout_4.setWidget(23, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.midTermWindowStepSizeLabel = QtWidgets.QLabel(self.frame_5)
        self.midTermWindowStepSizeLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.midTermWindowStepSizeLabel.setObjectName("midTermWindowStepSizeLabel")
        self.formLayout_4.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.midTermWindowStepSizeLabel)
        self.midTermWindowSizeLabel = QtWidgets.QLabel(self.frame_5)
        self.midTermWindowSizeLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.midTermWindowSizeLabel.setObjectName("midTermWindowSizeLabel")
        self.formLayout_4.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.midTermWindowSizeLabel)
        self.Audio_Feature_Extraction_SingleFilemidTermWindowSize = QtWidgets.QLineEdit(self.frame_5)
        self.Audio_Feature_Extraction_SingleFilemidTermWindowSize.setObjectName("Audio_Feature_Extraction_SingleFilemidTermWindowSize")
        self.formLayout_4.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.Audio_Feature_Extraction_SingleFilemidTermWindowSize)
        self.Audio_Feature_Extraction_SingleFilemidTermWindowStepSize = QtWidgets.QLineEdit(self.frame_5)
        self.Audio_Feature_Extraction_SingleFilemidTermWindowStepSize.setObjectName("Audio_Feature_Extraction_SingleFilemidTermWindowStepSize")
        self.formLayout_4.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.Audio_Feature_Extraction_SingleFilemidTermWindowStepSize)
        self.gridLayout_3.addWidget(self.frame_5, 1, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.Audio_Feature_Extraction)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setObjectName("frame_6")
        self.formLayout_5 = QtWidgets.QFormLayout(self.frame_6)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_19 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_19)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_5.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.label_17 = QtWidgets.QLabel(self.frame_6)
        self.label_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.Audio_Feature_Extraction_DirectoryWindowTerm = QtWidgets.QComboBox(self.frame_6)
        self.Audio_Feature_Extraction_DirectoryWindowTerm.setObjectName("Audio_Feature_Extraction_DirectoryWindowTerm")
        self.Audio_Feature_Extraction_DirectoryWindowTerm.addItem("")
        self.Audio_Feature_Extraction_DirectoryWindowTerm.addItem("")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Audio_Feature_Extraction_DirectoryWindowTerm)
        self.label_22 = QtWidgets.QLabel(self.frame_6)
        self.label_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_22.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_22.setObjectName("label_22")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.Audio_Feature_Extraction_DirectoryWindowSize = QtWidgets.QLineEdit(self.frame_6)
        self.Audio_Feature_Extraction_DirectoryWindowSize.setObjectName("Audio_Feature_Extraction_DirectoryWindowSize")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Audio_Feature_Extraction_DirectoryWindowSize)
        self.label_23 = QtWidgets.QLabel(self.frame_6)
        self.label_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_23.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_23.setObjectName("label_23")
        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.Audio_Feature_Extraction_DirectoryStepSize = QtWidgets.QLineEdit(self.frame_6)
        self.Audio_Feature_Extraction_DirectoryStepSize.setObjectName("Audio_Feature_Extraction_DirectoryStepSize")
        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.Audio_Feature_Extraction_DirectoryStepSize)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_5.setItem(11, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        self.label_27 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.formLayout_5.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.Audio_Feature_Extraction_DirectoryBrowserButton = QtWidgets.QToolButton(self.frame_6)
        self.Audio_Feature_Extraction_DirectoryBrowserButton.setObjectName("Audio_Feature_Extraction_DirectoryBrowserButton")
        self.formLayout_5.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.Audio_Feature_Extraction_DirectoryBrowserButton)
        self.Audio_Feature_Extraction_DirectoryPath = QtWidgets.QLineEdit(self.frame_6)
        self.Audio_Feature_Extraction_DirectoryPath.setObjectName("Audio_Feature_Extraction_DirectoryPath")
        self.formLayout_5.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.Audio_Feature_Extraction_DirectoryPath)
        self.label_29 = QtWidgets.QLabel(self.frame_6)
        self.label_29.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_29.setWordWrap(True)
        self.label_29.setObjectName("label_29")
        self.formLayout_5.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.Audio_Feature_Extraction_DirectoryExtractButton = QtWidgets.QPushButton(self.frame_6)
        self.Audio_Feature_Extraction_DirectoryExtractButton.setObjectName("Audio_Feature_Extraction_DirectoryExtractButton")
        self.formLayout_5.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.Audio_Feature_Extraction_DirectoryExtractButton)
        self.midTermWindowStepSizeLabel_2 = QtWidgets.QLabel(self.frame_6)
        self.midTermWindowStepSizeLabel_2.setObjectName("midTermWindowStepSizeLabel_2")
        self.formLayout_5.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.midTermWindowStepSizeLabel_2)
        self.midTermWindowSizeLabel_2 = QtWidgets.QLabel(self.frame_6)
        self.midTermWindowSizeLabel_2.setObjectName("midTermWindowSizeLabel_2")
        self.formLayout_5.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.midTermWindowSizeLabel_2)
        self.Audio_Feature_Extraction_DirectorymidTermWindowStepSize = QtWidgets.QLineEdit(self.frame_6)
        self.Audio_Feature_Extraction_DirectorymidTermWindowStepSize.setObjectName("Audio_Feature_Extraction_DirectorymidTermWindowStepSize")
        self.formLayout_5.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.Audio_Feature_Extraction_DirectorymidTermWindowStepSize)
        self.Audio_Feature_Extraction_DirectorymidTermWindowSize = QtWidgets.QLineEdit(self.frame_6)
        self.Audio_Feature_Extraction_DirectorymidTermWindowSize.setObjectName("Audio_Feature_Extraction_DirectorymidTermWindowSize")
        self.formLayout_5.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.Audio_Feature_Extraction_DirectorymidTermWindowSize)
        self.label_19.raise_()
        self.label_22.raise_()
        self.Audio_Feature_Extraction_DirectoryWindowSize.raise_()
        self.label_23.raise_()
        self.Audio_Feature_Extraction_DirectoryStepSize.raise_()
        self.label_17.raise_()
        self.Audio_Feature_Extraction_DirectoryWindowTerm.raise_()
        self.Audio_Feature_Extraction_DirectoryBrowserButton.raise_()
        self.Audio_Feature_Extraction_DirectoryPath.raise_()
        self.label_27.raise_()
        self.label_29.raise_()
        self.Audio_Feature_Extraction_DirectoryExtractButton.raise_()
        self.midTermWindowStepSizeLabel_2.raise_()
        self.midTermWindowSizeLabel_2.raise_()
        self.Audio_Feature_Extraction_DirectorymidTermWindowStepSize.raise_()
        self.Audio_Feature_Extraction_DirectorymidTermWindowSize.raise_()
        self.gridLayout_3.addWidget(self.frame_6, 1, 1, 1, 1)
        self.tabWidget.addTab(self.Audio_Feature_Extraction, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Frame)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TensorFlow_Audio), _translate("Frame", "TensorFlow_Test_Audio"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Kit_Test_Audio), _translate("Frame", "Sci-Kit_Test_Audio"))
        self.label_10.setText(_translate("Frame", "TESTING"))
        self.label_6.setText(_translate("Frame", "Input Root Training Folder "))
        self.Quick_Train_Train_RootFolderButton.setText(_translate("Frame", "..."))
        self.Quick_Train_TrainButton.setText(_translate("Frame", "TRAIN"))
        self.label_14.setText(_translate("Frame", "An example of the root folder would be if you had two folders of data named male and female, you would put them in a new folder and find that new folder here."))
        self.label_9.setText(_translate("Frame", "Input the folder of WAV files you want to test"))
        self.Quick_Train_TestFolderButton.setText(_translate("Frame", "..."))
        self.Quick_Train_TestButton.setText(_translate("Frame", "TEST"))
        self.label_15.setText(_translate("Frame", "Quick_Train_Audio is for quick feature extraction and testing.  The features will not be saved."))
        self.label_11.setText(_translate("Frame", "Select A Classifier Type"))
        self.Quick_Train_ModelFileButton.setText(_translate("Frame", "..."))
        self.Quick_Train_TestClassifier.setItemText(0, _translate("Frame", "SVM"))
        self.Quick_Train_TestClassifier.setItemText(1, _translate("Frame", "SVM_RBF"))
        self.Quick_Train_TestClassifier.setItemText(2, _translate("Frame", "KNN"))
        self.Quick_Train_TestClassifier.setItemText(3, _translate("Frame", "GradientBoosting"))
        self.Quick_Train_TestClassifier.setItemText(4, _translate("Frame", "ExtraTrees"))
        self.label_8.setText(_translate("Frame", "Input the trained model you want to use below."))
        self.label_7.setText(_translate("Frame", "TRAINING"))
        self.label_3.setText(_translate("Frame", "Window Step Size"))
        self.label_4.setText(_translate("Frame", "Name of the model when trained"))
        self.label_2.setText(_translate("Frame", "Window Size"))
        self.label_30.setText(_translate("Frame", "Compute Beat?"))
        self.label_5.setText(_translate("Frame", "TRAINING PARAMETERS"))
        self.label.setText(_translate("Frame", "Select a Classifier"))
        self.Quick_Train_TrainClassifier.setItemText(0, _translate("Frame", "SVM"))
        self.Quick_Train_TrainClassifier.setItemText(1, _translate("Frame", "SVM_RBF"))
        self.Quick_Train_TrainClassifier.setItemText(2, _translate("Frame", "KNN"))
        self.Quick_Train_TrainClassifier.setItemText(3, _translate("Frame", "GradientBoosting"))
        self.Quick_Train_TrainClassifier.setItemText(4, _translate("Frame", "ExtraTrees"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.QuickAudio), _translate("Frame", "Quick_Train_Audio"))
        self.label_18.setText(_translate("Frame", "Single File Feature Extraction"))
        self.label_16.setText(_translate("Frame", "ShortTerm or MidTerm Feature Extraction.  Midterm will give both."))
        self.Audio_Feature_Extraction_SingleFileWindowTerm.setItemText(0, _translate("Frame", "ShortTerm"))
        self.Audio_Feature_Extraction_SingleFileWindowTerm.setItemText(1, _translate("Frame", "MidTerm"))
        self.label_20.setText(_translate("Frame", "ShortTerm Window Size"))
        self.label_21.setText(_translate("Frame", "ShortTerm Window Step Size"))
        self.label_24.setText(_translate("Frame", "Do you want to visualize the data?"))
        self.label_26.setText(_translate("Frame", "Input The WAV File here"))
        self.Audio_Feature_Extraction_SingleFileBrowserButton.setText(_translate("Frame", "..."))
        self.Audio_Feature_Extraction_SingleFileExtractButton.setText(_translate("Frame", "EXTRACT"))
        self.label_28.setText(_translate("Frame", "Features can be averaged or returned as a Matrix.  Need to Implement."))
        self.midTermWindowStepSizeLabel.setText(_translate("Frame", "MidTerm Window Step Size"))
        self.midTermWindowSizeLabel.setText(_translate("Frame", "MidTerm Window Size"))
        self.label_19.setText(_translate("Frame", "Directory of Files Feature Extraction"))
        self.label_17.setText(_translate("Frame", "ShortTerm or MidTerm Feature Extraction. Midterm will give both."))
        self.Audio_Feature_Extraction_DirectoryWindowTerm.setItemText(0, _translate("Frame", "ShortTerm"))
        self.Audio_Feature_Extraction_DirectoryWindowTerm.setItemText(1, _translate("Frame", "MidTerm"))
        self.label_22.setText(_translate("Frame", "Window Size"))
        self.label_23.setText(_translate("Frame", "Window Step Size"))
        self.label_27.setText(_translate("Frame", "Input the Directory of WAV files here"))
        self.Audio_Feature_Extraction_DirectoryBrowserButton.setText(_translate("Frame", "..."))
        self.label_29.setText(_translate("Frame", "Features can be averaged or returned as a Matrix.  Need to Implement."))
        self.Audio_Feature_Extraction_DirectoryExtractButton.setText(_translate("Frame", "EXTRACT"))
        self.midTermWindowStepSizeLabel_2.setText(_translate("Frame", "MidTerm Window Step Size"))
        self.midTermWindowSizeLabel_2.setText(_translate("Frame", "MidTerm Window Size"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Audio_Feature_Extraction), _translate("Frame", "Audio_Feature_Extraction"))
        
        self.somethingToPass = Frame
        self.Audio_Feature_Extraction_SingleFilemidTermWindowSize.setEnabled(False)
        self.Audio_Feature_Extraction_SingleFilemidTermWindowStepSize.setEnabled(False)
        self.Audio_Feature_Extraction_DirectorymidTermWindowSize.setEnabled(False)
        self.Audio_Feature_Extraction_DirectorymidTermWindowStepSize.setEnabled(False)
        
        self.Quick_Train_TrainButton.clicked.connect(self.Quick_Train_startTraining)
        self.Quick_Train_TestButton.clicked.connect(self.Quick_Train_StartTesting)
        self.Quick_Train_Train_RootFolderButton.clicked.connect(self.Quick_Train_SelectDirectory)
        self.Quick_Train_ModelFileButton.clicked.connect(self.Quick_Train_SelectModelFile)
        self.Quick_Train_TestFolderButton.clicked.connect(self.Quick_Train_SelectTestDirectory)
        
        self.Audio_Feature_Extraction_SingleFileBrowserButton.clicked.connect(
                self.Audio_Feature_Extraction_SelectTestFile)
        
        self.Audio_Feature_Extraction_SingleFileExtractButton.clicked.connect(
                self.Audio_Feature_Extraction_Extract)
        
        self.Audio_Feature_Extraction_SingleFileWindowTerm.currentIndexChanged.connect(
                 self.Audio_Feature_Extraction_AllowInputSingle )
        
        self.Audio_Feature_Extraction_DirectoryBrowserButton.clicked.connect(
                self.Audio_Feature_Extraction_Select_Directory)
        
        self.Audio_Feature_Extraction_DirectoryExtractButton.clicked.connect(
                self.Audio_Feature_Extraction_Extract_Directory)
        
        self.Audio_Feature_Extraction_DirectoryWindowTerm.currentIndexChanged.connect(
                self.Audio_Feature_Extraction_AllowInputDirectory)
       
    def Quick_Train_startTraining(self): 
        path = str(self.Quick_Train_RootFolderName.text())
        trainingDir = []
        for root, directs, files in os.walk(path):
                trainingDir.append(root)
        trainingDir = trainingDir[1:]
        if self.Quick_Train_BeatBoolean.isChecked() :
            aT.featureAndTrain(trainingDir, float(self.Quick_Train_Window.text()), float(self.Quick_Train_Step.text()), aT.shortTermWindow, aT.shortTermStep, str(self.Quick_Train_TrainClassifier.currentText()).lower(), self.Quick_Train_ModelName.text(), True)
            
        else :
            aT.featureAndTrain(trainingDir, float(self.Quick_Train_Window.text()), float(self.Quick_Train_Step.text()), aT.shortTermWindow, aT.shortTermStep, str(self.Quick_Train_TrainClassifier.currentText()).lower(), self.Quick_Train_ModelName.text(), False)

            
    def Quick_Train_SelectDirectory(self):
        filename= QFileDialog.getExistingDirectory(self.somethingToPass, "Select Directory")
        if filename:
                self.Quick_Train_RootFolderName.setText(filename)
                
    def Quick_Train_SelectModelFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self.somethingToPass,"Pick Trained Model", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.Quick_Train_TestModelPath.setText(fileName)

    def Quick_Train_StartTesting(self):
        path = str(self.Quick_Train_TestFolder.text())
        testDir = []
        for root, directs, files in os.walk(path):
            for x in files:
                testDir.append(root + "/" + x)
        for x in testDir:
            result = aT.fileClassification(x, self.Quick_Train_TestModelPath.text(), str(self.Quick_Train_TestClassifier.currentText()).lower())
            print(result) 
        
    def Quick_Train_SelectTestDirectory(self):
        filename= QFileDialog.getExistingDirectory(self.somethingToPass, "Select Directory")
        if filename:
                self.Quick_Train_TestFolder.setText(filename)
                
    def Audio_Feature_Extraction_SelectTestFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self.somethingToPass,"Pick File To Extract", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.Audio_Feature_Extraction_SingleFilePath.setText(fileName)
 
    def Audio_Feature_Extraction_AllowInputSingle(self):
            if self.Audio_Feature_Extraction_SingleFileWindowTerm.currentText() == "ShortTerm":
               self.Audio_Feature_Extraction_SingleFilemidTermWindowSize.setEnabled(False)
               self.Audio_Feature_Extraction_SingleFilemidTermWindowStepSize.setEnabled(False)
               
            else:
                self.Audio_Feature_Extraction_SingleFilemidTermWindowSize.setEnabled(True)
                self.Audio_Feature_Extraction_SingleFilemidTermWindowStepSize.setEnabled(True)
                
    def Audio_Feature_Extraction_AllowInputDirectory(self):
        if self.Audio_Feature_Extraction_DirectoryWindowTerm.currentText() == "ShortTerm":
            self.Audio_Feature_Extraction_DirectorymidTermWindowSize.setEnabled(False)
            self.Audio_Feature_Extraction_DirectorymidTermWindowStepSize.setEnabled(False)
        else:
            self.Audio_Feature_Extraction_DirectorymidTermWindowSize.setEnabled(True)
            self.Audio_Feature_Extraction_DirectorymidTermWindowStepSize.setEnabled(True)
               
    def Audio_Feature_Extraction_Extract(self):
        if self.Audio_Feature_Extraction_SingleFileWindowTerm.currentText() == "ShortTerm":
            [Fs, x] = audioBasicIO.readAudioFile(self.Audio_Feature_Extraction_SingleFilePath.text())
            stFeatures = audioFeatureExtraction.stFeatureExtraction(x, Fs, float(self.Audio_Feature_Extraction_SingleFileWindowSize.text()) * Fs, float(self.Audio_Feature_Extraction_SingleFileStepSize.text()) * Fs)
     
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getSaveFileName(self.somethingToPass,"Where to save?", "","CSV files (*.csv)", options=options)
            
            numpy.savetxt(fileName + ".csv", stFeatures, delimiter = ',')
            QMessageBox.about(self.somethingToPass,"Files Created", "File has been saved as CSV file")
            ## Let the User specify how many features and what features to see eventually.
#==============================================================================
#             if self.Audio_Feature_Extraction_SingleFileDataVisualisation.isChecked():
#                 stFeatures = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs)
#                 
#                 labels = ["Zero Crossing Rate", "Energy", "Entropy of Energy", "Spectral Centroid",
#                           "Spectral Spread", "Spectral Entropy", "Spectral Flux", "Spectral Rolloff",
#                           "MFCC 1", "MFCC 2", "MFCC 3", "MFCC 4",
#                           "MFCC 5", "MFCC 6", "MFCC 7", "MFCC 8",
#                           "MFCC 9", "MFCC 10", "MFCC 11", "MFCC 12", "MFCC 13",
#                           "Chroma Vector 1", "Chroma Vector 2", "Chroma Vector 3", "Chroma Vector 4",
#                           "Chroma Vector 5", "Chroma Vector 6", "Chroma Vector 7", "Chroma Vector 8",
#                           "Chroma Vector 9", "Chroma Vector 10", "Chroma Vector 11","Chroma Vector 12", "Chroma Deviation"]
#                 
#                 
#                 for x in range(0, len(labels)-1):
#                     plt.subplot(34,1,x+1); plt.plot(stFeatures[x,:]); plt.xlabel('Frame no'); plt.ylabel(labels[x])                
#                 
#                 plt.show()
#             
#==============================================================================
            
        else:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getSaveFileName(self.somethingToPass,"Where to save?", "","CSV files (*.csv)", options=options)
            
            audioFeatureExtraction.mtFeatureExtractionToFile(self.Audio_Feature_Extraction_SingleFilePath.text(),
                                                                          float(self.Audio_Feature_Extraction_SingleFilemidTermWindowSize.text()), 
                                                                          float(self.Audio_Feature_Extraction_SingleFilemidTermWindowStepSize.text()),
                                                                          float(self.Audio_Feature_Extraction_SingleFileWindowSize.text()), 
                                                                          float(self.Audio_Feature_Extraction_SingleFileStepSize.text()), fileName, storeStFeatures = True, storeToCSV = True, PLOT = False)
            
            QMessageBox.about(self.somethingToPass,"Files Created", "Files have been saved as CSV files and .npy files")
            
    def Audio_Feature_Extraction_Select_Directory(self):
        filename= QFileDialog.getExistingDirectory(self.somethingToPass, "Select Directory")
        if filename:
                self.Audio_Feature_Extraction_DirectoryPath.setText(filename)
            
    def Audio_Feature_Extraction_Extract_Directory(self):
        
        pathToSaveFiles= QFileDialog.getExistingDirectory(self.somethingToPass, "Select Directory to Save Files")
        
        i = 0
        
        path = self.Audio_Feature_Extraction_DirectoryPath.text()
        extractionList = []
        nameList = []
        tempHold = []
        
        for root, directs, files in os.walk(path):
            for x in files:
                extractionList.append(root + "/" + x)
                nameList.append(x)
        
        for name in nameList:
            x = name.split('.')
            tempHold.append(x[0])
        
        nameList = tempHold
        
        
        if self.Audio_Feature_Extraction_DirectoryWindowTerm.currentText() == "ShortTerm":
            
            for audio in extractionList:
                [Fs, x] = audioBasicIO.readAudioFile(audio)
                print(audio)
                stFeatures = audioFeatureExtraction.stFeatureExtraction(x, Fs, float(self.Audio_Feature_Extraction_DirectoryWindowSize.text()) * Fs, float(self.Audio_Feature_Extraction_DirectoryStepSize.text()) * Fs)
                #I think the files are overwriting each other.  I am getting
                #299 files but it should be 5134.  I changed the namelist[i] to
                #just i
                numpy.savetxt(pathToSaveFiles + "/" + str(i) + ".csv", stFeatures, delimiter = ',')
                
                i += 1
            
            QMessageBox.about(self.somethingToPass,"Files Created", "Files have been saved as CSV files.")
            
        else:
            for x in extractionList:
            
                audioFeatureExtraction.mtFeatureExtractionToFile(x,
                float(self.Audio_Feature_Extraction_DirectorymidTermWindowSize.text()), 
                float(self.Audio_Feature_Extraction_DirectorymidTermWindowStepSize.text()),
                float(self.Audio_Feature_Extraction_DirectoryWindowSize.text()), 
                float(self.Audio_Feature_Extraction_DirectoryStepSize.text()),
                pathToSaveFiles + "/" + nameList[i], storeStFeatures = True, storeToCSV = True, PLOT = False)
                i += 1
                
            QMessageBox.about(self.somethingToPass,"Files Created", "Files have been saved as CSV files and .npy files. There ")
            



