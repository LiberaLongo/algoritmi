#ifndef DICTIONARY_ARRAY_ORDINATO_HPP
#define DICTIONARY_ARRAY_ORDINATO_HPP

#include "./Dictionary.hpp"

template <typename KeyType, typename DataType>
class ArrayDisordDict : public Dictionary {
	private:
		A[];
		int size;
	public:
		//costruttore
		ArrayDisordDict();
		//distruttore
		virtual ~ArrayDisordDict(){};
		//dictionary
		DataType Search(KeyType k);
		void Insert(KeyType k, DataType e);
		void Delete(KeyType k);
		//stampe
		void print(void);
};

#endif //DICTIONARY_ARRAY_ORDINATO_HPP
