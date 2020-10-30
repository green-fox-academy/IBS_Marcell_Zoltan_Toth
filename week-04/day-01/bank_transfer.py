accounts = [
    {'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2},
    {'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23},
    {'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0}
]

def get_name_and_balance(list, account_num):
    ret = []
    for i in list:
        if i.get("account_number") == account_num:
            ret.append(i.get("client_name"))
            ret.append(i.get("balance"))

    return ret

print(get_name_and_balance(accounts, 11234543))


def transfer_amount(from_acc, to_acc, amount):
    for i in accounts:
        if i.get("account_number") == from_acc:
            i["balance"] = i.get("balance") - amount
        if i.get("account_number") == to_acc:
            i["balance"] = i.get("balance") + amount

transfer_amount(43546731, 23456311, 500.0)
print(accounts)