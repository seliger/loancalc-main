
import logging
import loancalc.view.windows as windows

log = logging.getLogger(__name__)


class LoanCalc:

    @staticmethod
    def run():

        # Bootstrap our main application window and kick off
        # the central event loop.
        main_window = windows.MainAppWindow()
        main_window.mainloop()
