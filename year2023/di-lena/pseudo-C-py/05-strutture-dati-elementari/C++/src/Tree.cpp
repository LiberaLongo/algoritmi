#include "./Tree.hpp"

//costruttore e distruttore
template <typename Type>
Tree<Type>::Tree(Type radice) {
	this->parent = NULL;
	this->info = radice;
}

//albero
template <typename Type>
void Tree<Type>::insert_child(Tree<Type> child) {}

//stampe
template <typename Type>
void Tree<Type>::print() {
	cout << "Tree(" << this->info << ")" << endl;
	//this->childrens.print();
}

template <typename Type>
void Tree<Type>::print(string str) {}
