def converte_hora(segundos):
    hora = segundos // 3600
    return hora
    
def converte_minuto(segundos):
    minutos = segundos // 60
    return minutos
    
# segundos = int(input())
segundos = 140153
hora = converte_hora(segundos)
segundos= segundos - (hora*3600)
minuto = converte_minuto(segundos)
segundos= segundos - (minuto*60)

print(f'{hora}:{minuto}:{segundos}')
