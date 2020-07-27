# Willkommen bei UrbanGardening

Wenn Sie unsere Urban Gardening Seite starten wollen, dann müssen sie folgende Schitte durchführen:

1. Klonen Sie sich das GitHub Repository und speichern Sie diesen an einem gewünschten Ort
2. Erstellen und starten Sie nun eine virtuelle Umgebung in diesem Ordner
3. Installieren Sie nun die requirements, die Sie in der requirements.txt finden.
3. Da die Datenbank nicht im GitHub gespeichert wird, müssen Sie nun diese mit dem Befehl "python manage.py makemigrations" in der Konsole anlegen. 
Hier werden Sie nun gefragt, wie Sie die Felder benennen wollen. Sie geben hier "y" für yes ein und bekommen nun den Vorschlag diese
mit timezone.now zu benennen. Genau das tun Sie (ggf. zwei mal).
4. Um später selber z.B. einen Blogartikel zu verfassen, bearbeiten und zu löschen müssen Sie als Superuser angemeldet sein.
Diesen Superuser müssen Sie vorher allerdings erstellen, indem Sie "paython manage.py createsuperuser" in die Konsole eingeben und anschließend
Benutzername, E-Mail und Passwort eingeben.
5. Nun kann der Server mit "python manage.py runserver" gestartet werden. Im Broser gelangen Sie mit der folgenden url auf die Seite: http://127.0.0.1:8000/
6. Wenn Sie sich noch einloggen wollen müssen Sie http://127.0.0.1:8000/admin eingeben und gelangen so zu einem Log-In, wo Sie sich mit dem zuvor erstellten 
Superuser einloggen können

Wir wünschen nun viel Freude mit der Seite!

Ihr Team EINS
