-- Используем нужную базу
USE CinemaDB;
GO

-- 1. Таблица залов
CREATE TABLE Halls (
    HallID INT PRIMARY KEY IDENTITY(1,1),
    CinemaID INT NOT NULL,
    Name NVARCHAR(50),
    SeatsCount INT,
    FOREIGN KEY (CinemaID) REFERENCES Cinemas(CinemaID)
);

-- 2. Таблица сеансов
CREATE TABLE Sessions (
    SessionID INT PRIMARY KEY IDENTITY(1,1),
    MovieID INT NOT NULL,
    HallID INT NOT NULL,
    StartTime DATETIME,
    Price DECIMAL(6,2),
    FOREIGN KEY (MovieID) REFERENCES Movies(MovieID),
    FOREIGN KEY (HallID) REFERENCES Halls(HallID)
);

-- 3. Таблица билетов
CREATE TABLE Tickets (
    TicketID INT PRIMARY KEY IDENTITY(1,1),
    SessionID INT NOT NULL,
    SeatNumber INT,
    BuyerName NVARCHAR(100),
    FOREIGN KEY (SessionID) REFERENCES Sessions(SessionID)
);
