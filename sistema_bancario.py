# ==========================================================
# FUNÇÕES DE OPERAÇÃO BANCÁRIA
# ==========================================================
def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print(
            "\nOperação falhou! O valor informado é inválido (menor ou igual a zero)."
        )
    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print(
            f"\nOperação falhou! O valor do saque excede o limite de R$ {limite:.2f}."
        )
    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")

    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


# ==========================================================
# FUNÇÕES DE CADASTRO E FILTRO
# ==========================================================
def filtrar_usuario(cpf, usuarios):
    """Retorna o usuário (dicionário) se o CPF for encontrado, senão retorna None."""
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None


def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    if filtrar_usuario(cpf, usuarios):
        print("\n@@@ Já existe usuário com este CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )

    usuarios.append(
        {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco,
        }
    )
    print("\n=== Usuário cadastrado com sucesso! ===")


def cadastrar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        contas.append(
            {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        )
        print(
            f"\n=== Conta {agencia}-{numero_conta} criada com sucesso para {usuario['nome']}! ==="
        )
        return True

    print("\n@@@ Usuário não encontrado, cadastro de conta encerrado! @@@")
    return False  #


# ==========================================================
# VARIÁVEIS GLOBAIS E INICIALIZAÇÃO
# ==========================================================
AGENCIA = "0001"
usuarios = []
contas = []

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def main():
    global saldo, extrato, numero_saques
    global contas
    menu = """
    \n======= MENU =======  
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [q] Sair
    => """

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "nu":
            cadastrar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1

            cadastrar_conta(AGENCIA, numero_conta, usuarios, contas)

        elif opcao == "q":
            break

        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


if __name__ == "__main__":
    main()
