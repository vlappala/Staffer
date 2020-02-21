# User stories, käyttötapaukset. Lista päivittyy sovelluksen kehittyessä. 
### Kaikkia toiminnallisuuksia ei ole tässä listattu, joitain ei ole vielä kehitetty ja ne saattavat muuttua ajan myötä. Lista siis päivittyy vielä.

Ylläpitäjän kannalta: 

*  Voin lisätä uuden näytännön työvuorolistaan
    SQL-lause:
##    

    INSERT INTO show 
    (show_date, date_modified, name, open_for_recruitment, production_id) 
    VALUES 
    (?, CURRENT_TIMESTAMP, ?, ?, ?)
    ('2020-02-21 19:00:00.000000', 'Taikaviulu', 0, 1)
    
*  Voin merkitä näytännön sellaiseksi, että siihen on mahdollista ilmoittautua työvuoroon (Vanhentuva käyttötapaus, kaikki näytännöt ovat aluksi sellaisia että ilmoittautuminen on mahdollista)
*  Voin jakaa työvuoroja ja lukita ne tietyn näytännön osalta (Käyttötapausta ei vielä toteutettu, tulossa)

Työntekijän kannalta:

*  Voin ilmoittautua työvuoroon
    SQL-lause:
    
##

    INSERT INTO shift 
    (account_id, show_id, shift_role, shift_locked, shift_completed, shift_billed, date_modified) 
    VALUES 
    (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
    (2, '1', None, 0, 0, 0)

*  Voin selata mahdollisia työvuoroja

## 

Ensin kysytään sellaiset näytösten id:t, joihin on jo ilmoittauduttu, kyseessä SQLAlchemy-lause, jossa käytetään text-funktiota ja parametrejä:

    text("SELECT shift.show_id FROM shift WHERE shift.account_id = :ac_id").params(ac_id=account_id)
    
Sen jälkeen kysytään kaikki näytännöt ja verrataan jo tehtyjä työvuoroiloittautumisia siihen.

    SELECT show.id AS show_id, show.show_date AS show_show_date, show.date_modified AS show_date_modified, show.name AS show_name, show.open_for_recruitment AS show_open_for_recruitment, show.production_id AS show_production_id FROM show

*  Voin tarkastella työvuorohistoriaani. Allaoleva lause listaa kaikki kirjautuneen käyttäjän työvuorot, sekä tehdyt että ne, joita ei ole vielä tehty mutta joihin on ilmoittauduttu.

##

    text(SELECT * FROM shift WHERE shift.account_id = :ac_id").params(ac_id=account_id)
    
    
    
    
    


    
