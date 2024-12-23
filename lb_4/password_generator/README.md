# Генератор паролей

`psswrdgen` — это простая библиотека на Python для генерации надежных и настраиваемых паролей. Вы можете задать длину пароля, включить или исключить заглавные буквы, цифры и специальные символы.

## Возможности
- Генерация паролей любой длины.
- Настраиваемое включение:
  - Заглавных букв
  - Цифр
  - Специальных символов
- Легкость использования и небольшой размер.

## Установка

Установите библиотеку с помощью pip:

```bash
pip install psswrdgen
```

## Использование

Пример использования библиотеки:

```python
from password_generator import PasswordGenerator

# Создаем экземпляр генератора
generator = PasswordGenerator(length=16, include_uppercase=True, include_digits=True, include_special=True)

# Генерируем пароль
password = generator.generate()
print(f"Сгенерированный пароль: {password}")
```

### Параметры
- `length` (int): Длина пароля (по умолчанию: 12).
- `include_uppercase` (bool): Включать ли заглавные буквы (по умолчанию: True).
- `include_digits` (bool): Включать ли цифры (по умолчанию: True).
- `include_special` (bool): Включать ли специальные символы (по умолчанию: True).

## Лицензия

Этот проект лицензирован на условиях MIT License. Подробнее см. файл [LICENSE](LICENSE).

## Контакты

По любым вопросам пишите на [tenderboylive3@gmail.com](mailto:tenderboylive3@gmail.com).