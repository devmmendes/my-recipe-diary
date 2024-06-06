import sqlite3 # Importa o módulo sqlite3 para trabalhar com bancos de dados SQLite.
import tkinter as tk # Importa o módulo tkinter e o renomeia como tk.
from tkinter import messagebox # Importa a classe messagebox do módulo tkinter.
from tkinter import ttk # Importa o módulo ttk do tkinter para criar widgets temáticos.

# Função para carregar as receitas do banco de dados.
def load_recipes():
    conn = sqlite3.connect("database/recipes.db") # Conecta ao banco de dados recipes.db.
    c = conn.cursor()  # Cria um cursor para executar comandos SQL.
    c.execute("SELECT rowid, name FROM recipes") # Executa uma consulta SQL para selecionar os IDs e nomes das receitas.
    rows = c.fetchall() # Recupera todas as linhas retornadas pela consulta.
    conn.close() # Fecha a conexão com o banco de dados.
    return rows # Retorna as linhas recuperadas.

# Função para exibir os detalhes de uma receita selecionada.
def show_recipe_details(event): 
    global selected_recipe_id # Declara a variável global selected_recipe_id.
    selected_item = recipe_list.focus() # Obtém o item selecionado na Treeview.
    if selected_item:
        selected_recipe_id = recipe_list.item(selected_item)["values"][0] # Obtém o ID da receita selecionada.
        conn = sqlite3.connect("database/recipes.db") # Conecta ao banco de dados recipes.db.
        c = conn.cursor() # Cria um cursor para executar comandos SQL
        c.execute("SELECT * FROM recipes WHERE rowid=?", (selected_recipe_id,)) # Executa uma consulta SQL para selecionar os detalhes da receita com base no ID.
        recipe = c.fetchone() # Executa uma consulta SQL para selecionar os detalhes da receita com base no ID.
        conn.close() # Fecha a conexão com o banco de dados.
        if recipe: # Verifica se a receita existe.
            details_text.config(state=tk.NORMAL) # Configura o campo de texto para ser editável.
            details_text.delete("1.0", tk.END) # Limpa o campo de texto.
            details_text.insert(tk.END, f"Name: {recipe[0]}\n\n") # Insere o nome da receita no campo de texto.
            details_text.insert(tk.END, f"Ingredients:\n{recipe[1]}\n\n") # Insere os ingredientes da receita no campo de texto.
            details_text.insert(tk.END, f"Preparation Mode:\n{recipe[2]}\n") # Insere o modo de preparo da receita no campo de texto.
            details_text.config(state=tk.DISABLED) # Configura o campo de texto para ser somente leitura.
        else:
            details_text.config(state=tk.NORMAL) # Configura o campo de texto para ser editável.
            details_text.delete("1.0", tk.END) # Limpa o campo de texto.
            details_text.config(state=tk.DISABLED) # Configura o campo de texto para ser somente leitura.

# Função para excluir a receita selecionada.
def delete_recipe(): # Declara a variável global selected_recipe_id.
    global selected_recipe_id # Verifica se há uma receita selecionada.
    if selected_recipe_id is not None: # Conecta ao banco de dados recipes.db.
        conn = sqlite3.connect("database/recipes.db") # Cria um cursor para executar comandos SQL.
        c = conn.cursor() # Executa uma consulta SQL para excluir a receita com base no ID.
        c.execute("DELETE FROM recipes WHERE rowid=?", (selected_recipe_id,)) # Executa uma consulta SQL para excluir a receita com base no ID.
        conn.commit() # Salva as alterações no banco de dados.
        conn.close() # Fecha a conexão com o banco de dados.
        messagebox.showinfo("Deleted", "Recipe deleted successfully!") # Exibe uma mensagem informativa.
        refresh_recipes() #Atualiza a lista de receitas.


# Função para atualizar a lista de receitas.
def refresh_recipes(): 
    global selected_recipe_id  # Declara a variável global selected_recipe_id.
    selected_recipe_id = None  # Reinicializa o ID da receita selecionada como None.
    for item in recipe_list.get_children():  # Itera sobre todos os itens na Treeview.
        recipe_list.delete(item)  # Deleta cada item da Treeview.
    recipes = load_recipes()  # Carrega as receitas do banco de dados.
    for row in recipes:  # Itera sobre cada receita carregada.
        recipe_list.insert("", tk.END, values=row)  # Insere cada receita na Treeview.
    details_text.config(state=tk.NORMAL)  # Configura o campo de texto para ser editável.
    details_text.delete("1.0", tk.END)  # Limpa o campo de texto.
    details_text.config(state=tk.DISABLED)  # Configura o campo de texto para ser somente leitura. 

# Função para exibir o menu de contexto.
def show_context_menu(event):
    selected_item = recipe_list.identify_row(event.y)  # Identifica o item selecionado na Treeview.
    if selected_item:  # Verifica se há um item selecionado.
        recipe_list.selection_set(selected_item)  # Define o item selecionado na Treeview.
        context_menu.post(event.x_root, event.y_root)  # Exibe o menu de contexto na posição do cursor.

# Função para inicializar a interface de visualização de receitas.
def initiate_menu():
    global recipe_list, details_text, context_menu, selected_recipe_id  # Declara as variáveis globais necessárias.

    selected_recipe_id = None  # Inicializa o ID da receita selecionada como None.

    root = tk.Tk()  # Inicializa a janela principal.
    root.title("My Recipes")  # Define o título da janela.

    recipe_list = ttk.Treeview(root, columns=("ID", "Name"), show="headings")  # Cria a Treeview para exibir as receitas.
    recipe_list.heading("ID", text="ID")  # Define o cabeçalho da coluna ID.
    recipe_list.heading("Name", text="Name")  # Define o cabeçalho da coluna Name.
    recipe_list.column("ID", width=30)  # Define a largura da coluna ID.
    recipe_list.column("Name", width=200)  # Define a largura da coluna Name.
    recipe_list.pack(pady=10, padx=10)  # Empacota a Treeview na janela.
    recipe_list.bind("<<TreeviewSelect>>", show_recipe_details)  # Associa a função show_recipe_details ao evento de seleção de item na Treeview.
    recipe_list.bind("<Button-3>", show_context_menu)  # Associa a função show_context_menu ao evento de clique do botão direito do mouse.

    details_text = tk.Text(root, width=60, height=20, state=tk.DISABLED)  # Cria o campo de texto para exibir os detalhes da receita.
    details_text.pack(pady=10, padx=10)  # Empacota o campo de texto na janela.

    context_menu = tk.Menu(root, tearoff=0)  # Cria o menu de contexto.
    context_menu.add_command(label="Delete Recipe", command=delete_recipe)  # Adiciona uma opção para excluir a receita ao menu de contexto.

    close_button = tk.Button(root, text="Close", command=lambda: (root.destroy(), main_menu()))  # Cria um botão para fechar a janela.
    close_button.pack(pady=10)  # Empacota o botão na janela.

    refresh_recipes()  # Chama a função para atualizar a lista de receitas.

    # Centralizar a janela na tela
    root.update_idletasks()  # Atualiza a interface gráfica da janela.
    width = root.winfo_width()  # Obtém a largura da janela.
    height = root.winfo_height()  # Obtém a altura da janela.
    x = (root.winfo_screenwidth() // 2) - (width // 2)  # Calcula a posição horizontal da janela.
    y = (root.winfo_screenheight() // 2) - (height // 2)  # Calcula a posição vertical da janela.
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # Define a geometria da janela.

    root.mainloop()  # Inicia o loop principal da interface gráfica.

# Função para retornar ao menu principal
def main_menu():
    import main_menu  # Import