import tkinter.ttk

import news
import NewsItem
from tkinter import *

tk = Tk()
tk.geometry("520x700")

# Create main frame
main_frame = Frame(tk)
main_frame.pack(fill=BOTH,expand=1)

# Create Canvas
my_canvas = Canvas(main_frame,bg="#FFFFFF")
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

# Add scrollbar to canvas
my_scrollbar = tkinter.ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)

# Configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_scrollbar.bind("<Configure>",lambda e: my_canvas.configure(scrollregion= my_canvas.bbox("all")))

# Create Another Frame Inside canvas
second_frame = Frame(my_canvas,bg="#FFFFFF")

# Add frame to window in canvas
my_canvas.create_window((0,0),window=second_frame,anchor="nw")

news_data = news.getNews()

for x in news_data:
    frame = NewsItem.NewsItem(second_frame,news=x)
    frame.configure(bg="#ffffff",highlightbackground="black",highlightthickness=1.)
    frame.pack(fill=BOTH)

tk.mainloop()
