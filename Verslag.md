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

Doordat de items vooraf gesorteerd zijn, wordt het algoritme iets efficiënter.(bron en uitleg over natuurlijke manier van sorteren)

(plaatje van ons algoritme gesorteerd.)
UITWERKEN WAT DEPTH FIRST IS ETC. --> Kim


Welk algoritme gaan we gebruiken?
-depth first
-brute force en compleet
- geen breadth fist, want te veel geheugen en geen optimalisatie. wij hebben wel een soort sorteer strategie. 


####DATASTRUCTUUR

<b>Tileset</b>

De tegels die gebruikt moeten worden om het canvas te vullen zijn een van de objecten in onze data. Aangezien er vrij veel tegels en sets van tegels zijn, hebben wij ervoor gekozen om deze tegelsets in een externe file te zetten en ze vanuit daar in te laden. Hieronder volgt een voorbeeld van hoe een tegelset is gerepresenteerd.<br>

tileSet1 = [('A',2,2),('B',3,3),('C',3,3),('D',3,3),('E',3,3),('F',3,3),('G',3,3),
('H',3,3),('I',5,5),('J',5,5),('K',5,5),('L',7,7),('M',7,7),('N',7,7)]
<br>

Elke tegelset is genummerd, aan de hand van het nummer van de problemsets. De tegelset bestaat uit een list of lists. Een list die de totale weergave van de tegelset representeert, bestaande uit lists waarin elke list een tegel weergeeft. 
Elke tegel heeft een naam, bestaande uit 1 of 2 letters. En een tegel heeft een breedte en een lengte. 

De tegels hebben een naam, omdat we zo makkelijker kunnen kijken welke tegels gebruikt zijn en of de tegels op de juiste manier gebruikt zijn. Als je een tegel alleen plaatst, weten we niet welke tegel dit is. Dan valt wel te achterhalen hoe groot een tegel is, maar niet welke tegel dat dan geweest is, als er bijvoorbeeld meerdere tegels van 3 bij 3 zijn. En misschien is de tegel er wel met de foute afmetingen ingezet. Door de naam van de tegel is dan achteraf makkelijker te controleren of de plaatsing van de tegels op de juist manier is gegaan. 


<b>Canvas</b>

Het canvas is een belangrijk object in onze data, het moet laten zien waar welke plek vrij is of waar welke tegel is gezet. Hiervoor is er een soort matrix gebruikt. Deze wordt gerepresenteerd als een list of lists. 
Er is een grote list die het canvas als totaal weergeeft en daarin zitten lists die elk een row representeert. De rijen zijn dan de lists en de elementen in de lists representeren het aantal kolommen. Op deze manier heb je meteen een soort coördinaat systeem, waar je een plek kan aanwijzen door te verwijzen naar een rij(de positie van een list in de list) en vervolgens naar het nummer van een kolom(de positie van het element in de list). Elk element in het canvas heeft dus een waarde van 1 bij 1, aangezien de tegels geen halve waardes hebben levert dit geen problemen op. Een leeg canvas van 4 bij 4, komt er dan als volgt uit te zien:<br>

Canvas= <br>
[[0,0,0,0]<br>
[0,0,0,0]<br>
[0,0,0,0]<br>
[0,0,0,0]]<br>
<br>


Een 0 representeert een leeg vlak, als een tegel in het canvas past, dan wordt de letter ingevuld op die positie in het canvas. Bijvoorbeeld een tegel A van 2 bij 2, wordt als volgt in het canvas geplaatst.<br> 

Canvas= <br>
[[A,A,0,0]<br>
[A,A,0,0]<br>
[0,0,0,0]<br>
[0,0,0,0]]<br>
<br>

Doordat de rijen onder elkaar geprint worden, is het ook visueel snel duidelijk waar nog ruimte over is en hoe de tegels geplaatst zijn. Je loopt door het canvas heen en als Canvas[0][1]==0 is, dan weet je dat deze plek vrij is om te plaatsen. 

####MODELLEREN

We hebben een canvas waarop de tegels geplaatst moeten worden. We hebben ook een set met tegels van verschillende groottes. 
We willen eerst die tegelsets sorteren van groot naar klein. 
De grootste tegel zetten we op de coördinaten 0,0. De plekken waar we tegels neer zetten is used space. Het stuk canvas dat over blijft noemen we free space. De blokken die in de free space vrij staan zetten we ook in een array met coördinaten. 
Bovenstaande is nu te ingewikkeld. Onze aanpak nu is om alles gewoon random er in te zetten en als het niet past een stap terug te doen, we moeten dus die boom uitwerken. 
-gridlines toevoegen in toekomst. 


