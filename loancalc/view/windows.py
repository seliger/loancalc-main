import logging
import tkinter as tk
import loancalc
import loancalc.view.frames as frames

# Instantiate our global logger
logger = logging.getLogger(__name__)


class MainAppWindow(tk.Tk):
    frames = {}
    child_windows = {}

    def __init__(self, *args, **kwargs):
        # Init code heavily inspired by:
        # https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes
        super().__init__(*args, **kwargs)
        logger.info('Initializing main window...')

        self.wm_title(f'{loancalc.APP_NAME} {loancalc.APP_VERSION}')

        # Calculate geometry and position of the main window
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = screen_width // 2
        center_y = screen_height // 2

        window_width = int(screen_width / 1.5)
        window_height = int(screen_height / 1.5)

        titlebarHeight = self.winfo_rooty() - self.winfo_y()

        self.geometry('{}x{}+{}+{}'.format(
            window_width,
            window_height,
            center_x - (window_width // 2),
            center_y - (window_height // 2)
        ))

        # Set the window to be a static size (no re-sizing!)
        self.resizable(False, False)

        # Configure the grid to have a specific shape (approximately 40/60)
        self.grid_columnconfigure(0, minsize=window_width)
        self.grid_rowconfigure(0, minsize=(window_height // 10))
        self.grid_rowconfigure(1, minsize=(window_height - (window_height // 10)))

        self.frames['button'] = tk.Button(text="Enter Loan Parameters",
                                          command=self.__show_loan_config)
        self.frames['button'].grid(row=0,
                                   column=0,
                                   sticky='nsew',
                                   padx=10,
                                   pady=10)

        self.frames['results'] = frames.ResultsGridFrame(self)
        self.frames['results'].grid(row=1,
                                    column=0,
                                    sticky='nsew',
                                    padx=10,
                                    pady=10)

    def __show_loan_config(self):
        logger.info(f'Child windows: {self.child_windows.keys()}')
        self.child_windows['loan_config'] = LoanConfigurationWindow(master=self)


class LoanConfigurationWindow(tk.Toplevel):
    frames = {}

    def __init__(self, *args, **kwargs):
        # Init code heavily inspired by:
        # https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes
        super().__init__(*args, **kwargs)
        logger.info('Initializing main window...')

        self.wm_title(f'{loancalc.APP_NAME} - Loan Parameters')

        # Calculate geometry and position of the main window
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = screen_width // 2
        center_y = screen_height // 2

        window_width = int(screen_width / 4)
        window_height = int(screen_height / 2)

        self.geometry('{}x{}+{}+{}'.format(
            window_width,
            window_height,
            center_x - (window_width // 2),
            center_y - (window_height // 2)
        ))

        # Set the window to be a static size (no re-sizing!)
        self.resizable(False, False)

        # Configure the grid to have a specific shape (approximately 40/60)
        self.grid_columnconfigure(0, minsize=window_width)
        self.grid_rowconfigure(0, minsize=window_height)

        self.frames['inputs'] = frames.LoanConfigurationFrame(self)
        self.frames['inputs'].grid(row=0,
                                   column=0,
                                   sticky='nsew',
                                   padx=10,
                                   pady=10)