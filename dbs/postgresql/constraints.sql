--able to constain your data
--to make sure its ok
--Rules for data integrity
DROP TABLE IF EXISTS student;
CREATE TABLE IF NOT EXISTS student(
    id SERIAL PRIMARY KEY,
    name VARCHAR(500) NOT NULL,
    email VARCHAR(500) NOT NULL UNIQUE,
    dob DATE,
    phone VARCHAR(20) NOT NULL,
    marks REAL CHECK(marks>-1 AND marks<101),
    pocket_money INTEGER,
    is_married BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- TEXT -> holw book
-- VARCHAR(50)                