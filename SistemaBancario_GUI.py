import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog  # Para pedir valores ao usuário

# ==========================================================
# CLASSE PRINCIPAL DO BANCO (UNE LÓGICA E GUI)
# ==========================================================


class BancoGUI:
    def __init__(self, master):
        # 1. Configuração da Janela
        self.master = master
        master.title("Sistema Bancário Python - GUI")
        master.geometry("350x300")
        master.config(padx=20, pady=20)

        # 2. Variáveis de Estado (Substituindo as Globais)
        self.AGENCIA = "0001"
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3
        self.usuarios = []
        self.contas = []

        # Variáveis Tkinter para display (atualização em tempo real)
        self.tk_saldo = tk.StringVar(value=f"R$ {self.saldo:.2f}")

        # 3. Construção da Interface
        self.criar_widgets()

    # --- Métodos de Lógica (Adaptados das suas funções originais) ---

    def filtrar_usuario(self, cpf):
        """Retorna o usuário (dicionário) se o CPF for encontrado, senão retorna None."""
        usuario_filtrado = [
            usuario for usuario in self.usuarios if usuario["cpf"] == cpf
        ]
        return usuario_filtrado[0] if usuario_filtrado else None

    # --- CADASTROS ---

    def cadastrar_usuario_gui(self):
        cpf = simpledialog.askstring("Novo Usuário", "Informe o CPF (somente números):")
        if not cpf:
            return

        if self.filtrar_usuario(cpf):
            messagebox.showerror("Erro de Cadastro", "Já existe usuário com este CPF!")
            return

        nome = simpledialog.askstring("Novo Usuário", "Informe o nome completo:")
        data_nascimento = simpledialog.askstring(
            "Novo Usuário", "Informe a data de nascimento (dd/mm/aaaa):"
        )
        endereco = simpledialog.askstring(
            "Novo Usuário", "Informe o endereço(rua, numero, bairro, cidade e estado):"
        )

        if nome and data_nascimento and endereco:
            self.usuarios.append(
                {
                    "nome": nome,
                    "data_nascimento": data_nascimento,
                    "cpf": cpf,
                    "endereco": endereco,
                }
            )
            messagebox.showinfo("Sucesso", f"Usuário {nome} cadastrado com sucesso!")
        else:
            messagebox.showerror("Erro", "Cadastro cancelado ou dados incompletos.")

    def cadastrar_conta_gui(self):
        cpf = simpledialog.askstring(
            "Nova Conta", "Informe o CPF do usuário para vincular a conta:"
        )
        if not cpf:
            return

        usuario = self.filtrar_usuario(cpf)

        if usuario:
            numero_conta = len(self.contas) + 1
            self.contas.append(
                {
                    "agencia": self.AGENCIA,
                    "numero_conta": numero_conta,
                    "usuario": usuario,
                }
            )
            messagebox.showinfo(
                "Sucesso",
                f"Conta {self.AGENCIA}-{numero_conta} criada para {usuario['nome']}!",
            )
        else:
            messagebox.showerror(
                "Erro", "Usuário não encontrado, cadastro de conta encerrado!"
            )

    # --- OPERAÇÕES ---

    def depositar_gui(self):
        valor_str = simpledialog.askstring("Depósito", "Informe o valor do depósito:")
        if not valor_str:
            return

        try:
            valor = float(valor_str)
            if valor > 0:
                self.saldo += valor
                self.extrato += f"Depósito: R$ {valor:.2f}\n"

                # ATUALIZAÇÃO DA GUI
                self.tk_saldo.set(f"R$ {self.saldo:.2f}")

                messagebox.showinfo("Sucesso", f"Depósito de R$ {valor:.2f} realizado.")
            else:
                messagebox.showerror("Erro", "O valor informado é inválido.")
        except ValueError:
            messagebox.showerror("Erro", "Informe um valor numérico válido.")

    def sacar_gui(self):
        valor_str = simpledialog.askstring("Saque", "Informe o valor do saque:")
        if not valor_str:
            return

        try:
            valor = float(valor_str)

            excedeu_saldo = valor > self.saldo
            excedeu_limite = valor > self.limite
            excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

            if excedeu_saldo:
                messagebox.showerror("Erro", "Saldo insuficiente.")
            elif excedeu_limite:
                messagebox.showerror(
                    "Erro", f"Valor excede o limite de R$ {self.limite:.2f}."
                )
            elif excedeu_saques:
                messagebox.showerror(
                    "Erro", f"Número máximo de saques ({self.LIMITE_SAQUES}) excedido."
                )
            elif valor > 0:
                self.saldo -= valor
                self.extrato += f"Saque: R$ {valor:.2f}\n"
                self.numero_saques += 1

                # ATUALIZAÇÃO DA GUI
                self.tk_saldo.set(f"R$ {self.saldo:.2f}")

                messagebox.showinfo("Sucesso", f"Saque de R$ {valor:.2f} realizado.")
            else:
                messagebox.showerror("Erro", "O valor informado é inválido.")

        except ValueError:
            messagebox.showerror("Erro", "Informe um valor numérico válido.")

    def exibir_extrato_gui(self):
        historico = "================ EXTRATO ================\n"
        historico += (
            "Não foram realizadas movimentações.\n"
            if not self.extrato
            else self.extrato
        )
        historico += f"\nSaldo Atual: R$ {self.saldo:.2f}"
        historico += f"\nSaques Restantes: {self.LIMITE_SAQUES - self.numero_saques}\n"
        historico += "========================================="
        messagebox.showinfo("Extrato Bancário", historico)

    # --- Construção dos Widgets (O Layout) ---

    def criar_widgets(self):
        # 1. Rótulo de Saldo Atual
        label_titulo = tk.Label(
            self.master, text="Seu Saldo Atual:", font=("Arial", 12)
        )
        label_titulo.pack(pady=(10, 0))

        # Rótulo que exibe o saldo (será atualizado via tk_saldo)
        label_saldo = tk.Label(
            self.master,
            textvariable=self.tk_saldo,
            font=("Arial", 20, "bold"),
            fg="green",
        )
        label_saldo.pack(pady=5)

        # 2. Botões de Operação
        frame_op = tk.Frame(self.master)
        frame_op.pack(pady=10)

        tk.Button(
            frame_op, text="Depositar", command=self.depositar_gui, width=10
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_op, text="Sacar", command=self.sacar_gui, width=10).pack(
            side=tk.LEFT, padx=5
        )
        tk.Button(
            frame_op, text="Extrato", command=self.exibir_extrato_gui, width=10
        ).pack(side=tk.LEFT, padx=5)

        # 3. Botões de Cadastro
        frame_cad = tk.Frame(self.master)
        frame_cad.pack(pady=10)

        tk.Button(
            frame_cad, text="Novo Usuário", command=self.cadastrar_usuario_gui, width=15
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(
            frame_cad, text="Nova Conta", command=self.cadastrar_conta_gui, width=15
        ).pack(side=tk.LEFT, padx=5)

        # 4. Botão Sair
        tk.Button(
            self.master,
            text="Sair",
            command=self.master.quit,
            width=20,
            bg="red",
            fg="white",
        ).pack(pady=10)


# ==========================================================
# INICIALIZAÇÃO DA APLICAÇÃO
# ==========================================================
if __name__ == "__main__":
    # Cria a janela raiz (root)
    root = tk.Tk()

    # Cria uma instância da sua classe de banco, passando a janela raiz
    app = BancoGUI(root)

    # Inicia o loop da aplicação
    root.mainloop()
