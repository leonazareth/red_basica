from PyQt5.QtWidgets import (QAbstractItemView, QDataWidgetMapper, QCompleter, QComboBox,
    QHeaderView, QDialog, QMessageBox)
from PyQt5.QtGui import QKeySequence
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlRelationalDelegate
from PyQt5.QtCore import Qt, pyqtSlot, QModelIndex

from ..models.Project import Project
from .ui.NewProjectDialogUi import Ui_NewProjectDialog

class NewProjectView(QDialog, Ui_NewProjectDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.model = Project()
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)

        #Remember the index of country
        country_idx = self.model.fieldIndex("country_id")

        #set the relations to the other ddbb tables
        self.model.setRelation(country_idx, QSqlRelation("countries", "id", "name_en"))

        if not self.model.select():
            print(self.model.lastError())

        #Initialize the Country combobox
        self.countryBox.setModel(self.model.relationModel(country_idx))
        self.countryBox.setModelColumn(self.model.relationModel(country_idx).fieldIndex("name_en"))

        #completer
        selectCountryCompleter = QCompleter(self.model.relationModel(country_idx))
        selectCountryCompleter.setCompletionMode(QCompleter.InlineCompletion)
        selectCountryCompleter.setCaseSensitivity(Qt.CaseInsensitive)
        self.countryBox.setCompleter(selectCountryCompleter)
        self.countryBox.setEditable(True)
        self.countryBox.setInsertPolicy(QComboBox.NoInsert)

        self.mapper = QDataWidgetMapper(self)
        self.mapper.setModel(self.model)
        #self.mapper.setSubmitPolicy(QDataWidgetMapper.AutoSubmit)
        #setitemdelegate
        self.mapper.setItemDelegate(QSqlRelationalDelegate(self))
        self.mapper.addMapping(self.projectNameEdit, self.model.fieldIndex("name"))
        self.mapper.addMapping(self.cityEdit, self.model.fieldIndex("city"))
        self.mapper.addMapping(self.microsystemEdit, self.model.fieldIndex("microsystem"))
        self.mapper.addMapping(self.authorEdit, self.model.fieldIndex("author"))
        self.mapper.addMapping(self.dateEdit, self.model.fieldIndex("date"))
        self.mapper.addMapping(self.countryBox, country_idx)

        #TODOaca fijarse de poner toActive
        self.mapper.toFirst()
        
        self.buttonBox.accepted.connect(self.saveRecord)

    def saveRecord(self):
        #row = self.model.rowCount()
        #self.model.insertRow(row)
        self.mapper.submit()
        # self.mapper.setCurrentIndex(row)
        # if not self.model.submitAll():
        #     print(self.model.lastError().text())
        #     print(self.model.lastError().number())