# ToDo-List-J.Beumer
mein erstes kleines und vollfunktionsfähiges Programm, eine einfache ToDo-Liste

Ich habe eine einfache To-Do-Liste-Anwendung mit Python erstellt. Mit dieser Anwendung lassen sich Aufgaben hinzufügen, entfernen, als erledigt markieren und die Reihenfolge der Aufgaben ändern, entweder über die entsprechenden Button am linken Rand, oder per Drag&Drop mit der Maus. Während der Erstellung dieser To-Do-Liste habe ich u.a. auf Hilfe durch Chat GPT zurückgegriffen, um die richtigen Funktionen zu ermitteln, die ich benötige, um die zu Beginn des Projekts festgelegten Features umzusetzen. Chat GPT hat mir auch dabei geholfen, den Code auf Logikfehler und etwaige Bugs zu überprüfen.
Das größte Problem, das ich während der Programmierung hatte, war es, die Drag&Drop Funktion vernünftig zu implementieren. Zunächst überlagerte Drag&Drop die Möglichkeit eine andere Aufgabe in der Aufgabenliste auszuwählen, die erste Aufgabe blieb angewählt und wurde mit jedem Mausklick nur an die entsprechende Position verschoben.
Inzwischen funktionieren aber alle Features, die ich für die ToDo-Liste geplant hatte, wie beabsichtigt.

Features der ToDo Liste (Soll)

 - Aufgabe hinzufügen: Die ToDo Liste soll ein Eingabefeld haben und Aufgaben sollen sich entweder per Enter Taste zur Aufgabenliste hinzufügen lassen, oder wenn man auf den Button “Aufgaben hinzufügen” klickt.
  
 - Aufgaben in der Aufgabenliste per Mausklick anwählen: Es soll möglich sein Aufgaben per Mausklick auszuwählen
  
 - Aufgabe entfernen: Die ausgewählte Aufgabe wird über den Klick auf den Button “Aufgabe entfernen” aus der Aufgabenliste entfernt.
  
 - Aufgabe erledigen: Jede Aufgabe hat einen Status, der angibt, ob sie erledigt ist oder nicht. Erledigte Aufgaben erhalten die Endung “ (Erledigt)". Per Klick auf den Button "Aufgabe erledigt" lässt sich für die gerade    ausgewählte Aufgabe der Status von erledigt zu offen und vice versa umschalten.
  
 - Aufgabe verschieben: Es soll möglich sein, die Reihenfolge der Aufgaben in der Aufgabenliste zu verändern, entweder über die beiden Buttons links von der Aufgabenliste (Pfeil hoch und runter), oder per Drag&Drop. Wenn    man einen der beiden Button anklickt, wird die Aufgabe entsprechend entweder um eine Position hoch oder runter verschoben in der Aufgabenliste, die Aufgabe bleibt weiter ausgewählt.
  
 - Drag&Drop: Die zweite Möglichkeit, um eine Aufgabe zu verschieben, ist per Drag&Drop. Dies wird initiiert, wenn man auf eine Aufgabe in der Aufgabenliste klickt und die linke Maustaste gedrückt hält. Die Aufgabe soll     an dem Platz in der Aufgabenliste platziert werden, wo der Maus-Cursor gerade ist, während man die Maustaste loslässt.

