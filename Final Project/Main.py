import sys
from GUI import Gui

sys.setrecursionlimit(2000)     # Increasing the recursion limit so the RecursiveWalk solutions may run without errors.

gui: Gui = Gui()
gui.run_gui_loop()
