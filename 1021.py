value = float(input())
print("NOTAS:")
notes = [100, 50, 20, 10, 5, 2]
for note in notes:
    count = int(value // note)
    print(f"{count} nota(s) de R$ {note}.00")
    value = value % note
print("MOEDAS:")
value = round(value * 100)
coins = [100, 50, 25, 10, 5, 1]
for coin in coins:
    count = int(value // coin)
    print(f"{count} moeda(s) de R$ {coin/100:.2f}")
    value = value % coin