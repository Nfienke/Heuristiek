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

week 3
8.Algoritme volledig werkend --> visualisatie.
9. Verslag verder uitwerken. 
10. verbeteren algoritme 
--> bouwcamp code: http://mathworld.wolfram.com/PerfectSquareDissection.html
--> of gridlines??

####Inleiding
Het probleem waar wij ons mee bezig hebben gehouden heet tegelzetten. Zoals de naam al doet vermoeden moeten wij een bepaald aantal tegels van verschillende groottes zetten op een canvas van bepaalde grootte. Het lastige aan dit probleem is dat de tegels precies moeten passen, er mogen geen tussenruimtes tussen de tegels zitten en de tegels mogen ook niet overlappen (website heuristieken). 

Dit maakt het probleem een constraint satisfaction probleem. Er moet worden voldaan aan een  aantal voorwaarden, de oplossing is goed zodra hier aan is voldaan. Er zijn daarom geen goede of slechte oplossingen, alle oplossingen zijn even goed (college 25 april).	

Het probleem van tegelzetten is iets wat we op gevarieerde wijze in de praktijk tegen komen. Denk bijvoorbeeld aan het zo efficiënt mogelijk inpakken van de laadruimte van een vliegtuig, of zelfs je eigen koffer. Dit soort inpak problemen worden ook wel het packing problems genoemd, in ons geval hebben we te maken met een probleem dat lijkt op het two-dimensional bin packing problem. In dit probleem krijgt men een minimaal aantal rechthoekige “bins” met een breedte van B en een hoogte van H, en een set van rechthoekige items met een breedte van bj <= B en een hoogte van hj, waarbij 1 <= j <= n. Het probleem is dat men de items wilt inpakken in het minimale aantal “bins” zonder dat er overlap is tussen de items. Daarnaast mogen de items in dit probleem ook niet gedraaid worden (survey on two dimensional packing en Bansal et al p. 1). De algoritmes die in de literatuur worden genoemd om dit soort problemen op te lossen zijn te verdelen in twee soorten. Ten eerste de one phase algoritmes. Hierin worden de items regelrecht in het minimum aantal bins geplaatst. De tweede soort is het two phase algoritme. In deze algoritmes wordt er gestart met het plaatsen van items in een enkele strip. In de tweede fase wordt de strip oplossing gebruikt om het inpakken van het minimale aantal bins op te bouwen (survey on two dimensional packing).

Dit two-dimensional bin packing problem sluit echter niet helemaal aan op ons probleem. In het tegelzet probleem hebben we namelijk niet te maken met meerdere twee-dimensionale bins, maar met één twee-dimensionaal canvas waar het aantal tegels dat we hebben precies op moet passen. Bij bin packin problems heeft men nog de optie om ruimte over te houden, er wordt gezocht naar een optimale manier van inpakken, bij ons bestaat die mogelijkheid niet. 



####State space

De moeilijkheid van het probleem zit hem vooral in de grootte van de state space.
De upperbound van het tegelzetprobleem is normaal N!, maar door het vooraf sorteren van de items op grootte is de eerste stap al bepaald. Dit maakt de upperbound kleiner, de upperbound is dan N-1!. Ookal is de state space nu wel iets kleiner, het aantal opties is nog steeds zeer groot. 
Het minimaal aantal stappen dat moet worden gezet voor een oplossing is normaal N, maar door het vooraf sorteren is de lowerbound N-1. Tegels met dezelfde grootte kan de state space verkleinen. Stel je hebt 4 vierkante tegels met een breedte 2,3,4,5 dan heb je meer keuze in het plaatsen van de tegels dan als alle tegels een breedte hebben van alleen 2 en 4. <br>

Wat het probleem minder lastig maakt is dat het geen optimalisatie probleem is. Er kunnen in theorie meerdere mogelijkheden zijn en die zijn allen even goed. Er is dan geen betere of slechtere oplossing. Het probleem heeft ook geen leads die het probleem makkelijker zouden kunnen maken. <br>

Wel kan het probleem door het maken van patronen makkelijker worden gemaakt. Dit zou kunnen door het toevoegen van gridlines. Deze splitsen het canvas, na het plaatsen van de eerste en grootste tegel, op in kleinere vlakken. Op deze manier wordt het canvas opgedeeld in kleinere vlakken en dus kleinere problemen. Door de kleinere canvassen op te vullen met tegels, ontstaan er kleine canvassen met tegels in een groot canvas, waardoor de canvas uit grotere blokken(de kleine canvassen) bestaat. <br>

(plaatje)
<br>

Ook kunnen patronen in het canvas worden gemaakt door het toepassen van de bouwcampcode. Hier worden de tegels geplaatst aangrenzend aan de meest linkstaande en bovenstaande tegel geplaatst. Hierdoor ontstaan ook groepen tegels. <br>
(plaatje)
<br>

PATRONEN HELDER, bouwcamp/gridlines nog meer??)



####Algoritme
Voor ons algoritme maken we gebruik van de Depth First Search (DFS), waarin we onze items vooraf sorteren op grootte. DFS algoritmes zijn constructief, ze worden stap voor stap opgebouwd en alle mogelijkheden worden afgegaan, dit noemen we brute force. Uiteindelijk zal het algoritme een oplossing terug geven, of een ‘oplossing bestaat niet’, het is dus een compleet algoritme. Het verschil met de Breadth First Search zit met name in de snelheid en het aantal geheugen dat wordt gebruikt. Breadt First wordt vaak gebruikt voor optimalisatie problemen, en daar zijn wij niet mee bezig  (college 18 april).

De Depth First Search kan het beste worden gezien als een boom waarin men steeds een tak volgt waar aan het einde ofwel een oplossing is, ofwel geen oplossing. Als er geen oplossing is aan het einde van de tak moet men terugzoeken naar de laatste vertakking en deze vertakking afgaan, enzovoort (zie afbeeld n). De punt waar vertakkingen ontstaan noemen we nodes, alle nodes zijn in eerste instantie ongemarkeerd. In de code van een dergelijk algoritme moet men wel verwerken of een node al eerder bezocht is of niet, zodat er steeds naar een nieuwe vertakking wordt gezocht(K. Mehlhorn en P. Sanders, 2008: 178). 

De pseudocode van een dergelijk algoritme zou er als volgt uit kunnen zien:

Def DFS(graph, start):
	stack = [start]
	visited = []
	while stack:
		parent = stack.pop() #pop from end
		if parent not in visited
			visited.append(parent)
			for n in parent.children
				stack.append(n) #push

<i>Bron: College 18 april</i>




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


