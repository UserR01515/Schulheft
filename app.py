import streamlit as st
import math
import sqlite3
import pandas as pd
import os

# def Bild_hochladen():
#     con = sqlite3.connect("Bilder")
#     cur = con.cursor()
#     Bilder = cur.execute("CREATE TABLE IF OT EXISTS Bilder(Datum TEXT, Bild BLOB)")
#     uploaded_file = st.file_uploader("Wähle ein Bild aus", type=["jpg", "jpeg", "png"])
#     if uploaded_file is not None:
#         file_name = uploaded_file.name
#         saved_path = os.path.join(Bilder, file_name)
#         with open(saved_path, 'wb') as f:
#             f.write(uploaded_file.getbuffer())
#         st.success(f"Bild erfolgreich hochgeladen")


def Taschenrechner():
    def addieren(x, y):
        return x + y
    def subtrahieren(x, y):
        return x - y
    def multiplizieren(x, y):
        return x * y
    def dividieren(x, y):
        return x / y
    

    st.write(":blue-background[:blue[Taschenrechner]]")
    st.write("1 = Wurzel, Potenz ----- 2 = Addieren, Subtrahieren, Multiplizieren, Dividieren")
    eingabe_auswahl = st.pills("Wie viele Zahlen brauchst du zum berechnen? ", ["1", "2"])
    if eingabe_auswahl == "2":
        zahl_1 = st.number_input("Wie lautet deine erste Zahl? ")
        zahl_2 = st.number_input("Wie lautet deine zweite Zahl? ")
        eingabe = st.pills("Was möchtest du machen?", ["addieren", "subtrahieren", "multiplizieren", "dividieren"])
        if eingabe == "addieren":
            st.success(addieren(zahl_1, zahl_2))
        elif eingabe == "subtrahieren":
            st.success(subtrahieren(zahl_1, zahl_2))
        elif eingabe == "multiplizieren":
            st.success(multiplizieren(zahl_1, zahl_2))
        elif eingabe == "dividieren":
            st.success(dividieren(zahl_1, zahl_2))
    
    elif eingabe_auswahl == "1":
        zahl_1 = st.number_input("Wie lautet deine Zahl? ")
        eingabe = st.pills("Was möchtest du machen?", ["Wurzel ziehen", "Potenz"])
        if eingabe == "Wurzel ziehen":
            wurzel = math.sqrt(zahl_1)
            st.success(wurzel)
        elif eingabe == "Potenz":
            a = st.number_input("Mit welcher Zahl soll Zahl1 potenziert werden?", 1, step=1)
            st.write(zahl_1 ** a)


def Aufgabenheft(fach):
    con = sqlite3.connect("Fach.db")
    cur = con.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {fach}(Datum, Eintrag)")
    auswahl = st.pills("Wähle aus was du machen möchtest", ["Eintrag hinzufügen",
                                                            "Eintrag löschen",
                                                            "Einträge anzeigen"]
                                                            )

    if auswahl == "Eintrag hinzufügen":
        eingabe1 = st.text_area("Bitte gebe hier deinen Eintrag ein:")
        datum1 = st.text_input("Bitte gebe hier das aktuelle Datum ein:")
        if st.button("Eintrag bestätigen"):
            eintrag = cur.execute(f"INSERT INTO {fach}(Datum, Eintrag) VALUES(?, ?)", (datum1, eingabe1))
            ein = cur.execute(f"SELECT Datum, Eintrag FROM {fach}")
            st.data_editor(ein)
            con.commit()

    elif auswahl == "Eintrag löschen":
        datum = cur.execute(f"SELECT Datum FROM {fach}")
        datum_löschen = st.selectbox("Welches Datum möchtest du löschen?", datum)
        eintrag = cur.execute(f"SELECT Eintrag FROM {fach}")
        eintrag_löschen = st.selectbox("Welchen Eintrag möchtest du löschen", eintrag)
        if st.button("Diesen Eintrag löschen"):
            cur.execute(f"DELETE FROM {fach} WHERE Datum ='{datum_löschen}' AND Eintrag ='{eintrag_löschen}'")
            con.commit()

    elif auswahl == "Einträge anzeigen":
        dt = cur.execute(f"SELECT * FROM {fach}")
        st.write(dt)
        con.commit()

