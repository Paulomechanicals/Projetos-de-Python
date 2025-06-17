import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("400x500")

entrada = tk.Entry(janela, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10,pady=20)

def inserir(valor):
    entrada.insert(tk.END, valor)

def calcular():
    try:
         resultado = eval(entrada.get())
         entrada.delete(0, tk.END)
         entrada.insert(0, str(resultado))
    except:
         entrada.delete(0, tk.END)
         entrada.insert(0, "Erro")

def limpar():
    entrada.delete(0, tk.END)

botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (texto, linha, coluna) in botoes:
    if texto == "=":
        botao = tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 18), command=calcular)
        botao.grid(row=linha, column=coluna)
    elif texto == "C":
        botao = tk.Button(janela, text=texto, width=23, height=2, font=("Arial", 18), command=limpar)
        botao.grid(row=linha, column=0, columnspan=4, padx=5, pady=10)
    else:
        botao = tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 18),
                          command=lambda t=texto: inserir(t))
        botao.grid(row=linha, column=coluna)

janela.mainloop()