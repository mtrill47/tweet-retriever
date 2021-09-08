import tkinter as tk
import retriever_for_interface
def close_app():
    window.destroy()


def bufffer(event):
    if len(search1.get()) > 100: search1.set(search1.get()[:100])


def search_tweets():
    username = str(username_entry.get())
    password = str(password_entry.get())
    search = str(search_entry.get())

    print("Retrieving tweets")
    retriever_for_interface.get_info(username, password, search)
    retriever_for_interface.main()
    

window = tk.Tk()

window.title("Tweet Retriever by mtrill")
frame_header = tk.Frame(master= window, borderwidth =2, pady =2)
frame_center = tk.Frame(window, borderwidth =2, pady = 5)
frame_bottom = tk.Frame(window, borderwidth=2, pady=5)
frame_header.grid(row=0, column=0)
frame_center.grid(row=1, column=0)
frame_bottom.grid(row=2, column=0)

header = tk.Label(frame_header, text="Tweet Retriever", bg='#1E9CD8', fg='white', height='3', width='50', font=("Helvetica 16 italic"))
header.grid(row=0, column=0)

frame_main_1 = tk.Frame(frame_center, borderwidth=2, relief='raised')
frame_main_2 = tk.Frame(frame_center, borderwidth=2, relief='raised')
frame_main_3 = tk.Frame(frame_center, borderwidth=2, relief='raised')

username = tk.Label(frame_main_1, text="Username:    ",)
password = tk.Label(frame_main_2, text="Password:     ")
search = tk.Label(frame_main_3, text="Search term: ",)

username1 = tk.StringVar()
password1 = tk.StringVar()
search1 = tk.StringVar()

username_entry = tk.Entry(frame_main_1, textvariable=username1, width = 30)
password_entry = tk.Entry(frame_main_2, textvariable=password1, width=30)
search_entry = tk.Entry(frame_main_3,textvariable=search1, width=30)
search_entry.bind("<KeyRelease>", bufffer)

button_search = tk.Button(frame_bottom, text="Search", command=search_tweets, bg='#1E9CD8', fg='white', relief='raised', width = 10, font=("Helvetica 10 bold"))
button_search.grid(column=0, row=0, sticky='w', padx=100, pady=2)

button_close = tk.Button(frame_bottom, text="Exit", command=close_app, bg='#E50707', fg='white', relief='raised', width = 10, font=("Helvetica 10 bold"))
button_close.grid(column=1, row=0, sticky='e', padx=100, pady=2)

frame_main_1.pack(fill='x', pady=3)
frame_main_2.pack(fill='x', pady=3)
frame_main_3.pack(fill='x', pady=3)
username.pack(side="left")
username_entry.pack(side="left", padx=1)
password.pack(side="left")
password_entry.pack(side="left", padx=1)
search.pack(side="left")
search_entry.pack(side="left", padx=1)

window.mainloop()