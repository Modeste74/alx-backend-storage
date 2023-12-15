-- creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS U
    JOIN (
        SELECT U.id, 
               COALESCE(SUM(C.score * P.weight) / SUM(P.weight), 0) AS weighed_avg_score
        FROM users AS U
        LEFT JOIN corrections AS C ON U.id = C.user_id 
        LEFT JOIN projects AS P ON C.project_id = P.id 
        GROUP BY U.id
    ) AS T ON U.id = T.id
    SET U.average_score = T.weighed_avg_score;
END;
//

DELIMITER ;
