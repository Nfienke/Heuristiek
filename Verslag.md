Verslag Heuristiek
Tegelzetten
Tegeltjeswijsheid: Kim Schuiten, Ruben Postma en Nienke Pot.

PLAN DE CAMPAGNE

1.	artikelen zoeken
2.	op basis artikelen algoritme bepalen
3.	op basis algoritme state space, boven grens en onder grens bepalen

4.	algoritme – depth first. Van groot naar klein.
5.	Hoe gaan we dat in programmeertaal en formule opschrijven. 
6.	Voor GUI kijken naar voorbeeldcode Python.
7.	Wat voor package hebben we nodig om python te runnen

<b>Vragen Wouter 19/04:</b>
- Tips voor GUI om de tegels te visualiseren?
- Hoe kunnen we het beste de gridlines en de coördinaten aanpakken?
- Feedback op ons algoritme (depth first): Kunnen we zoals ons eerste plan het beste van groot naar klein werken? Of is het beter als het algoritme is de eerst de grootste tegel plaatst en dan op basis van de gridlines bepaalt of de volgende tegel een grote of een kleine moet zijn?

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

Lowerbound is,

N-1

probleem is vrij lastig omdat het een grootte state space hebt. Wel kunnen er meerdere mogelijkheden zijn en de ene oplossing is niet meer efficient dan een ander. Dus als er een oplossing gevonden is hoeft er niet gezocht worden naar een betere/efficientere oplossing. 


