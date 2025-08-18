--SELECT <columns //  *>
--FROM <table>
--WHERE <READ CONSTRAINTS>
--ORDER <>  LIMIT <>
--Read all columns and 

--SELECT * FROM student;

--Read only name, email 
--SELECT name, email FROM student;

--Using filter
--be specific and select the email and name column to get only the name and email

-- SELECT name, email FROM student
-- WHERE email= 'jane@gmail.com'
-- OR
-- email ='alice@gmail.com'

--filter by AND
SELECT * FROM student
WHERE pocket_money>10
AND pocket_money<51

--SELECT * FROM student
--ORDER BY name ASC
--LIMIT 2