def Hefteintrag(fach):
    con = sqlite3.connect("Fach2.db")
    cur = con.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {fach}(Datum, Eintrag)")
    auswahl = st.pills("Wähle aus was du machen möchtest", ["Eintrag hinzufügen",
                                                            "Eintrag löschen",
                                                            "Einträge anzeigen"]
                                                            )

    if auswahl == "Eintrag hinzufügen":
        eingabe1 = st.text_area("Bitte gebe hier deinen Eintrag ein:")
        datum1 = st.text_input("Bitte gebe hier das aktuelle Datum ein:")
        if st.button("Eintrag bestätigen"):
            eintrag = cur.execute(f"INSERT INTO {fach}(Datum, Eintrag) VALUES(?, ?)", (datum1, eingabe1))
            ein = cur.execute(f"SELECT Datum, Eintrag FROM {fach}")
            st.data_editor(ein)
            con.commit()

    elif auswahl == "Eintrag löschen":
        datum = cur.execute(f"SELECT Datum FROM {fach}")
        datum_löschen = st.selectbox("Welches Datum möchtest du löschen?", datum)
        eintrag = cur.execute(f"SELECT Eintrag FROM {fach}")
        eintrag_löschen = st.selectbox("Welchen Eintrag möchtest du löschen", eintrag)
        if st.button("Diesen Eintrag löschen"):
            cur.execute(f"DELETE FROM {fach} WHERE Datum ='{datum_löschen}' AND Eintrag ='{eintrag_löschen}'")
            con.commit()

    elif auswahl == "Einträge anzeigen":
        dt = cur.execute(f"SELECT * FROM {fach}")
        st.write(dt)
        con.commit()

def Notizheft(fach):
    con = sqlite3.connect("Fach3.db")
    cur = con.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {fach}(Datum, Eintrag)")
    auswahl = st.pills("Wähle aus was du machen möchtest", ["Eintrag hinzufügen",
                                                            "Eintrag löschen",
                                                            "Einträge anzeigen"]
                                                            )

    if auswahl == "Eintrag hinzufügen":
        eingabe1 = st.text_area("Bitte gebe hier deinen Eintrag ein:")
        datum1 = st.text_input("Bitte gebe hier das aktuelle Datum ein:")
        if st.button("Eintrag bestätigen"):
            eintrag = cur.execute(f"INSERT INTO {fach}(Datum, Eintrag) VALUES(?, ?)", (datum1, eingabe1))
            ein = cur.execute(f"SELECT Datum, Eintrag FROM {fach}")
            st.data_editor(ein)
            con.commit()

    elif auswahl == "Eintrag löschen":
        datum = cur.execute(f"SELECT Datum FROM {fach}")
        datum_löschen = st.selectbox("Welches Datum möchtest du löschen?", datum)
        eintrag = cur.execute(f"SELECT Eintrag FROM {fach}")
        eintrag_löschen = st.selectbox("Welchen Eintrag möchtest du löschen", eintrag)
        if st.button("Diesen Eintrag löschen"):
            cur.execute(f"DELETE FROM {fach} WHERE Datum ='{datum_löschen}' AND Eintrag ='{eintrag_löschen}'")
            con.commit()

    elif auswahl == "Einträge anzeigen":
        dt = cur.execute(f"SELECT * FROM {fach}")
        st.write(dt)
        con.commit()

