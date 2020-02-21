# User stories, käyttötapaukset. Lista päivittyy sovelluksen kehittyessä. 
# Kaikkia toiminnallisuuksia ei ole vielä kehitetty ja ne saattavat muuttua ajan myötä.

Ylläpitäjän kannalta: 

*  Voin lisätä uuden näytännön työvuorolistaan
    SQL-lause:
    
    
    
*  Voin merkitä näytännön sellaiseksi, että siihen on mahdollista ilmoittautua työvuoroon
*  Voin jakaa työvuoroja ja lukita ne tietyn näytännön osalta

Työntekijän kannalta:

*  Voin ilmoittautua työvuoroon
*  Voin selata mahdollisia työvuoroja
*  Voin tarkastella työvuorohistoriaani

    INSERT INTO show (show_date, date_modified, name, open_for_recruitment, production_id) VALUES (?, CURRENT_TIMESTAMP, ?, ?, ?)
    2020-02-21 20:13:33,913 INFO sqlalchemy.engine.base.Engine ('2020-02-21 19:00:00.000000', 'Taikaviulu', 0, 1)
