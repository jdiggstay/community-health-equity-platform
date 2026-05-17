from health_utils import calculate_bmi, classify_bmi

patients = [
    {"name": "Hannah", "weight_kg": 68, "height_m": 1.65},
    {"name": "Barrett", "weight_kg": 95, "height_m": 1.75},
    {"name": "Cleo", "weight_kg": 52, "height_m": 1.60},
]

for patient in patients:
    bmi = calculate_bmi(patient["weight_kg"], patient["height_m"])
    category = classify_bmi(bmi)

    print(
        f"{patient['name']}: "
        f"BMI {bmi:.1f} - {category}"
    )