import random
import string


def create_captcha(size=6):
    pool = string.ascii_uppercase + string.ascii_lowercase + string.digits
    code = ""

    for i in range(size):
        code += random.choice(pool)

    return code


def verify_user():
    captcha_code = create_captcha()

    print("\nGenerated CAPTCHA:", captcha_code)

    entered = input("Type the CAPTCHA shown above: ")

    if entered.strip() == captcha_code:
        print("Verification Successful! Human confirmed.")
    else:
        print("Verification Failed! Try again.")


if __name__ == "__main__":
    verify_user()
