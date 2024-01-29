from tkinter import *
from tkinter.ttk import Combobox

class Window:
    def __init__(self, width, height, title='MyWindow', resizable=(False, False)):
        self.root = Tk()
        self.root.title(title)
        self.root.resizable(resizable[0], resizable[1])
        self.root['bg'] = '#fafafa'
        self.root.wm_attributes('-alpha', 0.9)
        self.root.geometry('450x700')

    def draw_widgets(self):
        def sngsizes(event):
            sngindex = self.sngsizes.current()
            self.sngsizes.current(sngindex)
            self.ussizes.current(sngindex)
            self.grsizes.current(sngindex)
            self.uksizes.current(sngindex)
            self.frsizes.current(sngindex)

            self.asizes.current(sngindex)
            self.bsizes.current(sngindex)
            self.csizes.current(sngindex)
            self.dsizes.current(sngindex)
            self.esizes.current(sngindex)
            self.fsizes.current(sngindex)
        def ussizes(event):
            usindex = self.ussizes.current()
            self.sngsizes.current(usindex)
            self.ussizes.current(usindex)
            self.grsizes.current(usindex)
            self.uksizes.current(usindex)
            self.frsizes.current(usindex)

            self.asizes.current(usindex)
            self.bsizes.current(usindex)
            self.csizes.current(usindex)
            self.dsizes.current(usindex)
            self.esizes.current(usindex)
            self.fsizes.current(usindex)
        def grsizes(event):
            grindex = self.grsizes.current()
            self.sngsizes.current(grindex)
            self.ussizes.current(grindex)
            self.grsizes.current(grindex)
            self.uksizes.current(grindex)
            self.frsizes.current(grindex)

            self.asizes.current(grindex)
            self.bsizes.current(grindex)
            self.csizes.current(grindex)
            self.dsizes.current(grindex)
            self.esizes.current(grindex)
            self.fsizes.current(grindex)
        def uksizes(event):
            ukindex = self.uksizes.current()
            self.sngsizes.current(ukindex)
            self.ussizes.current(ukindex)
            self.grsizes.current(ukindex)
            self.uksizes.current(ukindex)
            self.frsizes.current(ukindex)

            self.asizes.current(ukindex)
            self.bsizes.current(ukindex)
            self.csizes.current(ukindex)
            self.dsizes.current(ukindex)
            self.esizes.current(ukindex)
            self.fsizes.current(ukindex)
        def frsizes(event):
            frindex = self.frsizes.current()
            self.sngsizes.current(frindex)
            self.ussizes.current(frindex)
            self.grsizes.current(frindex)
            self.uksizes.current(frindex)
            self.frsizes.current(frindex)
    
            self.asizes.current(frindex)
            self.bsizes.current(frindex)
            self.csizes.current(frindex)
            self.dsizes.current(frindex)
            self.esizes.current(frindex)
            self.fsizes.current(frindex)
        
        def asizes(event):
            aindex = self.asizes.current()
            self.sngsizes.current(aindex)
            self.ussizes.current(aindex)
            self.grsizes.current(aindex)
            self.uksizes.current(aindex)
            self.frsizes.current(aindex)

            self.asizes.current(aindex)
            self.bsizes.current(aindex)
            self.csizes.current(aindex)
            self.dsizes.current(aindex)
            self.esizes.current(aindex)
            self.fsizes.current(aindex)
        def bsizes(event):
            bindex = self.bsizes.current()
            self.sngsizes.current(bindex)
            self.ussizes.current(bindex)
            self.grsizes.current(bindex)
            self.uksizes.current(bindex)
            self.frsizes.current(bindex)

            self.asizes.current(bindex)
            self.bsizes.current(bindex)
            self.csizes.current(bindex)
            self.dsizes.current(bindex)
            self.esizes.current(bindex)
            self.fsizes.current(bindex)
        def csizes(event):
            cindex = self.csizes.current()
            self.sngsizes.current(cindex)
            self.ussizes.current(cindex)
            self.grsizes.current(cindex)
            self.uksizes.current(cindex)
            self.frsizes.current(cindex)

            self.asizes.current(cindex)
            self.bsizes.current(cindex)
            self.csizes.current(cindex)
            self.dsizes.current(cindex)
            self.esizes.current(cindex)
            self.fsizes.current(cindex)
        def dsizes(event):
            dindex = self.dsizes.current()
            self.sngsizes.current(dindex)
            self.ussizes.current(dindex)
            self.grsizes.current(dindex)
            self.uksizes.current(dindex)
            self.frsizes.current(dindex)

            self.asizes.current(dindex)
            self.bsizes.current(dindex)
            self.csizes.current(dindex)
            self.dsizes.current(dindex)
            self.esizes.current(dindex)
            self.fsizes.current(dindex)
        def esizes(event):
            eindex = self.esizes.current()
            self.sngsizes.current(eindex)
            self.ussizes.current(eindex)
            self.grsizes.current(eindex)
            self.uksizes.current(eindex)
            self.frsizes.current(eindex)
    
            self.asizes.current(eindex)
            self.bsizes.current(eindex)
            self.csizes.current(eindex)
            self.dsizes.current(eindex)
            self.esizes.current(eindex)
            self.fsizes.current(eindex)
        def fsizes(event):
            findex = self.fsizes.current()
            self.sngsizes.current(findex)
            self.ussizes.current(findex)
            self.grsizes.current(findex)
            self.uksizes.current(findex)
            self.frsizes.current(findex)
    
            self.asizes.current(findex)
            self.bsizes.current(findex)
            self.csizes.current(findex)
            self.dsizes.current(findex)
            self.esizes.current(findex)
            self.fsizes.current(findex)

        frame1 = Frame(self.root)
        frame1.grid(column=0, row=0, ipadx=6, ipady=6, padx=14, pady=14)

        frame2 = Frame(self.root)
        frame2.grid(column=1, row=0, ipadx=6, ipady=6, padx=14, pady=14)

        frame3 = Frame(self.root)
        frame3.grid(columnspan=2, row=1, ipadx=6, ipady=6, padx=14, pady=14)

        frame4 = Frame(self.root)
        frame4.grid(column=0, row=2, ipadx=6, ipady=6, padx=14, pady=14)

        frame5 = Frame(self.root)
        frame5.grid(column=1, row=2, ipadx=6, ipady=6, padx=14, pady=14)

        title1 = Label(frame1, padx=20, pady=10, text='Россия и Украина', font=80).grid()
        title2 = Label(frame1, padx=20, pady=10, text='США', font=80).grid()
        title3 = Label(frame1, padx=20, pady=10, text='Германия', font=80).grid()
        title4 = Label(frame1, padx=20, pady=10, text='Англия', font=80).grid()
        title5 = Label(frame1, padx=20, pady=10, text='Франция', font=80).grid()

        self.sngsizes = Combobox(frame2, values=(42,44,46,48,50,52,54,56,58), width=15, height=25)
        self.ussizes = Combobox(frame2, values=('XXS','XS','S','M','L','XL','XXL','2XL','3XL'), width=15, height=25)
        self.grsizes = Combobox(frame2, values=(36,38,40,42,44,46,48,50,52), width=15, height=25)
        self.uksizes = Combobox(frame2, values=(4,6,8,10,12,14,16,18,20), width=15, height=25)
        self.frsizes = Combobox(frame2, values=(36,38,40,42,44,46,48,50,52), width=15, height=25)
        
        self.sngsizes.bind("<<ComboboxSelected>>", sngsizes)
        self.ussizes.bind("<<ComboboxSelected>>", ussizes)
        self.grsizes.bind("<<ComboboxSelected>>", grsizes)
        self.uksizes.bind("<<ComboboxSelected>>", uksizes)
        self.frsizes.bind("<<ComboboxSelected>>", frsizes)

        self.sngsizes.current(0)
        self.sngsizes.pack(anchor=NW, padx=6, pady=11)

        self.ussizes.current(0)
        self.ussizes.pack(anchor=NW, padx=6, pady=11)

        self.grsizes.current(0)
        self.grsizes.pack(anchor=NW, padx=6, pady=11)

        self.uksizes.current(0)
        self.uksizes.pack(anchor=NW, padx=6, pady=11)

        self.frsizes.current(0)
        self.frsizes.pack(anchor=NW, padx=6, pady=11)
    
        title6 = Label(frame3, padx=20, pady=10, text='Физические параметры', font=80).pack()

        title1 = Label(frame4, padx=20, pady=10, text='Рост (см)', font=80).grid()
        title2 = Label(frame4, padx=20, pady=10, text='Обхват груди (см)', font=80).grid()
        title3 = Label(frame4, padx=20, pady=10, text='Обхват талии (см)', font=80).grid()
        title4 = Label(frame4, padx=20, pady=10, text='Обхват бедер (см)', font=80).grid()
        title5 = Label(frame4, padx=20, pady=10, text='Длина руки (см)', font=80).grid()
        title6 = Label(frame4, padx=20, pady=10, text='Длина ноги (см)', font=80).grid()

        self.asizes = Combobox(frame5, values=('160-163','162-165','164-167','166-169','168-171','170-173','172-175','174-177','176-179'), width=15, height=25)
        self.bsizes = Combobox(frame5, values=('82-85','86-89','90-93','94-97','98-101','102-105','106-109','110-113','114-117'), width=15, height=25)
        self.csizes = Combobox(frame5, values=('58-62', '61-65','64-68','67-71','70-74','73-77','76-80','79-83','82-86'), width=15, height=25)
        self.dsizes = Combobox(frame5, values=('86-90','89-93','92-96','95-99','98-102','101-105','104-108','107-111','110-114'), width=15, height=25)
        self.esizes = Combobox(frame5, values=(72,75,77,80,82,85,87,90,92), width=15, height=25)
        self.fsizes = Combobox(frame5, values=('101-104','102-105','103-106','104-107','105-108','106-109','107-110','108-111','109-112'), width=15, height=25)

        self.asizes.bind("<<ComboboxSelected>>", asizes)
        self.bsizes.bind("<<ComboboxSelected>>", bsizes)
        self.csizes.bind("<<ComboboxSelected>>", csizes)
        self.dsizes.bind("<<ComboboxSelected>>", dsizes)
        self.esizes.bind("<<ComboboxSelected>>", esizes)
        self.fsizes.bind("<<ComboboxSelected>>", fsizes)

        self.asizes.current(0)
        self.asizes.pack(anchor=SE, padx=6, pady=11)

        self.bsizes.current(0)
        self.bsizes.pack(anchor=SE, padx=6, pady=11)

        self.csizes.current(0)
        self.csizes.pack(anchor=SE, padx=6, pady=11)

        self.dsizes.current(0)
        self.dsizes.pack(anchor=SE, padx=6, pady=11)

        self.esizes.current(0)
        self.esizes.pack(anchor=SE, padx=6, pady=11)

        self.fsizes.current(0)
        self.fsizes.pack(anchor=SE, padx=6, pady=11)
    
    def run(self):
        self.draw_widgets()
        self.root.mainloop()

if __name__ == "__main__":
    window = Window(800, 720, "КАЛЬКУЛЯТОР ЖЕНСКОЙ ОДЕЖДЫ")
    window.run()