import json

with open('data.json', 'r') as file:
    data = json.load(file)

revenues = [entry["revenue"] for entry in data["daily_revenue"] if entry["revenue"] > 0]

min_revenue = min(revenues)
max_revenue = max(revenues)
average_revenue = sum(revenues) / len(revenues)
days_above_average = sum(1 for revenue in revenues if revenue > average_revenue)

print(f"Minimum daily revenue: {min_revenue}")
print(f"Maximum daily revenue: {max_revenue}")
print(f"Days with revenue above average: {days_above_average}")