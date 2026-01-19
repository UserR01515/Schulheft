import streamlit as st
import math
import sqlite3
psw= st.text_input("Gebe das Passwort ein:")
if psw == "192837465":
    st.sidebar.title("Schulheft")
    auswahl = st.sidebar.radio("Wähle eine der folgenden Funktionen aus:", ["Mathe", 
                                                                            "Deutsch", 
                                                                            "Französisch", 
                                                                            "Geschichte",
                                                                            "Englisch",
                                                                            "Physik", 
                                                                            "Chemie", 
                                                                            "Informatik", 
                                                                            "Religion", 
                                                                            "Biologie", 
                                                                            "Terminplaner", 
                                                                            "Chat",
                                                                            "Ideen zur Verbesserung"]
                                                                            )
    
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

    st.sidebar.feedback("stars")
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
        
    
#Mathe
    elif auswahl == "Mathe":
        # Definitionen
        def addieren(x, y):
            return x + y
        def subtrahieren(x, y):
            return x - y
        def multiplizieren(x, y):
            return x * y
        def dividieren(x, y):
            return x / y

        st.header(":blue[Mathe]")
        m_auswahl = st.pills("Wähle aus was du machen möchtest:", ["Taschenrechner",
                                                                "Hefteintrag", 
                                                                "Notizheft", 
                                                                "Aufgabenheft"]
                                                                )
        if m_auswahl == "Taschenrechner": 
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
                    quad = st.write(zahl_1 ** a)

        elif m_auswahl == "Hefteintrag":
            #Eintrag und Datum in Liste hinzufügen
            con = sqlite3.connect("Hefteintrag_mathe")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Hefteintrag_mathe(datum, eintrag)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Datum löschen", "Hefteinträge anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                # dta = ["Vorlage", "Vorlage"]
                # cur.execute("INSERT INTO Hefteintrag_mathe VALUES(?, ?)", dta)
                # con.commit()
                eintrag = st.text_area("Gebe hier zuerst einen Titel und dann deine Notizen ein:")
                datum = st.text_input("Gebe ein Datum zu dem Eintrag ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Hefteintrag_mathe VALUES('{datum}', '{eintrag}')")
                    data = cur.execute("SELECT * FROM Hefteintrag_mathe")
                    con.commit()
                    st.table(data)
            
            elif eingabe == "Datum löschen":
                #Eintrag löschen
                datum_löschen = cur.execute("SELECT datum FROM Hefteintrag_mathe")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", datum_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Hefteintrag_mathe WHERE datum = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Hefteinträge anzeigen":
                dt = cur.execute("SELECT * FROM Hefteintrag_mathe")
                st.data_editor(dt)
                con.commit()
        
        elif m_auswahl == "Notizheft":
            #Eintrag und Datum in Liste hinzufügen
            con = sqlite3.connect("Hefteintrag_mathe")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Notizheft_mathe(datum, eintrag)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Datum löschen", "Notizheft anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                # dta = ["Vorlage", "Vorlage"]
                # cur.execute("INSERT INTO Hefteintrag_mathe VALUES(?, ?)", dta)
                # con.commit()
                eintrag = st.text_area("Gebe hier zuerst einen Titel und dann deine Notizen ein:")
                datum = st.text_input("Gebe ein Datum zu dem Eintrag ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Notizheft_mathe VALUES('{datum}', '{eintrag}')")
                    data = cur.execute("SELECT * FROM Notizheft_mathe")
                    con.commit()
                    st.data_editor(data)
            
            elif eingabe == "Datum löschen":
                #Eintrag löschen
                datum_löschen = cur.execute("SELECT datum FROM Notizheft_mathe")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", datum_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Notizheft_mathe WHERE datum = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Notizheft anzeigen":
                dt = cur.execute("SELECT * FROM Notizheft_mathe")
                st.data_editor(dt)
                con.commit()

        elif m_auswahl == "Aufgabenheft":
            #Eintrag und Datum in Liste hinzufügen
            con = sqlite3.connect("Hefteintrag_mathe")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Aufgabenheft_mathe(datum, eintrag)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Datum löschen", "Aufgabenheft anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                # dta = ["Vorlage", "Vorlage"]
                # cur.execute("INSERT INTO Hefteintrag_mathe VALUES(?, ?)", dta)
                # con.commit()
                eintrag = st.text_area("Gebe hier zuerst einen Titel und dann deine Notizen ein:")
                datum = st.text_input("Gebe ein Datum zu dem Eintrag ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Aufgabenheft_mathe VALUES('{datum}', '{eintrag}')")
                    data = cur.execute("SELECT * FROM Aufgabenheft_mathe")
                    con.commit()
                    st.data_editor(data)
            
            elif eingabe == "Datum löschen":
                #Eintrag löschen
                datum_löschen = cur.execute("SELECT datum FROM Aufgabenheft_mathe")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", datum_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Aufgabenheft_mathe WHERE datum = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Aufgabenheft anzeigen":
                dt = cur.execute("SELECT * FROM Aufgabenheft_mathe")
                st.data_editor(dt)
                con.commit()
