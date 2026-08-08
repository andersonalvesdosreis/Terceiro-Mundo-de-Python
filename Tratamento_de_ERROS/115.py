import json
import os
import time

ARQUIVO_DADOS = "pessoas.json"


def carregar_dados():
    """Carrega os dados salvos do arquivo JSON, se existir."""
    if os.path.exists(ARQUIVO_DADOS):
        try:
            with open(ARQUIVO_DADOS, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


def salvar_dados(pessoas):
    """Salva a lista de pessoas no arquivo JSON."""
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as file:
        json.dump(pessoas, file, indent=4, ensure_ascii=False)


def limpar_tela():
    """Limpa o console para manter a interface limpa."""
    os.system("cls" if os.name == "nt" else "clear")


def listar_pessoas(pessoas):
    """Exibe a lista de pessoas cadastradas."""
    limpar_tela()
    print("=" * 40)
    print(f"{'PESSOAS CADASTRADAS':^40}")
    print("=" * 40)

    if not pessoas:
        print("Nenhuma pessoa cadastrada ainda.\n")
    else:
        # Exibição em formato de tabela
        print(f"{'ID':<5} | {'NOME':<20} | {'IDADE':<5}")
        print("-" * 40)
        for i, pessoa in enumerate(pessoas, 1):
            print(f"{i:<5} | {pessoa['nome']:<20} | {pessoa['idade']:<5}")
        print("-" * 40)

    input("\nPressione [ENTER] para voltar ao menu principal...")


def cadastrar_pessoa(pessoas):
    """Realiza o cadastro validando os dados digitados."""
    limpar_tela()
    print("=" * 40)
    print(f"{'NOVO CADASTRO':^40}")
    print("=" * 40)

    # Validação do Nome
    while True:
        nome = input("Digite o nome: ").strip()
        if nome and not nome.isdigit():
            break
        print("❌ Erro: O nome não pode estar vazio nem conter apenas números!")

    # Validação da Idade
    while True:
        try:
            idade = int(input("Digite a idade: "))
            if 0 <= idade <= 130:
                break
            else:
                print("❌ Erro: Por favor, insira uma idade válida (0 a 130).")
        except ValueError:
            print("❌ Erro de Digitação: A idade deve ser um número inteiro!")

    # Adicionando o registro
    pessoas.append({"nome": nome.title(), "idade": idade})
    salvar_dados(pessoas)

    print("\n✅ Pessoa cadastrada com sucesso!")
    time.sleep(1.5)


def menu_principal():
    """Menu principal do sistema."""
    pessoas = carregar_dados()

    while True:
        limpar_tela()
        print("=" * 40)
        print(f"{'MENU PRINCIPAL':^40}")
        print("=" * 40)
        print("1 - Ver pessoas cadastradas")
        print("2 - Cadastrar nova pessoa")
        print("3 - Sair do sistema")
        print("=" * 40)

        opcao = input("Escolha uma opção (1-3): ").strip()

        if opcao == "1":
            listar_pessoas(pessoas)
        elif opcao == "2":
            cadastrar_pessoa(pessoas)
        elif opcao == "3":
            limpar_tela()
            print("Encerrando o sistema... Até logo!")
            break
        else:
            print(
                "\n❌ Opção inválida! Por favor, escolha um número entre 1 e 3."
            )
            time.sleep(1.5)


if __name__ == "__main__":
    menu_principal()