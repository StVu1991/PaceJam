
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from repository import get_user_name_surname

# import mysql.connector

# # Set up the connection parameters
# connection = mysql.connector.connect(
#     user='svukelic',
#     password='Nagobrijed1991',
#     host='svukelic.mysql.pythonanywhere-services.com',
#     database='svukelic$paceri'
# )

# #Check if the connection is successful
# if connection.is_connected():
#     print('Connected to the database!')

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://svukelic:kokolo1991@svukelic.mysql.pythonanywhere-services.com:3306/svukelic$paceri'
db = SQLAlchemy(app)
# def check_connection():
#     print("sranje")
#     print(app)
try:
    result = db.session.execute('SELECT * FROM users')  # Execute the query
    for row in result:
        print(row)  # Print each user
except Exception as e:
    print(e)

training_data = {
    "marko":
        [
        "Marko",
        "Radanović",
        ["Week 15", "5.6.-11.6.", ["35 minuta @6:40-6:45", "30 minuta @6:40-6:45", "7km @6:40-6:45"], "Prije svega čestitam ti na odličnoj utrci jučer, fantastičan rezultat! A sada je vrijeme da nastavimo s treninzima, i uvedemo novu stvar u trening - a to su dužinski treninzi. Dužinski trening je najduži trening u tjednu i služi za povećavanje izdržljivosti i otpornosti organizma na napor. U ovom tjednu tvoj dužinski trening je 7km što nije puno više od udaljenosti koju si pretrčao za 45 minuta, ali odnekud moramo početi :) Ova dužina će iz tjedna u tjedan biti sve veća, polako se približavajući brojci od 10km - idućoj duljini koja ti je cilj. Redoslijed prva dva treninga u tjednu možeš obrnuti ako želiš, 30 pa 35 minuta ili obrnuto, svejedno je... a kada budeš radio trening od 7km ako imaš potrebu stati, popiti vode, osvježiti se, slobodno, samo pazi da ti ta stajanja nisu dugačka - objasniti ću ti zašto - uživo. Npr na 7km ti je dovoljno jedno stajanje od 1-1.5min.   "],
        ["Week 14", "29.5.-4.6.", ["40-45 minuta trčanja @6:40-6:45"], "Dobrodošao u zadnji tjedan škole trčanja. Trening odradi kad hoćeš, naravno ne prije ponedjeljka, a onda kad odradiš se čujemo za dalje. Do tada razmisli još o planu utrka. Ja bi ti sugerirao da prije prve 10-ke ne trčiš ništa osim eventualno one utrke u Našicama (6.7km). 5km sada možeš trčati i tu na ligi u Brodu svake prve subote u mjesecu, šteta plaćati 150kn, a ionako ih ni nema blizu preko ljeta. Što se tiče samog treninga od 45min, pokušaj odraditi to bez hodanja kao i ove do sada, no ako zbog vrućine budeš žedan i baš budeš trebao stati, odradi to na brzinu - kroz 15-20 sekundi. Nisam gonič robova i naravno da je dopušteno stajati na treninzima i stajati ćeš, pogotovo preko ljeta, ali ovo je finale škole trčanja i zadnji trening i bilo bi baš super da odradiš 45min u komadu."],
        ["Week 13", "22.5.-28.5.", ["35-40 minuta trčanja @6:40-6:45", "10 minuta @6:40-6:45<br><br>1 minuta pauze (ne hodanje, nego skroz stati)<br><br>5 minuta @6:30<br><br>1 minuta pauze (ne hodanje, nego skroz stati)<br><br>5 minuta @6:20<br><br>5 minuta @6:40-6:45", "Utrku započni na tempu 6:30 i drži tako 2km. U trećem kilometru postepeno ubrzavaj na 6:20. Četvrti kilometar drži 6:20. Zadnji kilometar postepeno ubrzavaj prvih 500m do 6:10, a onda zadnjih 500m raspali koliko misliš da možeš, ako ti 6:10 bude jako onda nemoj ubrzavati više od toga.  "], "Drugi trening odradi najkasnije u srijedu, nikako u četvrtak. Možeš i dan za danom ako slučajno ne možeš u srijedu trenirati npr. u ponedjeljak prvi trening i utorak drugi trening. "],
        ["Week 12", "15.5.-21.5.", ["22-25 minuta trčanja", "više minuta nego na prošlom treningu ali maksimalno 30 minuta", "više minuta nego na prošlom treningu ali maksimalno 35 minuta"], "na prvom treningu drži tempo 6:40-6:45, za druga dva ćemo se čuti"],
        ["Week 11", "8.5.-14.5.", ["3 x (15 min trčanja + 1-2 min hoda)", "Cooper test", "20 minuta trčanja @6:40-6:45"]]
        ]
    ,
     "marica":
        [
        "Marica",
        "Janković",
        ["Week 5", "29.5.-4.6.", ["8 minuta brzog hoda pa 5 x (3 min trčanja + 2 min hoda)", "8 minuta brzog hoda pa 6 x (3 min trčanja + 1.5 min hoda)", "8 minuta brzog hoda pa 6 x (3 min trčanja + 1 min hoda)"]],
        ["Week 4", "22.5.-28.5.", ["10 minuta brzog hoda pa 6 x (2 min trčanja + 1.5 min hoda)", "10 minuta brzog hoda pa 6 x (2 min trčanja + 1 min hoda)", "10 minuta brzog hoda pa 7 x (2 min trčanja + 1 min hoda)"]],
        ["Week 3", "15.5.-21.5.", ["10 minuta brzog hoda pa 9 x (1 min trčanja + 1.5 min hoda)", "10 minuta brzog hoda pa 10 x (1 min trčanja + 1 min hoda)", "10 minuta brzog hoda pa 5 x (2 min trčanja + 2 min hoda)"]],
        ["Week 2", "8.5.-14.5.", ["10 minuta brzog hoda pa 6 x (1 min trčanja + 2 min hoda)", "10 minuta brzog hoda pa 7 x (1 min trčanja + 2 min hoda)", "10 minuta brzog hoda pa 8 x (1 min trčanja + 1.5 min hoda)"]]
        ]
    , "kristina":
        [
        "Kristina",
        "Vukelić",
        ["Week 1", "29.5.-4.6.", ["zagrijavanje i rastrčavanje po 10-15min <br><br> Glavni dio treninga: 3km tempo polumaratona (TH) + 4km fartleka 1+2 (1min brzo + 2 sporo), bez pauze, znači ukupno 7km. <br><br>Tempa po grupama: TH - brza minuta - spore minute =  5:30 - 5:10 - 6:30", "45-60 min @6:30<br>", "zagrijavanje i rastrčavanje po 10-15min<br><br> Glavni dio: 2 seta po 3km (1 set = 1km tempo maratona TM + 1km tempo polumaratona TH + 1km tempo petice T5, sve spojeno), pauza između setova 1km lagano u tempu grupe ili sporije, znači ukupno 7km. Vremena po grupama: TM - TH - T5: 5:45 - 5:30 - 5:05", " Poludužina 18km (15km u tempu grupe TG + 3km u tempu polumaratona TH). 8. 5:30 / 6:30", "dan iza dužine ->60-75min @6:30-6:40" ], "Samo rokaj!"]]
    , "davor":
        [
        "Davor",
        "Turinski",
        ["Week 17", "5.6.-11.6.", ["3 x (13 min trčanja + 1 min hoda)", "2 x (14 min trčanja + 2 min hoda) + 8 min trčanja na kraju", "3 x (15 min trčanja + 1-2 min hoda)"], "Dobrodošao u zadnji tjedan u kojemu kao dio treninga imaš hodanje. Konačno je došao i taj trenutak :) Iako si spreman trčati 35 minuta bez hodanja što si dokazao na utrci, nemoj podcijeniti treninge koji su na meniju ovaj tjedan. Daj sve od sebe da ih odradiš, a onda idući tjedan idu malo lakši treninzi. "],
        ["Week 16", "29.5.-4.6.", ["3 x (11 minuta trčanja + 1 min hoda)", "2 x (12 minuta trčanja + 2 min hoda) + 10 minuta trčanja na kraju", "3 x (12 minuta trčanja + 1 min hoda)"], "Razmišljao sam što napraviti ako dobro otrčiš današnju utrku, odnosno otrčiš ju bez stajanja, a to si i uspio. Ima li smisla da radiš sve ove treninge koji vode prema tome da trčiš 35minuta u komadu ili ne, pošto si sada otrčao praktički 35 minuta u komadu i već sam ti mislio reći da ćemo preskočiti par stepenica. No nećemo to raditi, odraditi ćeš redom treninge koji su ti preostali. Ukupno imaš još 12 treninga u školi trčanja, od kojih je 6 sa hodanjem i 6 bez hodanja. Znači kroz 4 tjedna bi trebao završiti sa školom trčanja. No ono što je dobro je saznanje da sve te treninge si već sad sposoban odraditi. "],
        ["Week 15", "22.5.-28.5.", ["3 x (10 minuta trčanja + 2 min hoda) + 5 minuta trčanja na kraju", "10 minuta @6:40-6:45<br><br>1 minuta pauze (ne hodanje, nego skroz stati)<br><br>5 minuta @6:30<br><br>1 minuta pauze (ne hodanje, nego skroz stati)<br><br>5 minuta @6:20<br><br>5 minuta @6:40-6:45", "Vukovar 5km"], "Drugi trening odradi najkasnije u srijedu, nikako u četvrtak. Možeš i dan za danom ako slučajno ne možeš u srijedu trenirati npr. u ponedjeljak prvi trening i utorak drugi trening. "],
        ["Week 14", "15.5.-21.5.", ["3 x (9 minuta trčanja + 2 min hoda) + 5 minuta trčanja na kraju", "3 x (9 minuta trčanja + 1 min hoda)", "2 x (10 min trčanja + 2 min hoda) + 5 min trčanja na kraju"]],
        ["Week 13", "8.5.-14.5.", ["3 x (8 min trčanja + 1 min hoda) + 6 minuta trčanja na kraju", "Cooper Test", "3 x (9 minuta trčanja + 2 min hoda) + 5 minuta trčanja na kraju"]]
        ]
    }

