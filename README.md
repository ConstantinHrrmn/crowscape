# CrowScape

## Projet

Le but du projet est de créer à l'aide de la CrowPi un mini escapegame. Afin de gagner la partie, il va falloir résoudre le plus rapidement possible toutes les énigmes de la valise

## Installation 

* Tkinter
* python3

## Utilisation 
```bash
./gamemanager.py
```
ou
```bash
python3 gamemanager.py
```

## Modules à désamorcer

### Et la lumière fut

#### Parties utilisées

* Capteur de luminosité

#### But

Réduire la lumière que détecte le capteur de luminosité.

### Labyrinthe

#### Parties utilisées

* Boutons verts
* Matrice de LED

#### But

Ramener le point sur la matrice de LED à la sortie notée sur l’écran par le point vert.

### Il fait froid

#### Parties utilisées

* Capteur d’humidité et de température

#### But

Souffler de l’air chaud sur le capteur d’humidité afin d’en augmenter l’humidité.

### Bataille navale

#### Parties utilisées

* Afficheur LCD
* Boutons jaunes

#### But

Appuyer sur les bons boutons jaunes par rapport aux coordonnées. Les colonnes sont notées de A à D et les lignes de 0 à 3. 

### LightSwitch

#### Parties utilisées

* Matrice de LED
* Boutons jaunes

#### But

Faire en sorte que toute la matrice de LED soit rouge avec les boutons jaunes. Chaque bouton change les led correspondantes sur la LED ainsi que ses voisins. 

### La bonne séquence

#### Parties utilisées

* Capteur RFID

#### But

Reproduire la séquence donnée avec les bonnes cartes RFID

### Simon dit ... 

#### Parties utilisées

* Boutons verts

#### But

Reproduire la séquence donnée avec les boutons verts.