#Deutsch
    elif auswahl == "Deutsch":
        st.header(":orange[Deutsch]")
        eingabe = st.pills("Wähle aus was du machen möchtest:", ["Notizheft", "Hefteintrag", "Aufsatz schreiben"])
        if eingabe == "Notizheft":
            #Eintrag und Datum in Liste hinzufügen
            con = sqlite3.connect("Hefteintrag_deutsch")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Notizheft_deutsch(datum, eintrag)")
            eingabe1 = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Datum löschen", "Notizheft anzeigen"])
            if eingabe1 == "Eintrag hinzufügen":
                # dta = ["Vorlage", "Vorlage"]
                # cur.execute("INSERT INTO Hefteintrag_mathe VALUES(?, ?)", dta)
                # con.commit()
                eintrag = st.text_area("Gebe hier zuerst einen Titel und dann deine Notizen ein:")
                datum = st.text_input("Gebe ein Datum zu dem Eintrag ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Notizheft_deutsch VALUES('{datum}', '{eintrag}')")
                    data = cur.execute("SELECT * FROM Notizheft_deutsch")
                    con.commit()
                    st.data_editor(data)
            
            elif eingabe1 == "Datum löschen":
                #Eintrag löschen
                datum_löschen = cur.execute("SELECT datum FROM Notizheft_deutsch")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", datum_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Notizheft_deutsch WHERE datum = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe1 == "Notizheft anzeigen":
                dt = cur.execute("SELECT * FROM Notizheft_deutsch")
                st.data_editor(dt)
                con.commit()
        
        elif eingabe == "Hefteintrag":
            #Eintrag und Datum in Liste hinzufügen
            con = sqlite3.connect("Hefteintrag_deutsch")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Hefteintrag_deutsch(datum, eintrag)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Datum löschen", "Hefteinträge anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                # dta = ["Vorlage", "Vorlage"]
                # cur.execute("INSERT INTO Hefteintrag_mathe VALUES(?, ?)", dta)
                # con.commit()
                eintrag = st.text_area("Gebe hier zuerst einen Titel und dann deine Notizen ein:")
                datum = st.text_input("Gebe ein Datum zu dem Eintrag ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Hefteintrag_deutsch VALUES('{datum}', '{eintrag}')")
                    data = cur.execute("SELECT * FROM Hefteintrag_deutsch")
                    con.commit()
                    st.data_editor(data)
            
            elif eingabe == "Datum löschen":
                #Eintrag löschen
                datum_löschen = cur.execute("SELECT datum FROM Hefteintrag_deutsch")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", datum_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Hefteintrag_deutsch WHERE datum = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Hefteinträge anzeigen":
                dt = cur.execute("SELECT * FROM Hefteintrag_deutsch")
                st.data_editor(dt)
                con.commit()

        elif eingabe == "Aufsatz schreiben":
            #Eintrag und Datum in Liste hinzufügen
            con = sqlite3.connect("Aufsatz_dt")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Aufsatz_dt(datum, eintrag)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Datum löschen", "Aufsätze anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                # dta = ["Vorlage", "Vorlage"]
                # cur.execute("INSERT INTO Hefteintrag_mathe VALUES(?, ?)", dta)
                # con.commit()
                eintrag = st.text_area("Gebe hier zuerst einen Titel und dann deine Notizen ein:")
                datum = st.text_input("Gebe ein Datum zu dem Eintrag ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Aufsatz_dt VALUES('{datum}', '{eintrag}')")
                    data = cur.execute("SELECT * FROM Aufsatz_dt")
                    con.commit()
                    st.data_editor(data)
            
            elif eingabe == "Datum löschen":
                #Eintrag löschen
                datum_löschen = cur.execute("SELECT datum FROM Aufsatz_dt")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", datum_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Aufsatz_dt WHERE datum = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Aufsätze anzeigen":
                dt = cur.execute("SELECT * FROM Aufsatz_dt")
                st.data_editor(dt)
                con.commit()
#Französisch
    elif auswahl == "Französisch":
        st.header(":red[Französisch]")
        eingabe = st.pills("Wähle aus was du machen möchtest:", ["Notizheft", "Hefteintrag", "Übersetzer", "Vokabeln"])
        if eingabe == "Notizheft":
            #Eintrag und Datum in Liste hinzufügen
            con = sqlite3.connect("Hefteintrag_frz")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Notizheft_frz(datum, eintrag)")
            eingabe1 = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Datum löschen", "Notizheft anzeigen"])
            if eingabe1 == "Eintrag hinzufügen":
                # dta = ["Vorlage", "Vorlage"]
                # cur.execute("INSERT INTO Hefteintrag_mathe VALUES(?, ?)", dta)
                # con.commit()
                eintrag = st.text_area("Gebe hier zuerst einen Titel und dann deine Notizen ein:")
                datum = st.text_input("Gebe ein Datum zu dem Eintrag ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Notizheft_frz VALUES('{datum}', '{eintrag}')")
                    data = cur.execute("SELECT * FROM Notizheft_frz")
                    con.commit()
                    st.data_editor(data)
            
            elif eingabe1 == "Datum löschen":
                #Eintrag löschen
                datum_löschen = cur.execute("SELECT datum FROM Notizheft_frz")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", datum_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Notizheft_frz WHERE datum = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe1 == "Notizheft anzeigen":
                dt = cur.execute("SELECT * FROM Notizheft_frz")
                st.data_editor(dt)
                con.commit()
        
        elif eingabe == "Hefteintrag":
            #Eintrag und Datum in Liste hinzufügen
            con = sqlite3.connect("Hefteintrag_frz")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Hefteintrag_frz(datum, eintrag)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Datum löschen", "Hefteinträge anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                # dta = ["Vorlage", "Vorlage"]
                # cur.execute("INSERT INTO Hefteintrag_mathe VALUES(?, ?)", dta)
                # con.commit()
                eintrag = st.text_area("Gebe hier zuerst einen Titel und dann deine Notizen ein:")
                datum = st.text_input("Gebe ein Datum zu dem Eintrag ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Hefteintrag_frz VALUES('{datum}', '{eintrag}')")
                    data = cur.execute("SELECT * FROM Hefteintrag_frz")
                    con.commit()
                    st.data_editor(data)
            
            elif eingabe == "Datum löschen":
                #Eintrag löschen
                datum_löschen = cur.execute("SELECT datum FROM Hefteintrag_frz")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", datum_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Hefteintrag_frz WHERE datum = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Hefteinträge anzeigen":
                dt = cur.execute("SELECT * FROM Hefteintrag_frz")
                st.data_editor(dt)
                con.commit()

        elif eingabe == "Vokabeln":
            con = sqlite3.connect("Vokabeln_frz")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Vokabeln_frz(Deutsch, Französisch)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Vokabeln löschen", "Vokabeln anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                v1 = st.text_input("Bitte gebe hier die das deutsche Wort ein:")
                v2 = st.text_input("Bitte gebe hier das französische Wort ein:")
                if st.button("Eintrag bestätigen"):
                    cur.execute(f"INSERT INTO Vokabeln_frz VALUES('{v1}', '{v2}')")
                    dt = cur.execute("SELECT * FROM Vokabeln_frz")
                    st.data_editor(dt)
                    con.commit()
            elif eingabe == "Vokabeln löschen":
                #Eintrag löschen
                vokabel_löschen = cur.execute("SELECT Deutsch FROM Vokabeln_frz")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", vokabel_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Vokabeln_frz WHERE Deutsch = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Vokabeln anzeigen":
                dt = cur.execute("SELECT * FROM Vokabeln_frz")
                st.data_editor(dt)
                con.commit()

        elif eingabe == "Übersetzer":
            st.page_link("https://www.deepl.com/de/translator", label="Übersetzer", icon="📃")
