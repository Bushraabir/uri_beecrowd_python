number = float(input())
if number < 0 or number > 100:
    print("Fora de intervalo")
elif 0 <= number <= 25:
    print("Intervalo [0,25]")
elif 25 < number <= 50:
    print("Intervalo (25,50]")
elif 50 < number <= 75:
    print("Intervalo (50,75]")
else:
    print("Intervalo (75,100]")