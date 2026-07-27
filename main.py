from tkinter import Tk, Label


def main():
    root = Tk()
    root.title("Sales OS")
    root.geometry("1000x700")

    Label(
        root,
        text="Sales OS\nПервая рабочая версия",
        font=("Segoe UI", 20)
    ).pack(expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()