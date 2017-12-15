# RailNL - Team 11=

Deze case gaat over het maken van een lijnvoering van intercitytreinen. De bedoeling is dat we binnen een gegeven tijdsframe een aantal trajecten moeten uitzetten, waarbij het de bedoeling is dat we een algoritme creëren die een zo hoog mogelijke score geeft. Deze score is gebaseerd op een formule waarbij de score hoger is wanneer je zoveel mogelijk kritieke verbindingen hebt bereden met zo min mogelijk lijnvoeringen. 

## Aan de slag

Deze instructies zorgen ervoor dat je een kopie van ons project bemachtigt en hem kan runnen op je pc/laptop.

### Vereisten

Wat je moet installeren en hoe je het moet installeren:

Het is een vereiste om een text Editor te installeren waar de codes in te lezen zijn en waar de codes mee valt te runnen. Een voorbeeld hiervan is Sublime Text. Sublime Text valt te installeren op de volgende site: https://www.sublimetext.com/3

Daarnaast is Excel een handig programma om de CSV files te openen en ze te bestuderen, zodat je weet wat er in staat om zo de juiste gegevens eruit te halen.

### Packages 

Welke packages je moet installeren om om de code te kunnen runnen:

* networkx
* matplotlib.pyplot
* matplotlib.mlab
* numpy
* csv
* copy
* randint (from random)
* gc
* operator (from itemgetter)

### Opstarten code

Om ervoor te zorgen dat alle imports in orde zijn en je elk bestand zonder errors kan laten runnen, is het als eerst zaak om het bestand main.py te runnen om de andere losse files te importeren.

## Onze code

Kleine en korte introductie om als buitenstaander de grote lijnen te begrijpen.

### Mappen

We hebben op onze GIT repository 3 mappen staan, namelijk: 
* **code** - Is een map met losse files met code. Bij de een zit de score functie in, bij de ander een functie om een graph te plotten, bij weer een ander een random-neighbour algorithme. 

* **csv-files** - Zijn de 4 csv-files waar de data vandaan wordt gehaald. In ConnectiesHolland.csv staan de connecties tussen de stations van Noord en Zuid-Holland met daarnaast de tijd in minuten om van de ene naar de andere station te komen. In ConnectiesNationaal.csv staat hetzelfde, maar dan voor alle stations van heel Nederland. In StationsHolland.csv staan alle stations gegeven van Noord en Zuid-Holland met de daarbij behorende coördinaten en of de station kritiek is of niet. In StationsNationaal.csv staat hetzelfde als in StationsHolland.csv, maar dan voor alle stations van heel Nederland.

* **old-files** - Is een map met ook losse files, maar dan nog niet geordend. Dus hier staat in bestanden nog een heleboel codes en algoritmes en daardoor deels onoverzichtelijk voor iemand die geen kennis heeft van waar we mee bezig zijn.

## Gewerkt met

* [Sublime Text 3](https://www.sublimetext.com/) - Text editor
* [Python 3.6.3](https://www.python.org/) - Programmeertaal

## Groepsleden

* **Kennet Botan**
* **Elvis Afrifa**
* **Michael van der Zwet**

## Licentie
Dit project is mede mogelijk gemaakt door het vak Heuristieken als onderdeel van de minor Programmeren aan de Universiteit van Amsterdam FNWI

## Dankwoord

* Stack Overflow
* Hulp bij Tech Assistentie - Maarten van der Sande
* Hulp bij werkcolleges - Bas Terwijn

