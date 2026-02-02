SELECT
    str_value,
    LENGTH(str_value) - LENGTH(REPLACE(str_value, 'a', '')) AS a_count
FROM strings_table;
