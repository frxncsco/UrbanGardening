# Willkommen bei UrbanGardening

Wenn Sie unsere Urban Gardening Seite starten wollen, dann müssen sie folgende Schitte durchführen:

1. Installieren von Python und Git.
2. Klonen Sie sich das GitHub Repository und speichern Sie diesen an einem gewünschten Ort.
3. Erstellen (Befehl z.b.: "python -m venv myvenv") und starten (Befehl z.B.:"myvenv\Scripts\activate") Sie nun eine virtuelle Umgebung in diesem Ordner.
4. Installieren Sie nun die requirements, die Sie in der requirements.txt finden. Nutzen Sie hierfür den Befehl "pip install -r requirements.txt".
5. Da die Datenbank nicht im GitHub gespeichert wird, müssen Sie nun die Migrationen mit dem Befehl "python manage.py migrate" in der Konsole anwenden. 
6. Um selbst z.B. einen Blogartikel verfassen, bearbeiten und löschen zu können, müssen Sie als Superuser angemeldet sein.
Diesen Superuser müssen Sie vorher allerdings erstellen, indem Sie "python manage.py createsuperuser" in die Konsole eingeben und anschließend
Benutzername, E-Mail und Passwort eingeben.
7. Nun kann der Server mit "python manage.py runserver" gestartet werden. Im Browser gelangen Sie mit der folgenden url auf die Seite: http://127.0.0.1:8000/
8. Wenn Sie sich noch einloggen wollen, müssen Sie http://127.0.0.1:8000/admin eingeben und gelangen so zu einem Log-In, wo Sie sich mit dem zuvor erstellten 
Superuser einloggen können.

Wir wünschen nun viel Freude mit der Seite!

Ihr Team Susan Bloom
