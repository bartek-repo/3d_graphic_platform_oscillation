from tkinter import Frame, Entry


class InputText (Frame):
    def __init__(self, parent, item_color='white', background_color='grey', item_pad_x=0, item_pad_y=0, radius=0,
                 row=0, column=0, row_span=1, column_span=1):

        tk.Frame.__init__(self,parent)

        cn3ov1 = tk.Canvas(parent, bg=background_color, highlightthickness=0, width=radius * 2, height=radius * 2)
        cn3ov1.grid(row=row, column=column, padx=item_pad_x, pady=item_pad_y, sticky='nw')

        cn3ov2 = tk.Canvas(parent, bg=background_color, highlightthickness=0, width=radius * 2, height=radius * 2)
        cn3ov2.grid(row=row, column=column, padx=item_pad_x, pady=item_pad_y, sticky='sw')

        cn3ov3 = tk.Canvas(parent, bg=background_color, highlightthickness=0, width=radius * 2, height=radius * 2)
        cn3ov3.grid(row=row, column=column, padx=item_pad_x, pady=item_pad_y, sticky='se')

        cn3ov4 = tk.Canvas(parent, bg=background_color, highlightthickness=0, width=radius * 2, height=radius * 2)
        cn3ov4.grid(row=row, column=column, padx=item_pad_x, pady=item_pad_y, sticky='ne')

        cn3ov1.create_oval(0, 0, radius * 2, radius * 2, fill=item_color, outline=item_color)

        cn3ov2.create_oval(0, 0, radius * 2, radius * 2, fill=item_color, outline=item_color)

        cn3ov3.create_oval(0, 0, radius * 2, radius * 2, fill=item_color, outline=item_color)

        cn3ov4.create_oval(0, 0, radius * 2, radius * 2, fill=item_color, outline=item_color)

        cn = tk.Canvas(parent, bg=item_color, highlightthickness=0)
        cn2 = tk.Canvas(parent, bg=item_color, highlightthickness=0)

        cn.grid(row=row, column=column, columnspan=column_span, rowspan=row_span, padx=radius + item_pad_x,
                pady=item_pad_y, sticky='nswe')
        cn2.grid(row=row, column=column, columnspan=column_span, rowspan=row_span, pady=radius + item_pad_y,
                 padx=item_pad_x, sticky='nswe')

        frm = tk.Frame(parent)
        frm.grid(row=row, column=column, columnspan=column_span, padx=item_pad_x + radius / pow(2, 1 / 2),
                 pady=item_pad_y + radius / pow(2, 1 / 2), sticky='nswe')
        frm.grid_rowconfigure(0, weight=1)
        frm.grid_columnconfigure(0, weight=1)
        tl = Entry(frm)
        tl.grid(row=row, column=column, sticky='nswe')