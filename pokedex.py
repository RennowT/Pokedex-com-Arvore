import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np


class Pokemon:
    def __init__(self, id, nome, tipo):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.esquerda = None
        self.direita = None


class Pokedex:
    def __init__(self):
        self.raiz = None

    def adicionar_pokemon(self, pokemon):
        if self.raiz is None:
            self.raiz = pokemon
        else:
            self._adicionar_pokemon(self.raiz, pokemon)

    def _adicionar_pokemon(self, no_atual, novo_pokemon):
        if novo_pokemon.id < no_atual.id:
            if no_atual.esquerda is None:
                no_atual.esquerda = novo_pokemon
            else:
                self._adicionar_pokemon(no_atual.esquerda, novo_pokemon)
        else:
            if no_atual.direita is None:
                no_atual.direita = novo_pokemon
            else:
                self._adicionar_pokemon(no_atual.direita, novo_pokemon)

    def remover_pokemon(self, id_pokemon):
        self.raiz = self._remover_pokemon(self.raiz, id_pokemon)

    def _remover_pokemon(self, no_atual, id_pokemon):
        if no_atual is None:
            return None
        if id_pokemon < no_atual.id:
            no_atual.esquerda = self._remover_pokemon(no_atual.esquerda, id_pokemon)
        elif id_pokemon > no_atual.id:
            no_atual.direita = self._remover_pokemon(no_atual.direita, id_pokemon)
        else:
            if no_atual.esquerda is None:
                return no_atual.direita
            elif no_atual.direita is None:
                return no_atual.esquerda
            else:
                substituto = self._encontrar_minimo(no_atual.direita)
                no_atual.id = substituto.id
                no_atual.nome = substituto.nome
                no_atual.tipo = substituto.tipo
                no_atual.direita = self._remover_pokemon(no_atual.direita, substituto.id)
        return no_atual

    def _encontrar_minimo(self, no_atual):
        while no_atual.esquerda is not None:
            no_atual = no_atual.esquerda
        return no_atual

    def buscar_por_indice(self, id_pokemon):
        return self._buscar_por_indice(self.raiz, id_pokemon)

    def _buscar_por_indice(self, no_atual, id_pokemon):
        if no_atual is None or no_atual.id == id_pokemon:
            return no_atual
        if id_pokemon < no_atual.id:
            return self._buscar_por_indice(no_atual.esquerda, id_pokemon)
        return self._buscar_por_indice(no_atual.direita, id_pokemon)

    def buscar_por_nome(self, nome_pokemon):
        resultados = []
        self._buscar_por_nome(self.raiz, nome_pokemon, resultados)
        return resultados

    def _buscar_por_nome(self, no_atual, nome_pokemon, resultados):
        if no_atual is None:
            return
        if nome_pokemon.lower() in no_atual.nome.lower():
            resultados.append(no_atual)
        self._buscar_por_nome(no_atual.esquerda, nome_pokemon, resultados)
        self._buscar_por_nome(no_atual.direita, nome_pokemon, resultados)

    def buscar_por_tipo(self, tipo_pokemon):
        resultados = []
        self._buscar_por_tipo(self.raiz, tipo_pokemon, resultados)
        return resultados

    def _buscar_por_tipo(self, no_atual, tipo_pokemon, resultados):
        if no_atual is None:
            return
        if tipo_pokemon.lower() in no_atual.tipo.lower():
            resultados.append(no_atual)
        self._buscar_por_tipo(no_atual.esquerda, tipo_pokemon, resultados)
        self._buscar_por_tipo(no_atual.direita, tipo_pokemon, resultados)

    def percorrer_in_order(self):
        resultados = []
        self._percorrer_in_order(self.raiz, resultados)
        return resultados

    def _percorrer_in_order(self, no_atual, resultados):
        if no_atual is not None:
            self._percorrer_in_order(no_atual.esquerda, resultados)
            resultados.append(no_atual)
            self._percorrer_in_order(no_atual.direita, resultados)


def criar_pokemon():
    id = int(id_entry.get())
    nome = nome_entry.get()
    tipo = tipo_entry.get()
    pokemon = Pokemon(id, nome, tipo)
    dex.adicionar_pokemon(pokemon)
    preencher_treeview(dex.percorrer_in_order())
    plotar_arvore(dex.raiz)


def remover_pokemon():
    id = int(id_entry.get())
    dex.remover_pokemon(id)
    preencher_treeview(dex.percorrer_in_order())
    plotar_arvore(dex.raiz)


def buscar_pokemon():
    id = int(busca_entry.get())
    pokemon = dex.buscar_por_indice(id)
    if pokemon:
        resultado_label.config(text=f"ID: {pokemon.id}, Nome: {pokemon.nome}, Tipo: {pokemon.tipo}")
    else:
        resultado_label.config(text="Nenhum Pokémon encontrado.")


