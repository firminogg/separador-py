![image](https://github.com/user-attachments/assets/3ca9bf8a-1abc-4b27-a6aa-1d1785b465b1)

# Wordlist separator (in English)
This Python script allows the extraction of area codes (DDD) and phone numbers from a formatted CSV wordlist. The user can specify the input and output file names. The script processes each line, identifies the columns for DDD and phone numbers, and saves the results in a new file. It includes exception handling to ensure the input file exists and is correctly processed.

## Features:
- Extraction of area codes (DDD) and phone numbers from TXT files.
- Saving the extracted data to a separate file.
- Error handling, including checking for nonexistent files.


## FAQ
#### What format is the wordlist?
"TDOC";"CPF";"NOME";"TP_LOG";"LOGRAD";"NUM";"COMPL";"BAIRRO";"CIDADE";"UF";"CEP";"DDD";"TEL";"OPERADORA"

#### Can the file separate any wordlist?
No, this file is specifically for this type of wordlist, if you have another wordlist, you can message me.

# Installation

```bash
  git clone https://github.com/firminogg/separador-py.git
  cd separador
  python separator.py
```

## Autores
- [@hash](https://github.com/firminogg/)
