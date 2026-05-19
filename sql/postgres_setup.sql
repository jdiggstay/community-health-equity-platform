CREATE TABLE communities (
    id SERIAL PRIMARY KEY,
    community TEXT,
    diabetes_rate NUMERIC,
    clinic_count INTEGER
);

INSERT INTO communities (community, diabetes_rate, clinic_count)
VALUES 
('North Lawndale', 14.2, 4),
('Austin', 12.8, 7),
('Hyde Park', 7.4, 3);