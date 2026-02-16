import schedule
import time
import pandas as pd
import random
from faker import Faker
from datetime import datetime

# Instancia o Faker (pode ficar fora para não recriar toda vez)
fake = Faker('pt_BR')

# --- FUNÇÕES AUXILIARES ---
def obter_produto_e_preco():
    produtos = {
        'Notebook': 3500,
        'Smartphone': 2000,
        'Monitor': 700,
        'Teclado': 300,
        'Mouse': 150
    }
    nome_produto = random.choice(list(produtos.keys()))
    preco_produto = produtos[nome_produto]
    return nome_produto, preco_produto

def Filiais():
    locais = {
        'José': 'Barueri',
        'Amanda': 'Barueri',
        'Augusto': 'Carapicuiba',
        'Fernanda': 'Carapicuiba',
        'Antonio': 'Osasco',
        'Izabely': 'Osasco',
        'Gustavo': 'São Paulo',
        'Ana': 'São Paulo'
    }
    vendedor_sorteado = random.choice(list(locais.keys()))
    cidade_do_vendedor = locais[vendedor_sorteado]
    return vendedor_sorteado, cidade_do_vendedor

# --- FUNÇÃO PRINCIPAL (O JOB) ---
# Esta é a função que o schedule vai chamar a cada 20 segundos
def gerar_relatorio_completo():
    print("Iniciando geração do relatório...")
    
    Quantidade_linhas = 100
    dados_lista = [] # ZERA a lista a cada execução para não acumular lixo antigo

    # Loop para gerar as 100 linhas
    for _ in range(Quantidade_linhas):
        prod, valor = obter_produto_e_preco()
        nome, cidade = Filiais()

        perfil = {
            'Nome': fake.name(),
            'CPF': fake.cpf(),
            'Data de nascimento': fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%d/%m/%Y'),
            'Telefone': fake.cellphone_number(),
            'Cidade': cidade,
            'Produto': prod,
            'Valor Gasto': valor,
            'Vendedor': nome
        }
        dados_lista.append(perfil)

    # Transforma em DataFrame
    df = pd.DataFrame(dados_lista)

    # Cria nome do arquivo com SEGUNDOS para não sobrescrever
    # Adicionei '-%S' no final do formato de hora
    nome_arquivo = f"relatorio_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.xlsx"
    
    # Salva o arquivo
    df.to_excel(nome_arquivo, index=False)
    
    print(f"Relatório '{nome_arquivo}' gerado com sucesso!")

# --- AGENDAMENTO ---
# Agendamos a função 'gerar_relatorio_completo'
schedule.every(20).seconds.do(gerar_relatorio_completo)

print("Robô iniciado. Aguardando 20 segundos para a primeira execução...")

# Loop infinito para manter o script vivo
while True:
    schedule.run_pending()
    time.sleep(1)