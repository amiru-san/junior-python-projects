print("=== BODY MASS INDEX ===")
while True:
    try:
        height = int(input("> Your Height: ")) / 100
        mass = float(input("> Your Weight (kg): "))
        bmi = round(mass/(height**2))
        print(f"\nBMI: {bmi}\n")
        if bmi >= 40.0:
            print(f"==============================\nSTATUS: Obesity class III\nDESCRIPTION: Morbid (extreme) obesity.\nRECOMMENDATION: Critical health risk. Weight management should be strictly supervised by a team of medical professionals (endocrinologist, cardiologist, bariatric specialist). Medical or surgical intervention may be considered.\n==============================\n")
        elif bmi >= 35.0:
            print(f"==============================\nSTATUS: Obesity class II\nDESCRIPTION: Severe Obesity.\nRECOMMENDATION: High risk for type 2 diabetes and hypertension. It is highly advised to check blood sugar and hormone levels with a doctor. Focus on safe, gradual weight loss without crash diets.\n==============================\n")
        elif bmi >= 30.0:
            print(f"==============================\nSTATUS: Obesity class I\nDESCRIPTION: Moderate Obesity.\nRECOMMENDATION: Chronic condition baseline. Consider consulting a dietitian. A sustainable caloric deficit (10–15% below maintenance) combined with regular cardio and strength workouts is highly recommended.\n==============================\n")
        elif bmi >= 25.0:
            print(f"==============================\nSTATUS: Overweight (Pre-obesity)\nDESCRIPTION: Increased body strain, tendency to weight gain.\nRECOMMENDATION: Your weight is starting to strain your joints and cardiovascular system. Consider reducing added sugars and ultra-processed foods. Focus on increasing daily steps and physical activity.\n==============================\n")
        elif bmi >= 18.5:
            print(f"==============================\nSTATUS: Normal weight\nDESCRIPTION: Optimal weight, lowest risk of disease.\nRECOMMENDATION: Your weight is optimal. Maintain your current lifestyle by eating a balanced diet and getting at least 150 minutes of moderate exercise per week.\n==============================\n")
        elif bmi >= 17.0:
            print(f"==============================\nSTATUS: Mild thinness\nDESCRIPTION: Slight weight deficit, borderline state.\nRECOMMENDATION: Borderline weight deficit. Optimize your macronutrient balance, ensure adequate protein intake, and incorporate light strength training to safely build lean muscle mass.\n==============================\n")
        elif bmi >= 16.0:
            print(f"==============================\nSTATUS: Moderate thinness\nDESCRIPTION: Moderate weight deficit.\nRECOMMENDATION: Consult a nutritionist. Focus on gradually increasing daily caloric intake using nutrient-dense foods (healthy fats, complex carbs, and proteins) rather than empty calories.\n==============================\n")
        else:
            print(f"==============================\nSTATUS: Severe thinness\nDESCRIPTION: Acute weight deficit, critical health risks.\nRECOMMENDATION: Urgent medical evaluation required. Consult a physician or endocrinologist immediately to rule out underlying health conditions and create a supervised nutritional recovery plan.\n==============================\n")
    except ValueError:
        print("\n===============\nERROR 100: The input must contain only digitals.\n===============\n")
    except ZeroDivisionError:
        print("\n===============\nERROR 200: Height cannot be zero.\n===============\n")
    except KeyboardInterrupt:
        print("\n===============\nERROR 300: Operation was interrupted.\n===============\n")
