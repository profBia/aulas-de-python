ANO_ATUAL = 2025
DIAS_POR_MES = 30

ano_nascimento = int(input("Em que ano você nasceu? "))

idade_anos = ANO_ATUAL - ano_nascimento
idade_meses = idade_anos * 12
idade_dias = idade_anos * 365  # Considerando ano com 365 dias

print(f"Você tem aproximadamente {idade_anos} anos, {idade_meses} meses ou {idade_dias} dias de vida.")
