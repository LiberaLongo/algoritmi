//header liste
#ifndef Tree_BINARIO_HPP
#define Tree_BINARIO_HPP

#include "./Lista.hpp"
#include <iostream>
#include <string>
using namespace std;

template <typename Type>
class Node
{
	public:
		class Node<Type>* parent;
		struct Lista<Node<Type>> childrens;
		Type info;
		bool operator ==(const Node<Type> &n) {
			return this->info == n.info;
		}
};

template <typename Type>
class Tree
{
private:
	Node<Type> *radix;
public:
	//costruttore e distruttore
	Tree(void);
	Tree(Type radice);
	virtual ~Tree(void) {};

	//Tree
	Node<Type>* createNode(Type info);
	bool empty_child(Node<Type> *parentNode);
	void insert_child(Node<Type> *parentNode, Node<Type>* childNode);
	void insert_child(Node<Type> *parentNode, Type childInfo);
	Node<Type> remove_child(Node<Type> *parentNode);
	Node<Type> out_child(Node<Type> *childNode);

	//funzioni
	Node<Type>* radice();
	Type info(Node<Type> *v);
	Node<Type>* padre(Node<Type> *v);
	int numNodi(void);
	int grado(Node<Type> *v);
	Lista<Node<Type>> figli(Node<Type> *v);
	Lista<Node<Type>> visitaDFS(Node<Type> *t);
	Lista<Node<Type>> visitaBFS(Node<Type> *t);

	//stampe
	void print(void);
    void print(string str);
};

#endif //LISTA_PARENT_HPP
