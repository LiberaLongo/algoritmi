#include "./Stack.hpp"

//costruttore e distruttore
template <typename Tipo>
Stack<Tipo>::Stack(void)
{
	this->list = Lista<Tipo>();
}

//read
template <typename Tipo>
Tipo Stack<Tipo>::read(void)
{
	return this->list.read(this->list.head());
}

//stack
template <typename Tipo>
void Stack<Tipo>::push(Tipo elem)
{
	this->list.insert_head(elem);
}

template <typename Tipo>
Tipo Stack<Tipo>::pop(void)
{
	return this->list.read(this->list.remove_head());
}

// stampe
template <typename Tipo>
void Stack<Tipo>::print(void)
{
	cout << "Stack";
	this->list.print();
}

template <typename Tipo>
void Stack<Tipo>::print(string str)
{
    cout << str << "\t";
	this->print();
}

