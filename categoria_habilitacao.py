quantidadesRodas = 6;
pesoBrutoEmQuilogramas = 5500;
quantidadePessoasNoVeiculo = 9;


if (quantidadesRodas < 4):
    print("Categoria de habilitação A")
elif (quantidadesRodas == 4) & (quantidadePessoasNoVeiculo <= 8) & (pesoBrutoEmQuilogramas <= 3500):
    print("Categoria de habilitação B")
elif (quantidadesRodas >= 4) & ((pesoBrutoEmQuilogramas > 3500) & (pesoBrutoEmQuilogramas < 6000)):
    print("Categoria de habilitação C")
elif ((quantidadesRodas >= 4) & (quantidadePessoasNoVeiculo > 8)) & ((quantidadesRodas >= 4) & (pesoBrutoEmQuilogramas >= 6000)):
    print("Categoria de habilitação D")

# Desenvolva um código que utilize as seguintes características de um veículo:
# - Quantidade de rodas;
# - Peso bruto em quilogramas;
# - Quantidade de pessoas no veículo.

# Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
# A: Veículos com duas ou três rodas;
# B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
# C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
# D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; E: Veículos com quatro rodas ou mais e com mais de 6000 kg.
