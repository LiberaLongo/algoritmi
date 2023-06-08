#include "./ArrayDisordDict.hpp"

//costruttore
template <typename KeyType, typename DataType>
ArrayDisordDict<KeyType, DataType>::ArrayDisordDict() {
	this->size = 0;
}

//linsearch (privata)
template <typename KeyType, typename DataType>
int ArrayDisordDict<KeyType, DataType>::linsearch(KeyType key) {
	for (int i = 0; i < this->size; i++)
		if (this->A.at(i).first == key)
			return i;
	return -1;
}

//dictionary
template <typename KeyType, typename DataType>
DataType ArrayDisordDict<KeyType, DataType>::Search(KeyType key) {
	int i = linsearch(key);
	if (i != -1)
		return this->A.at(i).second;
	else
		return NULL;
}

template <typename KeyType, typename DataType>
void ArrayDisordDict<KeyType, DataType>::Insert(KeyType key, DataType data) {
	int i = linsearch(key);
	if (i == -1) {
		i = this->size;
		this->size ++;
		this->A.insert(this->A.begin() +i, make_pair(key, data));
	}
	this->A[i] = make_pair(key, data);
}

template <typename KeyType, typename DataType>
void ArrayDisordDict<KeyType, DataType>::Delete(KeyType key) {
	int i = linsearch(key);
	if (i != -1) {
		//leftshift(i);
		this->size --;	
	}
}

//stampe
template <typename KeyType, typename DataType>
void ArrayDisordDict<KeyType, DataType>::print(void) {
	cout << "Array Disordinato:\n";
	for (int i = 0; i < this->size; ++i) {
        cout << "(" << this->A.at(i).first << ","
            << this->A.at(i).second << ")" << "-> ";
    }
    cout << endl;
}

template <typename KeyType, typename DataType>
void ArrayDisordDict<KeyType, DataType>::print(string str)
{
    cout << str << "\t";
	this->print();
}
