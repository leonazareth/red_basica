from PyQt5.QtCore import pyqtSignal, QModelIndex
from PyQt5.QtSql import QSqlTableModel, QSqlQuery
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtCore import Qt
from ..lib.Store import Store

class Country(QSqlTableModel):
    
    def __init__(self, *args, db=Store().getDB(), **kwargs):        
        super(Country, self).__init__(*args, **kwargs)
        self.setTable("countries")
        self.nameFieldIndex = self.fieldIndex('name_es')
        self.index = self.fieldIndex('id')
        self.setSort(self.nameFieldIndex, Qt.AscendingOrder)        
        self.select()

    def getList(self):
        countryModel = QSqlTableModel(self)
        countryModel.setTable("countries")
        countryModel.select()
        countries_list = []
        for i in range(countryModel.rowCount()):
            _id = countryModel.record(i).value("id")
            name = countryModel.record(i).value("name_es")
            countries_list.append((_id, name))
        return countries_list

    def getDisplayColumn(self):
        return self.nameFieldIndex