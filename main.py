#importar o twilio

# instalar:
    # pandas
    # openpyxl
    # twilio

import pandas as pd
from twilio.rest import Client


# Your Account SID and Auth Token from console.twilio.com
account_sid = "account_sid" # É necessário cadastrar  no twillo para obter.
auth_token  = "auth_token" # É necessário cadastrar  no twillo para obter.
client = Client(account_sid, auth_token)


# Abrir os 6 arquivos em excel

lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]


for mes in lista_meses:
    #print(mes)
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    #print(tabela_vendas)
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]
        print(f"No mês {mes}, o {vendedor} vendeu {vendas}! Parabéns por batera meta!")
        message = client.messages.create(
            to="+5531xxxxxxx", # your phone number
            from_="seu_numero_twillio", # your twillo number
            body=f"No mês {mes}, o {vendedor} vendeu {vendas}! Parabéns por batera meta!")
        print(message.sid)


# Para cada arquivo:
    # Verificar se algum valor na coluna vendas daquele arquivo é maior que 55.000
    # Se for maior que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor
    # Caso não seja maior que 55.000 -> não fazer nada
