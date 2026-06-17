import sys

def perguntar(prompt_questionary):

    resposta = prompt_questionary.ask()
    
    if resposta is None:
        print("\n[!] Operação cancelada pelo usuário. Retornando ao menu...")
        raise LookupError("Prompt cancelado") 
        
    return resposta