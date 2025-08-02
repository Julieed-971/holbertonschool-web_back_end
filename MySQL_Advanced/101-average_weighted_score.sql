-- Creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Variables
    DECLARE done_users INT DEFAULT 0;
    DECLARE current_user_id INT;
    DECLARE weighted_score_sum FLOAT DEFAULT 0;
    DECLARE weighting_factor_sum FLOAT DEFAULT 0;
    DECLARE avg_weighted_score FLOAT DEFAULT 0;

    -- Cursors
    DECLARE cur_users CURSOR FOR SELECT id FROM users;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done_users = 1;

    OPEN cur_users;

    read_users_loop: LOOP
        FETCH cur_users INTO current_user_id;
        IF done_users THEN
            LEAVE read_users_loop;
        END IF;

        -- Calculate weighted average for current user using a subquery approach
        SELECT
            COALESCE(SUM(c.score * p.weight), 0),
            COALESCE(SUM(p.weight), 0) 
        INTO weighted_score_sum, weighting_factor_sum
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = current_user_id;

        -- Calculate average
        IF weighting_factor_sum > 0 THEN
            SET avg_weighted_score = weighted_score_sum / weighting_factor_sum;
        ELSE
            SET avg_weighted_score = 0;
        END IF;

        UPDATE users SET average_score = avg_weighted_score WHERE id = current_user_id;
    END LOOP;

    CLOSE cur_users;
END$$

DELIMITER ;