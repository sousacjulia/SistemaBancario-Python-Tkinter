# 🏦 Sistema Bancário em Python

Este projeto demonstra a evolução de um sistema bancário simples, começando com uma interface de linha de comando e evoluindo para uma aplicação de desktop usando a biblioteca **Tkinter**.

As regras de negócio (limite de R$ 500 por saque, máximo de 3 saques por dia, e cadastro de usuários/contas) foram mantidas e refatoradas em funções para garantir a modularidade do código.

## 🚀 Como Rodar o Projeto

### Pré-requisitos
Você precisa ter o Python 3 instalado. A biblioteca `tkinter` geralmente vem instalada por padrão com o Python.

### Execução da Versão Gráfica (Recomendada)

1.  Baixe o arquivo `SistemaBancario_GUI.py`.
2.  Abra o terminal na pasta do arquivo.
3.  Execute o script:
    ```bash
    python SistemaBancario_GUI.py
    ```

**Dica:** Para interagir, use os botões de **"Novo Usuário"** e **"Nova Conta"** primeiro, e depois use as operações de **"Depositar"**, **"Sacar"** e **"Extrato"**.

## 📁 Estrutura do Projeto

O projeto é dividido em três arquivos principais que mostram a progressão do desenvolvimento:

| Arquivo | Descrição | Interface |
| :--- | :--- | :--- |
| `SistemaBancario_desafio.py` | **Versão Inicial.** Código monolítico, sem funções de cadastro. O código é executado em um único loop `while`. | Terminal (Linha de Comando) |
| `sistema_bancario.py` | **Versão Refatorada.** As operações de saque, depósito e extrato foram separadas em funções. Adicionadas funções de `cadastrar_usuario` e `cadastrar_conta` com validação de CPF. | Terminal (Linha de Comando) |
| `SistemaBancario_GUI.py` | **Versão Final (GUI).** Todo o código refatorado foi encapsulado em uma classe (`BancoGUI`) e conectado à interface gráfica **Tkinter**, usando `messagebox` e `simpledialog` para interação com o usuário. | Interface Gráfica (Tkinter) |

## ✨ Funcionalidades

* **Operações Financeiras:** Depósito, Saque e Extrato.
* **Controles de Saque:** Limite diário de R$ 500 e máximo de 3 saques.
* **Cadastro de Clientes:** Cadastro de novos usuários (validando CPF único).
* **Cadastro de Contas:** Criação de contas vinculadas a um usuário existente (Agência fixa: 0001).
* **Interface Gráfica:** Utilização do Tkinter para uma experiência de usuário mais amigável.

---

Desenvolvido com 💙 em Python.
