
import json

lista_pacientes = []

def exibir_menu():
    print("=-= Sistema de Monitoramento de Saúde =-=")
    print("1. Adicionar Paciente")
    print("2. Visualizar Pacientes")
    print("3. Remover Pacientes")
    print("4. Sair")

def adicionar_paciente():
    nome = input("Digite o nome do paciente: ")
    idade = int(input("Digite a idade do paciente: "))
    sintomas = input("Digite os sintomas do paciente: ")
    pressao_arterial = input("Digite a pressão arterial do paciente: ")
    frequencia_cardiaca = input("Digite a frequência cardíaca do paciente: ")
    temperatura_corporal = input("Digite a temperatura corporal do paciente: ")

    paciente = {
        "Nome": nome,
        "Idade": idade,
        "Sintomas": sintomas,
        "PressaoArterial": pressao_arterial,
        "FrequenciaCardiaca": frequencia_cardiaca,
        "TemperaturaCorporal": temperatura_corporal
        }
    lista_pacientes.append(paciente)
    print("Paciente adicionado com sucesso!")
    salvar_dados()

def visualizar_pacientes():
    if not lista_pacientes:
        print("Nenhum paciente cadastrado.")
    else:
        print("\n### Lista de Pacientes ###")
        for i, paciente in enumerate(lista_pacientes, 1):
            print(f"{i}. {paciente['Nome']} - Sintomas: {paciente['Sintomas']}")
        print()

        escolha_filtro = input("Deseja filtrar por sintomas? (S para sim, qualquer outra tecla para não): ")
        
        if escolha_filtro.upper() == "S":
            filtro_sintomas = input("Digite os sintomas para filtrar: ")
            pacientes_filtrados = [paciente for paciente in lista_pacientes if filtro_sintomas.lower() in paciente['Sintomas'].lower()]

            if pacientes_filtrados:
                print("\n### Pacientes Filtrados ###")
                for i, paciente in enumerate(pacientes_filtrados, 1):
                    print(f"{i}. {paciente['Nome']} - Sintomas: {paciente['Sintomas']}")
                print()
            else:
                print(f"Nenhum paciente com sintomas contendo '{filtro_sintomas}' encontrado.")
        else:
            escolha = input("Escolha o número do paciente para visualizar detalhes (ou pressione Enter para voltar): ")
            if escolha.isdigit():
                indice_paciente = int(escolha) - 1
                if 0 <= indice_paciente < len(lista_pacientes):
                    visualizar_paciente_detalhes(lista_pacientes[indice_paciente])
                else:
                    print("Número de paciente inválido.")
            else:
                print("Retornando ao menu principal.")

def visualizar_paciente_detalhes(paciente):
    print("\n=-= Detalhes do Paciente =-=")
    print(f"Nome: {paciente['Nome']}")
    print(f"Idade: {paciente['Idade']}")
    print(f"Sintomas: {paciente['Sintomas']}")
    print(f"Pressão Arterial: {paciente['PressaoArterial']}mmHg")
    print(f"Frequência Cardíaca: {paciente['FrequenciaCardiaca']} bpm")
    print(f"Temperatura Corporal: {paciente['TemperaturaCorporal']}°C")
    print()

def remover_paciente():
    if not lista_pacientes:
        print("Nenhum paciente cadastrado para remover.")
    else:
        print("\n=-= Remover Paciente =-=")
        for i, paciente in enumerate(lista_pacientes, 1):
            print(f"{i}. {paciente['Nome']}")
        
        escolha = input("Escolha o número do paciente para remover (ou pressione Enter para voltar): ")
        if escolha.isdigit():
            indice_paciente = int(escolha) - 1
            if 0 <= indice_paciente < len(lista_pacientes):
                paciente_removido = lista_pacientes.pop(indice_paciente)
                print(f"Paciente {paciente_removido['Nome']} removido com sucesso.")
                salvar_dados()
            else:
                print("Número de paciente inválido.")
        else:
            print("Retornando ao menu principal.")

def salvar_dados():
    with open("dados_pacientes.json", "w") as arquivo:
        json.dump(lista_pacientes, arquivo)
    print("Dados salvos com sucesso!")

def carregar_dados():
    try:
        with open("dados_pacientes.json", "r") as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        return []

def main():
    lista_pacientes.extend(carregar_dados())

    while True:
        exibir_menu()

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_paciente()
        elif escolha == "2":
            visualizar_pacientes()
        elif escolha == "3":
            remover_paciente()
        elif escolha == "4":
            salvar_dados()
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()