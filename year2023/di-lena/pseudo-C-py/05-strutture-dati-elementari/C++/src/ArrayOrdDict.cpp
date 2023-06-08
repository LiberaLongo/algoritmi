#include "./ArrayOrdDict.hpp"

//costruttore
template <typename KeyType, typename DataType>
ArrayOrdDict<KeyType, DataType>::ArrayOrdDict() {
	this->size = 0;
}

//binsearch (privata)
template <typename KeyType, typename DataType>
int ArrayOrdDict<KeyType, DataType>::binsearch(bool *found, KeyType key) {
	*found = true; //suppongo di trovarlo
	int inizio = 0, fine = this->size-1;
	while ( inizio <= fine ) {
		int medio = ( inizio + fine ) / 2; //divisione intera
		if ( this->A[medio].first == key )
			return medio;
		else if ( this->A[medio].first < key )
			inizio = medio +1;
		else
			fine = medio -1;
	}
	*found = false; //se non lo trovo lo metto a false
	return inizio; //ritorno la posizione in cui 'dovrebbe' essere
}

//dictionary
template <typename KeyType, typename DataType>
DataType ArrayOrdDict<KeyType, DataType>::search(KeyType key) {
	bool found;
	int i = binsearch(&found, key);
	if ( !found ) //if (i == -1) se binsearch avesse trovato -1 (non ha trovato)
		return this->A.at(i).second;
	else
		return NULL;
}

template <typename KeyType, typename DataType>
void ArrayOrdDict<KeyType, DataType>::insert(KeyType key, DataType data) {
	bool found;
	int i = binsearch(&found, key);
	if ( !found )//se binsearch non ha trovato restituisce la pos in cui inserirlo
	{
		//rightshift(i);
		//i è cmq la posizione in cui dovrei inserirlo
		this->size ++;
		//inserimento in posizione i
		this->A.insert(this->A.begin() +i, make_pair(key, data));
	} else
		this->A[i] = make_pair(key, data);
}

template <typename KeyType, typename DataType>
void ArrayOrdDict<KeyType, DataType>::remove(KeyType key) {
	bool found;
	int i = binsearch(&found, key);
	if ( found ) { //if (i != -1) se binsearch ha trovato
		//leftshift(i);
		this->size --;
		this->A.erase(this->A.begin() + i);
	}
}

//stampe
template <typename KeyType, typename DataType>
void ArrayOrdDict<KeyType, DataType>::print(void) {
	cout << "Array Ordinato: [";
	for (int i = 0; i < this->size; ++i) {
        cout << "(" << this->A.at(i).first << ","
            << this->A.at(i).second << ")" << "; ";
    }
    cout << "]" << endl;
}

template <typename KeyType, typename DataType>
void ArrayOrdDict<KeyType, DataType>::print(string str)
{
    cout << str << "\t";
	this->print();
}
