"""
Entry point for the Clean Paste application.
Initializes and launches the CustomTkinter desktop interface.
"""

from gui import CleanPasteApp

def main():
    app = CleanPasteApp()
    app.mainloop()

if __name__ == "__main__":
    main()