def periodensystem():
    eingabe2 = st.radio("Welche Hauptgruppe möchtest du angezeigt haben?", ["Alkalimetalle", "Erdalkalimetalle", "Borgruppe", "Kohlenstoffgruppe", "Stickstoffgruppe", "Chalkogene", "Halogene", "Edelgase"])
    if eingabe2 == "Alkalimetalle":
        #Alkalimetalle
        con = sqlite3.connect("Periodensystem")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Alkalimetalle(Ordnungszahl, Symbol, Name, Atomare Masse)")
        # alkalimetalle = [
        #     (1, "H", "hydrogen", 1.008),
        #     (3, "Li", "lithium", 6.94),
        #     (11, "Na", "sodium", 22.98976928),
        #     (19, "K", "potassium", 39.0983),
        #     (37, "Rb", "rubidium", 85.4678),
        #     (55, "Cs", "caesium", 132.90545196),
        #     (87, "Fr", "francium", 223)
        # ]
        # cur.executemany("INSERT INTO Alkalimetalle VALUES(?, ?, ?, ?)", alkalimetalle)
        dt = cur.execute("SELECT DISTINCT * FROM Alkalimetalle")
        st.data_editor(dt)
        con.commit()

    elif eingabe2 == "Erdalkalimetalle":
        #Erdalkalimetalle
        con = sqlite3.connect("Periodensystem")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Erdalkalimetalle(Ordnungszahl, Symbol, Name, Atomare Masse)")
        # erdalkalimetalle = [
        #     (4, "Be", "beryllium", 9.0121831),
        #     (12, "Mg", "magnesium", 24.305),
        #     (20, "Ca", "calcium", 40.078),
        #     (38, "Sr", "strontium", 87.62),
        #     (56, "Ba", "barium", 137.327),
        #     (88, "Ra", "radium", 226)
        # ]
        # cur.executemany("INSERT INTO Erdalkalimetalle VALUES(?, ?, ? ,?)", erdalkalimetalle)
        dt = cur.execute("SELECT DISTINCT* FROM Erdalkalimetalle")
        st.data_editor(dt)
        con.commit()

    elif eingabe2 == "Borgruppe":
        #Borgruppe
        con = sqlite3.connect("Periodensystem")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Borgruppe(Ordnungszahl, Symbol, Name, Atomare Masse)")
        # borgruppe = [
        #     (5, "B", "boron", 10.81),
        #     (13, "Al", "aluminium", 26.9815385),
        #     (31, "Ga", "gallium", 69.723),
        #     (49, "In", "indium", 114.818),
        #     (81, "Tl", "thallium", 204.38)
        # ]
        # cur.executemany("INSERT INTO Borgruppe VALUES(?, ?, ? ,?)", borgruppe)
        dt = cur.execute("SELECT DISTINCT * FROM Borgruppe")
        st.data_editor(dt)
        con.commit()

    elif eingabe2 == "Kohlenstoffgruppe":
        #Kohlenstoffgruppe
        con = sqlite3.connect("Periodensystem")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Kohlenstoffgruppe(Ordnungszahl, Symbol, Name, Atomare Masse)")
        # kohlenstoffgruppe = [
        #     (6, "C", "carbon", 12.011),
        #     (14, "Si", "silicon", 28.085),
        #     (32, "Ge", "germanium", 72.63),
        #     (50, "Sn", "tin", 118.71),
        #     (82, "Pb", "lead", 207.2)
        # ]
        # cur.executemany("INSERT INTO Kohlenstoffgruppe VALUES(?, ?, ? ,?)", kohlenstoffgruppe)
        dt = cur.execute("SELECT DISTINCT * FROM Kohlenstoffgruppe")
        st.data_editor(dt)
        con.commit()

    elif eingabe2 == "Stickstoffgruppe":
        #Stickstoffgruppe
        con = sqlite3.connect("Periodensystem")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Stickstoffgruppe(Ordnungszahl, Symbol, Name, Atomare Masse)")
        # stickstoffgruppe = [
        #     (7, "N", "nitrogen", 14.007),
        #     (15, "P", "phosphorus", 30.973761998),
        #     (33, "As", "arsenic", 74.921595),
        #     (51, "Sb", "antimony", 121.76),
        #     (83, "Bi", "bismuth", 208.9804)
        # ]
        # cur.executemany("INSERT INTO Stickstoffgruppe VALUES(?, ?, ? ,?)", stickstoffgruppe)
        dt = cur.execute("SELECT DISTINCT * FROM Stickstoffgruppe")
        st.data_editor(dt)
        con.commit()

    elif eingabe2 == "Chalkogene":
        #Chalkogene
        con = sqlite3.connect("Periodensystem")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Chalkogene(Ordnungszahl, Symbol, Name, Atomare Masse)")
        # chalkogene = [
        #     (8, "O", "oxygen", 15.999),
        #     (16, "S", "sulfur", 32.06),
        #     (34, "Se", "selenium", 78.971),
        #     (52, "Te", "tellurium", 127.6),
        #     (84, "Po", "polonium", 209)
        # ]
        # cur.executemany("INSERT INTO Chalkogene VALUES(?, ?, ? ,?)", chalkogene)
        dt = cur.execute("SELECT DISTINCT* FROM Chalkogene")
        st.data_editor(dt)
        con.commit()

    elif eingabe2 == "Halogene":
        #Halogene
        con = sqlite3.connect("Periodensystem")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Halogene(Ordnungszahl, Symbol, Name, Atomare Masse)")
        # halogene = [
        #     (9, "F", "fluorine", 18.998403163),
        #     (17, "Cl", "chlorine", 35.45),
        #     (35, "Br", "bromine", 79.904),
        #     (53, "I", "iodine", 126.90447),
        #     (85, "At", "astatine", 210)
        # ]
        # cur.executemany("INSERT INTO Halogene VALUES(?, ?, ? ,?)", halogene)
        dt = cur.execute("SELECT DISTINCT * FROM Halogene")
        st.data_editor(dt)
        con.commit()

    elif eingabe2 == "Edelgase":
        #Edelgase
        con = sqlite3.connect("Periodensystem")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Edelgase(Ordnungszahl, Symbol, Name, Atomare Masse)")
        # edelgase = [
        #     (2, "He", "helium", 4.002602),
        #     (10, "Ne", "neon", 20.1797),
        #     (18, "Ar", "argon", 39.948),
        #     (36, "Kr", "krypton", 83.798),
        #     (54, "Xe", "xenon", 131.293),
        #     (86, "Rn", "radon", 222)
        # ]
        # cur.executemany("INSERT INTO Edelgase VALUES(?, ?, ? ,?)", edelgase)
        dt = cur.execute("SELECT DISTINCT * FROM Edelgase")
        st.data_editor(dt)
        con.commit()


