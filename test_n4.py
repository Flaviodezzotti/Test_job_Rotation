faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total = sum(faturamento.values())

percentuais = {}
for estado, valor in faturamento.items():
    percentual = (valor / total) * 100
    percentuais[estado] = percentual

print(percentuais)

# saida será {'SP': 38.31686476715302,
#             'RJ': 20.729341354765276,
#             'MG': 16.53492952125834,
#             'ES': 15.334907476355317,
#             'Outros': 9.084956880468043}