#Geschichte
    elif auswahl == "Geschichte":
        st.header("Geschichte")
        eingabe = st.pills("Wähle aus was du machen willst", ["Planet-Wissen-Geschichte", "Aufgabenheft", "Hefteintrag", "Wikipedia"])
        if eingabe == "Planet-Wissen-Geschichte":
            st.page_link("https://www.planet-wissen.de/geschichte/index.html", label="Planet-Wissen-Geschichte", icon="🌍")
        elif eingabe == "Wikipedia":
            st.page_link("https://de.wikipedia.org/wiki/Wiki", label="Wikipedia", icon="📖")
        elif eingabe == "Aufgabenheft":
            #Eintrag und Datum in Liste hinzufügen
            con = sqlite3.connect("Aufgabenheft_ges")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Aufgabenheft_ges(datum, eintrag)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Datum löschen", "Aufgabenheft anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                # dta = ["Vorlage", "Vorlage"]
                # cur.execute("INSERT INTO Hefteintrag_mathe VALUES(?, ?)", dta)
                # con.commit()
                eintrag = st.text_area("Gebe hier zuerst einen Titel und dann deine Notizen ein:")
                datum = st.text_input("Gebe ein Datum zu dem Eintrag ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Aufgabenheft_ges VALUES('{datum}', '{eintrag}')")
                    data = cur.execute("SELECT * FROM Aufgabenheft_ges")
                    con.commit()
                    st.data_editor(data)
            
            elif eingabe == "Datum löschen":
                #Eintrag löschen
                datum_löschen = cur.execute("SELECT datum FROM Aufgabenheft_ges")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", datum_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Aufgabenheft_ges WHERE datum = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Aufgabenheft anzeigen":
                dt = cur.execute("SELECT * FROM Aufgabenheft_ges")
                st.data_editor(dt)
                con.commit()

        elif eingabe == "Hefteintrag":
             #Eintrag und Datum in Liste hinzufügen
            con = sqlite3.connect("Hefteintrag_ges")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Hefteintrag_ges(datum, eintrag)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Datum löschen", "Hefteinträge anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                # dta = ["Vorlage", "Vorlage"]
                # cur.execute("INSERT INTO Hefteintrag_mathe VALUES(?, ?)", dta)
                # con.commit()
                eintrag = st.text_area("Gebe hier zuerst einen Titel und dann deine Notizen ein:")
                datum = st.text_input("Gebe ein Datum zu dem Eintrag ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Hefteintrag_ges VALUES('{datum}', '{eintrag}')")
                    data = cur.execute("SELECT * FROM Hefteintrag_ges")
                    con.commit()
                    st.data_editor(data)
            
            elif eingabe == "Datum löschen":
                #Eintrag löschen
                datum_löschen = cur.execute("SELECT datum FROM Hefteintrag_ges")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", datum_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Hefteintrag_ges WHERE datum = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Hefteinträge anzeigen":
                dt = cur.execute("SELECT * FROM Hefteintrag_ges")
                st.data_editor(dt)
                con.commit()
#Englisch
    elif auswahl == "Englisch":
        st.header(":green[Englisch]")
        eingabe = st.pills("Bitte wähle aus was du machen möchtest.", ["Ego4U", "Hefteintrag", "Aufgabenheft", "Vokabeln", "Übersetzer"])
        if eingabe == "Ego4U":
            st.page_link("https://www.ego4u.de/", label="Ego4U-Englisch-Trainer", icon="🤖")

        elif eingabe == "Vokabeln":
            con = sqlite3.connect("Vokabeln_eng")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Vokabeln_eng(Deutsch, Englisch)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Vokabeln löschen", "Vokabeln anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                v1 = st.text_input("Bitte gebe hier die das deutsche Wort ein:")
                v2 = st.text_input("Bitte gebe hier das englische Wort ein:")
                if st.button("Eintrag bestätigen"):
                    cur.execute(f"INSERT INTO Vokabeln_eng VALUES('{v1}', '{v2}')")
                    dt = cur.execute("SELECT * FROM Vokabeln_eng")
                    st.data_editor(dt)
                    con.commit()
            elif eingabe == "Vokabeln löschen":
                #Eintrag löschen
                vokabel_löschen = cur.execute("SELECT Deutsch FROM Vokabeln_eng")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", vokabel_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Vokabeln_eng WHERE Deutsch = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Vokabeln anzeigen":
                dt = cur.execute("SELECT * FROM Vokabeln_eng")
                st.data_editor(dt)
                con.commit()

        elif eingabe == "Hefteintrag":
            con = sqlite3.connect("Hefteintrag_eng")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Hefteintrag_eng(datum, eintrag)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Datum löschen", "Hefteinträge anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                # dta = ["Vorlage", "Vorlage"]
                # cur.execute("INSERT INTO Hefteintrag_mathe VALUES(?, ?)", dta)
                # con.commit()
                eintrag = st.text_area("Gebe hier zuerst einen Titel und dann deine Notizen ein:")
                datum = st.text_input("Gebe ein Datum zu dem Eintrag ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Hefteintrag_eng VALUES('{datum}', '{eintrag}')")
                    data = cur.execute("SELECT * FROM Hefteintrag_eng")
                    con.commit()
                    st.data_editor(data)

            elif eingabe == "Datum löschen":
                #Eintrag löschen
                datum_löschen = cur.execute("SELECT datum FROM Hefteintrag_eng")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", datum_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Hefteintrag_eng WHERE datum = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Hefteinträge anzeigen":
                dt = cur.execute("SELECT * FROM Hefteintrag_eng")
                st.data_editor(dt)
                con.commit()

        elif eingabe == "Aufgabenheft":
            #Eintrag und Datum in Liste hinzufügen
            con = sqlite3.connect("Aufgabenheft_eng")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Aufgabenheft_eng(datum, eintrag)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Datum löschen", "Aufgabenheft anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                # dta = ["Vorlage", "Vorlage"]
                # cur.execute("INSERT INTO Hefteintrag_mathe VALUES(?, ?)", dta)
                # con.commit()
                eintrag = st.text_area("Gebe hier zuerst einen Titel und dann deine Notizen ein:")
                datum = st.text_input("Gebe ein Datum zu dem Eintrag ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Aufgabenheft_eng VALUES('{datum}', '{eintrag}')")
                    data = cur.execute("SELECT * FROM Aufgabenheft_eng")
                    con.commit()
                    st.data_editor(data)
            
            elif eingabe == "Datum löschen":
                #Eintrag löschen
                datum_löschen = cur.execute("SELECT datum FROM Aufgabenheft_eng")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", datum_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Aufgabenheft_eng WHERE datum = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Aufgabenheft anzeigen":
                dt = cur.execute("SELECT * FROM Aufgabenheft_eng")
                st.data_editor(dt)
                con.commit()

        elif eingabe == "Übersetzer":
            st.page_link("https://www.deepl.com/de/translator", label="Übersetzer", icon="📃")

