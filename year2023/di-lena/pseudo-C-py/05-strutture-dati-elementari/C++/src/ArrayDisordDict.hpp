#ifndef DICTIONARY_ARRAY_DISORDINATO_HPP
#define DICTIONARY_ARRAY_DISORDINATO_HPP

#include "./Dictionary.hpp"

#include <vector>
#include <utility>
using namespace std;


template <typename KeyType, typename DataType>
class ArrayDisordDict
{
	private:
		vector<pair<KeyType, DataType>> A = {};
		int size;
		//ricerca lineare
		int linsearch(KeyType key);
	public:
		//costruttore
		ArrayDisordDict();
		//distruttore
		virtual ~ArrayDisordDict(){};
		//dictionary
		DataType search(KeyType key);
		void insert(KeyType key, DataType data);
		void remove(KeyType key);
		//stampe
		void print(void);
		void print(string str);
};

#endif //DICTIONARY_ARRAY_ORDINATO_HPP
