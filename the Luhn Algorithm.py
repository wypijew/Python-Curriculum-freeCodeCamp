def verify_card_number(card_number):
    # Remove spaces and dashes
    card_number = card_number.replace(' ', '').replace('-', '')
    
    # Reject anything that isn't all digits
    if not card_number.isdigit():
        return 'INVALID!'
    
    total = 0
    reversed_digits = card_number[::-1]

    for i in range(len(reversed_digits)):
        digit = int(reversed_digits[i])

        # Double every second digit (starting from the second from the right)
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9

        total += digit

    if total % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'