def Noten(fach):
    con = sqlite3.connect("Note")
    cur = con.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {fach}(Notentyp, Note)")
    eingabe = st.pills("Was möchtest du machen, wähle aus", ["Note hinzufügen", "Note löschen", "Noten anzeigen", "Notendurchschnitt"])
    if eingabe == "Note hinzufügen":
        abc = st.selectbox("Wähle einen Notentyp aus", ["mN", "SA", "StgA"])
        if abc == "mN": 
            note = st.text_input("Gebe deine Note ein:")
            if st.button("Auswahl bestätigen"):
                cur.execute(f"INSERT INTO {fach} VALUES('mN', '{note}')" )
                con.commit()
                dt = cur.execute(f"SELECT * FROM {fach}")
                st.data_editor(dt)

        elif abc == "SA": 
            note = st.text_input("Gebe deine Note ein:")
            if st.button("Auswahl bestätigen"):
                cur.execute(f"INSERT INTO {fach} VALUES('SA', '{note}')" )
                con.commit()
                dt = cur.execute(f"SELECT * FROM {fach}")
                st.data_editor(dt)

        elif abc == "StgA": 
            note = st.text_input("Gebe deine Note ein:")
            if st.button("Auswahl bestätigen"):
                cur.execute(f"INSERT INTO {fach} VALUES('StgA', '{note}')" )
                con.commit()
                dt = cur.execute(f"SELECT * FROM {fach}")
                st.data_editor(dt)

    elif eingabe == "Note löschen":
        a = cur.execute(f"SELECT Note FROM {fach}")
        b = st.selectbox("Wähle aus welche Note du löschen möchtest", a)
        c = cur.execute(f"SELECT Notentyp FROM {fach}")
        d = st.selectbox("Wähle aus welchen Notentyp du löschen möchtest", c)
        if st.button("Auswahl löschen"):
            cur.execute(f"DELETE FROM {fach} WHERE Note = '{b}' AND Notentyp = '{d}'")
            con.commit()

    elif eingabe == "Noten anzeigen":
        print = cur.execute(f"SELECT * FROM {fach}")
        con.commit()
        st.data_editor(print)

    elif eingabe == "Notendurchschnitt":

        def dividieren(x, y):
            return x / y if y else None 

        a = cur.execute(f"SELECT COUNT(Note) FROM {fach}").fetchone()[0]
        b = cur.execute(f"SELECT SUM(Note) FROM {fach}").fetchone()[0]

        ergebnis = dividieren(b, a)

        if ergebnis is None:
            st.error("Keine Noten vorhanden")
        else:
            st.success(ergebnis)
            

