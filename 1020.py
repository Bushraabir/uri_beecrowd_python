days = int(input())
years = days // 365
remaining = days % 365
months = remaining // 30
days_left = remaining % 30
print(f"{years} ano(s)")
print(f"{months} mes(es)")
print(f"{days_left} dia(s)")