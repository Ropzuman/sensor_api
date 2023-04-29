# Sensor API loppuraportti

## Yleistä

Päätin käyttää luennoilla opittuja työkaluja aikalailla suoraan ja tukea sitä raivoisalla goolauksella. Lähtökohdat olivat hieman haasteelliset, kuten vauva-arkea elävällä aikuisopiskelijalla aina, joten vaikeamman tehtävänannon kanssa liikkeellelähteminen oli ehkä vähän uhkarohkeaa varsinkin tällaisilla kurssimäärillä, mutta tästäkin selvittiin. Ei ehkä ihan toivotulla tavalla, mutta siitä lisää myöhemmin.

## Suunnittelu

Lähdin lähestymään asiaa ihan kynä-paperi pohjalta, eli listasin tarvittavia asioita, joista lähdin kasaamaan endpointeja ja skeemoja. Tämä oli hyvä lähtökohta, mutta lopulta jouduin tekemään paljon muutoksia suunnitelmiin, koska en ollut ottanut huomioon kaikkia asioita. Tämä oli hyvä oppitunti, että suunnitelmaa pitää pystyä muokkaamaan ja joustamaan tarpeen mukaan.

## Toteutus

Koodailin hommaa kasaan pala kerrallaan ja testasin aina toimivuuden. Tavaraa kertyi äkkiä aika tavalla ja skeemoissa on todennäköisesti muutama turha edelleen.

## Ongelmat

Ongelmilta ei vältytty. Mittauksien liittämisessä hakutuloksiin oli valtavia ongelmia ja sen kanssa sai hakata päätä seinään pitkän aikaa.

Loppua kohden tajusin myös, kun olin tilamuutoksien historian kanssa aikani paininut, että niille olisi pitänyt tehdä alusta asti oma table. Tein hiukan kokeiluita, mutta totesin, että aika ei riitä, koska olisi pitänyt rakentaa suurin osa himmelistä uudestaan. Samalla kertaa jäi siis myös virhetilanteiden graafi tekemättä.

Mittaustulosten hakeminen kahdelle aikavälille puuttu myös, kun totesin timestampien olevan liian pitkiä ja hankalia siihen, eikä niiden formatoiminen lyhyemmiksi meinannut onnistua. Skill issue todennäköisesti tämäkin, mutta oppia ikä kaikki. Lisäsin siis sen sijaan hakutoiminnon, joka hakee tietokannasta kaikki mittaustulokset.

## Yhteenveto

Kaikkiaan olen kohtuullisen tyytyväinen lopputulokseen. Nyt pääsi ensimmäisen kerran kasaamaan ns. oikeaa ohjelmaa, jossa on aidon codebasen tuntua. Harrastelukoodaukselle, kun on äärettömän vähän aikaa tällä hetkellä, niin hyvää harjoitusta kuin se onkin.

GitHubia on toki tullut käytettyä melkein joka kurssilla, mutta nyt pääsi hääräämään kunnolla branchien kanssa.

Muutaman toiminnon poisjääminen harmittaa, mutta ei viitsi palauttaa ohjelmaa, jossa on keskeneräisiä tai rikkinäisiä osia kommentoituna pitkin koodia. Koin pienen ahaa-elämyksen, jolla olisin saanut ehkä ne tehtyä, mutta totesin, että aika loppuu kesken. Vaipparalli ja vuorotyöt tekee tehtävänsä :smile:

## Lopuksi

Tämä oli erittäin opettavainen kokemus ja odotan kyllä mielenkiinnolla mahdollista mallisuoritusta, että miten tämä ns. oikeasti tehdään. Oli myös mukava päästä tutustumaan läheltä, että mikä API on ja miten se toimii. Olin sitä sopivasti ihemtellyt, koska moni selitys oli mielestäni hieman epämääräinen.

Jälleen kerran erinomainen kurssi ja toivottavasti näemme vielä jonkun toisen kurssin äärellä! Kiitokset!

**Roope Vähä-Aho / AEA21SP**
