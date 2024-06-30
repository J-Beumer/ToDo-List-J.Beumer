import tkinter as tk                   # Importiert das Tkinter-Modul für die GUI-Erstellung (durch as tk lässt sich im gesamten code via tk hierauf verweisen)
from tkinter import messagebox         # Importiert das Messagebox-Modul für Warnmeldungen aus tkinter

## Funktion zum Hinzufügen einer Aufgabe zur Liste
def add_task(event=None):                               # definiert eine Funktion als wiederverwendaren code, hier add_task, der eine Zusammenhängende Aktion ausführt, hier einen Task zur Aufgabenliste hinzufügen. (das ereignis "event=none" ermöglicht es den Task durch drücken der entertaste hinzuzufügen, keybinding ist weiter unten definiert)
    task = task_entry.get()                             # Holt den Text aus dem Eingabefeld
    if task:                                            # Überprüft, ob text eingegeben wurde
        tasks.append({"task": task, "done": False})     # Fügt die Aufgabe zur Liste tasks hinzu, mit dem Status, dass sie noch nicht erledigt ist (task ist der text und False der Satus, bei neuen aufgaben ist er immer "nicht erledigt)
        update_task_listbox()                           # Aktualisiert die Listbox-Anzeige, indem die Funktion zum updaten ausgeführt wird, so können Änderunge übernommen und das GUI aktualisiert werden
        task_entry.delete(0, tk.END)                # Löscht den Text im Eingabefeld, damit man wieder etwas neues eingeben muss, ohne den vorherigen text zu extra manuell zu löschen
    else:                                               # Falls der Text leer ist:
        messagebox.showwarning("Warnung", "Du musst eine Aufgabe eingeben.")  # Zeigt eine Warnmeldung an, die dem Benutzer mitteilt, dass er keine Aufgabe eingegeben hat

## Funktion zum Entfernen einer ausgewählten Aufgabe aus der Liste
def remove_task():                                      # Definiert die Funktion remove_task
    selected_task_index = get_selected_task_index()     # ruft den Index der ausgewählten Aufgabe ab
    if selected_task_index is not None:                 # Überprüft, ob eine Aufgabe ausgewählt wurde
        tasks.pop(selected_task_index)                  # Entfernt die Aufgabe aus der Liste tasks mit pop (bezogen auf den zuvor ermittelten Index der Ausgabe
        update_task_listbox()                           # Aktualisiert die Listbox-Anzeige, indem die Funktion zum updaten ausgeführt wird, so können Änderunge übernommen und das GUI aktualisiert werden
    else:                                               # Falls keine Aufgabe ausgewählt wurde, dann:
        messagebox.showwarning("Warnung", "Du musst eine Aufgabe auswählen.")           # Zeigt eine Warnmeldung an

## Funktion zum Markieren einer Aufgabe als erledigt oder nicht erledigt
def toggle_task_done():                                 # Definiert die Funktion toggle_task_done
    selected_task_index = get_selected_task_index()     # Holt den Index der ausgewählten Aufgabe
    if selected_task_index is not None:                 # Überprüft, ob eine Aufgabe ausgewählt wurde
        tasks[selected_task_index]["done"] = not tasks[selected_task_index]["done"]                 # Schaltet den Erledigt-Status der ausgewählten Aufgabe um (durch verwendung des operators "not"
        update_task_listbox()                           # Aktualisiert die Listbox-Anzeige, indem die Funktion zum updaten ausgeführt wird, so können Änderunge übernommen und das GUI aktualisiert werden
        task_listbox.selection_set(selected_task_index)  # Wählt die Aufgabe in der Listbox erneut, ausdamit man z.b. mit einem weiteren Klick auf Erledigt den Status "Erledigt" wieder rückgängig machen kann, ohne den Task nochmal neu anzuklicken
    else:                                               # Falls keine Aufgabe ausgewählt wurde, dann:
        messagebox.showwarning("Warnung", "Du musst eine Aufgabe auswählen.")           # Zeigt eine Warnmeldung an

## Funktion zum Verschieben einer Aufgabe nach oben
def move_task_up():                                                             # Definiert die Funktion move_task_up
    selected_task_index = get_selected_task_index()                             # Holt den Index der ausgewählten Aufgabe
    if selected_task_index is not None and selected_task_index > 0:             # Überprüft, ob eine Aufgabe ausgewählt und nicht die erste ist (weil kein else: festgelegt wurde passiert nichts, wenn die Aufgabe schon auf Platz 1 ist)
        tasks.insert(selected_task_index - 1, tasks.pop(selected_task_index))   # Verschiebt die Aufgabe nach oben, indem sie aus dem Index entfernt und eine Position weiter oben wieder eingefügt wird
        update_task_listbox()                                                   # Aktualisiert die Listbox-Anzeige
        task_listbox.selection_set(selected_task_index - 1)                     # Wählt die Aufgabe in der neuen Position aus, um sicherzustellen das die Aufgabe durch mehrmaligen klick auf das Button "▲" entsprechend oft jedes mal eine Position nach oben rückt, ohne die Aufgabe jedes mal neu per klick anwählen zu müssen

