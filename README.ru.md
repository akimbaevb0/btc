# Графический интерфейс BTCTools

Этот пример демонстрирует простое графическое приложение на базе библиотеки
`libbtctools`. Интерфейс и строки локализованы на русский язык.

## Запуск

```bash
python gui/main.py
```

## Сборка исполняемого файла

### Linux/macOS

```bash
./build.sh
```

### Windows

```powershell
./build.ps1
```

Созданный файл появится в каталоге `dist/`.

## Тесты

Для запуска тестов требуется `pytest`:

```bash
python -m pip install pytest
pytest
```
