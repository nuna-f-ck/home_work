"""Функция принимает либо номер счета, либо номер карты и маскирует его"""
def mask_account_card(account_or_card):
    if "Счет" in account_or_card:
        account_masks = account_or_card[0:4] + " " + "**" + account_or_card[-4:]
        return account_masks
    else:
        card_mascks = account_or_card[0:-12] + " " + account_or_card[-12:-10] + "** **** " + account_or_card[-4:]
        return card_mascks


"""Функция принимает дату и возвращает ее в определенном формате"""
def get_date(time):
    time = time[0:10].split("-")
    time = ":".join(time[::-1])
    return time
