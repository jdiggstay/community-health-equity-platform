def validate_positive_number(value):
    if value <= 0:
        raise ValueError("Value must be greater than zero.")
    return value


if __name__ == "__main__":
    try:
        number = float(input("Enter a positive number: "))
        validated = validate_positive_number(number)
        print(f"Validated: {validated}")
    except ValueError as error:
        print(f"Validation error: {error}")