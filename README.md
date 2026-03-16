# Отчет о потреблении кофе ☕️

Консольная утилита для обработки CSV файла

## Возможности утилиты
- Чтение данных из одного или нескольких CSV файлов
- Расчет медианных затрат на кофе для каждого студента
- Вывод результатов в консоль в виде таблицы
- Тестирование

## Технологии
- **Python 3.13**
- **Tabulate**: для табличного вывода.
- **Pytest**: для тестирования

## Как запустить

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/anywaymy/coffee_reports.git
   cd coffee_reports
   ```

2. **Создайте и активируйте виртуальное окружение**
   ```bash
    # Для Windows
    python -m venv venv
    venv\Scripts\activate
    
    # Для macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
   ```

3. **Установите зависимости**
   ```bash
   pip install -r requirements.txt
   ```

4. **Запуск**
   ```bash
   python main.py --files data.csv --report median-coffee
   ```
   
## Запуск теста
**Находясь в папке coffee_reports запустите код ниже**
```bash
   python -m pytest tests/test.py
   ```