verwendete Funktionen
1. add_task(event=None)
Fügt eine neue Aufgabe zur Liste hinzu. Diese Funktion wird durch Drücken der Enter-Taste im Eingabefeld oder durch Klicken auf die Schaltfläche "Aufgabe hinzufügen" aufgerufen.
Parameter: event (optional) - Ermöglicht die Verwendung als Event-Handler für Key-Events.
Aktionen:
Holt den Text aus dem Eingabefeld.
Fügt die Aufgabe zur Liste hinzu, falls Text eingegeben wurde.
Aktualisiert die Anzeige der Aufgabenliste.
Löscht den Text im Eingabefeld.
Zeigt eine Warnung an, wenn kein Text eingegeben wurde.
2. remove_task()
Entfernt die ausgewählte Aufgabe aus der Liste.
Aktionen:
Holt den Index der ausgewählten Aufgabe.
Entfernt die Aufgabe, wenn eine Aufgabe ausgewählt wurde.
Aktualisiert die Anzeige der Aufgabenliste.
Zeigt eine Warnung an, wenn keine Aufgabe ausgewählt wurde.
3. toggle_task_done()
Markiert die ausgewählte Aufgabe als erledigt oder nicht erledigt.
Aktionen:
Holt den Index der ausgewählten Aufgabe.
Schaltet den Erledigt-Status der Aufgabe um.
Aktualisiert die Anzeige der Aufgabenliste.
Wählt die Aufgabe erneut aus.
Zeigt eine Warnung an, wenn keine Aufgabe ausgewählt wurde.
4. move_task_up()
Verschiebt die ausgewählte Aufgabe nach oben.
Aktionen:
Holt den Index der ausgewählten Aufgabe.
Verschiebt die Aufgabe nach oben, wenn eine Aufgabe ausgewählt wurde und nicht die erste ist.
Aktualisiert die Anzeige der Aufgabenliste.
Wählt die Aufgabe in der neuen Position aus.
5. move_task_down()
Verschiebt die ausgewählte Aufgabe nach unten.
Aktionen:
Holt den Index der ausgewählten Aufgabe.
Verschiebt die Aufgabe nach unten, wenn eine Aufgabe ausgewählt wurde und nicht die letzte ist.
Aktualisiert die Anzeige der Aufgabenliste.
Wählt die Aufgabe in der neuen Position aus.
6. get_selected_task_index()
Holt den Index der ausgewählten Aufgabe.
Rückgabewert: Index der ausgewählten Aufgabe oder None, wenn keine Aufgabe ausgewählt wurde.
7. update_task_listbox()
Aktualisiert die Anzeige der Aufgabenliste.
Aktionen:
Löscht alle Einträge in der Listbox.
Fügt alle Aufgaben aus der Liste tasks in die Listbox ein.
Markiert erledigte Aufgaben entsprechend.
8. create_handle(listbox, index)
Erstellt einen Drag-and-Drop-Handle für eine Aufgabe.
Parameter: listbox - Die Listbox, in der die Aufgabe angezeigt wird. index - Der Index der Aufgabe in der Listbox.
Aktionen:
Erstellt ein Label als Handle.
Platziert das Handle in der Listbox.
Bindet die Drag-and-Drop-Ereignisse an das Handle.
9. on_drag_start(event)
Startet den Drag-and-Drop-Vorgang.
Parameter: event - Das Event-Objekt, das die Drag-and-Drop-Aktion startet.
Aktionen:
Holt das Widget, das das Ereignis ausgelöst hat.
Speichert die Drag-Daten.
Setzt das Dragging-Flag auf True.
10. on_drag_motion(event)
Verarbeitet die Drag-and-Drop-Bewegung.
Parameter: event - Das Event-Objekt, das die Drag-and-Drop-Bewegung auslöst.
Aktionen:
Holt das Widget, das das Ereignis ausgelöst hat.
Überprüft, ob Dragging aktiv ist.
Holt den Index des nächstgelegenen Eintrags.
Hebt die Auswahl aller Einträge auf.
Wählt den nächstgelegenen Eintrag aus.
11. on_drop(event)
Beendet den Drag-and-Drop-Vorgang.
Parameter: event - Das Event-Objekt, das die Drop-Aktion auslöst.
Aktionen:
Holt das Widget, das das Ereignis ausgelöst hat.
Überprüft, ob Dragging aktiv ist.
Holt das ursprüngliche Drag-Element.
Holt den Index des Drop-Ziels.
Verschiebt die Aufgabe an die neue Position, falls sie sich geändert hat.
Aktualisiert die Anzeige der Aufgabenliste.
Setzt die Drag-Daten zurück.
Setzt das Dragging-Flag auf False.
