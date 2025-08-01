-- Creates a stored procedure AddBonus that adds a new correction for a student
DELIMITER $$

CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score FLOAT)
BEGIN
    DECLARE project_id_var INT;

    SELECT id INTO project_id_var
    FROM projects
    WHERE projects.name = project_name;

    IF project_id_var is NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id_var = LAST_INSERT_ID();
    END IF;

    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_id_var, score);
END$$

DELIMITER ;
