import unittest
import pytest
import tkinter as tk
from check_videos import CheckVideos


def setUpModule():
    global root
    root = tk.Tk()

def tearDownModule():
    global root
    root.update_idletasks()
    root.destroy()
    del root
    
class ToolTipBaseTest(unittest.TestCase):
    

    def test_base_class_is_unusable(self):
        global root
