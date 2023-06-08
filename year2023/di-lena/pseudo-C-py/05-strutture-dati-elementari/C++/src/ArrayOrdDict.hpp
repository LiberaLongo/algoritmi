#ifndef DICTIONARY_ARRAY_ORDINATO_HPP
#define DICTIONARY_ARRAY_ORDINATO_HPP

#include "./Dictionary.hpp"

#include <vector>
#include <utility>
using namespace std;


template <typename KeyType, typename DataType>
class ArrayOrdDict
{
	private:
		//array ordinato
		vector<pair<KeyType, DataType>> A = {};
		int size;
		//ricerca binaria
		int binsearch(bool *found, KeyType key);
	public:
		//costruttore
		ArrayOrdDict();
		//distruttore
		virtual ~ArrayOrdDict(){};
		//dictionary
		DataType search(KeyType key);
		void insert(KeyType key, DataType data);
		void remove(KeyType key);
		//stampe
		void print(void);
		void print(string str);
};

#endif //DICTIONARY_ARRAY_ORDINATO_HPP
