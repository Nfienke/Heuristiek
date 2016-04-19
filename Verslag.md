Verslag Heuristiek
Tegelzetten
Tegeltjeswijsheid: Kim Schuiten, Ruben Postma en Nienke Pot.

PLAN DE CAMPAGNE

1.Datastructuur
2.Modelleren--> beetje programmeren, classes neerzetten etc. 
3. Schrijven over statespace
4. welk algoritme en schrijven --> algoritme – depth first. Van groot naar klein.


<b>Inleiding</b>

Bij het tegelset probleem..... PROBLEEM UITWERKEN
Dit probleem komen we ook in meer praktische varianten tegen in het dagelijks leven, hoe pak je je koffer in en hoe worden deze koffers allemaal weer netjes in het vliegtuig geladen. TOEPASBAARHEID UITWERKEN

We hebben het probleem vergeleken met het bin packing problem(bron?). Waarbij we een depth first algoritme gebruiken, waarbij de items vooraf gesorteerd zijn op grootte. Het depth first algoritme werkt als volgt.....

(plaatje tree depth first algoritme)

Doordat de items vooraf gesorteerd zijn, wordt het algoritme iets efficienter.(bron en uitleg over natuurlijke manier van sorteren)

(plaatje van ons algoritme gesorteerd.)

<b>State space:</b>
Onze upperbound is,

(N-1)!
doordat de items al gesorteerd zijn N-1! ipv N!

Lowerbound is,

N-1

Het probleem is vrij lastig omdat het een grootte state space hebt. Wel kunnen er meerdere mogelijkheden zijn en de ene oplossing is niet meer efficient dan een ander. Dus als er een oplossing gevonden is hoeft er niet gezocht worden naar een betere/efficientere oplossing.(geen optimalisatie probleem) STATE SPACE UITWERKEN
-complexiteit
-dezelfde tegels zou state space kunnen verkleinen. 
- hoeveeheid oplossingen?
- leads/hints hebben we niet
- -patronen, willen we gaan proberen met gridlines
- geen optimalisatie/effientie.

<b>ALGORITME</b>
Welk algoritme gaan we gebruiken?
-depth first
-brute force en compleet
- geen breadth fist, want te veel geheugen en geen optimalisatie. wij hebben wel een soort sorteer strategie. 


<b>DATASTRUCTUUR</b>
Welke data structuur gebruiken we?
We maken in ieder geval twee objecten aan. De eerste is ons canvas. In dit object staan de functies FreeSpace en UsedSpace. UsedSpace zijn de coordinaten van de geplaatste tegels. FreeSpace is de grootte van het canvas minus de UsedSpace. Het tweede object is de TileSet. Hierin staat een array met alle tegels in het probleem en een array waarin ze worden gesorteerd. In dit object staat ook een functie waarin elke tegel staat beschrijven. 
Tiles in een apart bestandje zetten waaruit we ze importeren. 

<b>MODELLEREN:</b>
We hebben een canvas waarop de tegels geplaatst moeten worden. We hebben ook een set met tegels van verschillende groottes. 
We willen eerst die tegelsets sorteren van groot naar klein. 
De grootste tegel zetten we op de coördinaten 0,0. De plekken waar we tegels neer zetten is used space. Het stuk canvas dat over blijft noemen we free space. De blokken die in de free space vrij staan zetten we ook in een array met coördinaten. 
Bovenstaande is nu te ingewikkeld. Onze aanpak nu is om alles gewoon random er in te zetten en als het niet past een stap terug te doen, we moeten dus die boom uitwerken. 
-gridlines toevoegen in toekomst. 


