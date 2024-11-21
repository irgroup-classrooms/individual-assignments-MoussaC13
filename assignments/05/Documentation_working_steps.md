# Dokumentation des Assignments 05
--------------------------------------
## 1. Download der csv-Datei: 
  - Erstellen eines kaggle Accounts und anschließender Download der ZIP-Datei sowie Entpackung
## 2. Beschreibung der Datenfelder
  - **Spalte 1:** ID / Eindeutige fortlaufende Nummerierung der Zeile
  - **Spalte 2: char** - Steht für die Rolle
  - **Spalte 3: dialog** - Steht für den gesprochenen Text der Rolle
  - **Spalte 4: movie** - Steht für den Film
## 3. Datenbereinigung
  - **Spalte2: char**
    1. Pivot erstellen, um alle eindeutigen Namen zu identifizieren
    2. Inkonsistenzen identifizieren:
      - unpassende Sonderzeichen
      - doppelte Namen (welche aber Rechtschreibfehler oder Leerzeichen am Anfang oder Ende haben und deshalb mehr als 1 mal vorkommen)
      - Unterschiedliche Schreibweisen bei "VOICEOVER"
    3. Diese korrigieren
  - **Spalte 3: dialog**
    1. GLÄTTEN() Funktion
    2. Ersetzen von:
      - Â
      - Leerzeichen am Satzanfang
      - '
      - 2 Leerzeichen und mehr hintereinander
      - ., hintereinander
      - Mehr als 3 Punkte hintereinander
      - usw.
