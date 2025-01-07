-- database: test.db
-- Create a new user
INSERT INTO
    user (
        user_name,
        user_dateofbirth,
        user_email,
        user_password
    )
VALUES
    (
        "John Doe",
        "2002-08-01",
        "example1@gmail.com",
        "1234password"
    );

-- Get user by id
SELECT
    *
FROM
    user
WHERE
    user_id = 2;

-- Get user by email
SELECT
    *
FROM
    user
WHERE
    user_email = "example1@gmail.com";

-- Update user by id
UPDATE user
SET
    user_name = "Misa",
    user_email = "misa@gmail.com",
    user_dateofbirth = "2002-08-08",
    user_password = "mon_mot_de_passe"
WHERE
    user_id = 2;

-- Delete user by id
DELETE FROM user
WHERE
    user_id = 2;
