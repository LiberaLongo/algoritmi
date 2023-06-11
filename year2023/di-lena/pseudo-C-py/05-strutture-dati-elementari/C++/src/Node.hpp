#ifndef NODE_HPP
#define NODE_HPP

#include "./Lista.hpp"

template <typename Type>
class Node {
	private:
		Type info;
		Node<Type> *parent;
		//Lista<Node<Type>> childrens;
	public:
		Node() {};
		Node(Type info);
		friend ostream& operator<< (ostream& os, const Node<Type>& n) {
			return os << n.info;
		}
};

#endif //NODE_HPP
