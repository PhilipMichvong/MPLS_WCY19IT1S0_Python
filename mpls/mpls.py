import frontend.gui as gui
import backend.controller as ctl

def main():
    global app
    app = gui.GUI()
    app.run()

if __name__ == '__main__':
    main()
