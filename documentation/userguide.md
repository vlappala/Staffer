# Käyttöohje

Staffer on sovellus, jonka avulla voit hallinnoida tapahtumien työvuoroja Sovelluksen avulla työntekijät voivat ilmoittautua työvuoroihin. 

Sovelluksen käyttäjät voidaan jakaa kahteen ryhmään käyttäjäroolin mukaan. Tapahtumia hallinnoiva pääkäyttäjä voi lisätä uusia tapahtumia järjestelmään. Pääkäyttäjä voi myös lisätä tapahtumille ilmentymiä. Tapahtumia kutsutaan järjestelmässä produktioiksi (production) ja tapahtumien ilmentymiä esityksiksi (show).

## Aloitus

Sovellus tarvitsee toimiakseen tietokannan. Asennusohjeessa kerrotaan, miten tietokanta asennetaan paikalliseen ympäristöön, sekä heroku-palveluun. 

### Tietokannan käyttö paikallisesti

Aloitettaessa sovelluksen käyttöä, on sen tietokanta tyhjä. Sovellukseen kannattaakin lisätä aluksi pääkäyttäjä- eli "Admin"-roolin omaava käyttäjä, joka voi lisätä järjestelmään produktioita ja esityksiä. Kun sovellus käynnistetään ensimmäisen kerran, luo se sovelluksen käyttämän tietokannan 

    shows.db
    
sovelluksen hakemistoon allaolevan kaltaisesti:

    application/shows.db
    
Tämän jälkeen tietokanta tulee avata komennolla

    sqlite3 shows.db
    
ja syöttää tietokantaan pääkäyttäjän käyttäjätiedot komennoilla

    INSERT INTO account (name, username, password) VALUES ('hello world', 'hello', 'world');
    
    INSERT INTO role (account_id, role_name) VALUES (1, 'ADMIN');

    
Tämän jälkeen voit kirjautua sovellukseen www-selaimen osoitteessa 

    localhost:5000
    
tunnuksella 

    hello
    
ja salasanalla

    world

## Sovelluksen peruskäyttö

### Kirjautuneena Admin-käyttäjänä voit luoda järjestelmään erilaisia tapahtumia ja niille esiintymisiä. Sovelluksen peruskäyttäjät voivat ilmoittautua työvuoroon näihin esityksiin.

Kirjautumis-, eli Login-näkymä on alempana kuvassa:

![admin_loginscreen](https://github.com/vlappala/Staffer/blob/master/documentation/screenshots/admin_loginscreen.jpg)

Kirjautumisen jälkeen voit luoda tapahtumia järjestelmään ylävalikon kohdasta Add a new production:

![admin_add_productions](https://github.com/vlappala/Staffer/blob/master/documentation/screenshots/admin_add_new_production.jpg)

Voit luoda tapahtumille (productions) esiintymiä (show) ylävalikon kohdasta List / Edit all productions. Näet samassa näkymässä myös kaikki järjestelmään tähän asti lisätyt tapahtumat ja niiden esiintymät. Voit tässä näkymässä myös editoida jo luomiasi tapahtumia tai esiintymiä sekä poistaa luotuja tapahtumia. Yksittäisten esiintymien poistaminen tapahtuu ylävalikon kohdasta List / Edit all shows.

### Kirjautuneena peruskäyttäjänä voit ilmoittautua sovelluksen avulla työvuoroon

Kirjautuneena peruskäyttäjänä näet tapahtumat, joihin tarvitaan työvoimaa ylävalikon Sign up for work! -kohdan alta:

![user_sign_up](https://github.com/vlappala/Staffer/blob/master/documentation/screenshots/user_sign_up.jpg)

Näet vuorosi, joihin olet ilmoittautunut sekä aiemmalta sivulta että myös sovelluksen pääsivulta, minne sovellus sinut kirjautumisen onnistuttua ohjaa:

![user_main_menu](https://github.com/vlappala/Staffer/blob/master/documentation/screenshots/user_main_menu.jpg)

Pääset sovelluksen pääsivulle aina ylävalikon linkistä Main menu.