#Physik   
    elif auswahl == "Physik":
        st.header(":violet[Physik]")
        eingabe = st.pills("Bitte wähle aus was du machen möchtest:", ["LeifiPhysik", "Hefteintrag", "Aufgabenheft", "Formeln"])
        if eingabe == "LeifiPhysik":
            st.page_link("https://www.leifiphysik.de/", label="LeifiPhysik", icon="🔭")

        elif eingabe == "Hefteintrag":
            con = sqlite3.connect("Hefteintrag_ph")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Hefteintrag_ph(datum, eintrag)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Datum löschen", "Hefteinträge anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                # dta = ["Vorlage", "Vorlage"]
                # cur.execute("INSERT INTO Hefteintrag_mathe VALUES(?, ?)", dta)
                # con.commit()
                eintrag = st.text_area("Gebe hier zuerst einen Titel und dann deine Notizen ein:")
                datum = st.text_input("Gebe ein Datum zu dem Eintrag ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Hefteintrag_ph VALUES('{datum}', '{eintrag}')")
                    data = cur.execute("SELECT * FROM Hefteintrag_ph")
                    con.commit()
                    st.data_editor(data)

            elif eingabe == "Datum löschen":
                #Eintrag löschen
                datum_löschen = cur.execute("SELECT datum FROM Hefteintrag_ph")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", datum_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Hefteintrag_ph WHERE datum = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Hefteinträge anzeigen":
                dt = cur.execute("SELECT * FROM Hefteintrag_ph")
                st.data_editor(dt)
                con.commit()

        elif eingabe == "Aufgabenheft":
            #Eintrag und Datum in Liste hinzufügen
            con = sqlite3.connect("Aufgabenheft_ph")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Aufgabenheft_ph(datum, eintrag)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Datum löschen", "Aufgabenheft anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                # dta = ["Vorlage", "Vorlage"]
                # cur.execute("INSERT INTO Hefteintrag_mathe VALUES(?, ?)", dta)
                # con.commit()
                eintrag = st.text_area("Gebe hier zuerst einen Titel und dann deine Notizen ein:")
                datum = st.text_input("Gebe ein Datum zu dem Eintrag ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Aufgabenheft_ph VALUES('{datum}', '{eintrag}')")
                    data = cur.execute("SELECT * FROM Aufgabenheft_ph")
                    con.commit()
                    st.data_editor(data)
            
            elif eingabe == "Datum löschen":
                #Eintrag löschen
                datum_löschen = cur.execute("SELECT datum FROM Aufgabenheft_ph")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", datum_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Aufgabenheft_ph WHERE datum = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Aufgabenheft anzeigen":
                dt = cur.execute("SELECT * FROM Aufgabenheft_ph")
                st.data_editor(dt)
                con.commit()

        elif eingabe == "Formeln":
            con = sqlite3.connect("Formel_ph")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Formel_ph(Name, Formel)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Formel löschen", "Formeln anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                v1 = st.text_input("Bitte gebe hier den Namen ein:")
                v2 = st.text_input("Bitte gebe hier die Formel ein:")
                if st.button("Eintrag bestätigen"):
                    cur.execute(f"INSERT INTO Formel_ph VALUES('{v1}', '{v2}')")
                    dt = cur.execute("SELECT * FROM Formel_ph")
                    con.commit()
            elif eingabe == "Formel löschen":
                #Eintrag löschen
                vokabel_löschen = cur.execute("SELECT Name FROM Formel_ph")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", vokabel_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Formel_ph WHERE Name = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Formeln anzeigen":
                dt = cur.execute("SELECT * FROM Formel_ph")
                st.data_editor(dt)
                con.commit()
