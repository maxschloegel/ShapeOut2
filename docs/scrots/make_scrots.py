"""Screenshots for documentation

Data available at https://doi.org/10.6084/m9.figshare.11302595.v1
"""

import pathlib
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from shapeout2.gui.main import ShapeOut2
from shapeout2 import session

app = QApplication(sys.argv)

QtCore.QLocale.setDefault(QtCore.QLocale(QtCore.QLocale.C))

mw = ShapeOut2()

# build up a session
session.open_session(pathlib.Path(__file__).parent / "scrots.so2",
                     pipeline=mw.pipeline)
mw.reload_pipeline()

# block matrix
mw.block_matrix.setFixedSize(425, 350)
mw.block_matrix.repaint()
QApplication.processEvents()
mw.block_matrix.scrollArea_block.grab().save("_block_matrix.png")

# analysis view
mw.on_modify_slot(mw.pipeline.slot_ids[0])
mw.widget_ana_view.repaint()
QApplication.processEvents()
mw.widget_ana_view.grab().save("_ana_slot.png")

mw.on_modify_filter(mw.pipeline.filter_ids[0])
mw.widget_ana_view.repaint()
QApplication.processEvents()
mw.widget_ana_view.grab().save("_ana_filter.png")

mw.on_modify_plot(mw.pipeline.plot_ids[0])
mw.widget_ana_view.repaint()
QApplication.processEvents()
mw.widget_ana_view.grab().save("_ana_plot.png")

mw.widget_ana_view.tabWidget.setCurrentIndex(0)
mw.widget_ana_view.repaint()
QApplication.processEvents()
mw.widget_ana_view.grab().save("_ana_meta.png")

# plots
mw.subwindows_plots[mw.pipeline.plot_ids[0]].widget().grab().save("_plot1.png")
mw.subwindows_plots[mw.pipeline.plot_ids[1]].widget().grab().save("_plot2.png")
mw.subwindows_plots[mw.pipeline.plot_ids[2]].widget().grab().save("_plot3.png")

mw.close()
