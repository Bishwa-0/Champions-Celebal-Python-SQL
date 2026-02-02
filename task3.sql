SELECT
    s,
    LENGTH(str_value) - LENGTH(REPLACE(str_value, 'b', '')) 
FROM table_name;
