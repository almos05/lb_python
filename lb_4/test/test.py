import unittest
from password_generator import PasswordGenerator
import string

class TestPasswordGenerator(unittest.TestCase):
    def test_default_length(self):
        """Тест на длину пароля по умолчанию."""
        generator = PasswordGenerator()
        password = generator.generate()
        self.assertEqual(len(password), 12)

    def test_custom_length(self):
        """Тест на кастомную длину пароля."""
        generator = PasswordGenerator(length=16)
        password = generator.generate()
        self.assertEqual(len(password), 16)

    def test_include_uppercase(self):
        """Тест, включает ли пароль заглавные буквы."""
        generator = PasswordGenerator(include_uppercase=True, include_digits=False, include_special=False)
        password = generator.generate()
        self.assertTrue(any(char.isupper() for char in password))

    def test_include_digits(self):
        """Тест, включает ли пароль цифры."""
        generator = PasswordGenerator(include_uppercase=False, include_digits=True, include_special=False)
        password = generator.generate()
        self.assertTrue(any(char.isdigit() for char in password))

    def test_exclude_digits(self):
        """Тест, исключены ли цифры."""
        generator = PasswordGenerator(include_uppercase=False, include_digits=False, include_special=False)
        password = generator.generate()
        self.assertFalse(any(char.isdigit() for char in password))

    def test_include_special(self):
        """Тест, включает ли пароль специальные символы."""
        generator = PasswordGenerator(include_uppercase=False, include_digits=False, include_special=True)
        password = generator.generate()
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_exclude_special(self):
        """Тест, исключены ли специальные символы."""
        generator = PasswordGenerator(include_uppercase=False, include_digits=False, include_special=False)
        password = generator.generate()
        self.assertFalse(any(char in string.punctuation for char in password))

    def test_invalid_length(self):
        """Тест на некорректную длину пароля."""
        with self.assertRaises(ValueError):
            PasswordGenerator(length=0).generate()


if __name__ == "__main__":
    unittest.main()
