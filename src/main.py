from analyzer import find_indicators
from scoring import calculate_score


text = input("Paste article text: ")

indicators = find_indicators(text)

score = calculate_score(indicators)

print("\n===== TRUTHGUARD AI =====")
print(f"Trust Score: {score}/100")

if score >= 80:
    print("Risk Level: LOW")
elif score >= 50:
    print("Risk Level: MEDIUM")
else:
    print("Risk Level: HIGH")

print("\nIndicators Found:")

for item in indicators:
    print(f"- {item}")