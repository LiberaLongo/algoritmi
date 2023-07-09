#!/usr/bin/env python3

import grafo;
import networkx as nx;

def test():
	G = grafo.grafo();
	G.aggiungiVertice('A');
	G.aggiungiVertice('B');
	G.aggiungiVertice('C');
	G.aggiungiArco('A', 'B');
	G.aggiungiArco('B', 'C', 'Etichetta2');
	G.draw();
	G.rimuoviVertice('D');
	G.rimuoviVertice('C');
	G.draw();

#un grafo su un gioco che non volevo disegnare a mano
def roblox_cart_pirate_lvl8():
	G = grafo.grafo();
	G.aggiungiVertice('start');
	G.aggiungiVertice('1');
	G.aggiungiArco('start', '1');
	G.aggiungiArco('1', '1', 'right or left')
	G.aggiungiVertice('back');
	G.aggiungiArco('back', '1', 'continue');
	G.aggiungiVertice('2');
	G.aggiungiArco('1', '2', 'jump');
	G.aggiungiArco('2', 'back', 'right');
	G.aggiungiVertice('3');
	G.aggiungiArco('2', '3', 'forward');
	G.aggiungiVertice('4');
	G.aggiungiArco('3', '4', 'forward');
	G.aggiungiVertice('5');
	G.aggiungiArco('4', '5', 'down');
	G.aggiungiArco('5', '3', 'right');
	G.aggiungiVertice('6');
	G.aggiungiArco('5', '6', 'left, jump, slow');
	G.aggiungiVertice('checkpoint');
	G.aggiungiArco('6', 'checkpoint', 'left');
	G.aggiungiVertice('die');
	G.aggiungiArco('6', 'die', 'forward');
	G.aggiungiArco('die', 'start', 'respawn')
	G.aggiungiVertice('idk');
	G.aggiungiArco('3', 'idk', 'left');
	G.aggiungiArco('6', 'idk', 'right');
	G.aggiungiVertice('7');
	G.aggiungiArco('4', '7', 'jump');
	G.aggiungiVertice('stuck');
	G.aggiungiArco('7', 'stuck', 'left');
	G.aggiungiArco('7', '1', 'forward');
	G.aggiungiArco('stuck', 'start', 'respawn');
	G.draw('kawai');
#test();
roblox_cart_pirate_lvl8();
