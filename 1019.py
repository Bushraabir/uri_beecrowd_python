seconds = int(input())
hours = seconds // 3600
remaining = seconds % 3600
minutes = remaining // 60
secs = remaining % 60
print(f"{hours}:{minutes}:{secs}")