# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def descrever_conceito(conceito):
    if conceito == "machine learning":
        return "permite que máquinas aprendam e se aprimorem com dados"
        
    # Completei as descrições com base nos conceitos fornecidos
    elif conceito == "ia generativa":
        return "sistemas de IA que criam novos conteúdos a partir de dados existentes"
        
    elif conceito == "processamento de linguagem natural":
        return "técnicas para entender e gerar linguagem humana"
                            
    elif conceito == "redes neurais":
        return "modelos inspirados no funcionamento do cérebro humano"

# Imprime a descrição do conceito recebido na "entrada" através da função "descrever_conceito". 
print(descrever_conceito(entrada))