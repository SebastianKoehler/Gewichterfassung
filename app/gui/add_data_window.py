from app import WeightService, Config, get_session, get_engine

from tkinter import Button, Label, Toplevel, DoubleVar, messagebox, Spinbox
from tkinter.constants import LEFT
from tkcalendar import DateEntry

from datetime import datetime


class AddDataWindow(Toplevel):
    def __init__(self, parent, update_callback):
        super().__init__(parent)

        self.title("Neuen Datensatz hinzufügen")
        self.geometry("300x250")

        self.treeview = None
        self.update_callback = update_callback

        self.date_label = Label(self, text="Datum:")
        self.date_label.pack(pady=5)

        self.date_entry = DateEntry(self, width=12, background='darkblue', foreground='white',
                                    borderwidth=2, date_pattern='dd.mm.yyyy')
        self.date_entry.pack(pady=5)

        self.weight_label = Label(self, text="Gewicht (kg):")
        self.weight_label.pack(pady=5)

        self.weight_var = DoubleVar(value=50)

        # Spinbox für das Gewicht, min=0, max=200, Schrittgröße=0.1
        self.weight_spinbox = Spinbox(
            self, from_=0, to=200, increment=0.1, format="%.1f",  # Format für eine Nachkommastelle
            width=10, textvariable=self.weight_var)
        self.weight_spinbox.pack(pady=5)

        self.add_button = Button(self, text="Hinzufügen", command=self.add_entry)
        self.add_button.pack(side=LEFT, padx=5, pady=20)

        self.cancel_button = Button(self, text="Abbrechen", command=self.destroy)
        self.cancel_button.pack(side=LEFT, padx=5, pady=20)

    def add_entry(self):
        date_str = self.date_entry.get()
        weight = self.weight_var.get()

        try:
            engine = get_engine(Config.SQLALCHEMY_DATABASE_URI)
            Session = get_session(engine)

            with Session() as session:
                date_obj = datetime.strptime(date_str, '%d.%m.%Y').date()
                new_entry = WeightService.add_weight_entry(date=date_obj, weight=weight)

                session.add(new_entry)
                session.commit()

                messagebox.showinfo("Erfolg", "Eintrag erfolgreich hinzugefügt")

                self.update_callback()
                self.destroy()
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Hinzufügen des Eintrags: {e}")
            session.rollback()
