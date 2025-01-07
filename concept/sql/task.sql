-- database: test.db
-- Create task
INSERT INTO
    task (
        task_name,
        task_description,
        task_datecreation,
        task_state,
        project_id
    )
VALUES
    (
        "Task 1 name",
        "Task 1 description",
        date('now'),
        FALSE,
        2
    );

-- Get by project_id
SELECT
    *
FROM
    task
WHERE
    project_id = 2;

-- Get by task_name
SELECT
    *
FROM
    task
WHERE
    task_name LIKE "%n%"
    AND project_id = 2;

-- get between two task_datecreation
SELECT
    *
FROM
    task
WHERE
    task_datecreation BETWEEN "2024-12-01" AND "2025-01-07"
    AND project_id = 2;

-- get by exact task_datecreation
SELECT
    *
FROM
    task
WHERE
    task_datecreation = "2025-01-07"
    AND project_id = 2;

-- get task by task_state
SELECT
    *
FROM
    task
WHERE
    task_state = FALSE
    AND project_id = 2;

-- update by task_id
UPDATE task
SET
    task_name = "Updated task 1",
    task_description = "Updated task 1 description"
WHERE
    task_id = 1;

-- update state by task_id
UPDATE task
SET
    task_state = TRUE
WHERE
    task_id = 1;

-- delete by task_id
DELETE FROM task
WHERE
    task_id = 1;