#Chemie
    elif auswahl == "Chemie":
        st.header("Chemie")
        eingabe = st.pills("Bitte wähle aus was du machen willst:", ["Periodensystem", "Aufgabenheft", "Hefteintrag", "Formeln"])
        if eingabe == "Formeln":
            con = sqlite3.connect("Formel_ch")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Formel_ch(Name, Formel)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Formel löschen", "Formeln anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                v1 = st.text_input("Bitte gebe hier den Namen ein:")
                v2 = st.text_input("Bitte gebe hier die Formel ein:")
                if st.button("Eintrag bestätigen"):
                    cur.execute(f"INSERT INTO Formel_ch VALUES('{v1}', '{v2}')")
                    dt = cur.execute("SELECT * FROM Formel_ch")
                    con.commit()
            elif eingabe == "Formel löschen":
                #Eintrag löschen
                vokabel_löschen = cur.execute("SELECT Name FROM Formel_ch")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", vokabel_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Formel_ch WHERE Name = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Formeln anzeigen":
                dt = cur.execute("SELECT * FROM Formel_ch")
                st.data_editor(dt)
                con.commit()
        elif eingabe == "Periodensystem":
            eingabe2 = st.radio("Welche Hauptgruppe möchtest du angezeigt haben?", ["Alkalimetalle", "Erdalkalimetalle", "Borgruppe", "Kohlenstoffgruppe", "Stickstoffgruppe", "Chalkogene", "Halogene", "Edelgase"])
            if eingabe2 == "Alkalimetalle":
                #Alkalimetalle
                con = sqlite3.connect("Periodensystem")
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS Alkalimetalle(Ordnungszahl, Symbol, Name, Atomare Masse)")
                #alkalimetalle = [
                 #    (1, "H", "hydrogen", 1.008),
                  #   (3, "Li", "lithium", 6.94),
                   #  (11, "Na", "sodium", 22.98976928),
                    # (19, "K", "potassium", 39.0983),
                     #(37, "Rb", "rubidium", 85.4678),
                     #(55, "Cs", "caesium", 132.90545196),
                     #(87, "Fr", "francium", 223)
                #]
                #cur.executemany("INSERT INTO Alkalimetalle VALUES(?, ?, ?, ?)", alkalimetalle)
                dt = cur.execute("SELECT DISTINCT * FROM Alkalimetalle")
                st.data_editor(dt)
                con.commit()

            elif eingabe2 == "Erdalkalimetalle":
                #Erdalkalimetalle
                con = sqlite3.connect("Periodensystem")
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS Erdalkalimetalle(Ordnungszahl, Symbol, Name, Atomare Masse)")
                #erdalkalimetalle = [
                 #   (4, "Be", "beryllium", 9.0121831),
                  #  (12, "Mg", "magnesium", 24.305),
                   # (20, "Ca", "calcium", 40.078),
                    #(38, "Sr", "strontium", 87.62),
                    #(56, "Ba", "barium", 137.327),
                    #(88, "Ra", "radium", 226)
                #]
                #cur.executemany("INSERT INTO Erdalkalimetalle VALUES(?, ?, ? ,?)", erdalkalimetalle)
                dt = cur.execute("SELECT DISTINCT* FROM Erdalkalimetalle")
                st.data_editor(dt)
                con.commit()

            elif eingabe2 == "Borgruppe":
                #Borgruppe
                con = sqlite3.connect("Periodensystem")
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS Borgruppe(Ordnungszahl, Symbol, Name, Atomare Masse)")
                #borgruppe = [
                 #  (5, "B", "boron", 10.81),
                  # (13, "Al", "aluminium", 26.9815385),
                   #(31, "Ga", "gallium", 69.723),
                   #(49, "In", "indium", 114.818),
                   #(81, "Tl", "thallium", 204.38)
                #]
                #cur.executemany("INSERT INTO Borgruppe VALUES(?, ?, ? ,?)", borgruppe)
                dt = cur.execute("SELECT DISTINCT* FROM Borgruppe")
                st.data_editor(dt)
                con.commit()

            elif eingabe2 == "Kohlenstoffgruppe":
                #Kohlenstoffgruppe
                con = sqlite3.connect("Periodensystem")
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS Kohlenstoffgruppe(Ordnungszahl, Symbol, Name, Atomare Masse)")
                #kohlenstoffgruppe = [
                 #  (6, "C", "carbon", 12.011),
                  # (14, "Si", "silicon", 28.085),
                   #(32, "Ge", "germanium", 72.63),
                   #(50, "Sn", "tin", 118.71),
                   #(82, "Pb", "lead", 207.2)
                #]
                #cur.executemany("INSERT INTO Kohlenstoffgruppe VALUES(?, ?, ? ,?)", kohlenstoffgruppe)
                dt = cur.execute("SELECT DISTINCT * FROM Kohlenstoffgruppe")
                st.data_editor(dt)
                con.commit()

            elif eingabe2 == "Stickstoffgruppe":
                #Stickstoffgruppe
                con = sqlite3.connect("Periodensystem")
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS Stickstoffgruppe(Ordnungszahl, Symbol, Name, Atomare Masse)")
                #stickstoffgruppe = [
                 #  (7, "N", "nitrogen", 14.007),
                  # (15, "P", "phosphorus", 30.973761998),
                   #(33, "As", "arsenic", 74.921595),
                   #(51, "Sb", "antimony", 121.76),
                   #(83, "Bi", "bismuth", 208.9804)
                #]
                #cur.executemany("INSERT INTO Stickstoffgruppe VALUES(?, ?, ? ,?)", stickstoffgruppe)
                dt = cur.execute("SELECT DISTINCT * FROM Stickstoffgruppe")
                st.data_editor(dt)
                con.commit()

            elif eingabe2 == "Chalkogene":
                #Chalkogene
                con = sqlite3.connect("Periodensystem")
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS Chalkogene(Ordnungszahl, Symbol, Name, Atomare Masse)")
                #chalkogene = [
                 #  (8, "O", "oxygen", 15.999),
                  # (16, "S", "sulfur", 32.06),
                   #(34, "Se", "selenium", 78.971),
                   #(52, "Te", "tellurium", 127.6),
                   #(84, "Po", "polonium", 209)
                #]
                #cur.executemany("INSERT INTO Chalkogene VALUES(?, ?, ? ,?)", chalkogene)
                dt = cur.execute("SELECT DISTINCT* FROM Chalkogene")
                st.data_editor(dt)
                con.commit()

            elif eingabe2 == "Halogene":
                #Halogene
                con = sqlite3.connect("Periodensystem")
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS Halogene(Ordnungszahl, Symbol, Name, Atomare Masse)")
                #halogene = [
                 #  (9, "F", "fluorine", 18.998403163),
                  # (17, "Cl", "chlorine", 35.45),
                   #(35, "Br", "bromine", 79.904),
                   #(53, "I", "iodine", 126.90447),
                   #(85, "At", "astatine", 210)
                #]
                #cur.executemany("INSERT INTO Halogene VALUES(?, ?, ? ,?)", halogene)
                dt = cur.execute("SELECT DISTINCT * FROM Halogene")
                st.data_editor(dt)
                con.commit()

            elif eingabe2 == "Edelgase":
                #Edelgase
                con = sqlite3.connect("Periodensystem")
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS Edelgase(Ordnungszahl, Symbol, Name, Atomare Masse)")
                #edelgase = [
                 #   (2, "He", "helium", 4.002602),
                  #  (10, "Ne", "neon", 20.1797),
                   # (18, "Ar", "argon", 39.948),
                    #(36, "Kr", "krypton", 83.798),
                    #(54, "Xe", "xenon", 131.293),
                    #(86, "Rn", "radon", 222)
                #]
                #cur.executemany("INSERT INTO Edelgase VALUES(?, ?, ? ,?)", edelgase)
                dt = cur.execute("SELECT DISTINCT * FROM Edelgase")
                st.data_editor(dt)
                con.commit()

        elif eingabe == "Aufgabenheft":
            #Eintrag und Datum in Liste hinzufügen
            con = sqlite3.connect("Aufgabenheft_ch")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Aufgabenheft_ch(datum, eintrag)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Datum löschen", "Aufgabenheft anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                # dta = ["Vorlage", "Vorlage"]
                # cur.execute("INSERT INTO Hefteintrag_mathe VALUES(?, ?)", dta)
                # con.commit()
                eintrag = st.text_area("Gebe hier zuerst einen Titel und dann deine Notizen ein:")
                datum = st.text_input("Gebe ein Datum zu dem Eintrag ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Aufgabenheft_ch VALUES('{datum}', '{eintrag}')")
                    data = cur.execute("SELECT * FROM Aufgabenheft_ch")
                    con.commit()
                    st.data_editor(data)
            
            elif eingabe == "Datum löschen":
                #Eintrag löschen
                datum_löschen = cur.execute("SELECT datum FROM Aufgabenheft_ch")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", datum_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Aufgabenheft_ch WHERE datum = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Aufgabenheft anzeigen":
                dt = cur.execute("SELECT * FROM Aufgabenheft_ch")
                st.data_editor(dt)
                con.commit()

        elif eingabe == "Hefteintrag":
            con = sqlite3.connect("Hefteintrag_ch")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Hefteintrag_ch(datum, eintrag)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Datum löschen", "Hefteinträge anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                # dta = ["Vorlage", "Vorlage"]
                # cur.execute("INSERT INTO Hefteintrag_mathe VALUES(?, ?)", dta)
                # con.commit()
                eintrag = st.text_area("Gebe hier zuerst einen Titel und dann deine Notizen ein:")
                datum = st.text_input("Gebe ein Datum zu dem Eintrag ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Hefteintrag_ch VALUES('{datum}', '{eintrag}')")
                    data = cur.execute("SELECT * FROM Hefteintrag_ch")
                    con.commit()
                    st.data_editor(data)

            elif eingabe == "Datum löschen":
                #Eintrag löschen
                datum_löschen = cur.execute("SELECT datum FROM Hefteintrag_ch")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", datum_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Hefteintrag_ch WHERE datum = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Hefteinträge anzeigen":
                dt = cur.execute("SELECT * FROM Hefteintrag_ch")
                st.data_editor(dt)
                con.commit()

