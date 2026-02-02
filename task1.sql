SELECT DISTINCT
       LEAST(source, destination) AS source,
       GREATEST(source, destination) AS destination,
       distance
FROM routes;
