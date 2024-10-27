import customtkinter as tk
import webAction

tk.set_appearance_mode("dark")  # Modes: system (default), light, dark
tk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = tk.CTk()  # create CTk window like you do with the Tk window
app.geometry("500x450")
app.title("Web Assistant Kit V 0.1.0")


def button_function():
    print("button pressed")

# # Use CTkButton instead of tkinter Button
# button = tk.CTkButton(master=app, text="CTkButton", command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Frame para o menu lateral
menu_frame = tk.CTkFrame(app, width=180)
menu_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

# Label para o título do menu
menu_label = tk.CTkLabel(menu_frame, text="Funções", font=("Arial", 20))
menu_label.pack(padx=20, pady=20)

# # Canvas para adicionar a rolagem
# canvas = tk.CTkCanvas(menu_frame, width=200, height=300)
# canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
# # Barra de rolagem
# scrollbar = tk.CTkScrollbar(menu_frame, orientation="vertical", command=canvas.yview)
# scrollbar.pack(side="right", fill="both")

# # Frame interno no canvas para inserir itens
# scrollable_frame = tk.CTkFrame(canvas)

# # Configuração do canvas para a barra de rolagem
# scrollable_frame.bind(
#     "<Configure>",
#     lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
# )

# canvas.create_window((0, 0), window=scrollable_frame, anchor="center")
# canvas.configure(yscrollcommand=scrollbar.set)

# Adiciona botões do menu lateral

button = tk.CTkButton(menu_frame, text=f"Buscar")
button.pack(pady=5, padx=5)

button = tk.CTkButton(menu_frame, text=f"Dados")
button.pack(pady=5, padx=5)

button = tk.CTkButton(menu_frame, text=f"Configurações")
button.pack(pady=5, padx=5)

# Frame para o conteúdo principal
content_frame = tk.CTkFrame(app)
content_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Adiciona um label ao conteúdo principal
content_label = tk.CTkLabel(content_frame, text="Conteúdo Principal", font=("Arial", 24))
content_label.pack(pady=20, padx=10)

# Campo de entrada para a URL
url_label = tk.CTkLabel(content_frame, text="URL do site:")
url_label.pack(anchor="w", pady=5, padx=10)
url_entry = tk.CTkEntry(content_frame, width=400)
url_entry.pack(pady=5, padx=10)

# Campo de entrada para o nome
name_label = tk.CTkLabel(content_frame, text="Nome:")
name_label.pack(anchor="w", pady=5, padx=10)
name_entry = tk.CTkEntry(content_frame, width=400)
name_entry.pack(pady=5, padx=10)

# Campo de entrada para o email
email_label = tk.CTkLabel(content_frame, text="Email:")
email_label.pack(anchor="w", pady=5, padx=10)
email_entry = tk.CTkEntry(content_frame, width=400)
email_entry.pack(pady=5, padx=10)

# Botão para varrer e preencher o formulário
scan_button = tk.CTkButton(content_frame, text="Varredura e Preenchimento", command="webAction.fill_form")
scan_button.pack(pady=20, padx=10)



app.mainloop()