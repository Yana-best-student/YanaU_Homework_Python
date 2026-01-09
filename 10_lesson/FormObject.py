from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class PageObject:
    def __init__(self, driver):
        """
        Конструктор класса PageObject.
        :param driver: Webdriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        """
        В переменную fields передаем словарь для заполнения формы
        в формате ключ:значение. Поле 'zip-code' оставляем пустым
        """
        self.fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    @allure.step("Открытие страницы с формой для заполнения")
    def open(self):
        """
        Открывает страницу "data-types.html" в браузере,
        использует driver.get для открытия страницы
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    @allure.step("Заполнение формы данными")
    def fill_form(self):
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)

    @allure.step("Нажатие на кнопку отправки формы")
    def submit_form(self):
        """
        Нажимает на кнопку отправки формы, ожидая,
        пока она станет кликабельной.
        """
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3"))
        ).click()

    @allure.step("Возвращает класс элементов на странице")
    def get_field_class(self, field_id):
        """
        функция ищет элемент на странице по его
        ID и возвращает значение его атрибута "class".
        :param field_id: str - ID идентификатор элемента .
        :return: str - класс элемента.
        """
        element = self.wait.until(
            EC.presence_of_element_located((
                By.ID, field_id))).get_attribute("class")
        return element

    @allure.step("Возвращает строку 'alert-danger', "
                 "если такая имеется в классе элемента с ID 'zip-code'")
    def check_zip_code_error(self):
        """
        Проверяет, содержит ли класс элемента с ID
        "zip-code" строку "alert-danger".
        """
        return "alert-danger" in self.get_field_class("zip-code")

    @allure.step("Проверка каждого элемента списка"
                 " на содержание в классе строки 'success'")
    def check_fields_success(self):
        """
        Для каждого поля из списка проверяет, содержит
        ли класс поля строку "success".
        Если хотя бы одно поле не прошло проверку,
        функция возвращает False, иначе True.
        """
        fields = ["first-name", "last-name", "address", "e-mail",
                  "phone", "city", "country",  "job-position", "company"
                  ]
        for field in fields:
            if "success" not in self.get_field_class(field):
                return False
        return True

    @allure.step("Проверка что обе предыдущие функции возвращают True")
    def check_form_submission(self):
        """
        Использует assert для проверки, что
        обе предыдущие функции возвращают True
        """
        assert self.check_zip_code_error()
        assert self.check_fields_success()
