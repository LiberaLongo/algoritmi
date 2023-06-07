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
* - Cerca la chiave k tramite ricerca lineare sull’array
* - Ritorna i dati associati a k o NIL */
		virtual DataType Search(KeyType key) = 0;
/* insert(Key k, Data d)
* - Verifica con ricerca lineare se k è presente nell’array
* - Se k è nell’array, sostituisce i dati
* - Altrimenti, inserisce la coppia (k, d) nella prima posizione libera*/
		virtual void Insert(KeyType key, DataType e) = 0;
/* delete(Key k)
Cerca k tramite ricerca lineare
Se k è nell’array, rimuove la coppia (k, d) dall’array
Sposta di una posizione a sinistra tutte le coppie dopo k */
		virtual void Delete(KeyType key) = 0;
};

#endif //DICTIONARY_HPP