def buscar_por_tipo():
    tipo = tipo_entry.get()
    resultados = dex.buscar_por_tipo(tipo)
    if resultados:
        resultado_text = ""
        for pokemon in resultados:
            resultado_text += f"ID: {pokemon.id}, Nome: {pokemon.nome}, Tipo: {pokemon.tipo}\n"
        resultado_label.config(text=resultado_text)
    else:
        resultado_label.config(text="Nenhum Pokémon encontrado.")


def preencher_treeview(pokemons):
    for i in treeview.get_children():
        treeview.delete(i)
    for pokemon in pokemons:
        treeview.insert("", "end", values=(pokemon.id, pokemon.nome, pokemon.tipo))


def plotar_arvore(raiz):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_axis_off()
    tree_pos = generate_tree_positions(raiz)
    draw_tree(raiz, tree_pos, ax)
    plt.tight_layout()
    plt.savefig("pokedex_tree.png")
    plt.close()
    image = tk.PhotoImage(file="pokedex_tree.png")
    tree_image.configure(image=image)
    tree_image.image = image


def generate_tree_positions(raiz):
    tree_pos = {}

    def traverse(node, level, pos, h_gap):
        if node:
            traverse(node.esquerda, level + 1, pos - h_gap, h_gap / 2)
            traverse(node.direita, level + 1, pos + h_gap, h_gap / 2)
            tree_pos[node] = (level, pos)

    traverse(raiz, 0, 0, 4)
    return tree_pos


def draw_tree(raiz, tree_pos, ax):
    if raiz:
        level, pos = tree_pos[raiz]
        ax.annotate(
            raiz.id,
            xy=(pos, -level),
            xytext=(0, 4),
            textcoords="offset points",
            ha="center",
            va="center",
            bbox=dict(boxstyle="circle,pad=0.3", fc="white", ec="black"),
        )
        if raiz.esquerda:
            left_pos = tree_pos[raiz.esquerda][1]
            ax.plot([pos, left_pos], [-level, -(level + 1)], "k-")
            draw_tree(raiz.esquerda, tree_pos, ax)
        if raiz.direita:
            right_pos = tree_pos[raiz.direita][1]
            ax.plot([pos, right_pos], [-level, -(level + 1)], "k-")
            draw_tree(raiz.direita, tree_pos, ax)


dex = Pokedex()

root = tk.Tk()
root.title("Pokédex")

# Criando widgets
id_label = ttk.Label(root, text="ID:")
nome_label = ttk.Label(root, text="Nome:")
tipo_label = ttk.Label(root, text="Tipo:")
id_entry = ttk.Entry(root)
nome_entry = ttk.Entry(root)
tipo_entry = ttk.Entry(root)
criar_button = ttk.Button(root, text="Adicionar Pokémon", command=criar_pokemon)
remover_button = ttk.Button(root, text="Remover Pokémon", command=remover_pokemon)
busca_label = ttk.Label(root, text="Buscar por ID:")
busca_entry = ttk.Entry(root)
busca_button = ttk.Button(root, text="Buscar", command=buscar_pokemon)
busca_tipo_label = ttk.Label(root, text="Buscar por Tipo:")
busca_tipo_entry = ttk.Entry(root)
busca_tipo_button = ttk.Button(root, text="Buscar", command=buscar_por_tipo)
resultado_label = ttk.Label(root, text="")
treeview = ttk.Treeview(root, columns=("ID", "Nome", "Tipo"), show="headings")
treeview.heading("ID", text="ID")
treeview.heading("Nome", text="Nome")
treeview.heading("Tipo", text="Tipo")
tree_scrollbar = ttk.Scrollbar(root, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=tree_scrollbar.set)
tree_image = ttk.Label(root)

# Posicionando widgets
id_label.grid(row=0, column=0, sticky="e")
nome_label.grid(row=1, column=0, sticky="e")
tipo_label.grid(row=2, column=0, sticky="e")
id_entry.grid(row=0, column=1, sticky="w")
nome_entry.grid(row=1, column=1, sticky="w")
tipo_entry.grid(row=2, column=1, sticky="w")
criar_button.grid(row=3, column=1, pady=10)
remover_button.grid(row=4, column=1, pady=10)
busca_label.grid(row=5, column=0, sticky="e")
busca_entry.grid(row=5, column=1, sticky="w")
busca_button.grid(row=6, column=1, pady=10)
busca_tipo_label.grid(row=7, column=0, sticky="e")
busca_tipo_entry.grid(row=7, column=1, sticky="w")
busca_tipo_button.grid(row=8, column=1, pady=10)
resultado_label.grid(row=9, column=1, pady=10)
treeview.grid(row=0, column=2, rowspan=10, padx=10, pady=10, sticky="nsew")
tree_scrollbar.grid(row=0, column=3, rowspan=10, sticky="ns")
tree_image.grid(row=10, column=0, columnspan=4)

# Configurando redimensionamento
root.grid_rowconfigure(9, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()
