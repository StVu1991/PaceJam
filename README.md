# PaceJam
Go to the root of project, open CMD and run:

set FLASK_APP=market.py

flask run


A ako se koristi Powershell onda:

$env:FLASK_APP = "market.py"

flask run


Nakon pokretanja lokalnog servera root stranice se otvara u browseru: 

http://127.0.0.1:5000/

Ako želimo da se stranica refresha on-the-fly kako mijenjamo kod, prije flask run postaviti ovo kroz Powershell:

$env:FLASK_DEBUG = "1"
