# Função para extrair apenas o número de telefone de cada linha da wordlist
def extrair_telefones(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            for linha in infile:
                dados = linha.split(";")  # Divide a linha pelos pontos e vírgulas
                telefone = dados[-3].replace('"', '').strip()  # Pega a penúltima coluna (número de telefone)
                outfile.write(telefone + '\n')  # Escreve o telefone no arquivo de saída
        print(f"Telefones extraídos com sucesso e salvos em '{output_file}'!")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{input_file}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Função principal
def main():
    # Solicitando o nome do arquivo ao usuário
    input_file = input("Digite o nome da wordlist (incluindo a extensão, por exemplo, 'wordlist.txt'): ")
    output_file = input("Digite o nome do arquivo para salvar os números de telefone (por exemplo, 'telefones.txt'): ")

    # Executando a função para extrair os telefones
    extrair_telefones(input_file, output_file)

# Executa a função principal
if __name__ == "__main__":
    main()
