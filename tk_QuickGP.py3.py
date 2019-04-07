#!/usr/bin/env python3
import tkinter as tk
# Author: StpircsDahc
# Author's github repo - https://github.com/stpircsdahc
#######################################################
# credit to Bryson Tyrrell for his excellent demo
# Bryson's video - https://www.youtube.com/watch?v=Wb1YFgHqUZ8
# Bryson's github repo for his demo - https://github.com/brysontyrrell/MacAdmins-2016-Craft-GUIs-with-Python-and-Tkinter
#######################################################



class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title("Quick GP Calculator")
        self.master.resizable(False, False)
        self.master.tk_setPalette(background='#4286f4')

        self.master.protocol('WM_DELETE_WINDOW', self.click_exit)
        self.master.bind('<Return>', self.click_calc)
        self.master.bind('<Escape>', self.click_clear)
        self.master.bind('<x>', self.click_exit)

        x = (self.master.winfo_screenwidth() - self.master.winfo_reqwidth()) // 2
        y = (self.master.winfo_screenheight() - self.master.winfo_reqheight()) // 2
        self.master.geometry("+{}+{}".format(x, y))

        self.master.config(menu=tk.Menu(self))

        dialog_frame = tk.Frame(self)
        dialog_frame.pack(padx=20, pady=15, anchor='w')

        tk.Label(dialog_frame, text='MSRP - List Price').grid(row=0, column=0, sticky='w')
        self.lPrice_input = tk.Entry(dialog_frame, background='black', bd=5, fg = 'green', width=24)
        self.lPrice_input.grid(row=0, column=1, sticky='w')
        self.lPrice_input.focus_set()

        tk.Label(dialog_frame, text='Discount Percentage').grid(row=1, column=0, sticky='w')
        self.discount_input = tk.Entry(dialog_frame, background='black', bd=5, fg = 'green', width=24)
        self.discount_input.grid(row=1, column=1, sticky='w')

        self.dPriceVar = tk.StringVar()
        self.dPriceVar.set('          $ 0.00')
        tk.Label(dialog_frame, text = 'Discounted price is:').grid(row=3, column=0, sticky='w')
        tk.Label(dialog_frame, textvariable = self.dPriceVar).grid(row=3, column=1, sticky='w')

        tk.Label(dialog_frame, text='Markup Percentage').grid(row=4, column=0, sticky='w')
        self.markup_input = tk.Entry(dialog_frame, background='black', bd=5, fg = 'green', width=24)
        self.markup_input.grid(row=4, column=1, sticky='w')

        self.fPriceVar = tk.StringVar()
        self.fPriceVar.set('          $ 0.00')
        tk.Label(dialog_frame, text = 'Marked-up price is:').grid(row=5, column=0, sticky='w')
        tk.Label(dialog_frame, textvariable = self.fPriceVar).grid(row=5, column=1, sticky='w')

        self.gpVar = tk.StringVar()
        self.gpVar.set('          $ 0.00')
        tk.Label(dialog_frame, text = 'Gross Profit on sale:').grid(row=6, column=0, sticky='w')
        tk.Label(dialog_frame, textvariable = self.gpVar).grid(row=6, column=1, sticky='w')

        button_frame = tk.Frame(self)
        button_frame.pack(padx=15, pady=(0, 15), anchor='e')

        tk.Button(button_frame, text='Exit (x)', height=1, width=6, bd=5, bg='red', command=self.click_exit).pack(side='right', padx=10)
        tk.Button(button_frame, text='Clear All (Esc)', height=1, width=15, bd=5, bg='#808384', command=self.click_clear).pack(side='right', padx=10)
        tk.Button(button_frame, text='Calculate (Enter)', height=1, width=15, bd=5, bg='#808384', fg='green', command=self.click_calc).pack(side='right', padx=10)

    def click_calc(self, event=None):
        if self.lPrice_input.get() and self.discount_input.get() and self.markup_input.get():
            discountPrice = self.discountit(self.lPrice_input.get(), self.discount_input.get())
            self.markitup(discountPrice, self.markup_input.get())
        elif self.lPrice_input.get() and self.discount_input.get():
            discountPrice = self.discountit(self.lPrice_input.get(), self.discount_input.get())
        else:
            pass

    def click_clear(self, event = None):
        self.lPrice_input.delete(0, 'end')
        self.discount_input.delete(0, 'end')
        self.markup_input.delete(0, 'end')
        self.dPriceVar.set('          $ 0.00')
        self.fPriceVar.set('          $ 0.00')
        self.lPrice_input.focus_set()


    def click_exit(self, event=None):
        self.master.destroy()

    def discountit(self, cost, discount):
        dPercentage = float(discount)/100.0
        salePrice = float(cost) - (float(cost) * dPercentage)
        salePrice = round(salePrice, 2)
        saleString = '          $ ' +str(salePrice)
        self.dPriceVar.set(saleString)
        return salePrice

    def markitup(self, cost, markup):
        muPercentage = float(markup)/100.0
        salePrice = float(cost) + (float(cost) * muPercentage)
        salePrice = round(salePrice, 2)
        saleString = '          $ ' +str(salePrice)
        self.fPriceVar.set(saleString)
        gp = round(salePrice - cost, 2)
        gpString = '          $ ' +str(gp)
        self.gpVar.set(gpString)



if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()
