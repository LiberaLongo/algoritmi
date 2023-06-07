#ifndef DICTIONARY_ARRAY_ORDINATO_HPP
#define DICTIONARY_ARRAY_ORDINATO_HPP

#include "./Dictionary.hpp"

const int MAXN = 200;

template <typename KeyType, typename DataType>
class ArrayDisordDict
{
	private:
		vector<pair<KeyType, DataType>> A[MAXN];
		int size;
		int linsearch(KeyType key);
	public:
		//costruttore
		ArrayDisordDict();
		//distruttore
		virtual ~ArrayDisordDict(){};
		//dictionary
		DataType Search(KeyType key);
		void Insert(KeyType key, DataType e);
		void Delete(KeyType key);
		//stampe
		void print(void);
		void print(string str);
};

#endif //DICTIONARY_ARRAY_ORDINATO_HPP
