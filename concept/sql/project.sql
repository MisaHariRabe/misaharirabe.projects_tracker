-- database: test.db
-- create project
INSERT INTO
    project (
        project_name,
        project_description,
        project_datecreation,
        project_state,
        user_id
    )
VALUES
    (
        "Test title",
        "Test description",
        date('now'),
        FALSE,
        3
    );

-- get by user_id
SELECT
    *
FROM
    project
WHERE
    user_id = 3;

-- get by project_id
SELECT
    *
FROM
    project
WHERE
    project_id = 1;

-- get by project_name
SELECT
    *
FROM
    project
WHERE
    project_name LIKE "%A%"
    AND user_id = 3;

-- get between two project_datecreation
SELECT
    *
FROM
    project
WHERE
    project_datecreation BETWEEN "2024-12-01" AND "2025-01-07"
    AND user_id = 3;

-- get by exact project_datecreation
SELECT
    *
FROM
    project
WHERE
    project_datecreation = "2025-01-07"
    AND user_id = 3;

-- get project by project_state
SELECT
    *
FROM
    project
WHERE
    project_state = FALSE
    AND user_id = 3;

-- update by project_id
UPDATE project
SET
    project_name = "Updated project",
    project_description = "New project description"
WHERE
    project_id = 1;

-- update state by project_id
UPDATE project
SET
    project_state = TRUE
WHERE
    project_id = 1;

-- delete by project_id
DELETE FROM project
WHERE
    project_id = 1;
