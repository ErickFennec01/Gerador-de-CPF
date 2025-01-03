import random
import tkinter as tk
from tkinter import ttk, messagebox


# Função para gerar os primeiros 9 dígitos do CPF
def gerador_digitos():
    cpf = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    return cpf


# Função para validar ou gerar um CPF
def validador_cpf(escolha, cpf_informado=""):
    cpf = ""

    if escolha == 1:  # Gerar CPF
        cpf = gerador_digitos()
    elif escolha == 2:  # Validar CPF
        cpf = cpf_informado.replace(".", "").replace("-", "")
        if len(cpf) != 11:
            messagebox.showerror("Erro", "O CPF informado é inválido!")
            return None
        cpf = cpf[:9]

    # Cálculo do primeiro dígito
    nove_digitos = cpf[:9]
    somador_1 = sum(int(nove_digitos[i]) * (10 - i) for i in range(9))
    digito1 = (somador_1 * 10) % 11
    digito1 = digito1 if digito1 < 10 else 0
    cpf += str(digito1)

    # Cálculo do segundo dígito
    dez_digitos = cpf[:10]
    somador_2 = sum(int(dez_digitos[i]) * (11 - i) for i in range(10))
    digito2 = (somador_2 * 10) % 11
    digito2 = digito2 if digito2 < 10 else 0
    cpf += str(digito2)

    # Formatar o CPF
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    if escolha == 1:
        return cpf_formatado
    elif escolha == 2:
        if cpf_informado.replace(".", "").replace("-", "") == cpf:
            return f"O CPF {cpf_formatado} é válido! ✅"
        else:
            return f"O CPF {cpf_informado} é inválido! ❌"


# Função para ação de gerar CPF
def gerar_cpf():
    cpf_gerado = validador_cpf(1)
    if cpf_gerado:
        entry_result.configure(state="normal")
        entry_result.delete(0, tk.END)  # Limpa o campo antes de exibir o novo CPF
        entry_result.insert(0, f'CPF GERADO:{cpf_gerado}✅')  # Insere o CPF gerado na caixa de texto
        entry_result.configure(state="readonly")


# Função para ação de validar CPF
def validar_cpf():
    cpf = entry_cpf.get()
    if not cpf:
        messagebox.showerror("Erro", "Por favor, insira um CPF para validar.")
        return
    resultado = validador_cpf(2, cpf)
    if resultado:
        entry_result.configure(state="normal")
        entry_result.delete(0, tk.END)  # Limpa o campo antes de exibir o resultado
        entry_result.insert(0, resultado)  # Insere o resultado na caixa de texto
        entry_result.configure(state="readonly")


# Criação da interface gráfica
app = tk.Tk()
app.title("Gerador e Validador de CPF")
app.geometry("500x300")
app.configure(bg="#2C2F33")

# Estilo personalizado
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#2C2F33", foreground="#FFFFFF", font=("Arial", 12))
style.configure("TButton", background="#7289DA", foreground="#FFFFFF", font=("Arial", 10, "bold"), padding=6)
style.map("TButton", background=[("active", "#5A73BA")])

# Título
label_title = ttk.Label(app, text="Gerador e Validador de CPF", font=("Arial", 16, "bold"))
label_title.pack(pady=15)

# Campo para entrada do CPF
frame_cpf = ttk.Frame(app)
frame_cpf.pack(pady=10)

label_cpf = ttk.Label(frame_cpf, text="Digite o CPF:")
label_cpf.pack(side=tk.LEFT, padx=5)

entry_cpf = ttk.Entry(frame_cpf, width=30, font=("Arial", 12))
entry_cpf.pack(side=tk.LEFT, padx=5)

btn_validate = ttk.Button(app, text="Validar CPF", command=validar_cpf)
btn_validate.pack(pady=10)

# Botão para gerar CPF
btn_generate = ttk.Button(app, text="Gerar CPF", command=gerar_cpf)
btn_generate.pack(pady=5)

# Campo para exibir resultados (CPF gerado ou validação)
entry_result = ttk.Entry(app, width=40, font=("Arial", 14), justify="center", state="readonly")
entry_result.pack(pady=20)

# Rodapé
footer = ttk.Label(app, text="Desenvolvido com ajuda do gpt", font=("Arial", 10))
footer.pack(side=tk.BOTTOM, pady=5)

# Executar a interface
app.mainloop()
