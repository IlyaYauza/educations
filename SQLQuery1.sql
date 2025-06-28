SELECT * FROM Tickets t
JOIN Sessions s ON t.SessionID = s.SessionID
JOIN Movies m ON s.MovieID = m.MovieID;
