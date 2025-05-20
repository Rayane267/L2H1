from sys import platform

if platform == "win32":
    import src.Menu.menu as menu
else:
    import Menu.menu as menu

def init():
    print("Space Relations script")
    print("By Asma Baitiche, Onur Basci, Hugo Demaret, Rayanne Taleb")
    menu.menu()
    print("Good Bye !")

if __name__ == "__main__":
    init()