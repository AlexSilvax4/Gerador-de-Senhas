import string
import random
import tkinter as tk
from tkinter import messagebox
import pyperclip

# Conjunto de caracteres possíveis
CARACTERES = string.ascii_letters + string.digits + string.punctuation

# Função para gerar a senha
def gerar_senha(tamanho: int) -> str:
    return ''.join(random.choice(CARACTERES) for _ in range(tamanho))

# Função para avaliar a força da senha
def avaliar_forca(senha: str) -> str:
    comprimento = len(senha)
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    tem_simbolo = any(c in string.punctuation for c in senha)

    pontuacao = sum([tem_maiuscula, tem_minuscula, tem_numero, tem_simbolo])

    if comprimento < 8:
        return "Fraca"
    elif pontuacao >= 3 and comprimento >= 12:
        return "Forte"
    else:
        return "Média"

# Função acionada ao clicar no botão
def ao_clicar():
    try:
        comprimento = int(entry_tamanho.get())
        senha = gerar_senha(comprimento)
        resultado_var.set(senha)
        pyperclip.copy(senha)

        forca = avaliar_forca(senha)
        label_forca.config(text=f"Força da senha: {forca}")

        messagebox.showinfo("Senha copiada", "Senha gerada e copiada com sucesso!")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido para o tamanho.")

# Criando a interface gráfica
janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("400x250")
janela.resizable(False, False)

# Campo para o tamanho da senha
tk.Label(janela, text="Tamanho da senha:").pack(pady=5)
entry_tamanho = tk.Entry(janela)
entry_tamanho.pack()

# Botão de gerar senha
tk.Button(janela, text="Gerar Senha", command=ao_clicar).pack(pady=10)

# Exibição da senha gerada
resultado_var = tk.StringVar()
tk.Entry(janela, textvariable=resultado_var, width=30).pack()

# Exibição da força da senha
label_forca = tk.Label(janela, text="Força da senha: ")
label_forca.pack(pady=10)

# Iniciar a janela
janela.mainloop()
