import re

def normalize_phone(phone_number: str) -> str:
    # Залишаємо лише цифри та символ '+'
    cleaned_phone_number = re.sub(r"[^\d+]", "", phone_number)

    if cleaned_phone_number.startswith('+'):
        return cleaned_phone_number
    elif cleaned_phone_number.startswith('380'):
        return "+" + cleaned_phone_number
    else:
        return "+38" + cleaned_phone_number