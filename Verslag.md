Verslag Heuristiek
Tegelzetten
Tegeltjeswijsheid: Kim Schuiten, Ruben Postma en Nienke Pot.

PLAN DE CAMPAGNE
week 1
1.Datastructuur
2.Modelleren--> beetje programmeren, classes neerzetten etc. 
3. Schrijven over statespace
4. welk algoritme en schrijven --> algoritme – depth first. Van groot naar klein.

week 2
5. Hoe krijgen we toegang tot elke coordinaat?
6. Hoe veranderen we een 0 naar een naam van een tegel?
7. Verslag verder uitwerken


####Inleiding

Bij het tegelset probleem..... PROBLEEM UITWERKEN --> Kim
Dit probleem komen we ook in meer praktische varianten tegen in het dagelijks leven, hoe pak je je koffer in en hoe worden deze koffers allemaal weer netjes in het vliegtuig geladen. TOEPASBAARHEID UITWERKEN --> Kim
Bin packing problem


####State space

De moeilijkheid van het probleem zit hem vooral in de grootte van de state space.
De upperbound van het tegelzetprobleem is normaal N!, maar door het vooraf sorteren van de items op grootte is de eerste stap al bepaald. Dit maakt de upperbound kleiner, de upperbound is dan N-1!. Ookal is de state space nu wel iets kleiner, het aantal opties is nog steeds zeer groot. 
Het minimaal aantal stappen dat moet worden gezet voor een oplossing is normaal N, maar door het vooraf sorteren is de lowerbound N-1. Tegels met dezelfde grootte kan de state space verkleinen. Stel je hebt 4 vierkante tegels met een breedte 2,3,4,5 dan heb je meer keuze in het plaatsen van de tegels dan als al tegels een breedte hebben van alleen 2 en 4. 

Wat het probleem minder lastig maakt is dat het geen optimalisatie probleem is. Er kunnen in theorie meerdere mogelijkheden zijn en die zijn alle even goed. Er is dan geen betere of slechtere oplossing. Wel kan door het maken van patronen de oplossing makkelijker worden gemaakt. Door het toevoegen van gridlines waardoor het canvas wordt opgedeeld in kleinere vlakken. Ook kan je dan binnen het canvas met de vlakken schuiven. (PATRONEN BETER UITLEGGEN) --> Nienke 
Het probleem heeft geen leads die het probleem makkelijker zouden kunnen maken.


####Algoritme
We hebben het probleem vergeleken met het bin packing problem(bron?).
 Waarbij we een depth first algoritme gebruiken, waarbij de items vooraf gesorteerd zijn op grootte. Het depth first algoritme werkt als volgt.....

(plaatje tree depth first algoritme)

Doordat de items vooraf gesorteerd zijn, wordt het algoritme iets efficienter.(bron en uitleg over natuurlijke manier van sorteren)

(plaatje van ons algoritme gesorteerd.)
UITWERKEN WAT DEPTH FIRST IS ETC. --> Kim


Welk algoritme gaan we gebruiken?
-depth first
-brute force en compleet
- geen breadth fist, want te veel geheugen en geen optimalisatie. wij hebben wel een soort sorteer strategie. 


####DATASTRUCTUUR

<b>Tileset</b>

<b>Canvas</b>

Welke data structuur gebruiken we?
We maken in ieder geval twee objecten aan. De eerste is ons canvas. In dit object staan de functies FreeSpace en UsedSpace. UsedSpace zijn de coordinaten van de geplaatste tegels. FreeSpace is de grootte van het canvas minus de UsedSpace. Het tweede object is de TileSet. Hierin staat een array met alle tegels in het probleem en een array waarin ze worden gesorteerd. In dit object staat ook een functie waarin elke tegel staat beschrijven. 
Tiles in een apart bestandje zetten waaruit we ze importeren. 

Elke keer door de array lopen kost heel veel tijd! Elk van de rij in ons canvas is een lijst. Waarin 1 bezet betekent, en 0  vrij. Bijv:
[[1, 1, 0],
[1, 1, 0],
[0, 0, 0]]
GRID[0][2] == 0 # hier kan je een tegel plaatsen. 

--> Nienke


####MODELLEREN

We hebben een canvas waarop de tegels geplaatst moeten worden. We hebben ook een set met tegels van verschillende groottes. 
We willen eerst die tegelsets sorteren van groot naar klein. 
De grootste tegel zetten we op de coördinaten 0,0. De plekken waar we tegels neer zetten is used space. Het stuk canvas dat over blijft noemen we free space. De blokken die in de free space vrij staan zetten we ook in een array met coördinaten. 
Bovenstaande is nu te ingewikkeld. Onze aanpak nu is om alles gewoon random er in te zetten en als het niet past een stap terug te doen, we moeten dus die boom uitwerken. 
-gridlines toevoegen in toekomst. 


