import tkinter
import re
from os import fsync
import configparser
import subprocess


class SpiboxTk(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def write_spibox_config(self):
        conf = configparser.ConfigParser()
        conf.read('/home/pi/spibox/spibox.conf')
        conf.set('email', 'emailsubject', self.emailsubject.get())
        conf.set('email', 'on', self.emailon.get())
        conf.set('email', 'emailrecipient', self.emailrecipient.get())
        with open('/home/pi/spibox/spibox.conf', 'wt') as configfile:
            conf.write(configfile)

    def write_config(self):
        self.write_spibox_config()
        self.quit()

    def test_email(self):
        subprocess.call(
            ['mpack', '-s', self.emailsubject.get(), '-c', 'image/jpeg', '/home/pi/spibox/capture/test.image',
             self.emailrecipient.get()])

    def initialize(self):
        self.emailsubject = tkinter.StringVar()
        self.emailrecipient = tkinter.StringVar()
        self.emailon = tkinter.StringVar()

        def make_entry(parent, caption, rw, **options):
            tkinter.Label(parent, text=caption).grid(column=0, row=rw, sticky="EW")
            entry = tkinter.Entry(parent, width=40, **options).grid(column=1, row=rw, sticky="EW")
            return entry

        def make_radio_button(parent, caption, rw, col, **options):
            if col == 1:
                tkinter.Label(parent, text=caption).grid(column=0, row=rw, sticky="EW")
            button = tkinter.Radiobutton(parent, **options).grid(column=col, row=rw, sticky="EW")

        def read_spiBox_config(self):
            spiboxConf = configparser.ConfigParser()
            spiboxConf.read('/home/pi/spibox/spibox.conf')
            text = spiboxConf.get('email', 'emailsubject')
            self.emailsubject.set(text)
            text = spiboxConf.get('email', 'emailrecipient')
            self.emailrecipient.set(text)
            text = spiboxConf.get('email', 'on')
            self.emailon.set(text)

        self.grid()
        self.lbl_email = tkinter.Label(self, text="Email Configuration")
        self.lbl_email.grid(column=1, row=0, sticky='EW')
        self.ent_emailOn = make_radio_button(self, "Email configuration", 1, 1, text="Email Off",
                                           variable=self.emailon, value='NO')
        self.ent_emailOn = make_radio_button(self, "Email configuration", 1, 2, text="Email On",
                                           variable=self.emailon, value='YES')
        self.ent_emailsubject = make_entry(self, "Email subject", 2, textvariable=self.emailsubject)
        self.ent_emailrecipient = make_entry(self, "Email recipient", 3, textvariable=self.emailrecipient)
        bt_test_email = tkinter.Button(self, text="Test Email", command=lambda: SpiboxTk.test_email(self))
        bt_test_email.grid(column=1, row=16)
        self.bt_save_and_close = tkinter.Button(self, text="Save and Quit",
                                                command=lambda: SpiboxTk.write_config(self))
        self.bt_save_and_close.grid(column=1, row=26)

        read_spiBox_config(self)

# check to make sure module is run as a program instead of being imported
# if imported from another module __name__ will be set to modules name and not run.
if __name__ == "__main__":
    app = SpiboxTk(None)
    app.title('SPi-Box Setup')
    app.mainloop()

