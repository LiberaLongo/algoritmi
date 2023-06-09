#include "./Tree.hpp"
//costruttore e distruttore
template <typename Type>
Tree<Type>::Tree()
{
	this->radix = NULL;
}

template <typename Type>
Tree<Type>::Tree(Type radice)
{
	this->radix = createNode(radice);
}

//Tree
template <typename Type>
Node<Type>* Tree<Type>::createNode(Type info)
{
	Node<Type> *newNode = new Node<Type>;
	newNode->parent = NULL;
	newNode->childrens = Lista<Node<Type>>();
	newNode->info = info;
	return newNode;
}

template <typename Type>
bool Tree<Type>::empty_child(Node<Type> *parentNode)
{
	return parentNode->childrens.empty();
}

template <typename Type>
void Tree<Type>::insert_child(Node<Type> *parentNode, Node<Type> *childNode)
{
	childNode->parent = parentNode;
	parentNode->childrens.insert_tail(*childNode);
}

template <typename Type>
void Tree<Type>::insert_child(Node<Type> *parentNode, Type childInfo)
{
	Node<Type> *newNode = this->createNode(childInfo);
	insert_child(parentNode, newNode);
}

template <typename Type>
Node<Type> Tree<Type>::remove_child(Node<Type> *parentNode)
{
	return parentNode->childrens.remove_head()->item;
}

template <typename Type>
Node<Type> Tree<Type>::out_child(Node<Type> *childNode)
{
	Node<Type> *parent = childNode->parent;
	if( parent != NULL ) {
		Elem<Node<Type>>* tmp = parent->childrens.search(*childNode);
		if( tmp != NULL )
			return parent->childrens.remove(tmp)->item;
	}
	cout << "something null";
	return Node<Type>();
}

//funzioni
template <typename Type>
Node<Type>* Tree<Type>::radice()
{
	return this->radix;
}

template <typename Type>
Type Tree<Type>::info(Node<Type> *v)
{
	return v->info;
}

template <typename Type>
Node<Type>* Tree<Type>::padre(Node<Type> *v)
{
	return v->parent;
}

template <typename Type>
int Tree<Type>::numNodi()
{
	return 0;
}
template <typename Type>
int Tree<Type>::grado(Node<Type> *v)
{
	return 0;
}

template <typename Type>
Lista<Node<Type>> Tree<Type>::figli(Node<Type> *v)
{
	return v->childrens;
}

template <typename Type>
Lista<Node<Type>> Tree<Type>::visitaDFS(Node<Type> *t)
{
	Lista<Node<Type>> list = Lista<Node<Type>>();

	return list;
}

template <typename Type>
Lista<Node<Type>> Tree<Type>::visitaBFS(Node<Type> *t)
{
	Lista<Node<Type>> list = Lista<Node<Type>>();
	return list;
}


// stampe
template <typename Type>
void Tree<Type>::print(void)
{
	//this->visitaDFS(this->radice()).print();
}

template <typename Type>
void Tree<Type>::print(string str)
{
    cout << str << "\t";
	this->print();
}
