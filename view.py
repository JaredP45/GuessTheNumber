import tkinter as tk
import tkinter as ttk
from tkinter.messagebox import showerror

import GameLoop as gL

root = tk.Tk()


def submit_clicked():
    try:
        score = 0
        count = 0
        rand_list = str(gL.generate_rand_list())
        dup_check = []

        while count < 5:
            user_int = entry.get()

            if int(user_int) > 9:
                raise gL.ValueNotInRange
            elif user_int in rand_list:
                if user_int in dup_check:
                    raise gL.DuplicateValue
                else:
                    dup_check.append(user_int)
                    result = gL.display_num_or_star(rand_list, dup_check)
                    count += 1
                    score += 1
            else:
                result = gL.display_num_or_star(rand_list, dup_check)
                count += 1

            result_label.config(text=result)
    except gL.ValueNotInRange:
        showerror(title='Incorrect value.', message='You number must be 9 or less.')
    except gL.DuplicateValue:
        showerror(title='Value already exists.', message='Correct number already exists.')
    finally:
        showerror(title='Unknown Error.', message='Unknown error has occurred.')


root.title('Guess the Number')
window_width = 300
window_height = 200

# screen dimension
screen_width = root.winfo_screenwidth()

screen_height = root.winfo_screenheight()
# center point
center_x = int(screen_width/2 - window_width / 2)

center_y = int(screen_height/2 - window_height / 2)
# set the position of the window to the center of the screen

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
frame = ttk.Frame(root)

options = {'padx': 5, 'pady': 5}
display_list = ttk.Label(frame)

display_list.grid(row=1, columnspan=3, **options)
entry = tk.StringVar()

user_entry = ttk.Entry(frame, textvariable=entry)
user_entry.grid(column=1, row=0, **options)
user_entry.focus()

submit = ttk.Button(frame, text='Enter Value')
submit.grid(column=2, row=0, sticky='W', **options)
submit.configure(command=submit_clicked)

result_label = ttk.Label(frame)
result_label.grid(row=1, columnspan=3, **options)

frame.grid(padx=10, pady=10)

root.mainloop()
