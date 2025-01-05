# Ristinolla
## Rakenne
- Ohjelma on rakenteeltaan nelitiedostoinen.
- Ohjelma koostuu funktioista, joista keskeisin on minimax-funktio.
- Ohjelma pyörii minimax-funktion ympärillä siten, että aluksi tarkistetaan onko tapahtunut voittoa, sen jälkeen selvitetään mahdollinen tasapeli ja sitten katsotaan ollaanko 0-syvyydessä. Jos ollaan 0-syvyydessä, niin arvioidaan lauta, jos taas ei olla 0-syvyydessä, niin kutsutaan minimax-funktiota rekursiivisesti.
- Muita funktioita ovat erinäisiä käännöksiä tekevät funktiot sekä ohjelman toiminnallisuutta pyörittävät funktiot.

## Saavutetut aika- ja tilavaativudet
- Ohjelman vaativuutta on rajoitettu tähän mennessä rajoittamalla rekursiivista syvyyttä ja uutena asiana rajoittamalla tarkasteltavien siirtojen määrä aikaisemmista siirroista maksimissaan kahden ruudun päässä oleviin siirtoihin.
- Ohjelman aikavaatimuuden määrittelee käytännössä minimax-algoritmi, jonka aikavaativuus on O({mahdolliset siirrot}^{etsinnän syvyys}) eli **O(m^e)** ja tilavaativuus on O({mahdolliset siirrot}*{etsinnän syvyys}) eli **O(me)**.

## Puutteet ja parannusehdotukset
- Graafinen käyttöliittymä, jotta pelikokemus paranisi.
- Uskoisin, että ohjelman toimintaa voisi vielä tehostaa suhteellisen pienellä vaivalla.

## Kielimallien käyttö projektissa
Ohjelman tekemisessä on käytetty apuna ChatGPT:tä ohjelman debuggauksessa ja ohjelmointiin liittyvien asioiden selittämisessä yleisellä tasolla, esimerkiksi: "Kuinka poistaa setistä jokin kohde?".


