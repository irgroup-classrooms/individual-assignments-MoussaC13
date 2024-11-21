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
  -------------
  # Analyse der Daten
  1. ***Total number of lines:***
    total_lines=$(tail -n +2 lotr_scripts.csv | wc -l)
    echo "Total number of lines: $total_lines"
  2. ***unique words used in the dialogs:***
    unique_words=$(awk -F ',' '{print $2}' lotr_scripts.csv | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr ' ' '\n' | sort | uniq | wc l) echo "Total number of unique words in dialogs: $unique_words"
  3. ***What is the distribution on the three different films?***
  awk -F ',' '{print $3}' lotr_scripts.csv | sort | uniq -c
  4. ***What are the top 5 characters in the char column?***
  awk -F ',' '{print $1}' lotr_scripts.csv | sort | uniq -c | sort -nr | head -n 5
  5. ***What are the top 5 characters in the dialogues?***
  awk -F ',' '{print $1}' lotr_scripts.csv | sort | uniq -c | sort -nr | head -n 5
