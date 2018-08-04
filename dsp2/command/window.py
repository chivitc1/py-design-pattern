import sys

"""Receivers"""
class Window:
    def exit(self):
        print("Exit")
        sys.exit(0)

class Document:
    def __init__(self, filename):
        self.filename = filename
        self.content = "This file cannot be modified"

    def save(self):
        with open(self.filename, 'w') as file:
            file.write(self.content)
        print("Saved")


"""Invokers"""

class ToolBarButton:
    def __init__(self, name, iconname):
        self.name = name
        self.iconname =iconname

    def click(self):
        print(self.command, "click")
        self.command.execute()

class MenuItem:
    def __init__(self, menu_name, menuitem_name):
        self.menu = menu_name
        self.item = menuitem_name

    def click(self):
        print(self.command, "click")
        self.command.execute()

class KeyboardShortcut:
    def __init__(self, key, modifier):
        self.key = key
        self.modifier = modifier

    def keypress(self):
        print(self.command, "keypress")
        self.command.execute()

"""Commands"""
class SaveCommand:
    def __init__(self, document):
        self.document = document

    def execute(self):
        self.document.save()

class ExitCommand:
    def __init__(self, window):
        self.window = window

    def execute(self):
        self.window.exit()

"""Test"""
def test():
    # Create receivers
    window = Window()
    document = Document("a_doc.txt")

    # Create a command with a receiver
    save_cmd = SaveCommand(document)
    exit_cmd = ExitCommand(window)

    # Create a receiver and later set the command property
    save_btn = ToolBarButton('save', 'save.png')
    save_btn.command = save_cmd

    save_keystroke = KeyboardShortcut("s", "ctrl")
    save_keystroke.command = save_cmd

    exit_menu = MenuItem("File", "Exit")
    exit_menu.command = exit_cmd

    save_keystroke.keypress()
    exit_menu.click()


test()