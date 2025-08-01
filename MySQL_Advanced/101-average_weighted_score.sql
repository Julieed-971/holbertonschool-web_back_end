DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Variables
    DECLARE done_users INT DEFAULT 0;
    DECLARE current_user_id INT;

    DECLARE done_user INT DEFAULT 0;
    DECLARE score_val FLOAT DEFAULT 0;
    DECLARE score_weight FLOAT DEFAULT 0;
    DECLARE weighted_score FLOAT DEFAULT 0;
    DECLARE weighted_score_sum FLOAT DEFAULT 0;
    DECLARE avg_weighted_score FLOAT DEFAULT 0;
    DECLARE weighting_factor_sum FLOAT DEFAULT 0;

    -- Cursors
    DECLARE cur_users CURSOR FOR SELECT id FROM users;
    DECLARE cur_user CURSOR FOR
        SELECT c.score, p.weight
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = current_user_id;

    -- Handlers
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done_users = 1;
    -- We'll need to reset done_user manually inside outer loop

    OPEN cur_users;

    read_users_loop: LOOP
        FETCH cur_users INTO current_user_id;
        IF done_users THEN
            LEAVE read_users_loop;
        END IF;

        -- Reset inner variables
        SET done_user = 0;
        SET weighted_score_sum = 0;
        SET weighting_factor_sum = 0;

        OPEN cur_user;

        read_user_loop: LOOP
            FETCH cur_user INTO score_val, score_weight;
            IF done_user THEN
                LEAVE read_user_loop;
            END IF;

            SET weighted_score = score_val * score_weight;
            SET weighted_score_sum = weighted_score_sum + weighted_score;
            SET weighting_factor_sum = weighting_factor_sum + score_weight;
        END LOOP;

        CLOSE cur_user;

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