#Informatik
    elif auswahl == "Informatik":
        st.header(":blue[Informatik]")
        eingabe = st.pills("Wähle aus was du machen willst", ["Aufgabenheft", "Hefteintrag", "Link zu Excel"])
        if eingabe == "Aufgabenheft":
            #Eintrag und Datum in Liste hinzufügen
            con = sqlite3.connect("Aufgabenheft_I")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Aufgabenheft_I(datum, eintrag)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Datum löschen", "Aufgabenheft anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                # dta = ["Vorlage", "Vorlage"]
                # cur.execute("INSERT INTO Hefteintrag_mathe VALUES(?, ?)", dta)
                # con.commit()
                eintrag = st.text_area("Gebe hier zuerst einen Titel und dann deine Notizen ein:")
                datum = st.text_input("Gebe ein Datum zu dem Eintrag ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Aufgabenheft_I VALUES('{datum}', '{eintrag}')")
                    data = cur.execute("SELECT * FROM Aufgabenheft_I")
                    con.commit()
                    st.data_editor(data)
            
            elif eingabe == "Datum löschen":
                #Eintrag löschen
                datum_löschen = cur.execute("SELECT datum FROM Aufgabenheft_I")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", datum_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Aufgabenheft_I WHERE datum = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Aufgabenheft anzeigen":
                dt = cur.execute("SELECT * FROM Aufgabenheft_I")
                st.data_editor(dt)
                con.commit()
        
        elif eingabe == "Hefteintrag":
            con = sqlite3.connect("Hefteintrag_I")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Hefteintrag_I(datum, eintrag)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Datum löschen", "Hefteinträge anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                # dta = ["Vorlage", "Vorlage"]
                # cur.execute("INSERT INTO Hefteintrag_mathe VALUES(?, ?)", dta)
                # con.commit()
                eintrag = st.text_area("Gebe hier zuerst einen Titel und dann deine Notizen ein:")
                datum = st.text_input("Gebe ein Datum zu dem Eintrag ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Hefteintrag_I VALUES('{datum}', '{eintrag}')")
                    data = cur.execute("SELECT * FROM Hefteintrag_I")
                    con.commit()
                    st.data_editor(data)

            elif eingabe == "Datum löschen":
                #Eintrag löschen
                datum_löschen = cur.execute("SELECT datum FROM Hefteintrag_I")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", datum_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Hefteintrag_I WHERE datum = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Hefteinträge anzeigen":
                dt = cur.execute("SELECT * FROM Hefteintrag_I")
                st.data_editor(dt)
                con.commit()

        elif eingabe == "Link zu Excel":
            st.page_link("https://excel.cloud.microsoft/de-de/", label= "Excel", icon="🧮")

