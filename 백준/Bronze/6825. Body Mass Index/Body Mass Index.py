def bmi(w, m):
    bmi_w = w / (m ** 2)
    if bmi_w > 25:
        return "Overweight"
    elif 18.5 <= bmi_w <= 25:
        return "Normal weight"
    else:
        return "Underweight"

w = float(input())
m = float(input())

result = bmi(w, m)
print(result)