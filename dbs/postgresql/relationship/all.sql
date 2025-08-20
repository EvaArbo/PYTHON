-- Drop old tables if they exist (order matters because of foreign keys)
DROP TABLE IF EXISTS student_subject CASCADE;
DROP TABLE IF EXISTS sports CASCADE;
DROP TABLE IF EXISTS hostel CASCADE;
DROP TABLE IF EXISTS subject CASCADE;
-- DROP TABLE IF EXISTS student CASCADE;  -- Uncomment if you also want to drop student

-- Hostel table
CREATE TABLE hostel(
    id BIGSERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL UNIQUE REFERENCES student(id) ON DELETE CASCADE,
    name TEXT,
    room TEXT
);

-- Sports table
CREATE TABLE sports(
    id BIGSERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES student(id) ON DELETE SET NULL,
    name TEXT,
    room TEXT
);

-- Subject table
CREATE TABLE subject(
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

-- Student_Subject join table
CREATE TABLE student_subject(
    id BIGSERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES student(id) ON DELETE CASCADE,
    subject_id BIGINT NOT NULL REFERENCES subject(id) ON DELETE RESTRICT,
    UNIQUE(student_id, subject_id)
);

-- Insert some subjects
INSERT INTO subject (name)
VALUES 
('English'),
('Math'),
('Physics'),
('History');



-- hostel.student_id → student.id ON DELETE CASCADE
-- If a student is deleted, their hostel record is deleted too.

-- sports.student_id → student.id ON DELETE SET NULL
-- If a student is deleted, the student_id in sports becomes NULL (keeps the sport record).

-- student_subject.student_id → student.id ON DELETE CASCADE
-- If a student is deleted, their subject enrollments are removed.

-- student_subject.subject_id → subject.id ON DELETE RESTRICT
-- You can’t delete a subject if students are still enrolled in it.