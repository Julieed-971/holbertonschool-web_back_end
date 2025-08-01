-- Creates a stored procedure ComputeAverageWeightedScoreForUser that computes
-- and store the average weighted score for a student
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE done INT default 0;
    DECLARE score_val FLOAT DEFAULT 0;
    DECLARE score_weight FLOAT DEFAULT 0;
    DECLARE weighted_score FLOAT DEFAULT 0;
    DECLARE weighted_score_sum FLOAT DEFAULT 0;
    DECLARE avg_weighted_score FLOAT DEFAULT 0;
    DECLARE weighting_factor_sum FLOAT DEFAULT 0;

    DECLARE cur CURSOR FOR 
        SELECT c.score, p.weight
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO score_val, score_weight;
        IF done THEN
            LEAVE read_loop;
        END IF;
        SET weighted_score = score_val * score_weight;
        SET weighting_factor_sum = weighting_factor_sum + score_weight;
        SET weighted_score_sum = weighted_score_sum + weighted_score;
    END LOOP;

    CLOSE cur;

    IF weighting_factor_sum > 0 THEN
        SET avg_weighted_score = weighted_score_sum / weighting_factor_sum;
    ELSE
        SET avg_weighted_score = 0;
    END IF;
    UPDATE users SET average_score = avg_weighted_score WHERE users.id = user_id;
END$$

DELIMITER ;
