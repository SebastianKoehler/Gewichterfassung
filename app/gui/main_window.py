from app import WeightService, Config, get_session, get_engine

from tkinter import Tk, Frame, Button, Scrollbar
from tkinter.ttk import Treeview

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.dates as mdates


class MainWindow(Tk):
    def __init__(self):
        super().__init__()

        self.title("Weight Tracker")
        self.geometry("800x900")
        self.resizable(False, False)

        self.treeview = None

        self.main_frame = Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        self.plot_frame = Frame(self.main_frame)
        self.plot_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.list_frame = Frame(self.main_frame)
        self.list_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.button_frame = Frame(self.main_frame)
        self.button_frame.pack(fill="x", padx=10, pady=10)

        self.create_line_plot()
        self.create_list()

        self.add_data_button = Button(self.button_frame,
                                      text="Neuen Datensatz hinzufügen",
                                      command=self.open_add_data_window)
        self.add_data_button.pack(pady=10)

    def create_line_plot(self):
        engine = get_engine(Config.SQLALCHEMY_DATABASE_URI)
        Session = get_session(engine)

        with Session() as session:
            weight_manager = WeightService(session)
            entries = weight_manager.get_weights()

        dates = [entry.date for entry in entries]
        weights = [entry.weight for entry in entries]

        fig = Figure(figsize=(8, 4), dpi=100)

        ax = fig.add_subplot(111)
        ax.plot(dates, weights, marker='o')
        ax.set_title("Gewicht über Zeit")
        ax.set_xlabel("Datum")
        ax.set_ylabel("Gewicht (kg)")
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y'))
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))

        fig.autofmt_xdate()

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def create_list(self):
        columns = ("ID", "Datum", "Gewicht")

        self.treeview = Treeview(self.list_frame, columns=columns, show='headings')
        self.treeview.heading("ID", text="ID")
        self.treeview.heading("Datum", text="Datum")
        self.treeview.heading("Gewicht", text="Gewicht (kg)")
        self.treeview.pack(side="left", fill="both", expand=True)

        scrollbar = Scrollbar(self.list_frame, orient="vertical", command=self.treeview.yview)
        scrollbar.pack(side="right", fill="y")

        self.treeview.configure(yscrollcommand=scrollbar.set)

        self.update_list()

    def update_list(self):

        engine = get_engine(Config.SQLALCHEMY_DATABASE_URI)
        Session = get_session(engine)

        with Session() as session:
            weight_manager = WeightService(session)
            entries = weight_manager.get_weights()

        for row in self.treeview.get_children():
            self.treeview.delete(row)

        for entry in entries:
            self.treeview.insert("", "end", values=(entry.id, entry.date.strftime('%d.%m.%Y'), entry.weight))

    def open_add_data_window(self):
        from app import AddDataWindow
        AddDataWindow(self, self.update_list)
