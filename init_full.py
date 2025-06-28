import pyodbc

# Подключение к локальной базе данных
conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=(localdb)\\MSSQLLocalDB;"
    "Database=CinemaDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

# SQL-запрос: сначала удалим таблицы (если уже есть)
drop_sql = """
IF OBJECT_ID('Tickets', 'U') IS NOT NULL DROP TABLE Tickets;
IF OBJECT_ID('Sessions', 'U') IS NOT NULL DROP TABLE Sessions;
IF OBJECT_ID('Movies', 'U') IS NOT NULL DROP TABLE Movies;
IF OBJECT_ID('Halls', 'U') IS NOT NULL DROP TABLE Halls;
IF OBJECT_ID('Cinemas', 'U') IS NOT NULL DROP TABLE Cinemas;
"""

# SQL-запрос: создание таблиц
create_sql = """
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
"""

# SQL-запрос: вставка данных
insert_sql = """
-- Кинотеатры
INSERT INTO Cinemas (Name, City, Address)
VALUES (N'Киномир', N'Москва', N'ул. Ленина, 1');

-- Залы
INSERT INTO Halls (CinemaID, Name, SeatsCount)
VALUES (1, N'Зал 1', 100), (1, N'Зал 2', 120);

-- Фильмы
INSERT INTO Movies (Title, Genre, DurationMinutes, CinemaID)
VALUES 
(N'Интерстеллар', N'Фантастика', 169, 1),
(N'Начало', N'Триллер', 148, 1),
(N'Крёстный отец', N'Драма', 175, 1);

-- Сеансы
INSERT INTO Sessions (MovieID, HallID, StartTime, Price)
VALUES
(1, 1, '2025-06-28 18:00', 500.00),
(2, 1, '2025-06-28 20:00', 500.00),
(3, 2, '2025-06-28 19:30', 600.00),
(1, 2, '2025-06-29 12:00', 400.00),
(2, 1, '2025-06-29 21:00', 450.00);

-- Билеты
INSERT INTO Tickets (SessionID, SeatNumber, BuyerName)
VALUES
(1, 1, N'Иванов И.И.'),
(1, 2, N'Петров П.П.'),
(2, 5, N'Сидоров С.С.'),
(3, 10, N'Кузнецова А.А.'),
(4, 7, N'Лебедев Л.Л.'),
(5, 3, N'Алексеева Е.Е.');
"""

# Выполнение запросов
cursor.execute(drop_sql)
cursor.execute(create_sql)
cursor.execute(insert_sql)

conn.commit()
print("✅ Все таблицы успешно созданы и заполнены.")
conn.close()
