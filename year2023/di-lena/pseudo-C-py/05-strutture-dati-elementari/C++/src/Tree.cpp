#include "./Tree.hpp"

//costruttore e distruttore
template <typename Type>
Tree<Type>::Tree(Type radice) {
	this->radix = Node<Type>(radice);
}

//albero
template <typename Type>
void Tree<Type>::insert_child(Node<Type> child) {}

//stampe
template <typename Type>
void Tree<Type>::print() {
	cout << this->radix;
	//this->childrens.print();
}

template <typename Type>
void Tree<Type>::print(string str) {}
