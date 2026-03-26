def classify_number(num):
    match num:
        case 0:
            return "Zero"
        case 1 | 2 | 3:
            return "Small number"
        case 4 | 5 | 6 | 7 | 8 | 9:
            return "Medium number"
        case _ if num < 0:
            return "Negative"
        case _:
            return "Large number"

# Test
print(classify_number(0))   # Zero
print(classify_number(2))   # Small number
print(classify_number(5))   # Medium number
print(classify_number(-3))  # Negative
print(classify_number(15))  # Large number