def Formeln(fach):
    con = sqlite3.connect("Formeln")
    cur = con.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {fach}(Begriff, AErklärung)")
    eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Formel löschen", "Formeln anzeigen"])
    if eingabe == "Eintrag hinzufügen":
        v1 = st.text_input("Bitte gebe hier den Begriff ein:")
        v2 = st.text_input("Bitte gebe hier die Erklärung ein:")
        if st.button("Eintrag bestätigen"):
            cur.execute(f"INSERT INTO {fach} VALUES('{v1}', '{v2}')")
            dt = cur.execute(f"SELECT * FROM {fach}")
            st.data_editor(dt)
            con.commit()
    elif eingabe == "Formel löschen":
        #Eintrag löschen
        vokabel_löschen = cur.execute(f"SELECT Begriff FROM {fach}")
        auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", vokabel_löschen)
        if st.button("Auswahl löschen"):
            cur.execute(f"DELETE FROM {fach} WHERE Begriff = ('{auswahl_datum_löschen}')")
            con.commit()
    elif eingabe == "Formeln anzeigen":
        dt = cur.execute(f"SELECT * FROM {fach}")
        st.data_editor(dt)
        con.commit()

def Vokabeln(fach):
    con = sqlite3.connect("Vokabeln")
    cur = con.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {fach}(Deutsch, Andere_Sprache)")
    eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Vokabeln löschen", "Vokabeln anzeigen"])
    if eingabe == "Eintrag hinzufügen":
        v1 = st.text_input("Bitte gebe hier die das deutsche Wort ein:")
        v2 = st.text_input("Bitte gebe hier das andersprachige Wort ein:")
        if st.button("Eintrag bestätigen"):
            cur.execute(f"INSERT INTO {fach} VALUES('{v1}', '{v2}')")
            dt = cur.execute(f"SELECT * FROM {fach}")
            st.data_editor(dt)
            con.commit()
    elif eingabe == "Vokabeln löschen":
        #Eintrag löschen
        vokabel_löschen = cur.execute(f"SELECT Deutsch FROM {fach}")
        auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", vokabel_löschen)
        if st.button("Auswahl löschen"):
            cur.execute(f"DELETE FROM {fach} WHERE Deutsch = ('{auswahl_datum_löschen}')")
            con.commit()
    elif eingabe == "Vokabeln anzeigen":
        dt = cur.execute(f"SELECT * FROM {fach}")
        st.data_editor(dt)
        con.commit()

