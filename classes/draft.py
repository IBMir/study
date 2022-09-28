def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False


def is_valid_password(password):
    password = password.split(':')
    print(password)
    return password[0] == password[0][::-1] and is_prime(int(password[1])) and int(password[2]) % 2 == 0 and len(password) == 3



# считываем данные
txt = '24422442:181:890000'

# вызываем функцию
print(is_valid_password(txt))
