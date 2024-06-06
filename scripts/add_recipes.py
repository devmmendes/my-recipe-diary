import sqlite3  # Importa o módulo sqlite3 para trabalhar com bancos de dados SQLite.
import tkinter as tk  # Importa o módulo tkinter e o renomeia como tk.
from tkinter import messagebox  # Importa a classe messagebox do módulo tkinter.

# Função para adicionar uma nova receita ao banco de dados.
def add_recipe():
    global entry_name, text_ingredients, text_preparation_mode  # Declaração das variáveis globais.

    # Banco de dados para as receitas.
    conn = sqlite3.connect("database/recipes.db")  # Conecta ao banco de dados recipes.db no diretório database.
    c = conn.cursor()  # Cria um cursor para executar comandos SQL.

    # Criar a tabela se ainda não existir.
    c.execute('''
              CREATE TABLE IF NOT EXISTS recipes (
              name text,
              ingredients text,
              preparation_mode text)'''
              )  # Cria a tabela recipes se ela ainda não existir.

    # Obter os valores dos campos de texto.
    name = entry_name.get()  # Obtém o texto inserido no campo de entrada entry_name.
    ingredients = text_ingredients.get("1.0", tk.END)  # Obtém o texto inserido no campo de texto text_ingredients.
    preparation_mode = text_preparation_mode.get("1.0", tk.END)  # Obtém o texto inserido no campo de texto text_preparation_mode.

    # Verificar se todos os campos foram preenchidos.
    if not (name and ingredients.strip() and preparation_mode.strip()):
        messagebox.showwarning("Empty Fields", "Please fill in all fields!")  # Mostra um aviso se algum campo estiver vazio.
        return

    # Adicionar a receita ao banco de dados.
    c.execute("INSERT INTO recipes (name, ingredients, preparation_mode) VALUES (?, ?, ?)", (name, ingredients, preparation_mode))  # Insere os dados na tabela recipes.
    conn.commit()  # Salva as alterações no banco de dados.

    # Fechar a conexão com o banco de dados.
    conn.close()

    # Limpar os campos de texto após adicionar a receita.
    entry_name.delete(0, tk.END)  # Limpa o campo de entrada entry_name.
    text_ingredients.delete("1.0", tk.END)  # Limpa o campo de texto text_ingredients.
    text_preparation_mode.delete("1.0", tk.END)  # Limpa o campo de texto text_preparation_mode.

    # Exibir uma mensagem de confirmação.
    messagebox.showinfo("Success", "Recipe added successfully!")  # Mostra uma mensagem informando que a receita foi adicionada com sucesso.

# Função para cancelar e retornar ao menu inicial.
def cancel_add():
    root.destroy()  # Fecha a janela atual.
    from main_menu import initiate_menu as main_menu  # Importa a função initiate_menu do main_menu.py.
    main_menu()     # Chama a função initiate_menu para retornar ao menu principal.

# Função para inicializar a interface de adicionar receitas.
def initiate_menu():
    global entry_name, text_ingredients, text_preparation_mode, root  # Declaração das variáveis globais.

    root = tk.Tk()  # Inicia uma instância da classe Tk() e atribui a root.
    root.title("Add Recipe")  # Define o título da janela como "Add Recipe".

    # Label e Entry para o nome da receita.
    label_name = tk.Label(root, text="Recipe Name:")  # Cria um rótulo com o texto "Recipe Name:".
    label_name.grid(row=0, column=0, padx=10, pady=5, sticky="W")  # Posiciona o rótulo na janela.

    entry_name = tk.Entry(root, width=50)  # Cria um campo de entrada para o nome da receita.
    entry_name.grid(row=0, column=1, padx=10, pady=5, sticky="W")  # Posiciona o campo de entrada na janela.

    # Label e Text para os ingredientes.
    label_ingredients = tk.Label(root, text="Ingredients:")  # Cria um rótulo com o texto "Ingredients:".
    label_ingredients.grid(row=1, column=0, padx=10, pady=5, sticky="W")  # Posiciona o rótulo na janela.

    text_ingredients = tk.Text(root, width=50, height=10)  # Cria um campo de texto para os ingredientes.
    text_ingredients.grid(row=1, column=1, padx=10, pady=5, sticky="W")  # Posiciona o campo de texto na janela.

    # Label e Text para o modo de preparo.
    label_preparation_mode = tk.Label(root, text="Preparation Mode:")  # Cria um rótulo com o texto "Preparation Mode:".
    label_preparation_mode.grid(row=2, column=0, padx=10, pady=5, sticky="W")  # Posiciona o rótulo na janela.

    text_preparation_mode = tk.Text(root, width=50, height=10)  # Cria um campo de texto para o modo de preparo.
    text_preparation_mode.grid(row=2, column=1, padx=10, pady=5, sticky="W")  # Posiciona o campo de texto na janela.

    # Botão para adicionar a receita.
    btn_add = tk.Button(root, text="Add Recipe", command=add_recipe)  # Cria um botão com o texto "Add Recipe" que, quando clicado, chama a função add_recipe().
    btn_add.grid(row=3, column=0, padx=10, pady=10, sticky="W")  # Posiciona o botão na janela.

    # Botão para cancelar e retornar ao menu principal.
    btn_cancel = tk.Button(root, text="Return", command=cancel_add)  # Cria um botão com o texto "Return" que, quando clicado, chama a função cancel_add().
    btn_cancel.grid(row=3, column=1, padx=10, pady=10, sticky="E")  # Posiciona o botão na janela.

    root.mainloop()  # Inicia o loop principal do tkinter para exibir a janela.

if __name__ == "__main__":
    initiate_menu()  # Se o script for executado diretamente, chama a função initiate_menu().
