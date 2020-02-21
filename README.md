# Staffer

Staffer on järjestelmä tapahtumien työvoiman hallinnointiin.

Pääkäyttäjäoikeuksilla varustettu käyttäjä, eli admin voi lisätä järjestelmään tapahtumia, esimerkiksi esitettäviä oopperateoksia. Admin voi lisätä teoksille yhden tai useampia näytäntöjä, joihin tarvitaan työvoimaa. Admin voi määritellä, onko ilmoittautuminen tiettyyn näytäntöön mahdollista. 

Normaalikäyttäjä voi selata työskentelymahdollisuuksia ja ilmoittaa kiinnostuksensa työvuorokohtaisesti. 

Perustoimintoihin liittyviä SQL-lauseita on listattu sivulla [User stories](https://github.com/vlappala/Staffer/tree/master/documentation/userstories.md)

Järjestelmän käyttö:

Työvuorojen laadinnasta vastaava henkilö voi

* Ilmoittaa työntekijöiden tarpeesta henkilöstölle lataamalla järjestelmään uuden tapahtuman
  * Määritellä uudelle tapahtumalle työvoiman tarpeen
    * Järjestelmä saattaa käyttää valmiita malleja työvoiman tarpeen määrittämiseksi eri tapahtumatyyppejä kohden
    * Työvuorojen laadinnasta vastaaava henkilö saattaa pystyä luomaan tällaisia malleja
  * Lukita tapahtuman, jolloin siihen ei enää oteta vastaan uusia työvuoroilmoittautumisia
  * Ilmoittaa työntekijöille määrätyt työvuorot (web, sähköposti)

Työntekijä voi

* Katsoa tarjolla olevia työvuoroja
  * Ilmoittautua työvuoroon
  * Tarkastella työskentelyhistoriaansa ja suorittaa erilaisia hakuja esimerkiksi tietyltä aikaväliltä.


  
Projektin alustava tietokantakaavio:

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

    


