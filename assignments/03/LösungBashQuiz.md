# Lösungen Bash-Quiz

## Frage 1: How do you get the first three lines of the file 2014-01_JA.tsv?
-> Bash: head -n 3 2014-01_JA.tsv

## Frage 2: How do you get the total number of lines in each of the *.tsvfiles?
-> Bash: wc -l

## Frage 3: How do you get the file with the highest number of lines and how many does it have? Can you get the output with a single command line call?
-> Bash: wc -l * 2>/dev/null | sort -nr | head -n 1 | awk '{print $2}'
