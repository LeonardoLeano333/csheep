from hashlib import sha256


def encrypt(data: str) -> str:
    len_data = len(data)
    data_list = []
    for char in data:
        char_value = ord(char)
        data_list.append(char_value*len_data)

    sum_data_list = sum(data_list)
    m = sha256(str.encode(f"{sum_data_list}"))
    res = m.hexdigest   ()
    return m.hexdigest()


if __name__ == "__main__":
    data = "CitricSheep"
    hex = encrypt(data)
    print(hex)
