import re
import sys


class ValidadorPlacas:
    def __init__(self):
        self.regex_antigo = r"^[A-Z]{3}-\d{4}$"

        self.regex_mercosul = r"^[A-Z]{3}\d[A-Z]\d{2}$"

    def validar_placa(self, placa, formato=None):
        placa = placa.strip().upper()

        if formato is None or formato == "auto":
            if re.match(self.regex_antigo, placa):
                return True, "Placa válida no formato antigo (AAA-9999)"
            elif re.match(self.regex_mercosul, placa):
                return True, "Placa válida no formato Mercosul (AAA9A99)"
            else:
                return False, "Placa inválida. Formatos aceitos: AAA-9999 ou AAA9A99"

        elif formato == "antigo":
            if re.match(self.regex_antigo, placa):
                return True, "Placa válida no formato antigo (AAA-9999)"
            else:
                return (
                    False,
                    "Placa inválida para o formato antigo. Formato esperado: AAA-9999",
                )

        elif formato == "mercosul":
            if re.match(self.regex_mercosul, placa):
                return True, "Placa válida no formato Mercosul (AAA9A99)"
            else:
                return (
                    False,
                    "Placa inválida para o formato Mercosul. Formato esperado: AAA9A99",
                )

        else:
            return False, "Formato de placa não reconhecido"


def exibir_menu():
    print("\n===== VALIDADOR DE PLACAS DE VEÍCULOS =====")
    print("1. Validar placa (detecção automática de formato)")
    print("2. Validar placa no formato antigo (AAA-9999)")
    print("3. Validar placa no formato Mercosul (AAA9A99)")
    print("4. Exibir informações sobre as expressões regulares")
    print("5. Sair")
    print("============================================")


def exibir_info_regex():
    print("\n===== INFORMAÇÕES SOBRE EXPRESSÕES REGULARES =====")
    print("Formato Antigo (AAA-9999):")
    print("  Regex: ^[A-Z]{3}-\\d{4}$")
    print("  Notação Algébrica: [A-Z]³-[0-9]⁴")
    print("\nFormato Mercosul (AAA9A99):")
    print("  Regex: ^[A-Z]{3}\\d[A-Z]\\d{2}$")
    print("  Notação Algébrica: [A-Z]³[0-9][A-Z][0-9]²")
    print("\nPressione ENTER para continuar...")
    input()


def main():
    validador = ValidadorPlacas()

    while True:
        exibir_menu()

        try:
            opcao = int(input("Escolha uma opção (1-5): "))
        except ValueError:
            print("Opção inválida! Por favor, digite um número de 1 a 5.")
            continue

        if opcao == 5:
            print("Encerrando o programa. Até mais!")
            sys.exit(0)

        elif opcao == 4:
            exibir_info_regex()

        elif opcao in [1, 2, 3]:
            placa = input("\nDigite a placa a ser validada: ")

            formato = None
            if opcao == 2:
                formato = "antigo"
            elif opcao == 3:
                formato = "mercosul"

            valida, mensagem = validador.validar_placa(placa, formato)

            print("\nResultado da validação:")
            if valida:
                print(f"✅ {mensagem}")
            else:
                print(f"❌ {mensagem}")

            input("\nPressione ENTER para continuar...")

        else:
            print("Opção inválida! Por favor, digite um número de 1 a 5.")


if __name__ == "__main__":
    main()
