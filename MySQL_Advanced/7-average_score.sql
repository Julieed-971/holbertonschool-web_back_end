-- Creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE avg_score FLOAT;

    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE corrections.user_id = user_id;

    IF avg_score is NOT NULL THEN
        UPDATE users
        SET average_score = avg_score
        WHERE users.id = user_id;
    END IF;
END$$

DELIMITER ;
    