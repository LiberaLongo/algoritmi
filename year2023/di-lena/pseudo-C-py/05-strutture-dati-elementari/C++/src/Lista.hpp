//header liste
#ifndef LISTA_HPP
#define LISTA_HPP

#include <iostream>
#include <string>
using namespace std;

template <typename Tipo>
struct Elem
{
	struct Elem<Tipo>* prev;
	struct Elem<Tipo>* next;
	Tipo item;
};

/*volevamo definire struct Elem* come pos e typeHead
ma non è facilmente disponibile typedef template
bisogna fare cose difficilmente comprensibili*/

template <typename Tipo>
class Lista
{
private:
	struct Elem<Tipo>* testa;
public:
	//costruttore e distruttore
	Lista(void);
	virtual ~Lista(void) {};

	//setters
	void setHead(struct Elem<Tipo>* head);
	struct Elem<Tipo>* getHead(void);

	//metodi
	bool empty(void);
	//primo elemento della lista esclusa sentinella
	struct Elem<Tipo>* head(void);
	struct Elem<Tipo>* tail(void);
	struct Elem<Tipo>* next(struct Elem<Tipo>* p);
	struct Elem<Tipo>* prev(struct Elem<Tipo>* p);
	bool finished(struct Elem<Tipo>* p);
	Tipo read(struct Elem<Tipo>* p);
	void write(struct Elem<Tipo>* p, Tipo v);
	struct Elem<Tipo>* insert(struct Elem<Tipo>* p, Tipo v);
	struct Elem<Tipo>* remove(struct Elem<Tipo>* p);

	//metodi ausiliari
	//inserisci in testa
	void insert_head(Tipo v);
	//inserisci in coda
	void insert_tail(Tipo v);
	//rimuovi in testa
	struct Elem<Tipo>* remove_head(void);
	//rimuovi in coda
	struct Elem<Tipo>* remove_tail(void);

	//calcola la lunghezza della ListaParent (e serve per non fare errori)
	int lunghezza(void);
	//cerca v scorrendo la ListaParent
	struct Elem<Tipo>* search(Tipo v);

	//stampe
	void print(void);
    void print(string str);
};

#endif //LISTA_PARENT_HPP
