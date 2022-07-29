import os
try:
    print("packages working contact boss")
    import tkinter
    from tkinter import *
    import os
    import PyPDF2
    import time
    import tkinter.messagebox
    from PIL import ImageTk, Image
    import tkinter as tk
except:
    try:
        print("installing packages")
        os.system("pip install tk")
        os.system("pip install PyPDF2")
        os.system("pip install Image")
        os.system("pip install Pillow")
    except:
        print("failed -- pip or python not installed on computer")
        f = open("FPsolve error.txt","w")
        f.write("failed -- pip or python not installed on computer \n contact boss")
        f.close()
        quit()
