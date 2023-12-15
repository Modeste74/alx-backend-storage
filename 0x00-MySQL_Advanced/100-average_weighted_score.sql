DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE average_score FLOAT;
    
    SELECT SUM(C.score * P.weight) INTO total_weighted_score
    FROM corrections C
    INNER JOIN projects P ON C.project_id = P.id
    WHERE C.user_id = user_id;
    
    SELECT SUM(P.weight) INTO total_weight
    FROM corrections C
    INNER JOIN projects P ON C.project_id = P.id
    WHERE C.user_id = user_id;
    
    IF total_weight > 0 THEN
        SET average_score = total_weighted_score / total_weight;
    ELSE
        SET average_score = 0;
    END IF;
    
    UPDATE users
    SET average_score = average_score
    WHERE id = user_id;
END;
//

DELIMITER ;
