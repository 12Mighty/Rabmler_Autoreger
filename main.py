from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import string
import random
import keyboard


class RamblerRegistration:
    def __init__(self, answer, email_domain="rambler.ru", password_length=12, output_file="\\pochts.txt"):
        self.answer = answer
        self.email_domain = email_domain
        self.password_length = password_length
        self.output_file = output_file
        self.driver = None

    @staticmethod
    def generate_random_string(length=12):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=length))

    def generate_password(self):
        characters = string.ascii_letters + string.digits + "@$"
        return ''.join(random.choice(characters) for _ in range(self.password_length))

    def save_credentials(self, username, password):
        with open(self.output_file, "a", encoding="utf-8") as file:
            file.write(f"mail: {username}@{self.email_domain}\n")
            file.write(f"pass: {password}\n\n")

    def open_browser(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://id.rambler.ru/login-20/mail-registration?rname=mail&theme=&session=false&back=https%3A%2F%2Fmail.rambler.ru%2F&param=embed&iframeOrigin=https%3A%2F%2Fmail.rambler.ru")

    def fill_registration_form(self, username, password):
        self.driver.find_element(By.ID, "login").send_keys(username)
        time.sleep(1)
        self.driver.find_element(By.ID, "newPassword").send_keys(password)
        time.sleep(1)
        self.driver.find_element(By.ID, "confirmPassword").send_keys(password)
        time.sleep(1)
        self.driver.find_element(By.ID, "answer").send_keys(self.answer)

    def wait_for_key(self, key='E'):
        print(f"Ожидание нажатия клавиши '{key}'...")
        keyboard.wait(key)

    def register(self):
        try:
            self.open_browser()
            self.wait_for_key('E')

            username = self.generate_random_string()
            password = self.generate_password()

            self.save_credentials(username, password)
            self.fill_registration_form(username, password)

            self.wait_for_key('E')
        finally:
            if self.driver:
                self.driver.quit()


if __name__ == "__main__":
    answer = "BMW"
    registration = RamblerRegistration(answer=answer)
    registration.register()
