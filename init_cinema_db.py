# init_cinema_db.py

def unicode(s):
    return f"N'{s}'"

sql_script = """
-- Удаление таблиц с учётом зависимостей
IF OBJECT_ID('Tickets', 'U') IS NOT NULL DROP TABLE Tickets;
IF OBJECT_ID('Sessions', 'U') IS NOT NULL DROP TABLE Sessions;
IF OBJECT_ID('Movies', 'U') IS NOT NULL DROP TABLE Movies;
IF OBJECT_ID('Halls', 'U') IS NOT NULL DROP TABLE Halls;
IF OBJECT_ID('Cinemas', 'U') IS NOT NULL DROP TABLE Cinemas;

-- Создание таблиц
CREATE TABLE Cinemas (
    CinemaID INT PRIMARY KEY IDENTITY(1,1),
    Name NVARCHAR(100) NOT NULL,
    City NVARCHAR(50),
    Address NVARCHAR(150)
);

CREATE TABLE Halls (
    HallID INT PRIMARY KEY IDENTITY(1,1),
    CinemaID INT FOREIGN KEY REFERENCES Cinemas(CinemaID),
    Name NVARCHAR(50),
    SeatsCount INT
);

CREATE TABLE Movies (
    MovieID INT PRIMARY KEY IDENTITY(1,1),
    Title NVARCHAR(100),
    Genre NVARCHAR(50),
    DurationMinutes INT,
    CinemaID INT FOREIGN KEY REFERENCES Cinemas(CinemaID)
);

CREATE TABLE Sessions (
    SessionID INT PRIMARY KEY IDENTITY(1,1),
    MovieID INT FOREIGN KEY REFERENCES Movies(MovieID),
    HallID INT FOREIGN KEY REFERENCES Halls(HallID),
    StartTime DATETIME,
    Price DECIMAL(10, 2)
);

CREATE TABLE Tickets (
    TicketID INT PRIMARY KEY IDENTITY(1,1),
    SessionID INT FOREIGN KEY REFERENCES Sessions(SessionID),
    SeatNumber INT,
    BuyerName NVARCHAR(100)
);

-- Вставка данных
-- Кинотеатры
INSERT INTO Cinemas (Name, City, Address) VALUES
    ({unicode("Киномакс")}, {unicode("Москва")}, {unicode("ул. Ленина, 1")}),
    ({unicode("Формула Кино")}, {unicode("Санкт-Петербург")}, {unicode("пр. Невский, 100")});

-- Залы
INSERT INTO Halls (CinemaID, Name, SeatsCount) VALUES
    (1, {unicode("Зал 1")}, 100),
    (1, {unicode("Зал 2")}, 80),
    (2, {unicode("IMAX")}, 120);

-- Фильмы
INSERT INTO Movies (Title, Genre, DurationMinutes, CinemaID) VALUES
    ({unicode("Интерстеллар")}, {unicode("Фантастика")}, 169, 1),
    ({unicode("Начало")}, {unicode("Триллер")}, 148, 1),
    ({unicode("Крёстный отец")}, {unicode("Драма")}, 175, 2);

-- Сеансы
INSERT INTO Sessions (MovieID, HallID, StartTime, Price) VALUES
    (1, 1, '2025-06-28 18:00:00', 500.00),
    (2, 1, '2025-06-28 20:00:00', 500.00),
    (3, 2, '2025-06-28 19:30:00', 600.00),
    (3, 3, '2025-06-29 12:00:00', 800.00),
    (1, 3, '2025-06-29 21:00:00', 650.00);

-- Билеты
INSERT INTO Tickets (SessionID, SeatNumber, BuyerName) VALUES
    (1, 1, {unicode("Иванов И.И.")}),
    (1, 2, {unicode("Петров П.П.")}),
    (2, 5, {unicode("Сидоров С.С.")}),
    (3, 10, {unicode("Кузнецова А.А.")}),
    (4, 7, {unicode("Лебедев Л.Л.")}),
    (5, 3, {unicode("Алексеева Е.Е.")});
"""

# Сохраняем результат в файл
with open("init_cinema_db.sql", "w", encoding="utf-8") as f:
    f.write(sql_script)

print("✅ SQL-скрипт успешно создан: init_cinema_db.sql")
