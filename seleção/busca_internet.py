def primeiro_link(clicksTerceiro):
    numero_clicks_primeiro = (clicksTerceiro * 2)*2
    return numero_clicks_primeiro

numero_clicks_terceiro = int(input())
resposta = primeiro_link( numero_clicks_terceiro )
print(resposta)