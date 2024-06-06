# Diario de receitas digital.
import tkinter as tk  # Importa o módulo tkinter e o renomeia como tk.

import add_recipes  # Importa o script add_recipes.py.
import my_recipes   # Importa o script my_recipes.py.

# Variaveis globais.
root = None  # Define a variável global root como None.

# Funções
def open_recipes():
    root.destroy()       # Destroi a janela atual.
    my_recipes.initiate_menu()  # Inicia o menu de receitas.

def open_add_recipes():
    root.destroy()       # Destroi a janela atual.
    add_recipes.initiate_menu()  # Inicia o menu de adição de receitas.

def initiate_menu():
    global root   # Declara root como variável global.

    root = tk.Tk()   # Inicia uma instância da classe Tk() e atribui a root.
    root.title("Main Menu")  # Define o título da janela como "Main Menu".

    btn_my_recipes = tk.Button(root, text="My Recipes", command=open_recipes)  # Cria um botão com o texto "My Recipes" que, quando clicado, chama a função open_recipes().
    btn_my_recipes.pack(pady=10)  # Empacota o botão na janela com um espaço de 10 pixels no eixo y.

    btn_add_recipes = tk.Button(root, text="Add Recipes", command=open_add_recipes)  # Cria um botão com o texto "Add Recipes" que, quando clicado, chama a função open_add_recipes().
    btn_add_recipes.pack(pady=10)  # Empacota o botão na janela com um espaço de 10 pixels no eixo y.

    btn_exit = tk.Button(root, text="Exit", command=root.destroy)  # Cria um botão com o texto "Exit" que, quando clicado, destroi a janela root.
    btn_exit.pack(pady=10)  # Empacota o botão na janela com um espaço de 10 pixels no eixo y.

    root.mainloop()  # Inicia o loop principal do tkinter para exibir a janela.

if __name__ == "__main__":
    initiate_menu()  # Se o script for executado diretamente, chama a função initiate_menu().
