# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flow_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FlowDialog(object):
    def setupUi(self, FlowDialog):
        FlowDialog.setObjectName("FlowDialog")
        FlowDialog.resize(602, 705)
        self.formLayout = QtWidgets.QFormLayout(FlowDialog)
        self.formLayout.setObjectName("formLayout")
        self.tabWidget = QtWidgets.QTabWidget(FlowDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.populationTab = QtWidgets.QWidget()
        self.populationTab.setObjectName("populationTab")
        self.formLayout_6 = QtWidgets.QFormLayout(self.populationTab)
        self.formLayout_6.setObjectName("formLayout_6")
        self.popLayerLabel = QtWidgets.QLabel(self.populationTab)
        self.popLayerLabel.setObjectName("popLayerLabel")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.popLayerLabel)
        self.popLayerSelect = QtWidgets.QComboBox(self.populationTab)
        self.popLayerSelect.setObjectName("popLayerSelect")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.popLayerSelect)
        self.popOnlySelectedVal = QtWidgets.QCheckBox(self.populationTab)
        self.popOnlySelectedVal.setObjectName("popOnlySelectedVal")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.popOnlySelectedVal)
        self.popStartPlanLabel = QtWidgets.QLabel(self.populationTab)
        self.popStartPlanLabel.setObjectName("popStartPlanLabel")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.popStartPlanLabel)
        self.popStartPlanVal = QtWidgets.QComboBox(self.populationTab)
        self.popStartPlanVal.setObjectName("popStartPlanVal")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.popStartPlanVal)
        self.popEndPlanLabel = QtWidgets.QLabel(self.populationTab)
        self.popEndPlanLabel.setObjectName("popEndPlanLabel")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.popEndPlanLabel)
        self.popEndPlanVal = QtWidgets.QComboBox(self.populationTab)
        self.popEndPlanVal.setObjectName("popEndPlanVal")
        self.formLayout_6.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.popEndPlanVal)
        self.groupBox = QtWidgets.QGroupBox(self.populationTab)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.popWaterConsumptionStartLabel = QtWidgets.QLabel(self.groupBox)
        self.popWaterConsumptionStartLabel.setObjectName("popWaterConsumptionStartLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.popWaterConsumptionStartLabel)
        self.popWaterConsumptionStartVal = QtWidgets.QSpinBox(self.groupBox)
        self.popWaterConsumptionStartVal.setMaximum(999999999)
        self.popWaterConsumptionStartVal.setProperty("value", 150)
        self.popWaterConsumptionStartVal.setObjectName("popWaterConsumptionStartVal")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.popWaterConsumptionStartVal)
        self.popWaterConsumptionEndLabel = QtWidgets.QLabel(self.groupBox)
        self.popWaterConsumptionEndLabel.setObjectName("popWaterConsumptionEndLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.popWaterConsumptionEndLabel)
        self.popWaterConsumptionEndVal = QtWidgets.QSpinBox(self.groupBox)
        self.popWaterConsumptionEndVal.setMaximum(999999999)
        self.popWaterConsumptionEndVal.setProperty("value", 150)
        self.popWaterConsumptionEndVal.setObjectName("popWaterConsumptionEndVal")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.popWaterConsumptionEndVal)
        self.popCoefficientReturnLabel = QtWidgets.QLabel(self.groupBox)
        self.popCoefficientReturnLabel.setObjectName("popCoefficientReturnLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.popCoefficientReturnLabel)
        self.popCoefficientReturnVal = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.popCoefficientReturnVal.setMaximum(9999999999.0)
        self.popCoefficientReturnVal.setProperty("value", 0.8)
        self.popCoefficientReturnVal.setObjectName("popCoefficientReturnVal")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.popCoefficientReturnVal)
        self.formLayout_6.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.groupBox)
        self.tabWidget.addTab(self.populationTab, "")
        self.connectionsTab = QtWidgets.QWidget()
        self.connectionsTab.setObjectName("connectionsTab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.connectionsTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.connLayerLabel = QtWidgets.QLabel(self.connectionsTab)
        self.connLayerLabel.setObjectName("connLayerLabel")
        self.verticalLayout.addWidget(self.connLayerLabel)
        self.connLayerSelect = QtWidgets.QComboBox(self.connectionsTab)
        self.connLayerSelect.setObjectName("connLayerSelect")
        self.verticalLayout.addWidget(self.connLayerSelect)
        self.connOnlySelectedVal = QtWidgets.QCheckBox(self.connectionsTab)
        self.connOnlySelectedVal.setObjectName("connOnlySelectedVal")
        self.verticalLayout.addWidget(self.connOnlySelectedVal)
        self.connNoConnectionsLabel = QtWidgets.QLabel(self.connectionsTab)
        self.connNoConnectionsLabel.setObjectName("connNoConnectionsLabel")
        self.verticalLayout.addWidget(self.connNoConnectionsLabel)
        self.connNoConnections = QtWidgets.QComboBox(self.connectionsTab)
        self.connNoConnections.setObjectName("connNoConnections")
        self.verticalLayout.addWidget(self.connNoConnections)
        self.connNoConnectionsEndPlanLabel = QtWidgets.QLabel(self.connectionsTab)
        self.connNoConnectionsEndPlanLabel.setObjectName("connNoConnectionsEndPlanLabel")
        self.verticalLayout.addWidget(self.connNoConnectionsEndPlanLabel)
        self.connNoConnectionsEndPlan = QtWidgets.QComboBox(self.connectionsTab)
        self.connNoConnectionsEndPlan.setObjectName("connNoConnectionsEndPlan")
        self.verticalLayout.addWidget(self.connNoConnectionsEndPlan)
        self.groupBox_2 = QtWidgets.QGroupBox(self.connectionsTab)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.connGrowthRateLabel = QtWidgets.QLabel(self.groupBox_2)
        self.connGrowthRateLabel.setObjectName("connGrowthRateLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.connGrowthRateLabel)
        self.connEconomyConnLabel = QtWidgets.QLabel(self.groupBox_2)
        self.connEconomyConnLabel.setObjectName("connEconomyConnLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.connEconomyConnLabel)
        self.connStartConsumptionLabel = QtWidgets.QLabel(self.groupBox_2)
        self.connStartConsumptionLabel.setObjectName("connStartConsumptionLabel")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.connStartConsumptionLabel)
        self.connEndConsumptionLabel = QtWidgets.QLabel(self.groupBox_2)
        self.connEndConsumptionLabel.setObjectName("connEndConsumptionLabel")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.connEndConsumptionLabel)
        self.connOcupancyRateStartLabel = QtWidgets.QLabel(self.groupBox_2)
        self.connOcupancyRateStartLabel.setObjectName("connOcupancyRateStartLabel")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.connOcupancyRateStartLabel)
        self.connOcupancyRateEndLabel = QtWidgets.QLabel(self.groupBox_2)
        self.connOcupancyRateEndLabel.setObjectName("connOcupancyRateEndLabel")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.connOcupancyRateEndLabel)
        self.connReturnCoefficientLabel = QtWidgets.QLabel(self.groupBox_2)
        self.connReturnCoefficientLabel.setObjectName("connReturnCoefficientLabel")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.connReturnCoefficientLabel)
        self.connGrowthRateVal = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.connGrowthRateVal.setObjectName("connGrowthRateVal")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.connGrowthRateVal)
        self.connEconomyConnVal = QtWidgets.QSpinBox(self.groupBox_2)
        self.connEconomyConnVal.setMaximum(999999999)
        self.connEconomyConnVal.setProperty("value", 1)
        self.connEconomyConnVal.setObjectName("connEconomyConnVal")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.connEconomyConnVal)
        self.connStartConsumptionVal = QtWidgets.QSpinBox(self.groupBox_2)
        self.connStartConsumptionVal.setMaximum(999999999)
        self.connStartConsumptionVal.setProperty("value", 150)
        self.connStartConsumptionVal.setObjectName("connStartConsumptionVal")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.connStartConsumptionVal)
        self.connEndConsumptionVal = QtWidgets.QSpinBox(self.groupBox_2)
        self.connEndConsumptionVal.setMaximum(999999999)
        self.connEndConsumptionVal.setProperty("value", 150)
        self.connEndConsumptionVal.setObjectName("connEndConsumptionVal")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.connEndConsumptionVal)
        self.connOcupancyRateStartVal = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.connOcupancyRateStartVal.setMaximum(999999999999.0)
        self.connOcupancyRateStartVal.setProperty("value", 0.0)
        self.connOcupancyRateStartVal.setObjectName("connOcupancyRateStartVal")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.connOcupancyRateStartVal)
        self.connOcupancyRateEndVal = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.connOcupancyRateEndVal.setMaximum(9999999999999.0)
        self.connOcupancyRateEndVal.setObjectName("connOcupancyRateEndVal")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.connOcupancyRateEndVal)
        self.connReturnCoefficientVal = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.connReturnCoefficientVal.setMaximum(9999999999.0)
        self.connReturnCoefficientVal.setProperty("value", 0.8)
        self.connReturnCoefficientVal.setObjectName("connReturnCoefficientVal")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.connReturnCoefficientVal)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.connectionsTab, "")
        self.flowTab = QtWidgets.QWidget()
        self.flowTab.setObjectName("flowTab")
        self.formLayout_5 = QtWidgets.QFormLayout(self.flowTab)
        self.formLayout_5.setObjectName("formLayout_5")
        self.flowLabel = QtWidgets.QLabel(self.flowTab)
        self.flowLabel.setObjectName("flowLabel")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.flowLabel)
        self.flowSelectedVal = QtWidgets.QCheckBox(self.flowTab)
        self.flowSelectedVal.setObjectName("flowSelectedVal")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.flowSelectedVal)
        self.label_22 = QtWidgets.QLabel(self.flowTab)
        self.label_22.setObjectName("label_22")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.label_22)
        self.flowCurrentStartPlan = QtWidgets.QComboBox(self.flowTab)
        self.flowCurrentStartPlan.setObjectName("flowCurrentStartPlan")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.flowCurrentStartPlan)
        self.label_23 = QtWidgets.QLabel(self.flowTab)
        self.label_23.setObjectName("label_23")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.label_23)
        self.flowProjected = QtWidgets.QComboBox(self.flowTab)
        self.flowProjected.setObjectName("flowProjected")
        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.flowProjected)
        self.groupBox_3 = QtWidgets.QGroupBox(self.flowTab)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout_4.setObjectName("formLayout_4")
        self.flowProjectionRateLabel = QtWidgets.QLabel(self.groupBox_3)
        self.flowProjectionRateLabel.setObjectName("flowProjectionRateLabel")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.flowProjectionRateLabel)
        self.flowProjectionRateVal = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.flowProjectionRateVal.setObjectName("flowProjectionRateVal")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.flowProjectionRateVal)
        self.formLayout_5.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.groupBox_3)
        self.flowLayer = QtWidgets.QComboBox(self.flowTab)
        self.flowLayer.setObjectName("flowLayer")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.flowLayer)
        self.tabWidget.addTab(self.flowTab, "")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.tabWidget)
        self.manholeLayerLabel = QtWidgets.QLabel(FlowDialog)
        self.manholeLayerLabel.setObjectName("manholeLayerLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.manholeLayerLabel)
        self.manholeLayerSelect = QtWidgets.QComboBox(FlowDialog)
        self.manholeLayerSelect.setObjectName("manholeLayerSelect")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.manholeLayerSelect)
        self.manholeOnlySelectedLabel = QtWidgets.QLabel(FlowDialog)
        self.manholeOnlySelectedLabel.setObjectName("manholeOnlySelectedLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.manholeOnlySelectedLabel)
        self.manholeOnlySelectedVal = QtWidgets.QCheckBox(FlowDialog)
        self.manholeOnlySelectedVal.setText("")
        self.manholeOnlySelectedVal.setObjectName("manholeOnlySelectedVal")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.manholeOnlySelectedVal)
        self.influenceAreaBufferLabel = QtWidgets.QLabel(FlowDialog)
        self.influenceAreaBufferLabel.setObjectName("influenceAreaBufferLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.influenceAreaBufferLabel)
        self.influenceAreaBufferVal = QtWidgets.QSpinBox(FlowDialog)
        self.influenceAreaBufferVal.setObjectName("influenceAreaBufferVal")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.influenceAreaBufferVal)
        self.errorMessage = QtWidgets.QLabel(FlowDialog)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.errorMessage.setFont(font)
        self.errorMessage.setStyleSheet("color: red")
        self.errorMessage.setText("")
        self.errorMessage.setObjectName("errorMessage")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.errorMessage)
        self.progressBar = QtWidgets.QProgressBar(FlowDialog)
        self.progressBar.setEnabled(True)
        self.progressBar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.progressBar)
        self.buttonBox = QtWidgets.QDialogButtonBox(FlowDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)

        self.retranslateUi(FlowDialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(FlowDialog.accept)
        self.buttonBox.rejected.connect(FlowDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FlowDialog)

    def retranslateUi(self, FlowDialog):
        _translate = QtCore.QCoreApplication.translate
        FlowDialog.setWindowTitle(_translate("FlowDialog", "Atribución de Caudales por Área de Influencia"))
        self.popLayerLabel.setText(_translate("FlowDialog", "Seleccione la capa"))
        self.popOnlySelectedVal.setText(_translate("FlowDialog", "Sólo seleccionados"))
        self.popStartPlanLabel.setText(_translate("FlowDialog", "Población inicio de plan"))
        self.popEndPlanLabel.setText(_translate("FlowDialog", "Población fin de plan"))
        self.popWaterConsumptionStartLabel.setText(_translate("FlowDialog", "Dotación de inicio de plan (l/hab.día) [qi]"))
        self.popWaterConsumptionEndLabel.setText(_translate("FlowDialog", "Dotación de final de plan (l/hab.día) [qf]"))
        self.popCoefficientReturnLabel.setText(_translate("FlowDialog", "Coeficiente de retorno [C]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.populationTab), _translate("FlowDialog", "Población"))
        self.connLayerLabel.setText(_translate("FlowDialog", "Seleccione la capa"))
        self.connOnlySelectedVal.setText(_translate("FlowDialog", "Sólo seleccionados"))
        self.connNoConnectionsLabel.setText(_translate("FlowDialog", "Cantidad de conexiones inicio de plan"))
        self.connNoConnectionsEndPlanLabel.setText(_translate("FlowDialog", "Cantidad de conexiones fin de plan (opcional)"))
        self.connGrowthRateLabel.setText(_translate("FlowDialog", "Tasa de crecimiento [Gr]"))
        self.connEconomyConnLabel.setText(_translate("FlowDialog", "Cantidad de economía por conexión [econ_con]"))
        self.connStartConsumptionLabel.setText(_translate("FlowDialog", "Dotación de inicio de plan (l/hab.día) [qi]"))
        self.connEndConsumptionLabel.setText(_translate("FlowDialog", "Dotación de final de plan (l/hab.día) [qf]"))
        self.connOcupancyRateStartLabel.setText(_translate("FlowDialog", "Tasa de ocupación inicio de plan (hab/vivienda) [Hi_Ini]"))
        self.connOcupancyRateEndLabel.setText(_translate("FlowDialog", "Tasa de ocupación final de plan (hab/vivienda) [Hf_Fin]"))
        self.connReturnCoefficientLabel.setText(_translate("FlowDialog", "Coeficiente de retorno [C]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.connectionsTab), _translate("FlowDialog", "Conexiones"))
        self.flowLabel.setText(_translate("FlowDialog", "Seleccione la capa"))
        self.flowSelectedVal.setText(_translate("FlowDialog", "Sólo seleccionados"))
        self.label_22.setText(_translate("FlowDialog", "Caudal actual (inicio de plan)"))
        self.label_23.setText(_translate("FlowDialog", "Caudal proyectado (opcional)"))
        self.flowProjectionRateLabel.setText(_translate("FlowDialog", "Tasa de proyección [ProjRate]"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.flowTab), _translate("FlowDialog", "Caudal"))
        self.manholeLayerLabel.setText(_translate("FlowDialog", "Capa de caja de inspección"))
        self.manholeOnlySelectedLabel.setText(_translate("FlowDialog", "Sólo seleccionados"))
        self.influenceAreaBufferLabel.setText(_translate("FlowDialog", "Buffer del área de influencia (% de extensión)"))