def Schulheft():
    st.sidebar.title(":blue[Schulheft]")
    b = st.sidebar.toggle("Fächer")
    if b is True:               
        options = ["Mathe",
                    "Deutsch",
                    "Französisch",
                    "Englisch",
                    "Geschichte",
                    "Religion",
                    "Chemie",
                    "Physik",
                    "Informatik",
                    "Biologie", 
                    ]
        fach = st.sidebar.radio("Wähle ein Fach aus", options)

        #mathe
        if fach == "Mathe":
            st.header(":blue[Mathe]")
            eingabe = st.pills("Wähle aus was du machen möchtest:", ["Aufgabenheft", "Hefteintrag", "Notizheft", "Taschenrechner", "Noten"])
            if eingabe == "Aufgabenheft":
                Aufgabenheft(fach)
            elif eingabe == "Hefteintrag":
                Hefteintrag(fach)
            elif eingabe == "Notizheft":
                Notizheft(fach)
            elif eingabe == "Taschenrechner":
                Taschenrechner()
            elif eingabe == "Noten":
                Noten(fach)


        #französisch
        elif fach == "Französisch":
            st.header(":red[Französisch]")
            eingabe = st.pills("Wähle aus was du machen möchtest:", ["Aufgabenheft", "Hefteintrag", "Notizheft", "Vokabeln", "Noten"])
            if eingabe == "Aufgabenheft":
                Aufgabenheft(fach)
            elif eingabe == "Hefteintrag":
                Hefteintrag(fach)
            elif eingabe == "Notizheft":
                Notizheft(fach)
            elif eingabe == "Vokabeln":
                Vokabeln(fach)
            elif eingabe == "Noten":
                Noten(fach)



        #englisch
        elif fach == "Englisch":
            st.header(":green[Englisch]")
            eingabe = st.pills("Wähle aus was du machen möchtest:", ["Aufgabenheft", "Hefteintrag", "Notizheft", "Vokabeln", "Noten"])
            if eingabe == "Aufgabenheft":
                Aufgabenheft(fach)
            elif eingabe == "Hefteintrag":
                Hefteintrag(fach)
            elif eingabe == "Notizheft":
                Notizheft(fach)
            elif eingabe == "Vokabeln":
                Vokabeln(fach)
            elif eingabe == "Noten":
                Noten(fach)


        #deutsch
        elif fach == "Deutsch":
            st.header(":orange[Deutsch]")
            eingabe = st.pills("Wähle aus was du machen möchtest:", ["Aufgabenheft", "Hefteintrag", "Notizheft", "Noten"])
            if eingabe == "Aufgabenheft":
                Aufgabenheft(fach)
            elif eingabe == "Hefteintrag":
                Hefteintrag(fach)
            elif eingabe == "Notizheft":
                Notizheft(fach)
            elif eingabe == "Noten":
                Noten(fach)

        #geschichte
        elif fach == "Geschichte":
            st.header("Geschichte")
            eingabe = st.pills("Wähle aus was du machen möchtest:", ["Aufgabenheft", "Hefteintrag", "Notizheft", "Noten"])
            if eingabe == "Aufgabenheft":
                Aufgabenheft(fach)
            elif eingabe == "Hefteintrag":
                Hefteintrag(fach)
            elif eingabe == "Notizheft":
                Notizheft(fach)
            elif eingabe == "Noten":
                Noten(fach)


        #chemie
        elif fach == "Chemie":
            st.header("Chemie")
            eingabe = st.pills("Wähle aus was du machen möchtest:", ["Aufgabenheft", "Hefteintrag", "Notizheft", "Periodensystem", "Noten"])
            if eingabe == "Aufgabenheft":
                Aufgabenheft(fach)
            elif eingabe == "Hefteintrag":
                Hefteintrag(fach)
            elif eingabe == "Notizheft":
                Notizheft(fach)
            elif eingabe == "Periodensystem":
                periodensystem()
            elif eingabe == "Noten":
                Noten(fach)

        #physik   
        elif fach == "Physik":
            st.header(":violet[Physik]")
            eingabe = st.pills("Wähle aus was du machen möchtest:", ["Aufgabenheft", "Hefteintrag", "Notizheft", "Formeln", "Noten"])
            if eingabe == "Aufgabenheft":
                Aufgabenheft(fach)
            elif eingabe == "Hefteintrag":
                Hefteintrag(fach)
            elif eingabe == "Notizheft":
                Notizheft(fach)
            elif eingabe == "Formeln":
                Formeln(fach)
            elif eingabe == "Noten":
                Noten(fach)


        #biologie
        elif fach == "Biologie":
            st.header(":orange[Biologie]")
            eingabe = st.pills("Wähle aus was du machen möchtest:", ["Aufgabenheft", "Hefteintrag", "Notizheft", "Noten"])
            if eingabe == "Aufgabenheft":
                Aufgabenheft(fach)
            elif eingabe == "Hefteintrag":
                Hefteintrag(fach)
            elif eingabe == "Notizheft":
                Notizheft(fach)
            elif eingabe == "Noten":
                Noten(fach)


        #religion
        elif fach == "Religion":
            st.header(":violet[Religion]")
            eingabe = st.pills("Wähle aus was du machen möchtest:", ["Aufgabenheft", "Hefteintrag", "Notizheft", "Noten"])
            if eingabe == "Aufgabenheft":
                Aufgabenheft(fach)
            elif eingabe == "Hefteintrag":
                Hefteintrag(fach)
            elif eingabe == "Notizheft":
                Notizheft(fach)
            elif eingabe == "Noten":
                Noten(fach)


        #informatik
        elif fach == "Informatik":
            st.header(":blue[Informatik]")
            eingabe = st.pills("Wähle aus was du machen möchtest:", ["Aufgabenheft", "Hefteintrag", "Notizheft", "Noten"])
            if eingabe == "Aufgabenheft":
                Aufgabenheft(fach)
            elif eingabe == "Hefteintrag":
                Hefteintrag(fach)
            elif eingabe == "Notizheft":
                Notizheft(fach)
            elif eingabe == "Noten":
                Noten(fach)


        



    a = st.sidebar.toggle("Andere Optionen")
    if a is True:
        auswahl = st.sidebar.radio("", ["Chat", "Ideen zur Verbesserung", "Terminplaner"])
        #ideen
        if auswahl == "Ideen zur Verbesserung":
            st.header("Ideen zur Verbesserung")
            con = sqlite3.connect("Ideen")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Ideen(Idee)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Ideen anzeigen", "Idee löschen"])
            if eingabe == "Eintrag hinzufügen":
                #dta = ["Vorlage", "Vorlage"]
                #cur.execute("INSERT INTO Ideen VALUES(?, ?)", dta)
                #con.commit()
                eintrag = st.text_input("Gebe hier zuerst einen Titel und dann deine Idee ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Ideen VALUES('{eintrag}')")
                    data = cur.execute("SELECT * FROM Ideen")
                    con.commit()
                    st.data_editor(data)
                    
            elif eingabe == "Ideen anzeigen":
                daten = cur.execute("SELECT * FROM Ideen")
                st.data_editor(daten)
                con.commit()
                    
            elif eingabe == "Idee löschen":
                idee_löschen = cur.execute("SELECT Idee FROM Ideen")
                auswahl_idee_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", idee_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Ideen WHERE Idee = ('{auswahl_idee_löschen}')")
                    con.commit()
                    st.success("Idee wurde gelöscht")
        
        #terminplaner
        elif auswahl == "Terminplaner":
            st.header("Terminplaner")
            con = sqlite3.connect("Terminplaner")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Terminplaner(Datum, Betreff)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Termine anzeigen", "Termin löschen"])
            if eingabe == "Eintrag hinzufügen":
                #dta = ["Vorlage", "Vorlage"]
                #cur.execute("INSERT INTO Ideen VALUES(?, ?)", dta)
                #con.commit()
                eintrag1 = st.text_input("Gebe hier das Datum ein:")
                eintrag2 = st.text_input("Gebe hier den Betreff ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Terminplaner VALUES('{eintrag1}', '{eintrag2}')")
                    data = cur.execute("SELECT * FROM Terminplaner")
                    con.commit()
                    st.data_editor(data)

            elif eingabe == "Termin löschen":
                b = cur.execute("SELECT * FROM Terminplaner")
                a = st.selectbox("Wähle aus welchen Termin du löschen möchtest", b)
                if st.button("Termin löschen"):
                    cur.execute(f"DELETE FROM Terminplaner WHERE Termin = '{a}'")
                    con.commit()
                
                    
            elif eingabe == "Termine anzeigen":
                daten = cur.execute("SELECT * FROM Terminplaner")
                st.data_editor(daten)
                con.commit()

        #Chat
        elif auswahl == "Chat":
            st.header("Chat")
            con = sqlite3.connect("Chat")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Chat(Nachricht)")
            eingabe = st.pills("Wähle aus:", ["Nachricht schreiben", "Chat anzeigen", "Nachricht löschen"])
            if eingabe == "Nachricht schreiben":
                #dta = ["Vorlage", "Vorlage"]
                #cur.execute("INSERT INTO Ideen VALUES(?, ?)", dta)
                #con.commit()
                eintrag = st.text_input("Gebe hier deine Nachricht ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Chat VALUES('{eintrag}')")
                    data = cur.execute("SELECT * FROM Chat")
                    con.commit()
                    st.write(data)

            elif eingabe == "Nachricht löschen":
                b = cur.execute("SELECT * FROM Chat")
                a = st.selectbox("Wähle aus welche Nachricht du löschen möchtest", b)
                if st.button("Nachricht löschen"):
                    cur.execute(f"DELETE FROM Chat WHERE Nachricht = '{a}'")
                    con.commit()
                
                    
            elif eingabe == "Chat anzeigen":
                daten = cur.execute("SELECT * FROM Chat")
                st.table(daten)
                con.commit()



    Link = st.sidebar.toggle("Links")
    if Link is True:
        st.sidebar.page_link("https://auth.bycs.de/realms/bycs/protocol/openid-connect/auth?response_type=code&client_id=portal.bycs-prod-oidc&scope=openid&state=FtVxjx8iQgKJGmYi-M9IfN-5Kb-p1S9exFqVaPXujLo%3D&redirect_uri=https://portal.bycs.de/api/login/oauth2/code/bycs_webportal&nonce=MUX6pVWfXmKOIBpiopAFK3xK1tQbaXSugwQxcM0kOqQ", label="Mebis", icon="Ⓜ️")
        st.sidebar.page_link("https://de.wikipedia.org/wiki/Wiki", label="Wikipedia", icon="📖")
        st.sidebar.page_link("https://dict.leo.org/englisch-deutsch/", label="LEO Dictionary", icon="🦁")
        st.sidebar.page_link("https://www.isb.bayern.de/schularten/gymnasium/lehrplan/", label="ISB-Bayern", icon="🏫")
        st.sidebar.page_link("https://www.office.com/", label="Microsoft Office", icon="🗃️")
        st.sidebar.page_link("https://mathegym.de/", label="Mathegym", icon="🎖️")
        st.sidebar.page_link("https://www.duden.de/", label="Duden", icon="📖")
        st.sidebar.page_link("https://studyflix.de/", label="Studyflix", icon="🧠")
        st.sidebar.page_link("https://schulminator.com/", label="Schulminator", icon="🚩")
        st.sidebar.page_link("https://www.geogebra.org/classic", label="GeoGebra Classic", icon="📈")
        st.sidebar.page_link("https://de.serlo.org/", label="SERLO Naturwissenschaften", icon="🔭")
        st.sidebar.page_link("https://www.deepl.com/de/translator", label="Übersetzer", icon="📃")


    st.sidebar.feedback("stars")

    

