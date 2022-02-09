valorAplicado = float(input("Digite o valor que deve ser aplicado: "))

percentual = float(input("Digite o valor do Juros"))
juros = valorAplicado * percentual / 100
valorJuros = valorAplicado + juros

mes = int(input("Digite a quantidade de meses: "))
mesesAcumulados = mes * valorJuros
mesContador = 1

print("O valor do juros é %d" % juros)
print("O Mensal é %d" % valorJuros)
print("Em %d meses você receberá um valor de: %d" % (mes, mesesAcumulados))

print("Antes do WHILE")

print("O seu valor aplicado é de %.2f" % valorAplicado)

while mesContador <= mes:
    print("Mês %d: %.2f"% (mesContador, valorJuros))
    mesContador = mesContador + 1
    valorJuros = valorJuros + valorJuros * percentual / 100