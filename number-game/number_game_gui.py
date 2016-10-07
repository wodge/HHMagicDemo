import tkinter as tk
from tkinter import ttk
import random

usr_name = 'Test'

LARGE_FONT= ("Verdana", 12)
SMALL_FONT = ("Verdana", 9)

class NumberGameApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        self.minsize(width=300, height=200)

        tk.Tk.wm_title(self, "Number Game App")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame = frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font = LARGE_FONT)
        label.pack(pady=20)

        entry_label = tk.Label(self, text="Enter your name", font = SMALL_FONT)
        entry_label.pack()

        global usr_name
        usr_name = tk.StringVar()
        name_entry = tk.Entry(self, textvariable= usr_name)
        name_entry.pack(pady=5, padx=5)

        button = ttk.Button(self, text="Lets Play!",
                           command=lambda: controller.show_frame(PageOne))

        button.pack(pady=5, padx=5)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        difficulty = 1
        com_num, high_num = self.generate_num(difficulty)

        print_var = tk.StringVar()
        print_var.set('I am thinking of a number between 1 and {}'.format(high_num))
        output_label = tk.Label(self, textvariable= print_var, font=SMALL_FONT)
        output_label.pack(pady=15)

        guess_label = tk.Label(self, text="Take a guess", font = SMALL_FONT)
        guess_label.pack()

        guess = tk.IntVar()
        guess_entry = tk.Entry(self, textvariable=guess)
        guess_entry.pack()

        button2 = ttk.Button(self, text="Enter",
                            command= lambda: self.check_num(print_var, high_num, com_num, guess.get()))
        button2.pack(pady=5, padx=5)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(pady=5, padx=5)

    def test1(self, var):
        var.set('did this work? {}'.format(usr_name.get()))
        return var

    def game_loop(self, user_name):
        pass

    def generate_num(self, difficulty):
        high_num = difficulty * 20
        com_num = random.randint(1, high_num)
        return com_num, high_num


    def check_num(self, print_var, high_num, com_num, guess):
        try:
            if 1 <= guess <= high_num:
                if guess < com_num:
                    print_var.set("Too Low.")
                    return print_var
                elif guess > com_num:
                    print_var.set("Too High.")
                    return print_var
                if com_num == guess:
                    print_var.set("Way to go!")
                    return print_var
            else:
                print_var.set("Invalid input.")
                return print_var
        except ValueError:
            print_var.set("Invalid input.")
            return print_var


def main():

    app = NumberGameApp()
    app.mainloop()

if __name__ == '__main__':
    main()