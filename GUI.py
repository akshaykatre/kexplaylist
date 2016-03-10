from Tkinter import Tk, W, IntVar, StringVar, Checkbutton
import kexplaylist
from datetime import datetime
import ttk
#from GUI_Reader import reader

class Application:
    # def decision(self):
    #     print self.check11.pack()

    def __init__(self, parent):
        self.parent = parent

        self.s_d = IntVar()
        self.s_m = IntVar()
        self.s_y = IntVar()
        self.s_h = IntVar()
        
        self.e_d = IntVar()
        self.e_m = IntVar()
        self.e_y = IntVar()
        self.e_h = IntVar()

        self.st_label = ttk.Label(self.parent, 
                                  text="Set Start Time").grid(column=0, 
                                                              row=0, sticky=W)
        
        self.sd_label = ttk.Label(self.parent, 
                                  text="Date").grid(column=0, row=1)
        
        self.s_d_entry = ttk.Combobox(self.parent, 
                                         textvariable=self.s_d, width=4)

        self.sm_label = ttk.Label(self.parent, 
                                  text="Month").grid(column=2, row=1)

        self.s_m_entry = ttk.Combobox(self.parent, 
                                      textvariable=self.s_m, width=4)

        self.sy_label = ttk.Label(self.parent, 
                                  text="Year").grid(column=4, row=1)
        self.s_y_entry = ttk.Combobox(self.parent, 
                                      textvariable=self.s_y, width=4)

        self.sh_label = ttk.Label(self.parent, 
                                  text="Hour").grid(column=6, row=1)

        self.s_h_entry = ttk.Combobox(self.parent, 
                                      textvariable=self.s_h, width=4)


        self.en_label = ttk.Label(self.parent, 
                                  text="Set End Time").grid(column=0, 
                                                            row=2, sticky=W)

        self.ed_label = ttk.Label(self.parent, 
                                  text="Date").grid(column=0, row=3)

        self.e_d_entry = ttk.Combobox(self.parent, 
                                      textvariable=self.e_d, width=4)

        self.em_label = ttk.Label(self.parent, 
                                  text="Month").grid(column=2, row=3)
        self.e_m_entry = ttk.Combobox(self.parent, 
                                      textvariable=self.e_m, width=4)

        self.ey_label = ttk.Label(self.parent, 
                                  text="Year").grid(column=4, row=3)
        self.e_y_entry = ttk.Combobox(self.parent, 
                                      textvariable=self.e_y, width=4)

        self.eh_label = ttk.Label(self.parent, 
                                  text="Hour").grid(column=6, row=3)
        self.e_h_entry = ttk.Combobox(self.parent, 
                                      textvariable=self.e_h, width=4)


        self.quit = ttk.Button(self.parent, text="Quit",  
                               command=self.parent.quit).grid(column = 0, 
                                                              row=10, sticky=W)

        self.print_excel = ttk.Button(self.parent, text="Make excel", 
                                  command=lambda : self.reader('excel')).grid(column = 2, 
                                                            row=10, sticky=W)

        self.print_csv = ttk.Button(self.parent, text="Make csv", 
                                  command=lambda : self.reader('csv')).grid(column = 4, 
                                                            row=10, sticky=W)


#        self.measureSystem = IntVar()
                         
        # self.check11 = Checkbutton(self.parent, text='Use Metric', 
        #                              command=self.decision, variable=self.measureSystem,
        #                              onvalue=1, offvalue=0)
        # self.check11.grid(column=1, row=5)
#        self.measureSystem.pack() 
        
        self.combo() 

    

    def reader(self, out_type):

        start_date = datetime(int(self.s_y_entry.get()), 
                              int(self.s_m_entry.get()), 
                              int(self.s_d_entry.get()), 
                              int(self.s_h_entry.get()))

        end_date = datetime(int(self.e_y_entry.get()), 
                            int(self.e_m_entry.get()), 
                            int(self.e_d_entry.get()), 
                            int(self.e_h_entry.get()))
        kexplaylist.Run_playlist(start_date, end_date, out_type)
        
    def combo(self):
        
        self.s_d_entry['values'] = range(1, 32)
        self.s_d_entry.grid(column=1, row=1)


        self.s_m_entry['values'] = range(1, 12)
        self.s_m_entry.grid(column=3, row=1)
        

        self.s_y_entry['values'] = range(2000, 2015)
        self.s_y_entry.grid(column=5, row=1)
        
        self.s_h_entry['values'] = range(00, 24)
        self.s_h_entry.grid(column=7, row=1)
        
        

        self.e_d_entry['values'] = range(1, 32)
        self.e_d_entry.grid(column=1, row=3)
        
        self.e_m_entry['values'] = range(1, 12)
        self.e_m_entry.grid(column=3, row=3)
        
        self.e_y_entry['values'] = range(2000, 2015)
        self.e_y_entry.grid(column=5, row=3)
        

        self.e_h_entry['values'] = range(00, 24)
        self.e_h_entry.grid(column=7, row=3)
        

        

if __name__  == '__main__':
    ROOT = Tk()
    ROOT.title("KEXP playlist")
    APP = Application(ROOT)
    ROOT.mainloop()



