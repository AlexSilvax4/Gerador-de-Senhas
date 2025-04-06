# 🔐 Gerador de Senhas Aleatórias

Projeto simples de gerador de senhas com interface gráfica usando **Python + Tkinter**.  
Ideal para criar senhas fortes e seguras com apenas um clique.

---

## ⚙️ Tecnologias e Bibliotecas Usadas

- **Python** – linguagem principal do projeto.
- **Tkinter** – biblioteca nativa para criação de interfaces gráficas.
- **random** – para gerar senhas aleatórias com segurança.
- **string** – para acessar conjuntos prontos de caracteres (letras, números e símbolos).
- **pyperclip** – para copiar automaticamente a senha gerada para a área de transferência.

---

## ✨ Funcionalidades

- 🔒 Geração de senhas com letras, números e símbolos
- 🖼️ Interface gráfica intuitiva com Tkinter
- 🧠 Teste de força da senha (Fraca, Média ou Forte)
- 📋 Cópia automática da senha para a área de transferência
- ⚠️ Validação de entrada para evitar erros

---

## 📷 Capturas de Tela e Explicações

### 📚 Importação de Bibliotecas
<img src="https://github.com/user-attachments/assets/d1efd42a-68e3-4c2f-ba63-7c020f2cef78" width="500"/>

- **string**: Fornece constantes como letras (ascii_letters), números (digits) e símbolos (punctuation) que serão usadas na senha.
- **random**: Utilizada para escolher caracteres aleatórios durante a criação da senha.
- **tkinter**: Biblioteca nativa do Python para criar janelas gráficas.
- **messagebox**: Submódulo do tkinter para exibir mensagens pop-up (alertas, erros).
- **pyperclip**: Permite copiar a senha gerada automaticamente para a área de transferência.

### 🧩 Definição do Conjunto de Caracteres
<img src="https://github.com/user-attachments/assets/2a97983b-295f-4d0b-8bf7-cae48fa95b28" width="500"/>

- Letras maiúsculas e minúsculas (ascii_letters)
- Dígitos de 0 a 9 (digits)
- Símbolos especiais como @, #, !, etc. (punctuation)

### 🔄 Função `gerar_senha`
<img src="https://github.com/user-attachments/assets/2fc60eab-7bd4-4f28-917f-9afc4068632d" width="500"/>

- **Parâmetro**: `tamanho` – número de caracteres desejados.
- Usa uma list comprehension para escolher um caractere aleatório da variável `CARACTERES` para cada posição da senha.
- `random.choice(CARACTERES)` escolhe um caractere aleatório.
- `''.join(...)` transforma a lista em uma única string (a senha final).

### 🛡️ Função `avaliar_forca`
<img src="https://github.com/user-attachments/assets/29a7ca35-2867-4515-91bb-5f38cf5858b4" width="500"/>

- Mede a "qualidade" da senha com base em critérios como presença de letras maiúsculas, minúsculas, números e símbolos.

<img src="https://github.com/user-attachments/assets/0dc4ff4a-f972-4ddd-9eef-73fff0f7ce97" width="500"/>

- A variável `pontuacao` soma quantos desses critérios a senha cumpre:

<img src="https://github.com/user-attachments/assets/7a892a37-72ba-48fe-a5ff-fe97d55bf802" width="500"/>

- Avalia a força:

<img src="https://github.com/user-attachments/assets/44f0f71d-bb2b-44ae-ab40-a87e18817d09" width="500"/>

### 🖱️ Função `ao_clicar`
<img src="https://github.com/user-attachments/assets/65708cfb-a13a-45b3-a33d-b5d8256f0276" width="500"/>

- É executada quando o botão “Gerar Senha” é pressionado.
- Converte a entrada do usuário em inteiro:

<img src="https://github.com/user-attachments/assets/6cb87095-d194-4fc0-8452-03a6f75d661a" width="500"/>

- Gera a senha, exibe na interface e copia para a área de transferência:

<img src="https://github.com/user-attachments/assets/f2b72a6c-2e6e-464f-982d-6d9f31768cc3" width="500"/>

- Avalia a força da senha e mostra na interface:

<img src="https://github.com/user-attachments/assets/4dfe142e-1a49-4bcf-8639-7380cdce3c8b" width="500"/>

- Mostra uma mensagem de confirmação:

<img src="https://github.com/user-attachments/assets/a00c05e8-2ba1-4f52-9034-53dd55c12510" width="500"/>

- Caso o usuário digite algo que não seja número, mostra um erro:

<img src="https://github.com/user-attachments/assets/b2c5f2c6-badd-467c-898b-ea0bfa86f7ef" width="500"/>

---

## 🚀 Como Usar

```bash
git clone https://github.com/seu-usuario/gerador-senhas.git
cd gerador-senhas
pip install pyperclip
python Gerador_Senha.py
```

---

## ✍️ Autor

Desenvolvido por **Alex Silvax4**. Sinta-se livre para colaborar ou sugerir melhorias!

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
