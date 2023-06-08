#ifndef DICTIONARY_HPP
#define DICTIONARY_HPP

#include <iostream>
#include <vector> //per le coppie <chiave, valore>
//quindi first è key, second è data

//interfaccia

template <typename KeyType, typename DataType>
class Dictionary{
    public:
/* search(Key k)
* - Cerca la chiave kì
* - Ritorna i dati associati a k o NIL */
		virtual DataType search(KeyType key) = 0;
/* insert(Key k, Data d)
* - Verifica con ricerca lineare se k è presente
* - Se k è presente, sostituisce i dati
* - Altrimenti, inserisce la coppia (k, d) nella prima posizione libera*/
		virtual void insert(KeyType key, DataType data) = 0;
/* delete(Key k)
Cerca k tramite ricerca lineare
Se k è presente, rimuove la coppia (k, d) dalla struttura dati
Sposta di una posizione a sinistra tutte le coppie dopo k */
		virtual void remove(KeyType key) = 0;
};

#endif //DICTIONARY_HPP
