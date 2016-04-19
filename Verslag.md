Verslag Heuristiek
Tegelzetten
Tegeltjeswijsheid: Kim Schuiten, Ruben Postma en Nienke Pot.

PLAN DE CAMPAGNE

1.Datastructuur
2.Modelleren--> beetje programmeren, classes neerzetten etc. 
3. Schrijven over statespace
4. welk algoritme en schrijven --> algoritme – depth first. Van groot naar klein.


<b>Inleiding</b>

(wat is ons probleem?) Het tegelset probleem.....
Dit probleem komen we ook in meer praktische varianten tegen in het dagelijks leven, hoe pak je je koffer in en hoe worden deze koffers allemaal weer netjes in het vliegtuig geladen. 

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

Het probleem is vrij lastig omdat het een grootte state space hebt. Wel kunnen er meerdere mogelijkheden zijn en de ene oplossing is niet meer efficient dan een ander. Dus als er een oplossing gevonden is hoeft er niet gezocht worden naar een betere/efficientere oplossing.(geen optimalisatie probleem) 


