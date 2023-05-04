import tkinter as tk
import logging

logger = logging.getLogger(__name__)


class Container(tk.Frame):
    widgets = {}

    def __init__(self, master, bd=2, relief=tk.GROOVE):
        super().__init__(master, relief=relief, bd=bd)
        self.columnconfigure(0, weight=1)
        logger.debug(f"{__class__.__name__}'s master: {self.master}")

    def generate_ui(self, widgets):
        for cur_loc, widget in enumerate(widgets):
            logger.info(f"Instantiating a {widget['widget']}")
            self.widgets[widget['name']] = widget['widget'](self,
                                                            text=widget['label'])

            if type(widget['widget']) is tk.Entry:
                widget['widget'].config(textvariable=widget['value'])

            self.widgets[widget['name']].grid(row=cur_loc,
                                              column=0,
                                              sticky=widget.get('sticky', 'new'),
                                              padx=widget.get('padx', 20),
                                              pady=widget.get('pady', 20))

            if widget.get('focus'):
                self.widgets[widget['name']].focus_set()


class StackedEntry(tk.Frame):

    def __init__(self, master, text="", textvariable=None):
        super().__init__(master)

        self.columnconfigure(0, weight=1)
        self['bg'] = '#ffc0c0'

        self.lbl_entry = tk.Label(self)
        self.txt_entry = tk.Entry(self, textvariable=textvariable)

        self.lbl_entry['text'] = text
        self.lbl_entry.grid(row=0, column=0, sticky='nsew')
        self.txt_entry.grid(row=1, column=0, sticky='nsew')

        # Force this widget to set the focus to the entry
        # box when called.
        self.focus_set = self.txt_entry.focus_set