#Religion
    elif auswahl == "Religion":
        st.header(":violet[Religion]")
        eingabe = st.pills("Wähle aus was du machen möchtest", ["Aufgabenheft", "Hefteintrag"])
        if eingabe == "Aufgabenheft":
            #Eintrag und Datum in Liste hinzufügen
            con = sqlite3.connect("Aufgabenheft_r")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Aufgabenheft_r(datum, eintrag)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Datum löschen", "Aufgabenheft anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                # dta = ["Vorlage", "Vorlage"]
                # cur.execute("INSERT INTO Hefteintrag_mathe VALUES(?, ?)", dta)
                # con.commit()
                eintrag = st.text_area("Gebe hier zuerst einen Titel und dann deine Notizen ein:")
                datum = st.text_input("Gebe ein Datum zu dem Eintrag ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Aufgabenheft_r VALUES('{datum}', '{eintrag}')")
                    data = cur.execute("SELECT * FROM Aufgabenheft_r")
                    con.commit()
                    st.data_editor(data)
            
            elif eingabe == "Datum löschen":
                #Eintrag löschen
                datum_löschen = cur.execute("SELECT datum FROM Aufgabenheft_r")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", datum_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Aufgabenheft_r WHERE datum = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Aufgabenheft anzeigen":
                dt = cur.execute("SELECT * FROM Aufgabenheft_r")
                st.data_editor(dt)
                con.commit()
        
        elif eingabe == "Hefteintrag":
            con = sqlite3.connect("Hefteintrag_R")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Hefteintrag_R(datum, eintrag)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Datum löschen", "Hefteinträge anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                # dta = ["Vorlage", "Vorlage"]
                # cur.execute("INSERT INTO Hefteintrag_mathe VALUES(?, ?)", dta)
                # con.commit()
                eintrag = st.text_area("Gebe hier zuerst einen Titel und dann deine Notizen ein:")
                datum = st.text_input("Gebe ein Datum zu dem Eintrag ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Hefteintrag_R VALUES('{datum}', '{eintrag}')")
                    data = cur.execute("SELECT * FROM Hefteintrag_R")
                    con.commit()
                    st.data_editor(data)

            elif eingabe == "Datum löschen":
                #Eintrag löschen
                datum_löschen = cur.execute("SELECT datum FROM Hefteintrag_R")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", datum_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Hefteintrag_R WHERE datum = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Hefteinträge anzeigen":
                dt = cur.execute("SELECT * FROM Hefteintrag_R")
                st.data_editor(dt)
                con.commit()