## Funktion zum Verschieben einer Aufgabe nach unten
def move_task_down():                                                               # Definiert die Funktion move_task_down
    selected_task_index = get_selected_task_index()                                 # Holt den Index der ausgewählten Aufgabe
    if selected_task_index is not None and selected_task_index < len(tasks) - 1:    # Überprüft, ob eine Aufgabe ausgewählt und nicht die letzte ist (durch len in kombination mit -1)
        tasks.insert(selected_task_index + 1, tasks.pop(selected_task_index))       # Verschiebt die Aufgabe nach unten
        update_task_listbox()                                                       # Aktualisiert die Listbox-Anzeige
        task_listbox.selection_set(selected_task_index + 1)                         # Wählt die Aufgabe in der neuen Position aus, um sicherzustellen das die Aufgabe durch mehrmaligen klick auf das Button "▼" entsprechend oft jedes mal eine Position nach unten rückt, ohne die Aufgabe jedes mal neu per klick anwählen zu müssen

## Hilfsfunktion zum Holen des Indexes der ausgewählten Aufgabe
def get_selected_task_index():                          # Definiert die Funktion get_selected_task_index
    try:                                                # Versucht, den Index der ausgewählten Aufgabe zu holen (ein Try-block, um potenzielle Fehler abzufangen)
        return task_listbox.curselection()[0]           # Gibt den Index der ausgewählten Aufgabe zurück
    except IndexError:                                  # Falls keine Aufgabe ausgewählt wurde
        return None                                     # Gibt None zurück

## Funktion zur Aktualisierung der Listbox-Anzeige
def update_task_listbox():                                      # Definiert die Funktion update_task_listbox
    task_listbox.delete(0, tk.END)                         # Löscht alle Einträge in der Listbox
    for index, task in enumerate(tasks, start=1):               # Durchläuft alle Aufgaben in tasks
        display_text = f"{index}. {task['task']}"               # Erstellt den Anzeigetext für die Aufgabe
        if task["done"]:                                        # Überprüft, ob die Aufgabe erledigt ist (bezieht sich auftoggle_task_done)
            display_text += " (Erledigt)"                       # Fügt "(Erledigt)" zum Anzeigetext hinzu
        task_listbox.insert(tk.END, display_text)      # Fügt den Anzeigetext in die Listbox ein
        create_handle(task_listbox, index - 1)                  # Erstellt den Drag-and-Drop-Handle für die Aufgabe (siehe funktion hierunter)

## Funktion zum Erstellen eines Drag-and-Drop-Handles für eine Aufgabe
def create_handle(listbox, index):                                          # Definiert die Funktion create_handle
    handle = tk.Label(listbox, text="≡", cursor="hand2")                    # Erstellt ein Label als Handle
    handle.place(relx=0, rely=0.5, x=-15, y=(index * 18) - 7, anchor="w")   # Platziert das Handle
    handle.bind("<ButtonPress-1>", on_drag_start)                           # Bindet den Drag-Start-Ereignis
    handle.bind("<B1-Motion>", on_drag_motion)                              # Bindet den Drag-Motion-Ereignis
    handle.bind("<ButtonRelease-1>", on_drop)                               # Bindet den Drop-Ereignis
    return handle                                                           # Gibt das Handle zurück

## Funktion für den Start des Drag-and-Drop-Vorgangs
def on_drag_start(event):                                                           # Definiert die Funktion on_drag_start
    widget = event.widget                                                           # Holt das Widget, das das Ereignis ausgelöst hat, in diesem fall das Handle
    widget._drag_data = {"item": widget.nearest(event.y), "start_y": event.y}       # Speichert die Drag-Daten
    widget._is_dragging = True                                                      # Setzt das Dragging-Flag auf True

## Funktion für den Drag-and-Drop-Bewegungsvorgang
def on_drag_motion(event):                              # Definiert die Funktion on_drag_motion, wird während des Dragging-Vorgans ausgeführt, wenn sich die Maus bewegt
    widget = event.widget                               # Holt das Widget, das das Ereignis ausgelöst hat
    if widget._is_dragging and widget._drag_data:       # Überprüft, ob Dragging aktiv ist und Drag Daten vorhanden sind
        index = widget.nearest(event.y)                 # Holt den Index des nächstgelegenen Eintrags, basierend auf der Position der Maus
        widget.selection_clear(0, tk.END)               # Hebt die Auswahl aller Einträge auf
        widget.selection_set(index)                     # Wählt den nächstgelegenen Eintrag aus

