## User stories, sovelluksen pääasialliset käyttötapaukset ja niihin liittyvät SQL-lauseet. 


Ylläpitäjänä haluan rekisteröityä järjestelmän käyttäjäksi pystyäkseni hallinnoimaan tapahtumia (Tämä täytyy tehdä suoraan tietokantaan, käyttöliittymästä ei tällä hetkellä voi rekisteröityä järjestelmän pääkäyttäjäksi)

    INSERT INTO account 
    (name, username, password) 
    VALUES 
    ('hello world', 'hello', 'world');
    
    INSERT INTO role 
    (account_id, role_name) 
    VALUES 
    (1, 'ADMIN');
    
Ylläpitäjänä haluan nähdä, millä tapahtumilla on eniten näytäntöjä:

    SELECT production.id, production.name, COUNT(show.id) AS LKM FROM production 
    LEFT JOIN show ON show.production_id = production.id 
    group by production.id 
    ORDER BY LKM DESC
    
Ylläpitäjänä haluan nähdä, ketkä käyttäjät ovat ilmoittautuneet eniten työvuoroihin:

    SELECT account.name, COUNT(shift.id) AS LKM FROM account 
    LEFT JOIN shift ON account.id = shift.account_id 
    group by account.name 
    ORDER BY LKM DESC
    
Ylläpitäjänä haluan lisätä järjestelmään uuden tapahtuman Lentävä hollantilainen voidakseni lisätä uusia tapahtuman esiintymiä

    INSERT INTO production (date_modified, name, show_duration_hours, show_duration_minutes, misc_info) 
    VALUES 
    (CURRENT_TIMESTAMP, ?, ?, ?, ?)
    ('Lentävä hollantilainen', 3, 40, 'Säveltäjä Richard Wagner');
    
Ylläpitäjänä haluan lisätä tapahtumalle Lentävä hollantilainen näytännön, jotta voin rekrytoida työntekijöitä

    INSERT INTO show 
    (show_date, date_modified, name, production_id) 
    VALUES 
    (?, CURRENT_TIMESTAMP, ?, ?)
    ('2020-02-29 19:00:00.000000', 'Lentävä hollantilainen', 4);
    
Kirjautuneena työntekijänä haluan ilmoittautua työvuoroon Lentävän hollantilaisen näytökseen, jotta pääsen töihin.

    INSERT INTO shift 
    (account_id, show_id, date_modified) 
    VALUES 
    (?, ?, CURRENT_TIMESTAMP)
    (2, '4');
    
    INSERT INTO shiftdetails 
    (shift_id, shift_role, shift_locked, shift_completed, shift_billed, date_modified) 
    VALUES 
    (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
    (5, None, 0, 0, 0);
    
Kirjautuneena työntekijänä haluan poistaa ilmoittautumiseni Lentävän hollantilaisen näytökseen, koska työvuoro ei sovikaan minulle.

    SELECT shift.id FROM shift 
    WHERE 
    shift.account_id = ? AND shift.show_id = ?
    (2, '4');
    
    SELECT id FROM shiftdetails
    WHERE shift_id = ?
    (5,);
    
    DELETE FROM shiftdetails 
    WHERE shiftdetails.id = ?
    (5,)
    
    DELETE FROM shift WHERE shift.id = ?
    (5,)


    
    
    
    
    


    
