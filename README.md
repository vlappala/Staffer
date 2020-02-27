# Staffer


Staffer on järjestelmä tapahtumien työvoiman hallinnointiin.


Pääkäyttäjäoikeuksilla varustettu käyttäjä voi lisätä järjestelmään tapahtumia, joihin tarvitaan työvoimaa. Pääkäyttäjä voi myös lisätä tapahtumille useita esiintymiä eri ajankohdilla, ja tapahtumia voi myös nimetä esiintymiskohtaisesti. Pääkäyttäjä voi myös muokata, listata ja poistaa tapahtumia ja niiden esiintymiä.

Tapahtumasta käytetään järjestelmässä nimeä Production ja tapahtuman esiintymästä nimeä Show. Tapahtuma voisi kuitenkin myös olla esimerkiksi nimeltään "Jääkiekko-ottelu" esiintyminään esimerkiksi "HIFK-TPS" ja "HIFK-Tappara".

Työntekijä voi rekisteröityä järjestelmän käyttäjäksi. Sen jälkeen hän voi kirjautua järjestelmään, selailla tulevia työskentelymahdollisuuksia, sekä ilmoittautua työvuoroon ja tarvittaessa perua ilmoittautumisensa.

Järjestelmään on toteutettu kahdentyyppisiä käyttäjärooleja, pääkäyttäjäoikeuksilla varustettu käyttäjä on rooliltaan "ADMIN" ja perustason oikeuksilla varustettu työntekijä "USER".

Perustoimintoihin liittyviä SQL-lauseita on listattu sivulla [User stories](https://github.com/vlappala/Staffer/tree/master/documentation/userstories.md)




## Järjestelmän käyttö:

Työvuorojen laadinnasta vastaava henkilö voi

* Rekisteröityä järjestelmän käyttäjäksi

* Kirjautua järjestelmään
  * Luoda uuden tapahtuman
    * Muokata tapahtuman yksityiskohtia
    * Määritellä tapahtumalle esiintymiä
      * Muokata esiintymien yksityiskohtia
      * Poistaa esiintymiä
    * Tarkastella tilastoja siitä, mitkä ovat tapahtumia joilla on eniten esiintymiä 
    * Tarkastella tilastoja siitä, ketkä käyttäjät ovat ilmoittautuneet eniten työvuoroihin.
  * Poistaa tapahtuman

* Kirjautua ulos järjestelmästä


Työntekijä voi

* Rekisteröityä järjestelmän käyttäjäksi

* Kirjautua järjestelmään
  * Tarkastella omia työvuoroilmoittautumisiaan
  * Ilmoittautua työvuoroon
  * Poistaa ilmoittautumisensa työvuoroon

* Kirjautua ulos järjestelmästä


EI TOTEUTETTUJA OMINAISUUKSIA / KEHITYSMAHDOLLISUUKSIA:

Tapahtumamallien lisääminen. Malleissa määriteltäisiin työvoiman tarve tapahtumatyyppikohtaisesti.

Työvuorojen jakaminen

Tehtyjen tuntien kirjaaminen lomakkeelle, jonka voisi edelleen välittää mahdollisesti palkanlaskentaan

Automatisoitu tapahtumien tuominen järjestelmään esimerkiksi csv-tiedostosta


Projektin tietokantakaavio:

![Tietokantakaavio](https://github.com/vlappala/Staffer/blob/master/documentation/DBChart.jpg)

[Tietokantarakenne](https://github.com/vlappala/Staffer/blob/master/documentation/dbstructure.md)

[Sovellus Herokussa](http://tsoha-staffer.herokuapp.com/)

[User stories](https://github.com/vlappala/Staffer/tree/master/documentation/userstories.md)

[Asennusohje](https://github.com/vlappala/Staffer/blob/master/documentation/installationguide.md)

[Käyttöohje](https://github.com/vlappala/Staffer/blob/master/documentation/userguide.md)

Komento riippuvuuksien tallentamiseksi tekstitiedostoon: 

    pip freeze | grep -v pkg-resources > requirements.txt
    
Testitunnukset:

    Login: hello
    Password: world
    
SQLite-komento testikäyttäjän lisäämiseksi sekä Admin-roolin asettamiseksi:

    INSERT INTO account (name, username, password) VALUES ('hello world', 'hello', 'world');
    INSERT INTO role (account_id, role_name) VALUES (1, 'ADMIN');


    


