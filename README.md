# education

# C# Console App

Это простое консольное приложение на C#. Для запуска используйте команду:

```
dotnet run
```

# C++ Console App

Это простое консольное приложение на C++. Для запуска используйте команды:

```
g++ cpp/main.cpp -o cpp/main.exe
cpp/main.exe
```

# Java Console App

Это простое консольное приложение на Java. Для проверки работы Java:

```
javac java/Main.java
java -cp java Main
```

В выводе должно появиться:
```
Hello, Java!
```

# Python + SQL

В проекте есть пример подключения к базе данных SQL Server через Python — файл `connect_sql.py`.

Для запуска:
```
python connect_sql.py
```

В скрипте используется библиотека `pyodbc` и подключение к базе данных CinemaDB через ODBC.

# C Console App

Это простое консольное приложение на C. Для запуска используйте команды:

```
gcc c/main.c -o c/main.exe
c/main.exe
```

## Структура
- `Program.cs` — основной файл приложения (C#)
- `Work.csproj` — файл проекта (C#)
- `cpp/main.cpp` — основной файл приложения (C++)
- `c/main.c` — основной файл приложения (C)
- `java/Main.java` — основной файл приложения (Java)
- `connect_sql.py` — пример работы с SQL Server через Python

## Требования
- .NET SDK (https://dotnet.microsoft.com/download)
- Компилятор g++ (например, из MinGW или WSL)
- Компилятор gcc (например, из MinGW или WSL)
- JDK (https://adoptium.net/ или https://www.oracle.com/java/technologies/downloads/)
- Python 3.x (https://www.python.org/downloads/), библиотека pyodbc
- SQL Server (для работы с connect_sql.py)

## Запуск
### C#
1. Откройте терминал в папке проекта
2. Выполните команду:
   ```
   dotnet run
   ```

### C++
1. Откройте терминал в папке проекта
2. Выполните команды:
   ```
   g++ cpp/main.cpp -o cpp/main.exe
   cpp/main.exe
   ```

### Java
1. Откройте терминал в папке проекта
2. Выполните команды:
   ```
   javac java/Main.java
   java -cp java Main
   ```

### Python + SQL
1. Установите pyodbc:
   ```
   pip install pyodbc
   ```
2. Запустите скрипт:
   ```
   python connect_sql.py
   ```

### C
1. Откройте терминал в папке проекта
2. Выполните команды:
   ```
   gcc c/main.c -o c/main.exe
   c/main.exe
   ```
