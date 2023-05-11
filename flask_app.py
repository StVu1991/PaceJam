
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates')

training_data = {
    "marko":
        [
        "Marko",
        "Radanović",
        ["Week 11", "8.5.-14.5.", ["3 x (15 min trčanja + 1-2 min hoda)", "Cooper test", "20 minuta trčanja @6:40-6:45"]]
        ]
    ,
     "marica":
        [
        "Marica",
        "Janković",
        ["Week 2", "8.5.-14.5.", ["10 minuta brzog hoda pa 6 x (1 min trčanja + 2 min hoda)", "10 minuta brzog hoda pa 7 x (1 min trčanja + 2 min hoda)", "10 minuta brzog hoda pa 8 x (1 min trčanja + 1.5 min hoda)"]]
        ]
    , "kristina":
        [
        "Kristina",
        "Vukelić",
        ["Week 1", "8.5.-14.5.", ["45-60 min @6:30<br>", "15 min zagrijavanje @6:30 <br><br>19min fartleka 1+2 (1 brza minuta + 2 spore minute) <br><br> 15 minuta rastrčavanje @6:30<br><br>Tempa: brza minuta - spora minuta 5:10 - 6:30", "12km -> 10km@6:30 + 2km@5:45", "Zagrijavanje i rastrčavanje po 10-15min@6:30 <br><br>Glavni dio treninga: 4 puta po 7 minuta fartleka 1+2 (minuta brzo + 2 minute sporo), međupauze 5 minuta TG"]]]
    , "davor":
        [
        "Davor",
        "Turinski",
        ["Week 13", "8.5.-14.5.", ["3 x (8 min trčanja + 1 min hoda) + 6 minuta trčanja na kraju", "Cooper Test", "3 x (9 minuta trčanja + 2 min hoda) + 5 minuta trčanja na kraju"]]
        ]
    }

@app.route('/davor')
def hello_davor():
    first_name = training_data["davor"][0]
    person_dict = {"davor": training_data["davor"]}
    return render_template('training_table.html', first_name=first_name, training_data=person_dict)

@app.route('/marko')
def hello_marko():
        # Render the template and pass data to it
    first_name = training_data["marko"][0]
    person_dict = {"marko": training_data["marko"]}
    return render_template('training_table.html', first_name=first_name, training_data=person_dict)

@app.route('/kristina')
def hello_kristina():
    first_name = training_data["kristina"][0]
    person_dict = {"kristina": training_data["kristina"]}
    return render_template('training_table.html', script=url_for("static", filename="script.js"), first_name=first_name, training_data=person_dict)

@app.route('/marica')
def hello_marica():
    # Sample data for the table
    first_name = training_data["marica"][0]
    person_dict = {"marica": training_data["marica"]}
    return render_template('training_table.html', first_name=first_name, training_data=person_dict)

@app.route('/')
def hello_world():
    return '<h1>Hello from Flask!<h1>'
