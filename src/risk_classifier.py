def classify_readmission_risk(score):
    if score >= 0.80:
        return "Very High Risk"
    elif score >= 0.60:
        return "High Risk"
    elif score >= 0.30:
        return "Moderate Risk"
    else:
        return "Low Risk"


# Example usage
if __name__ == "__main__":
    test_score = 0.72
    print(classify_readmission_risk(test_score))