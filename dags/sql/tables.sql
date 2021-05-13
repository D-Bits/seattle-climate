
CREATE TABLE pollution
(
    id SERIAL PRIMARY KEY,
    "date" DATE NOT NULL,
    aqi DECIMAL NOT NULL,
    co DECIMAL NOT NULL,
    no2 DECIMAL NOT NULL,
    o3 DECIMAL NOT NULL,
    pm10 DECIMAL NOT NULL,
    pm25 DECIMAL NOT NULL,
    so2 DECIMAL NOT NULL
);