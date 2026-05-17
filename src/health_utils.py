def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi):
    if bmi >= 30:
        return "Obesity"
    elif bmi >= 25:
        return "Overweight"
    elif bmi >= 18.5:
        return "Normal Weight"
    else:
        return "Underweight"


if __name__ == "__main__":
    bmi = calculate_bmi(82, 1.78)
    category = classify_bmi(bmi)

    print(f"BMI: {bmi:.1f}")
    print(f"Category: {category}")