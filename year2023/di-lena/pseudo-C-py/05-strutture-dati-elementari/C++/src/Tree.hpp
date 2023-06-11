//header liste
#ifndef TREE_BINARIO_HPP
#define TREE_BINARIO_HPP

#include "./Node.hpp"

template <typename Type>
class Tree
{
private:
	Node<Type> radix;
public:
	//costruttore e distruttore
	Tree() {};
	Tree(Type radice);
	virtual ~Tree(void) {};

	//albero
	void insert_child(Node<Type> child);

	//stampe
	void print(void);
    void print(string str);
};

#endif //LISTA_PARENT_HPP
