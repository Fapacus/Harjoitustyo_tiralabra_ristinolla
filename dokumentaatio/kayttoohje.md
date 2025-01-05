# Käyttöohje Ristinollaan
Lataa projekti githubista.

## Ohjelman käynnistäminen
Aivan aluksi on suositeltavaa asentaa projektin riippuvuudet käyttäen komentoa:
```bash
poetry install
```
Tämän jälkeen voit käynnistää ohjelman käyttäen komentoa:
```bash
poetry run invoke start
```
Mikäli edellä mainittu ei toimi, voi pelin käynnistöö suorittamalla src-kansiosta löytyvä "main.py"-tiedosto.


## Ohjelman käyttäminen
Ohjelman käyttöliittymä on tekstipohjainen.
Ohjelman avauduttua tulostuu konsoliin yksinkertaiset ohjeet pelin pelaamiseksi sekä pelilauta ja teksti "Your move: ".
Peli alkaa samantien ja odottaa pelaajan ensimmäistä siirtoa. 
Pelaajan tehtyä oman siirtonsa, tekee AI oman siirtonsa ja peli jatkuu samalla lailla vuorotellen kunnes jopmpikumpi voittaa tai pelilauta täyttyy ja peli päättyy tasapeliin.


## Pelin säännöt/toiminta
Peliä pelataan tekemällä siirtoja. Siirtojen tekeminen tapahtuu kirjoittamalla konsoliin rivin numero ja sarakkeen kirjain peräjälkeen, järjestyksellä ei ole väliä.
Mikäli pelaaja syöttää virheellisen arvon, tulostuu tästä tieto ja pelaaja saa uuden mahdollisuuden arvon syöttämiseksi.
Pelin nimi on Ristinolla ja siinä on tarkoituksena saada rakennettua omista symboleistaan viiden mittainen suora, samalla estäen vastustajaa pääsemästä samaan päämäärään.
Viiden suoran voi rakentaa mihin ilmansuuntaan tai väli-ilmansuuntaan hyvänsä.
Pelaajan pelimerkkeinä toimivat O-kirjaimet, jotka symboloivat "nollaa". 
Ai:n pelimerkkeinä toimivat X-kirjaimet, jotka symboloivat "ristiä".
