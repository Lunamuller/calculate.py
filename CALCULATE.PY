python
import tkinter as tk
from tkinter import messagebox

# Função para calcular e exibir o resultado
def calculate():
    try:
        expression = entry.get()
        # Verifique a entrada do usuário para evitar erros de cálculo
        if not expression.replace(" ", "").replace(".", "").replace("+", "").replace("-", "").replace("*", "").replace("/", "").isdigit():
            raise ValueError("Entrada inválida")
        
        result = eval(expression)
        
        # Lide com divisão por zero
        if result == float('inf') or result == float('-inf'):
            raise ZeroDivisionError
        
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Não é possível dividir por zero.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora")

# Entrada de texto
entry = tk.Entry(root, width=20, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4)

# Botões da calculadora
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 16), command=calculate).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 16),
                  command=lambda key=button: entry.insert(tk.END, key)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Iniciar a interface gráfica
root.mainloop()