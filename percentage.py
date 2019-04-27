import string as str

def get_percentage(text):
    text = text.lower()
    alpha = {}
    amount = 0
    for char in text:
       if char in str.ascii_lowercase:
            amount += 1
            if char in alpha:
                alpha[char] += 1
            else:
                 alpha[char] = 1

    for key,val in alpha.items():
        alpha[key] = val/amount

    return alpha


def get_percentage_all_chars(text):
    alpha = {}
    amount = 0
    for char in text:
        amount += 1
        if char in alpha:
            alpha[char] += 1
        else:
            alpha[char] = 1

    for key,val in alpha.items():
        alpha[key] = val/amount

    return alpha