#login
psd = st.text_input("Bitte gebe das Passwort ein:")
if psd == "192837465":
    Schulheft() 
    # con = sqlite3.connect("Anmeldung")
    # cur = con.cursor()
    # cur.execute("CREATE TABLE IF NOT EXISTS Anmeldung(Name, Passwort)")
    # a = st.pills("Wähle aus:", ["Registrieren", "Anmelden"])
    # if a == "Registrieren":
    #     c = st.text_input("Gebe deinen richtigen Namen ein")
    #     b = st.text_input("Gebe dein Passwort ein")
    #     st.warning("Wenn du den Button drückst, bestätigst du das du keine unerlaubten Sachen, wie zum Beispiel die Daten in einem Heft machst. Andernfalls wird dein Zugang gesperrt!")
    #     if st.button("Bestätigen"):
    #         cur.execute(f"INSERT INTO Anmeldung VALUES('{c}', '{b}')")
    #         con.commit()
    #         dt = st.success(f"Hallo {c}, deine Anmeldung wurde gespeichert")
    #         v = cur.execute("SELECT * FROM Anmeldung")
    #         st.write(v)
    #         # options = cur.execute("SELECT Name FROM Anmeldung")
    #         # cv = st.selectbox("", options)
    #         # cur.execute(f"DELETE FROM Anmeldung WHERE Name = '{cv}'")
    #         # con.commit()

    # elif a == "Anmelden":
    #     c = st.text_input("Gebe deinen richtigen Namen ein")
    #     b = st.text_input("Gebe dein Passwort ein")
    #     if st.button("Anmelden"):
    #         überprüfen = cur.execute(f"SELECT * FROM Anmeldung WHERE Name = '{c}' AND Passwort = '{b}'")
    #         con.commit()
    #         if überprüfen is True:
    #             Schulheft()


