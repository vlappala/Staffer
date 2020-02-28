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

Kirjautuneena Admin-käyttäjänä voit luoda järjestelmään erilaisia tapahtumia ja niille esiintymisiä. Sovelluksen peruskäyttäjät voivat ilmoittautua työvuoroon näihin esityksiin.

![admin_loginscreen]()
