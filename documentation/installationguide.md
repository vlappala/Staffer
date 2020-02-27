# Staffer-sovelluksen asentaminen

## Python

Sovellus tarvitsee toimiakseen Python-ohjelmointikielen suoritusympäristön. Voit hakea sen osoitteesta [python.org](https://www.python.org/)

Pythoniin on hyvä asentaa virtuaaliympäristö, johon ohjelman tarvitsemat riippuvuudet ladataan. Ohjeen virtuaaliympäristön luomiseksi löydät [pythonin dokumentaatiosta](https://docs.python.org/3/tutorial/venv.html)

Virtuaaliympäristön voi luoda esimerkiksi linux-komennolla

    python3 -m venv venv
    
Komento luo hakemistoon kansion nimeltä venv, mihin virtuaaliympäristö ladataan. Voit aktivoida virtuaaliympäristön komennolla

    source venv/bin/activate

Sen jälkeen voit asentaa Pythonin vaatimat riippuvuudet Pythonin mukana tulevan pip-paketinhallintasovelluksen avulla komennolla

    pip install -r requirements.txt
    
Sovelluksen mukana tulevassa tiedostossa requirements.txt -tiedostossa on lueteltu sovelluksen vaatimat Python-kirjastot. Ylläolevan komennon avulla pip osaa hakea automaattisesti kaikki sovelluksen vaatimat riippuvuudet.

Tiedoston requirements.txt sisältö on myös alla:

    astroid==2.3.3
    Click==7.0
    Flask==1.1.1
    Flask-Login==0.4.1
    Flask-SQLAlchemy==2.4.1
    Flask-WTF==0.14.2
    gunicorn==20.0.4
    isort==4.3.21
    itsdangerous==1.1.0
    Jinja2==2.10.3
    lazy-object-proxy==1.4.3
    MarkupSafe==1.1.1
    mccabe==0.6.1
    psycopg2==2.8.4
    python-dateutil==2.8.1
    six==1.14.0
    SQLAlchemy==1.3.12
    typed-ast==1.4.1
    Werkzeug==0.16.0
    wrapt==1.11.2
    WTForms==2.2.1
    
Tämän jälkeen voit käynnistää sovelluksen komennolla

    python3 run.py
    
Sovellus näkyy nyt www-selaimen osoitteessa 

    localhost:5000


## Tietokanta

Sovellus tarvitsee toimiakseen tietokantayhteyden. Käytettäessä sovellusta paikallisesti sovellus käyttää sqlite3-tietokannanhallintajärjestelmää. Lyhyt perehdytys aiheeseen löytyy esimerkiksi Tietokantojen perusteet-kurssin [sivulta:](https://tikape-k20.mooc.fi/luku-2/3)
