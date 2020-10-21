current_hours = 14
current_minutes = 34
current_seconds = 42

total_seconds = 24 * 60 * 60
ans = total_seconds - ( current_hours * 3600 + current_minutes * 60 + current_seconds)

print(ans)