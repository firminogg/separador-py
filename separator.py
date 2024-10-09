import os
import pyfiglet

# Função para limpar o terminal
def limpar_terminal():
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para sistemas Unix/Linux/Mac
        os.system('clear')

# Função para exibir uma mensagem estilizada com pyfiglet
def exibir_cabecalho():
    ascii_art = pyfiglet.figlet_format("Hash Script", font="slant")
    print(ascii_art)
    print("script feito por hash")
    print("um salve pro grupo do duck :D")
    print("=" * 100)

# Função para extrair o DDD e o número de telefone de cada linha da wordlist
def extrair_ddd_telefones(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            for linha in infile:
                # Remove aspas duplas e divide os dados corretamente
                dados = linha.strip().replace('"', '').split(";")  
                
                # Pega o DDD (12ª coluna) e o telefone (13ª coluna)
                ddd = dados[-3].strip()  # 12ª coluna (DDD)
                telefone = dados[-2].strip()  # 13ª coluna (Telefone)

                # Grava no arquivo de saída o DDD seguido do telefone
                outfile.write(f"{ddd}{telefone}\n")  

        print(f"DDDs e telefones extraídos com sucesso e salvos em '{output_file}'!")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{input_file}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Função principal
def main():
    # Limpa o terminal e exibe o cabeçalho
    limpar_terminal()
    exibir_cabecalho()
    
    # Solicitando o nome do arquivo ao usuário
    input_file = input("digite o nome do arquivo da wordlist (.txt) ")
    output_file = input("digite o nome do arquivo para salvar (.txt)")

    # Executando a função para extrair os DDDs e telefones
    extrair_ddd_telefones(input_file, output_file)

# Executa a função principal
if __name__ == "__main__":
    main()