# def datei_hochladen():
#     ab = st.pills("Wähle aus was du machen willst:", ["CSV", "JPG/JPEG/PNG"])
#     if ab == "JPG/JPEG/PNG":
#         con = sqlite3.connect("Images.db")
#         cur = con.cursor()

#         cur.execute("""
#             CREATE TABLE IF NOT EXISTS Images(
#                 Datum TEXT,
#                 Bild BLOB
#             )
#         """)

#         uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

#         if uploaded_file is not None:
#             st.success("Erfolgreich hochgeladen")

#             # Bild anzeigen (NUR Anzeige)
#             st.image(uploaded_file, caption="Hochgeladenes Bild", use_container_width=True)

#             q = st.text_input("Gebe das heutige Datum ein:")

#             if q:
#                 image_bytes = uploaded_file.read()

#                 cur.execute(
#                     "INSERT INTO Images (Datum, Bild) VALUES (?, ?)",(q, image_bytes))
#                 con.commit()
#                 dt = cur.execute("SELECT * FROM Images")
#                 st.write(dt)
#         con.close()
#     elif ab == "CSV":
#         con = sqlite3.connect("Files.db")
#         cur = con.cursor()

#         cur.execute("""
#             CREATE TABLE IF NOT EXISTS Files(
#                 Datum TEXT,
#                 Text TEXT
#             )
#         """)

#         uploaded_file = st.file_uploader("", type="csv")

#         if uploaded_file is not None:
#             st.success("Erfolgreich hochgeladen")

#             # CSV anzeigen (nur Anzeige!)
#             csv_text = uploaded_file.getvalue().decode("utf-8")
#             st.text_area("CSV Inhalt", csv_text, height=300)

#             p = st.text_input("Gebe das heutige Datum ein:")

#             if p:
#                 cur.execute(
#                     "INSERT INTO Files (Datum, Text) VALUES (?, ?)",
#                     (p, csv_text)
#                 )
#                 con.commit()
#                 con.close()



                   
	