## Funktion für das Beenden des Drag-and-Drop-Vorgangs
def on_drop(event):                                     # Definiert die Funktion on_drop
    widget = event.widget                               # Holt das Widget, das das Ereignis ausgelöst hat
    if widget._is_dragging and widget._drag_data:       # Überprüft, ob Dragging aktiv ist
        item = widget._drag_data["item"]                # Holt das ursprüngliche Drag-Element
        drop_index = widget.nearest(event.y)            # Holt den Index des Drop-Ziels, basierend auf der aktuellen Maus Position
        if item != drop_index:                          # Überprüft, ob das Drag-Element nicht das gleiche ist wie das Drop-Ziel
            tasks.insert(drop_index, tasks.pop(item))   # Verschiebt die Aufgabe an die neue Position
            update_task_listbox()                       # Aktualisiert die Listbox-Anzeige
    widget._drag_data = None                            # Setzt die Drag-Daten zurück
    widget._is_dragging = False                         # Setzt das Dragging-Flag auf False

# Hauptfenster der To-Do-Liste erstellen
root = tk.Tk()                              # Erstellt das Hauptfenster
root.title("To-Do-Liste")                   # Setzt den Fenstertitel
root.geometry("400x400")                    # Setzt die Fenstergröße auf 400x400 Pixel
root.resizable(False, False)    # verwindert, dass die Fenstergröße verändert werden kann - es gab probleme beim Drag&Drop ;)

tasks = []                               # Erstellt eine leere Liste für Aufgaben

# Eingabefeld für neue Aufgaben
task_entry = tk.Entry(root, width=40)       # Erstellt ein Eingabefeld für Aufgaben
task_entry.pack(pady=10)                    # Fügt das Eingabefeld zum Fenster hinzu und setzt den vertikalen Abstand auf 10 Pixel
task_entry.bind("<Return>", add_task)       # Bindet die Enter-Taste an die Funktion add_task

# Schaltfläche zum Hinzufügen von Aufgaben
add_button = tk.Button(root, text="Aufgabe hinzufügen", command=add_task)   # Erstellt die Schaltfläche zum Hinzufügen von Aufgaben und verknüpft sie mit der Funktion "add_task"
add_button.pack(pady=5)                                                     # Fügt die Schaltfläche zum Fenster hinzu und setzt den Abstand

# Rahmen für die Pfeil-Schaltflächen und die Listbox
frame = tk.Frame(root)                   # Erstellt einen Rahmen
frame.pack(pady=10)                      # Fügt den Rahmen zum Fenster hinzu und setzt den Abstand

# Pfeil-Schaltflächen zum Verschieben der Aufgaben
up_button = tk.Button(frame, text="▲", command=move_task_up)        # Erstellt die Schaltfläche zum Verschieben der Aufgaben nach oben und verknüpft sie mit der Funktion "move_task_up"
up_button.grid(row=0, column=0, padx=5)                             # Platziert die Schaltfläche im Raster

down_button = tk.Button(frame, text="▼", command=move_task_down)    # Erstellt die Schaltfläche zum Verschieben der Aufgaben nach unten und verknüpft sie mit der Funktion "move_task_down"
down_button.grid(row=1, column=0, padx=5)                           # Platziert die Schaltfläche im Raster

# Listbox zur Anzeige der Aufgaben
task_listbox = tk.Listbox(frame, width=50, height=10)               # Erstellt die Listbox zur Anzeige der Aufgaben
task_listbox.grid(row=0, column=1, rowspan=2)                       # Platziert die Listbox im Raster

# Initialisierung der Drag-and-Drop-Attribute
task_listbox._drag_data = None                                      # Initialisiert die Drag-Daten auf None
task_listbox._is_dragging = False                                   # Setzt das Dragging-Flag auf False

# Schaltfläche zum Entfernen von Aufgaben
remove_button = tk.Button(root, text="Aufgabe entfernen", command=remove_task)          # Erstellt die Schaltfläche zum Entfernen von Aufgaben und verknüpft mit der Funktion "remove_task"
remove_button.pack(pady=5)                                                              # Fügt die Schaltfläche zum Fenster hinzu und setzt den Abstand

# Schaltfläche zum Markieren von Aufgaben als erledigt
done_button = tk.Button(root, text="Aufgabe erledigt", command=toggle_task_done)        # Erstellt die Schaltfläche zum Markieren von Aufgaben als erledigt, verknüpft mit der Funktion "toggle_task_done"
done_button.pack(pady=5)                                                                # Fügt die Schaltfläche zum Fenster hinzu und setzt den Abstand

# Ereignisbindungen für die Listbox
task_listbox.bind("<ButtonPress-1>", on_drag_start)                 # Bindet das ButtonPress-1-Ereignis an die Funktion on_drag_start
task_listbox.bind("<B1-Motion>", on_drag_motion)                    # Bindet das B1-Motion-Ereignis an die Funktion on_drag_motion
task_listbox.bind("<ButtonRelease-1>", on_drop)                     # Bindet das ButtonRelease-1-Ereignis an die Funktion on_drop

# Hauptschleife starten
root.mainloop()                                                     #Startet die Hauptschleife der Anwendung, die auf Ereignisse wartet und darauf reagiert