#ifndef DICTIONARY_LISTA_HPP
#define DICTIONARY_LISTA_HPP

#include "./Dictionary.hpp"
#include "./Lista.hpp"

#include <vector>
#include <utility>
using namespace std;

template <typename KeyType, typename DataType>
class ListDict
{
	private:
		Lista<pair<KeyType,DataType>> list;
		Elem<pair<KeyType,DataType>>* search_ptr(KeyType key);
	public:
		//costruttore
		ListDict();
		//distruttore
		virtual ~ListDict(){};
		//dictionary
		DataType search(KeyType key);
		void insert(KeyType key, DataType data);
		void remove(KeyType key);
		//stampe
		void print(void);
		void print(string str);
};

#endif //DICTIONARY_ARRAY_ORDINATO_HPP
