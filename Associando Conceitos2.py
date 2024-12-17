# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber uma prática e retornar sua respectiva descrição.
def descrever_boas_praticas(pratica):
    if pratica == "clareza":
        return "ser claro e direto na formulação da pergunta"
  
    # Complete com as boas práticas restantes conforme descrições abaixo
    elif pratica == "contexto":
        return "fornecer informações adicionais relevantes"
        
    elif pratica == "especificidade":
        return "detalhar exatamente o que se deseja saber"
                            
    elif pratica == "objetividade":
        return "manter a pergunta focada e sem ambiguidades"
        
# Imprime a descrição da boa prática recebida na "entrada" através da função "descrever_boas_praticas". 
print(descrever_boas_praticas(entrada))