def calcular_total_episodios(temporadas):
    if temporadas == 0:
        return 0
    else:
        episodios_por_temporada = int(
            input(f"Quantos episódios na temporada {temporadas}? "))
        return episodios_por_temporada + calcular_total_episodios(temporadas - 1)


# Exemplo de uso
numero_temporadas = int(input("Quantas temporadas a série tem? "))
total_episodios = calcular_total_episodios(numero_temporadas)
print(f"O número total de episódios é: {total_episodios}")