@app.route('/davor')
def hello_davor():
    first_name = training_data["davor"][0]
    person_dict = {"davor": training_data["davor"]}
    return render_template('training_table.html', script=url_for("static", filename="script.js"), first_name=first_name, training_data=person_dict)

@app.route('/marko')
def hello_marko():
        # Render the template and pass data to it
    first_name = training_data["marko"][0]
    person_dict = {"marko": training_data["marko"]}
    return render_template('training_table.html', script=url_for("static", filename="script.js"), first_name=first_name, training_data=person_dict)

@app.route('/kristina90')
def hello_kristina():
    #check_connection()
    first_name = training_data["kristina"][0]
    person_dict = {"kristina": training_data["kristina"]}
    return render_template('training_table.html', script=url_for("static", filename="script.js"), first_name=first_name, training_data=person_dict)

@app.route('/marica')
def hello_marica():
    # Sample data for the table
    first_name = training_data["marica"][0]
    person_dict = {"marica": training_data["marica"]}
    return render_template('training_table.html', script=url_for("static", filename="script.js"), first_name=first_name, training_data=person_dict)

@app.route('/user/<username>')
def hello_user(username):
    #first_name = training_data[username][0]
    #person_dict = {username: training_data[username]}
    #first_name, last_name = get_user_name_surname(username)
    return render_template('training_table.html', script=url_for("static", filename="script.js"), first_name=first_name, training_data=person_dict)

@app.route('/whattoeat')
def hello_gladni():
    print("nešto")
    return "<h1>Bok! Želiš li kuhati ili naručiti?</h1>"

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html')
