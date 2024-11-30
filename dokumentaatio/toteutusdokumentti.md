# Ristinolla
## Rakenne
Ohjelma on rakenteeltaan tällä hetkellä yksitiedostoinen.
Ohjelma koostuu funktioista, joista keskeisin on minimax-funktio.
Ohjelma pyörii minimax-funktion ympärillä siten, että aluksi tarkistetaan onko tapahtunut voittoa, sen jälkeen selvitetään mahdollinen tasapeli ja sitten katsotaan ollaanko 0-syvyydessä. Jos ollaan 0-syvyydessä, niin arvioidaan lauta, jos taas ei olla 0-syvyydessä, niin kutsutaan minimax-funktiota rekursiivisesti.
Muita funktioita ovat erinäisiä käännöksiä tekevät funktiot sekä ohjelman toiminnallisuutta pyörittävät funktiot.

## Saavutetut aika- ja tilavaativudet
Ohjelman vaativuutta on rajoitettu tähän mennessä rajoittamalla rekursiivista syvyyttä ja uutena asiana rajoittamalla tarkasteltavien siirtojen määrä aikaisemmista siirroista maksimissaan kahden ruudun päässä oleviin siirtoihin.

## Puutteet ja parannusehdotukset
Ohjelma on edelleen työvaiheessa eikä sitä ole vielä pyritty viimeistelemään. Ohjelmasta puuttuu ainakin pienet hienoudet, kuten ilmoitukset virheellisistä siirroista tai tekstikäyttöliittymässä rivien ja sarakkeiden numerointi/merkintä.
Ohjelmassa ei ole myöskään vielä tehty lopullisen kokoista tyhjää pelilautaa, vaan toistaiseksi pelilaudat ovat if __name__ == '__main__': -lohkon alla ja kooltaan pienempiä sekä osittain valmiiksi täytettyjä.
Yhtenä ohjelman toimintaa tehostavana tekijänä olen harkinnut alpha-beta -karsinnan tuomista osaksi minimax-funktion toteutusta.

## Kielimallit
Ohjelman tekemisessä on käytetty apuna ChatGPT:tä ohjelman debuggauksessa ja asioiden selittämisessä. Esimerkiksi: "Kuinka poistaa setistä jokin kohde?".


