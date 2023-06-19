// Autor: Matheus Renó Torres
// Data: 19 de junho de 2023

/*
  Documentação da Pokedex com Árvore Binária em C++

  Introdução:
  O código apresentado implementa uma Pokedex utilizando uma árvore binária em C++. 
  Essa Pokedex é capaz de inserir, remover, buscar e exibir a lista completa de Pokémon armazenados. 
  A estrutura de dados utilizada para representar um Pokémon é composta por um ID, nome e tipo, sendo cada nó da árvore
  binária um Pokémon. A árvore é organizada com base nos IDs dos Pokémon, onde os Pokémon com IDs menores são armazenados
  à esquerda e os Pokémon com IDs maiores são armazenados à direita.

  Funcionalidades:
  - Inserir Pokémon:
    A função 'inserirPokemon' permite adicionar um novo Pokémon à Pokedex. Essa função percorre a árvore comparando o ID 
    do Pokémon a ser inserido com o ID do Pokémon no nó atual e decide em qual direção continuar a busca. Caso seja 
    encontrado um nó vazio, o novo Pokémon é inserido como um novo nó na posição correta.

  - Remover Pokémon:
    A função 'removerPokemon' permite remover um Pokémon da Pokedex com base no seu ID. Essa função também percorre a árvore
    comparando o ID do Pokémon a ser removido com o ID do Pokémon no nó atual. Quando o Pokémon é encontrado, diferentes 
    casos são considerados: se o nó não possui filhos, ele é removido diretamente; se o nó possui apenas um filho, esse 
    filho substitui o nó atual; se o nó possui dois filhos, o Pokémon de menor ID da subárvore direita é encontrado e 
    substitui o Pokémon a ser removido.

  - Buscar Pokémon:
    A função 'buscarPokemon' permite buscar um Pokémon na Pokedex com base no seu ID. Essa função percorre a árvore de forma
    semelhante às funções anteriores, comparando o ID do Pokémon buscado com o ID do Pokémon no nó atual. Se o Pokémon for
    encontrado, o nó correspondente é retornado. Caso contrário, é retornado um ponteiro nulo.

  - Exibir Lista Completa:
    A função 'imprimirListaCompleta' percorre a árvore em ordem, visitando primeiro os nós da subárvore esquerda, depois o 
    nó atual e, por fim, os nós da subárvore direita. Isso garante que todos os Pokémon sejam visitados e impressos na 
    ordem correta. Essa função permite exibir a lista completa de todos os Pokémon armazenados na Pokedex.

  Interface do Usuário:
  A interface do usuário foi implementada em modo de console. Ao executar o programa, é exibido um menu com opções numeradas
  que permitem interagir com a Pokedex. As opções incluem a inserção, remoção, busca de Pokémon, exibição da lista completa
  de Pokémon e saída do programa.

  Limpeza da Memória:
  Ao finalizar o programa, é realizada a limpeza da memória utilizada pela árvore, percorrendo todos os nós e deletando-os 
  um a um. Essa etapa é importante para evitar vazamentos de memória.

  Conclusão:
  A implementação da Pokedex com uma árvore binária oferece um método eficiente para armazenar, gerenciar e buscar Pokémon.
  Essa estrutura de dados proporciona uma organização adequada dos Pokémon, facilitando as operações de inserção, remoção,
  busca e exibição dos dados.
*/

#include <iostream>
using namespace std;

// Estrutura de dados para representar um Pokemon
struct Pokemon {
    int id;
    string nome;
    string tipo;
    Pokemon* esquerda;
    Pokemon* direita;

    Pokemon(int _id, string _nome, string _tipo) {
        id = _id;
        nome = _nome;
        tipo = _tipo;
        esquerda = nullptr;
        direita = nullptr;
    }
};

// Função para inserir um Pokemon na Pokedex
Pokemon* inserirPokemon(Pokemon* raiz, int id, string nome, string tipo) {
    if (raiz == nullptr) {
        return new Pokemon(id, nome, tipo);
    } else {
        if (id < raiz->id) {
            raiz->esquerda = inserirPokemon(raiz->esquerda, id, nome, tipo);
        } else {
            raiz->direita = inserirPokemon(raiz->direita, id, nome, tipo);
        }
        return raiz;
    }
}

// Função auxiliar para encontrar o nó mais à esquerda na árvore
Pokemon* encontrarMinimo(Pokemon* no) {
    if (no->esquerda == nullptr) {
        return no;
    }
    return encontrarMinimo(no->esquerda);
}

