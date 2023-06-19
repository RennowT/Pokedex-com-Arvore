# Documentação da Pokedex com Árvore Binária em C++

## Introdução
O código apresentado implementa uma Pokedex utilizando uma árvore binária em C++. Essa Pokedex é capaz de inserir, remover, buscar e exibir a lista completa de Pokémon armazenados. A estrutura de dados utilizada para representar um Pokémon é composta por um ID, nome e tipo, sendo cada nó da árvore binária um Pokémon. A árvore é organizada com base nos IDs dos Pokémon, onde os Pokémon com IDs menores são armazenados à esquerda e os Pokémon com IDs maiores são armazenados à direita.

## Funcionalidades
A Pokedex implementada oferece as seguintes funcionalidades:

### 1. Inserir Pokémon
A função `inserirPokemon` permite adicionar um novo Pokémon à Pokedex. Essa função percorre a árvore comparando o ID do Pokémon a ser inserido com o ID do Pokémon no nó atual e decide em qual direção continuar a busca. Caso seja encontrado um nó vazio, o novo Pokémon é inserido como um novo nó na posição correta.

### 2. Remover Pokémon
A função `removerPokemon` permite remover um Pokémon da Pokedex com base no seu ID. Essa função também percorre a árvore comparando o ID do Pokémon a ser removido com o ID do Pokémon no nó atual. Quando o Pokémon é encontrado, diferentes casos são considerados: se o nó não possui filhos, ele é removido diretamente; se o nó possui apenas um filho, esse filho substitui o nó atual; se o nó possui dois filhos, o Pokémon de menor ID da subárvore direita é encontrado e substitui o Pokémon a ser removido.

### 3. Buscar Pokémon
A função `buscarPokemon` permite buscar um Pokémon na Pokedex com base no seu ID. Essa função percorre a árvore de forma semelhante às funções anteriores, comparando o ID do Pokémon buscado com o ID do Pokémon no nó atual. Se o Pokémon for encontrado, o nó correspondente é retornado. Caso contrário, é retornado um ponteiro nulo.

### 4. Exibir Lista Completa
A função `imprimirListaCompleta` percorre a árvore em ordem, visitando primeiro os nós da subárvore esquerda, depois o nó atual e, por fim, os nós da subárvore direita. Isso garante que todos os Pokémon sejam visitados e impressos na ordem correta. Essa função permite exibir a lista completa de todos os Pokémon armazenados na Pokedex.

## Interface do Usuário
A interface do usuário foi implementada em modo de console. Ao executar o programa, é exibido um menu com opções numeradas que permitem interagir com a Pokedex. As opções incluem a inserção, remoção, busca de Pokémon, exibição da lista completa de Pokémon e saída do programa.

## Limpeza da Memória
Ao finalizar o programa, é realizada a limpeza da memória utilizada pela árvore, percorrendo todos os nós e deletando-os um a um. Essa etapa é importante para evitar vazamentos de memória.

## Conclusão
A implementação da Pokedex com uma árvore binária oferece um método eficiente para armazenar, gerenciar e buscar Pokémon. O código foi desenvolvido seguindo práticas de clean code, com comentários explicativos em cada função e uma documentação clara. Essa estrutura de dados proporciona uma organização adequada dos Pokémon, facilitando as operações de inserção, remoção, busca e exibição dos dados.
