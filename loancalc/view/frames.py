import tkinter as tk
import tkinter.ttk as ttk
import loancalc.view.widgets as widgets
import logging

logger = logging.getLogger(__name__)


class LoanConfigurationFrame(widgets.Container):

    def __init__(self, master):
        super().__init__(master)
        self.__widgets = [
            {'name': 'test1',
             'label': 'Test Entry 1:',
             'widget': widgets.StackedEntry,
             'value': tk.StringVar(),
             'focus': True
             },
            {'name': 'test2',
             'label': 'Test Entry 2:',
             'widget': widgets.StackedEntry,
             'value': tk.StringVar(),
             },
            {'name': 'test3',
             'label': 'Test Entry 3:',
             'widget': widgets.StackedEntry,
             'value': tk.StringVar(),
             },
            {'name': 'testbutton',
             'label': 'Click Me',
             'widget': tk.Button,
             'sticky': 'sew'
             },
            {'name': 'testbutton2',
             'label': 'Click Me 2',
             'widget': tk.Button,
             'sticky': 'sew'
             }
        ]

        self.generate_ui(self.__widgets)


class ResultsGridFrame(widgets.Container):

    def __init__(self, master):
        super().__init__(master)

        columns = ('current_month',
                   'current_balance',
                   'current_interest',
                   'current_principal',
                   'additional_principal',
                   'ending_balance')

        style = ttk.Style(self.master)
        style.configure('Treeview', rowheight=40)

        dg = ttk.Treeview(self,
                          columns=columns,
                          show='headings'
                          )
        dg.heading('current_month', text='Date')
        dg.heading('current_balance', text='Current Balance')
        dg.heading('current_interest', text='Interest Paid')
        dg.heading('current_principal', text='Principal Paid')
        dg.heading('additional_principal', text='Additional Principal')
        dg.heading('ending_balance', text='Balance Remaining')

        dg.grid(row=0,
                column=0,
                sticky='new',
                padx=20,
                pady=20)
