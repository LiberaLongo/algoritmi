#!/usr/bin/env python3

import grafo;

G = grafo.grafo()
G.aggiungiVertice('A')
G.aggiungiVertice('B')
G.aggiungiVertice('C')
G.aggiungiArco('A', 'B')
G.aggiungiArco('B', 'C', 'Etichetta2')
G.draw();
G.rimuoviVertice('D');
G.rimuoviVertice('C');
G.draw();