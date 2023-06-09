#include "./Lista.hpp"

#define for_each(iter) for (struct Elem<Tipo> *iter = this->head(); !this->finished(iter); iter = this->next(iter))

//costruttore e distruttore
template <typename Tipo>
Lista<Tipo>::Lista(void)
{
	struct Elem<Tipo> *sentinella = new Elem<Tipo>;
	sentinella->prev = sentinella;
	sentinella->next = sentinella;
	//sentinella.item non ci interessa
	this->testa = sentinella;
}

//setters
template <typename Tipo>
void Lista<Tipo>::setHead(struct Elem<Tipo> *head)
{
	this->testa = head;
}
template <typename Tipo>
struct Elem<Tipo> *Lista<Tipo>::getHead(void)
{
	return this->testa;
}

//metodi
template <typename Tipo>
bool Lista<Tipo>::empty(void)
{
	if (this->testa->next != this->testa->prev)
		return false;
	if (this->testa->next != this->testa)
		return false;
	return true;
}
//
template <typename Tipo>
struct Elem<Tipo> *Lista<Tipo>::head(void)
{
	return this->testa->next;
}
//
template <typename Tipo>
struct Elem<Tipo> *Lista<Tipo>::tail(void)
{
	return this->testa->prev;
}
//
template <typename Tipo>
struct Elem<Tipo> *Lista<Tipo>::next(struct Elem<Tipo> *p)
{
	return p->next;
}
//
template <typename Tipo>
struct Elem<Tipo> *Lista<Tipo>::prev(struct Elem<Tipo> *p)
{
	return p->prev;
}
//
template <typename Tipo>
bool Lista<Tipo>::finished(struct Elem<Tipo> *p)
{
	return (p == this->testa);
}
//
template <typename Tipo>
Tipo Lista<Tipo>::read(struct Elem<Tipo> *p)
{
	return p->item;
}
//
template <typename Tipo>
void Lista<Tipo>::write(struct Elem<Tipo> *p, Tipo v)
{
	p->item = v;
}
//
template <typename Tipo>
struct Elem<Tipo> *Lista<Tipo>::insert(struct Elem<Tipo> *p, Tipo v)
{
	struct Elem<Tipo> *inserito = new Elem<Tipo>;
	inserito->item = v;
	inserito->prev = p->prev;
	inserito->prev->next = inserito;
	inserito->next = p;
	p->prev = inserito;
	return inserito;
}
//
template <typename Tipo>
struct Elem<Tipo>* Lista<Tipo>::remove(struct Elem<Tipo> *p)
{
	p->prev->next = p->next;
	p->next->prev = p->prev;
	struct Elem<Tipo> *temp = p; //pk prima era 'temp = p->next;' ?
	delete p;
	return temp;
}

//metodi ausiliari
//inserisci in testa
template <typename Tipo>
void Lista<Tipo>::insert_head(Tipo v)
{
	this->insert(this->head(), v);
}
//inserisci in coda
template <typename Tipo>
void Lista<Tipo>::insert_tail(Tipo v)
{
	this->insert(this->next(this->tail()), v);
}
//rimuovi in testa
template <typename Tipo>
struct Elem<Tipo>* Lista<Tipo>::remove_head(void)
{
	return this->remove(this->head());
}
//rimuovi in coda
template <typename Tipo>
struct Elem<Tipo>* Lista<Tipo>::remove_tail(void)
{
	return this->remove(this->tail());
}

//calcola la lunghezza della Lista (e serve per non fare errori)
template <typename Tipo>
int Lista<Tipo>::lunghezza(void)
{
	int conta = 0;
	for_each(iter) {
		conta ++;
	}
	return conta;
}

//cerca v scorrendo la Lista
template <typename Tipo>
struct Elem<Tipo> *Lista<Tipo>::search(Tipo v)
{
	for_each(iter) {
		if(this->read(iter) == v) {
			return iter;
		}
	}
	return NULL;
}

template <typename Tipo>
void Lista<Tipo>::append(Lista<Tipo> l) {
	/*Elem<Tipo> *tmp = l.head();
	while(! l.finished(tmp)) {
		this->insert_tail(l.read(tmp));
		tmp = l.next(tmp);
	}*/
}

// stampe
template <typename Tipo>
void Lista<Tipo>::print(void)
{
	cout << ": [ ";
	for_each(iter) {
		//stampo elemento
		cout << this->read(iter);
		if (!(this->finished(this->next(iter))))
			cout << " --> ";
	}
	cout << " ]" << endl;
}

template <typename Tipo>
void Lista<Tipo>::print(string str)
{
    cout << str << "\t";
	this->print();
}
