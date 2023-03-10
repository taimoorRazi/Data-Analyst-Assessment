# The following queries were run on postgres to make sure the task was performed correctly. Please read from line 12-20 to see the query.
"""
-- CREATE TABLE vaccination_table(
    -- country VARCHAR(250),
    -- date DATE,
    -- daily_vaccinations NUMERIC,
    -- vaccines VARCHAR(255)
    - -)
-- GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO postgres
-- COPY vaccination_table
-- FROM 'C:\Users\country_vaccination_stats.csv' DELIMITER ',' CSV HEADER
-- UPDATE vaccination_table v
-- SET daily_vaccinations = COALESCE(
    -- (SELECT PERCENTILE_CONT(0.5) WITHIN GROUP(ORDER BY daily_vaccinations)
        - -      FROM vaccination_table
        - -      WHERE country=v.country AND daily_vaccinations IS NOT NULL
        - -      GROUP BY country), 0)
-- WHERE daily_vaccinations IS NULL
-- SELECT *
-- FROM vaccination_table

"""
