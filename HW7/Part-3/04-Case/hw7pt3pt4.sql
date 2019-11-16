SELECT id, animal_name, species
CASE
    WHEN id = 1 THEN 'mouse'
    WHEN id = 2 THEN 'mouse'
    ELSE 'duck'
END AS species
FROM disney; 