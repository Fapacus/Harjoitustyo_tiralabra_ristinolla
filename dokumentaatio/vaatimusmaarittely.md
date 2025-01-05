# Ristinolla-sovelluksen vaatimusmäärittely.

Ristinolla-sovelluksen vaatimusmäärittely perustuu kurssilla annettuun valmiiseen määrittelyyn, joka on esitetty alla jaoteltuna "toteutettuihin" ja "muihin":
- ## Ristinolla / Gomoku
- ### Toteutetut:
- 20 x 20 ruudukolla pelattava ristinolla, jossa voittaa kun saa vähintään 5 merkin pituisen rivin. *(toteutettu)*

- Lisävaatimukset. Hyväksyttyyn suoritukseen vaaditaan tehokas toteutus, johon kuuluu:

  - Tutkitaan vain vapaat ruudut, jotka ovat korkeintaan kahden ruudun päässä aiemmin tehdyistä siirroista, tai muu tätä tehokkaampi mielekäs kokeiltavien siirtojen karsinta. 
  - Tutkittavia siirtoja ei selvitetä erikseen joka pelitilanteessa, vaan pidetään yllä listaa tällaisista ruuduista, ja päivitetään sitä tehtyjen / minimaxissa kokeiltujen siirtojen myötä. Siirtojen mukaan päivitetty lista annetaan parametrina eteenpäin minimaxissa.
  - Voiton tarkistus tehdään tutkimalla vain rivit, jotka sisältävät edellisen siirron. 
  - Jos viiden rivi on syntynyt, voittaja on edellisen siirron tehnyt pelaaja, ja edellinen siirto on osa voittoriviä. 

- ### Muut:
-  Ristinollassa on usein pakko reagoida vastustajan edelliseen siirtoon, tai se on jatkoa ajatellen kannattavaa. Usein paras reaktio on jokin edellisen siirron viereinen siirto. Noudata tätä heuristiikkaa lisäämällä / nostamalla viimeisimmän siirron lähinaapurit ensimmäisiksi tutkittaviksi.
  
    - Sovellus ei toteuta heuristiikkaa, joka nostaisi viimeisimmän siirron lähinaapurit ensin tutkittaviksi. Sen sijaan sovelluksessa on käytössä "Alpha" ja "Beta" -arvot, jotka tilanteesta riippuen rajoittavat siirtoketjujen tarkastelua, mikäli aiemman tai aiempien siirtojen perusteella on selvää, ettei kyseinen siirtoketju tule tuottamaan parempaa arvoa.