#Biologie
    elif auswahl == "Biologie":
        st.header(":orange[Biologie]")
        eingabe = st.pills("Wähle aus was du machen möchtest", ["Fachbegriffe", "Hefteintrag", "Aufgabenheft", "ISB-Bayern Biologie Informationen"])
        if eingabe == "Aufgabenheft":
            #Eintrag und Datum in Liste hinzufügen
            con = sqlite3.connect("Aufgabenheft_b")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Aufgabenheft_b(datum, eintrag)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Datum löschen", "Aufgabenheft anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                # dta = ["Vorlage", "Vorlage"]
                # cur.execute("INSERT INTO Hefteintrag_mathe VALUES(?, ?)", dta)
                # con.commit()
                eintrag = st.text_area("Gebe hier zuerst einen Titel und dann deine Notizen ein:")
                datum = st.text_input("Gebe ein Datum zu dem Eintrag ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Aufgabenheft_b VALUES('{datum}', '{eintrag}')")
                    data = cur.execute("SELECT * FROM Aufgabenheft_b")
                    con.commit()
                    st.data_editor(data)
            
            elif eingabe == "Datum löschen":
                #Eintrag löschen
                datum_löschen = cur.execute("SELECT datum FROM Aufgabenheft_b")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", datum_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Aufgabenheft_b WHERE datum = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Aufgabenheft anzeigen":
                dt = cur.execute("SELECT * FROM Aufgabenheft_b")
                st.data_editor(dt)
                con.commit()
        elif eingabe == "Hefteintrag":
            con = sqlite3.connect("Hefteintrag_b")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Hefteintrag_b(datum, eintrag)")
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Datum löschen", "Hefteinträge anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                # dta = ["Vorlage", "Vorlage"]
                # cur.execute("INSERT INTO Hefteintrag_mathe VALUES(?, ?)", dta)
                # con.commit()
                eintrag = st.text_area("Gebe hier zuerst einen Titel und dann deine Notizen ein:")
                datum = st.text_input("Gebe ein Datum zu dem Eintrag ein:")
                #Eintrag bestätigen
                if st.button("Eintrag bestätigen!"):
                    cur.execute(f"INSERT INTO Hefteintrag_b VALUES('{datum}', '{eintrag}')")
                    data = cur.execute("SELECT * FROM Hefteintrag_b")
                    con.commit()
                    st.data_editor(data)

            elif eingabe == "Datum löschen":
                #Eintrag löschen
                datum_löschen = cur.execute("SELECT datum FROM Hefteintrag_b")
                auswahl_datum_löschen = st.selectbox("Wähle aus welchen Eintrag du löschen möchtest:", datum_löschen)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Hefteintrag_b WHERE datum = ('{auswahl_datum_löschen}')")
                    con.commit()
            elif eingabe == "Hefteinträge anzeigen":
                dt = cur.execute("SELECT * FROM Hefteintrag_b")
                st.data_editor(dt)
                con.commit()

        elif eingabe == "Fachbegriffe":
            con = sqlite3.connect("Fachebergriffe_b")
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Fachbegriffe_b(Fachbegriff, Erklärung)")
            # biologie_kl8 = [
            #     ["Biologie", "Wissenschaft von den Lebewesen"],
            #     ["Lebewesen", "Organismen mit Stoffwechsel, Wachstum und Fortpflanzung"],
            #     ["Zelle", "Kleinste lebende Einheit eines Organismus"],
            #     ["Zellkern", "Steuerzentrum der Zelle mit Erbinformation"],
            #     ["Zellmembran", "Begrenzt die Zelle und regelt den Stoffaustausch"],
            #     ["Zellwand", "Starre äußere Hülle pflanzlicher Zellen"],
            #     ["Cytoplasma", "Flüssiger Zellinhalt"],
            #     ["Mitochondrien", "Ort der Energiegewinnung in der Zelle"],
            #     ["Chloroplasten", "Ort der Fotosynthese"],
            #     ["Vakuole", "Speicherraum der Pflanzenzelle"],
            #     ["Gewebe", "Verband gleichartiger Zellen"],
            #     ["Organ", "Aus Geweben aufgebauter Körperteil mit bestimmter Funktion"],
            #     ["Organsystem", "Zusammenarbeit mehrerer Organe"],
            #     ["Stoffwechsel", "Aufnahme, Umwandlung und Abgabe von Stoffen"],
            #     ["Fotosynthese", "Aufbau von Zucker aus Wasser und Kohlenstoffdioxid mit Licht"],
            #     ["Atmung", "Aufnahme von Sauerstoff und Abgabe von Kohlenstoffdioxid"],
            #     ["Zellatmung", "Energiegewinnung aus Nährstoffen in der Zelle"],
            #     ["Enzym", "Biologischer Katalysator"],
            #     ["Verdauung", "Zerlegung von Nahrungsstoffen"],
            #     ["Nährstoffe", "Stoffe zur Energiegewinnung und zum Aufbau des Körpers"],
            #     ["Kohlenhydrate", "Energieliefernde Nährstoffe"],
            #     ["Fette", "Energiespeicher und Wärmeschutz"],
            #     ["Eiweiße", "Baustoffe des Körpers"],
            #     ["Vitamine", "Regelstoffe des Stoffwechsels"],
            #     ["Mineralstoffe", "Anorganische Baustoffe und Regler"],
            #     ["Skelett", "Stützgerüst des Körpers"],
            #     ["Muskeln", "Ermöglichen Bewegung"],
            #     ["Gelenk", "Bewegliche Verbindung von Knochen"],
            #     ["Herz", "Pumpt Blut durch den Körper"],
            #     ["Blut", "Transportiert Sauerstoff und Nährstoffe"],
            #     ["Arterie", "Blutgefäß vom Herzen weg"],
            #     ["Vene", "Blutgefäß zum Herzen hin"],
            #     ["Lunge", "Organ des Gasaustauschs"],
            #     ["Bronchien", "Luftleitende Röhren der Lunge"],
            #     ["Niere", "Reinigt das Blut"],
            #     ["Harn", "Ausscheidungsprodukt der Niere"],
            #     ["Nervensystem", "Steuert und koordiniert Körperfunktionen"],
            #     ["Gehirn", "Zentrales Steuerorgan"],
            #     ["Reflex", "Unwillkürliche schnelle Reaktion"],
            #     ["Sinnesorgan", "Nimmt Reize aus der Umwelt auf"],
            #     ["Reiz", "Einwirkung auf ein Sinnesorgan"],
            #     ["Hormon", "Chemischer Botenstoff"],
            #     ["Pubertät", "Phase der geschlechtlichen Reifung"],
            #     ["Fortpflanzung", "Erzeugung von Nachkommen"],
            #     ["Befruchtung", "Verschmelzung von Ei- und Samenzelle"],
            #     ["Keimzelle", "Geschlechtszelle"],
            #     ["Vererbung", "Weitergabe von Merkmalen"],
            #     ["DNA", "Träger der Erbinformation"],
            #     ["Chromosom", "Träger der Gene im Zellkern"],
            #     ["Gen", "Abschnitt der DNA mit Erbinformation"],
            #     ["Mutation", "Veränderung der Erbinformation"],
            #     ["Anpassung", "Angepasstheit an Umweltbedingungen"],
            #     ["Evolution", "Langfristige Veränderung von Arten"],
            #     ["Art", "Gruppe sich fortpflanzender Lebewesen"],
            #     ["Ökosystem", "Zusammenwirken von Lebewesen und Umwelt"],
            #     ["Biotop", "Lebensraum eines Ökosystems"],
            #     ["Biozönose", "Lebensgemeinschaft in einem Lebensraum"],
            #     ["Produzent", "Pflanze als Erzeuger organischer Stoffe"],
            #     ["Konsument", "Tier, das Pflanzen oder Tiere frisst"],
            #     ["Destruent", "Zersetzer organischer Stoffe"],
            #     ["Nahrungskette", "Abfolge von Fressbeziehungen"],
            #     ["Nahrungsnetz", "Mehrere verknüpfte Nahrungsketten"],
            #     ["Parasiten", "Lebewesen, die auf Kosten anderer leben"],
            #     ["Symbiose", "Zusammenleben zum gegenseitigen Vorteil"],
            #     ["Umweltschutz", "Erhaltung natürlicher Lebensgrundlagen"]
            # ]
            # cur.executemany("INSERT INTO Fachbegriffe_b VALUES(?, ?)", biologie_kl8)
            # con.commit()
            
            eingabe = st.pills("Wähle aus:", ["Eintrag hinzufügen", "Fachbegriff löschen", "Fachbegriffe anzeigen"])
            if eingabe == "Eintrag hinzufügen":
                eintrag1 = st.text_input("Bitte gebe den Fachbegriff ein")
                eintrag2 = st.text_area("Bitte gebe die Erklärung ein:")
                if st.button("Eintrag bestätigen"):
                    cur.execute(f"INSERT INTO Fachbegriffe_b VALUES('{eintrag1}', '{eintrag2}')")
                    dt = cur.execute("SELECT * FROM Fachbegriffe_b")
                    con.commit()
                    st.data_editor(dt)
            
            elif eingabe == "Fachbegriff löschen":
                a = cur.execute("SELECT Fachbegriff FROM Fachbegriffe_b")
                b = st.selectbox("Wähle aus welchen Fachbegriff du löschen willst", a)
                if st.button("Auswahl löschen"):
                    cur.execute(f"DELETE FROM Fachbegriffe_b WHERE Fachbegriff = '{b}'")
                    con.commit()

            elif eingabe == "Fachbegriffe anzeigen":
                a = cur.execute("SELECT * FROM Fachbegriffe_b")
                st.data_editor(a)
                con.commit()

        elif eingabe == "ISB-Bayern Biologie Informationen":
            st.page_link("https://www.isb.bayern.de/schularten/gymnasium/faecher/biologie/", label="Biologie Infromationen (ISB-Bayern)", icon="🧬")
   
