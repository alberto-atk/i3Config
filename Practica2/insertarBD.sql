
CREATE DATABASE IF NOT EXISTS practicaAS2;
USE practicaAS2;

/*
    Create table pagina and add urls from main url page
    Delete each time to not generate too much info
*/
DROP TABLE IF EXISTS pagina;
CREATE TABLE IF NOT EXISTS pagina(
    urlPagina TEXT,
    subenlaces TEXT
);


/*
    Load CSV created from info received
*/
LOAD DATA 
LOCAL INFILE 'aux.csv'
INTO TABLE pagina
FIELDS TERMINATED BY '~'
(urlPagina, subenlaces);

