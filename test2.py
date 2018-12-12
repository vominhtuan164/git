from PyQt5.QtWidgets import *
import sys


class Dialog(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		self.setWindowTitle("New state")
		layout = QGridLayout()
		self.setLayout(layout)
		label = QLabel("New state name :")
		layout.addWidget(label, 0, 0)
		state_name = QLineEdit()
		state_name.setPlaceholderText("New state name")
		layout.addWidget(state_name)
		initial = QCheckBox("Initial state")
		initial.setChecked(False)
		layout.addWidget(initial)
		buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
		layout.addWidget(buttons)
		buttons.accepted.connect(self.when_ok)
		buttons.rejected.connect(self.when_cancel)
		layout.setHorizontalSpacing(15)
		layout.setVerticalSpacing(10)
	def when_ok(self):
		if (self.initial.isChecked()):
			state_name.returnPressed.connect(new_initial_state(diagram, state_name.text(), pos_x=5, pos_y=5))
        #else:
		#	state_name.returnPressed.connect(new_normal_state(diagram, state_name.text(), pos_x=5, pos_y=5))
	def when_cancel():
		sys.exit()

app = QApplication(sys.argv)
screen = Dialog()
screen.show()
sys.exit(app.exec_())
