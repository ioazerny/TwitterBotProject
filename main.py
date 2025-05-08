import tkinter as tk
from gui import TwitterBotGUI

def main():
    root = tk.Tk()
    root.title("Twitter Bot")
    root.geometry("400x300")  # Adjust size as needed
    app = TwitterBotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