// Função para remover um Pokemon da Pokedex
Pokemon* removerPokemon(Pokemon* raiz, int id) {
    if (raiz == nullptr) {
        return raiz;
    }

    if (id < raiz->id) {
        raiz->esquerda = removerPokemon(raiz->esquerda, id);
    } else if (id > raiz->id) {
        raiz->direita = removerPokemon(raiz->direita, id);
    } else {
        if (raiz->esquerda == nullptr) {
            Pokemon* temp = raiz->direita;
            delete raiz;
            return temp;
        } else if (raiz->direita == nullptr) {
            Pokemon* temp = raiz->esquerda;
            delete raiz;
            return temp;
        }

        Pokemon* temp = encontrarMinimo(raiz->direita);
        raiz->id = temp->id;
        raiz->nome = temp->nome;
        raiz->tipo = temp->tipo;
        raiz->direita = removerPokemon(raiz->direita, temp->id);
    }

    return raiz;
}

// Função para buscar um Pokemon na Pokedex
Pokemon* buscarPokemon(Pokemon* raiz, int id) {
    if (raiz == nullptr || raiz->id == id) {
        return raiz;
    }

    if (id < raiz->id) {
        return buscarPokemon(raiz->esquerda, id);
    } else {
        return buscarPokemon(raiz->direita, id);
    }
}

// Função para liberar a memória utilizada pela árvore
void limparMemoria(Pokemon* raiz) {
    if (raiz != nullptr) {
        limparMemoria(raiz->esquerda);
        limparMemoria(raiz->direita);
        delete raiz;
    }
}

// Função auxiliar para imprimir um Pokemon
void imprimirPokemon(Pokemon* pokemon) {
    cout << "ID: " << pokemon->id << ", Nome: " << pokemon->nome << ", Tipo: " << pokemon->tipo << endl;
}

// Função para imprimir a lista completa de todos os Pokémon na Pokedex
void imprimirListaCompleta(Pokemon* raiz) {
    if (raiz != nullptr) {
        imprimirListaCompleta(raiz->esquerda);
        imprimirPokemon(raiz);
        imprimirListaCompleta(raiz->direita);
    }
}

// Função auxiliar para exibir o menu e obter a opção do usuário
char exibirMenu() {
    char opcao;
    cout << endl;
    cout << "Escolha uma opção:" << endl;
    cout << "1. Inserir Pokemon" << endl;
    cout << "2. Remover Pokemon" << endl;
    cout << "3. Buscar Pokemon" << endl;
    cout << "4. Imprimir lista completa" << endl;
    cout << "5. Sair" << endl;
    cout << "Opção: ";
    cin >> opcao;
    return opcao;
}

int main() {
    Pokemon* pokedex = nullptr;

    char opcao;
    do {
        opcao = exibirMenu();

        switch (opcao) {
            case '1': {
                int id;
                string nome, tipo;
                cout << "Informe o ID do Pokemon: ";
                cin >> id;
                cout << "Informe o nome do Pokemon: ";
                cin.ignore();
                getline(cin, nome);
                cout << "Informe o tipo do Pokemon: ";
                getline(cin, tipo);
                pokedex = inserirPokemon(pokedex, id, nome, tipo);
                cout << "Pokemon inserido na Pokedex." << endl;
                break;
            }
            case '2': {
                int id;
                cout << "Informe o ID do Pokemon a ser removido: ";
                cin >> id;
                pokedex = removerPokemon(pokedex, id);
                cout << "Pokemon com ID " << id << " removido." << endl;
                break;
            }
            case '3': {
                int id;
                cout << "Informe o ID do Pokemon a ser buscado: ";
                cin >> id;
                Pokemon* pokemonEncontrado = buscarPokemon(pokedex, id);
                if (pokemonEncontrado != nullptr) {
                    cout << "Pokemon encontrado: ";
                    imprimirPokemon(pokemonEncontrado);
                } else {
                    cout << "Pokemon com ID " << id << " não encontrado." << endl;
                }
                break;
            }
            case '4':
                cout << "Lista completa de Pokemons:" << endl;
                imprimirListaCompleta(pokedex);
                break;
            case '5':
                cout << "Encerrando o programa." << endl;
                break;
            default:
                cout << "Opção inválida. Tente novamente." << endl;
        }
    } while (opcao != '5');

    // Limpar a memória utilizada pela árvore
    limparMemoria(pokedex);

    return 0;
}
