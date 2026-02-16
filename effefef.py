import pandas as pd
import random

def simular_produtividade_anual():
    vendas = []
    
    # Definimos os produtos e preços fixos aqui (dicionário)
    produtos = {
        'Camisa': 23,
        'Calça': 25
    }
    
    meses = [
        '01/01/2026', '01/02/2026', '01/03/2026', '01/04/2026', '01/05/2026', '01/06/2026',
        '01/07/2026', '01/08/2026', '01/09/2026', '01/10/2026', '01/11/2026', '01/12/2026'
    ]

    for mes in meses:
        for nome_produto, valor_produto in produtos.items():
            
            # Define quantas vezes esse produto específico foi vendido no mês
            # (Ex: entre 5 e 20 vendas desse item)
            quantidade_aleatoria = random.randint(10, 100)
            
            venda = {
                'Mês': mes, 
                'Produto': nome_produto,        
                'Quantidade': quantidade_aleatoria,
                'Preco_Unitario': valor_produto,
                'Custo de produção': quantidade_aleatoria * valor_produto 
            }
            vendas.append(venda)

    df_vendas = pd.DataFrame(vendas) 

    df_vendas['Mês'] = pd.Categorical(df_vendas['Mês'], categories=meses, ordered=True)
    
    # Ordena: Primeiro junta todos de um Produto, depois ordena pelos Meses
    df_vendas = df_vendas.sort_values(by=['Produto', 'Mês'])

    return df_vendas

def gerar_lucro (df_vendas):

    margem = 0.50
    fator_aumento = 1 + margem

    for produto in ['Camisa', 'Calça']:

        valor_unitario = df_vendas.loc[df_vendas['Produto'] == produto, 'Preco_Unitario'].iloc[0] * fator_aumento

        df_vendas.loc[df_vendas['Produto'] == produto, 'Preco_Unitario'] = valor_unitario

        lucro_total = df_vendas.loc[df_vendas['Produto'] == produto, 'Quantidade'] * valor_unitario - df_vendas.loc[df_vendas['Produto'] == produto, 'Custo de produção']
        df_vendas.loc[df_vendas['Produto'] == produto, 'Lucro'] = lucro_total


    return df_vendas

if __name__ == "__main__":

    df_final = simular_produtividade_anual()
    df_final = gerar_lucro (df_final)
    
    print(df_final)
    
    # Exportar para Excel para ver igualzinho no vídeo
    df_final.to_excel("relatorio_cru.xlsx", index=False)