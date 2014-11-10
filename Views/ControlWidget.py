# -*- coding: utf8 -*-
__author__ = 'Clemens Prescher'

from PyQt4 import QtCore, QtGui


class ControlWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(ControlWidget, self).__init__(*args, **kwargs)
        self.vertical_layout = QtGui.QVBoxLayout()

        self.file_widget = FileWidget()
        self.background_options_gb = BackgroundOptionsGroupBox()
        self.smooth_gb = SmoothGroupBox()
        self.composition_gb = CompositionGroupBox()

        self.vertical_layout.addWidget(self.file_widget)
        self.vertical_layout.addWidget(self.background_options_gb)
        self.vertical_layout.addWidget(self.smooth_gb)
        self.vertical_layout.addSpacerItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed,
                                                             QtGui.QSizePolicy.Fixed))
        self.vertical_layout.addWidget(self.composition_gb)

        self.vertical_layout.addSpacerItem(QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed,
                                                             QtGui.QSizePolicy.Expanding))
        self.setLayout(self.vertical_layout)


class FileWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(FileWidget, self).__init__(*args, **kwargs)

        self.vertical_layout = QtGui.QVBoxLayout()

        self.load_data_btn = QtGui.QPushButton("Load Data")
        self.data_filename_lbl = QtGui.QLabel("None")
        self.data_filename_lbl.setAlignment(QtCore.Qt.AlignRight)
        self.load_background_btn = QtGui.QPushButton("Load Bkg")
        self.background_filename_lbl = QtGui.QLabel("None")
        self.background_filename_lbl.setAlignment(QtCore.Qt.AlignRight)

        self.vertical_layout.addWidget(self.load_data_btn)
        self.vertical_layout.addWidget(self.data_filename_lbl)
        self.vertical_layout.addWidget(self.load_background_btn)
        self.vertical_layout.addWidget(self.background_filename_lbl)

        self.setLayout(self.vertical_layout)


class BackgroundOptionsGroupBox(QtGui.QGroupBox):
    def __init__(self, *args):
        super(BackgroundOptionsGroupBox, self).__init__(*args)

        self.grid_layout = QtGui.QGridLayout()

        self.scale_lbl = QtGui.QLabel("Scale:")
        self.offset_lbl = QtGui.QLabel("Offset:")
        self.scale_lbl.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        self.offset_lbl.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)

        self.scale_sb = QtGui.QDoubleSpinBox()
        self.offset_sb = QtGui.QDoubleSpinBox()

        self.scale_sb.setAlignment(QtCore.Qt.AlignRight)
        self.offset_sb.setAlignment(QtCore.Qt.AlignRight)

        self.scale_sb.setSingleStep(0.01)
        self.offset_sb.setSingleStep(10)

        self.scale_step_txt = QtGui.QLineEdit("0.01")
        self.scale_step_txt.setMaximumWidth(60)
        self.offset_step_txt = QtGui.QLineEdit("10")
        self.offset_step_txt.setMaximumWidth(60)

        self.scale_step_txt.setAlignment(QtCore.Qt.AlignRight)
        self.offset_step_txt.setAlignment(QtCore.Qt.AlignRight)

        self.scale_step_txt.setValidator(QtGui.QDoubleValidator())
        self.offset_step_txt.setValidator(QtGui.QDoubleValidator())

        self.grid_layout.addWidget(self.scale_lbl, 0, 0)
        self.grid_layout.addWidget(self.scale_sb, 0, 1)
        self.grid_layout.addWidget(self.scale_step_txt, 0, 2)

        self.grid_layout.addWidget(self.offset_lbl, 1, 0)
        self.grid_layout.addWidget(self.offset_sb, 1, 1)
        self.grid_layout.addWidget(self.offset_step_txt, 1, 2)

        self.setLayout(self.grid_layout)


class SmoothGroupBox(QtGui.QGroupBox):
    def __init__(self, *args):
        super(SmoothGroupBox, self).__init__(*args)
        self.grid_layout = QtGui.QGridLayout()

        self.smooth_lbl = QtGui.QLabel("Smooth:")
        self.smooth_lbl.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)

        self.smooth_sb = QtGui.QDoubleSpinBox()
        self.smooth_sb.setAlignment(QtCore.Qt.AlignRight)
        self.smooth_sb.setSingleStep(0.01)

        self.smooth_step_txt = QtGui.QLineEdit("0.01")
        self.smooth_step_txt.setAlignment(QtCore.Qt.AlignRight)
        self.smooth_step_txt.setValidator(QtGui.QDoubleValidator())
        self.smooth_step_txt.setMaximumWidth(60)

        self.grid_layout.addWidget(self.smooth_lbl, 0, 0)
        self.grid_layout.addWidget(self.smooth_sb, 0, 1)
        self.grid_layout.addWidget(self.smooth_step_txt, 0, 2)

        self.setLayout(self.grid_layout)


class CompositionGroupBox(QtGui.QGroupBox):
    def __init__(self, *args):
        super(CompositionGroupBox, self).__init__("Composition", *args)
        self.create_widgets()

    def create_widgets(self):
        self.main_layout = QtGui.QVBoxLayout()

        self.button_layout = QtGui.QHBoxLayout()
        self.add_element_btn = QtGui.QPushButton("Add")
        self.delete_element_btn = QtGui.QPushButton("Delete")
        self.button_layout.addWidget(self.add_element_btn)
        self.button_layout.addWidget(self.delete_element_btn)

        self.density_layout = QtGui.QHBoxLayout()
        self.density_lbl = QtGui.QLabel("Density:")
        self.density_lbl.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        self.density_txt = QtGui.QLineEdit("2.2")
        self.density_txt.setAlignment(QtCore.Qt.AlignRight)
        self.density_txt.setValidator(QtGui.QDoubleValidator())
        self.density_txt.setMaximumWidth(100)
        self.density_layout.addWidget(self.density_lbl)
        self.density_layout.addWidget(self.density_txt)

        self.element_table = QtGui.QTableWidget()
        self.element_table.setColumnCount(2)

        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addWidget(self.element_table)
        self.main_layout.addLayout(self.density_layout)

        self.setLayout(self.main_layout)