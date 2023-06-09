#include "./ListDict.hpp"

#define for_each_elem(iter) for (struct Elem<pair<KeyType,DataType>> *iter = this->list.head(); !this->list.finished(iter); iter = this->list.next(iter))

//costruttore
template <typename KeyType, typename DataType>
ListDict<KeyType, DataType>::ListDict() {
	this->list = Lista<pair<KeyType,DataType>>();
}
//ausiliaria (privata)
template <typename KeyType, typename DataType>
Elem<pair<KeyType,DataType>>* ListDict<KeyType, DataType>::search_ptr(KeyType key) {
	for_each_elem(iter) {
		if(this->list.read(iter).first == key)
			return iter;
	}
	return NULL;
}

//dictionary
template <typename KeyType, typename DataType>
DataType ListDict<KeyType, DataType>::search(KeyType key) {
	Elem<pair<KeyType,DataType>> *res = this->search_ptr(key);
	if( res != NULL)
		return this->list.read(res).second;
	return NULL;
}

template <typename KeyType, typename DataType>
void ListDict<KeyType, DataType>::insert(KeyType key, DataType data) {
	/*
	//così c'è ripetizione di chiavi...ma costo O(1)
	this->list.insert_head(make_pair(key, data));
	*/
	//in questo modo non c'è ripetizioni di chiavi ma il costo non è O(1);
	Elem<pair<KeyType,DataType>> *res = this->search_ptr(key);
	if( res == NULL)
		this->list.insert_head(make_pair(key, data));
	else
		this->list.write(res, make_pair(key, data));
}

template <typename KeyType, typename DataType>
void ListDict<KeyType, DataType>::remove(KeyType key) {
	Elem<pair<KeyType,DataType>> *res = this->search_ptr(key);
	if(res != NULL) this->list.remove(res);
}

//stampe
template <typename KeyType, typename DataType>
void ListDict<KeyType, DataType>::print(void) {
	cout << "List Dictionary: [";
	for_each_elem(iter) {
		pair<KeyType, DataType> elem = this->list.read(iter);
		cout << "(" <<elem.first << "," << elem.second << ")";
		if( ! this->list.finished(this->list.next(iter)))
			cout << " --> ";
	}
	cout << "]" << endl;
}

template <typename KeyType, typename DataType>
void ListDict<KeyType, DataType>::print(string str)
{
    cout << str << "\t";
	this->print();
}
