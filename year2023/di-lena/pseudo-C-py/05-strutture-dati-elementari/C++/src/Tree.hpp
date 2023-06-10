//header liste
#ifndef TREE_BINARIO_HPP
#define TREE_BINARIO_HPP

#include "./Lista.hpp"

template <typename Type>
class Tree
{
private:
	Type info;
	Tree<Type> *parent;
	//Lista<Tree<Type>> childrens;
public:
	//costruttore e distruttore
	Tree() {};
	Tree(Type radice);
	virtual ~Tree(void) {};

	//albero
	void insert_child(Tree<Type> child);

	//stampe
	void print(void);
    void print(string str);
};

#endif //LISTA_PARENT_HPP
