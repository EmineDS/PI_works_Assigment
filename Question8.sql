WITH MedianValues AS (SELECT country, PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY daily_vaccinations) OVER (PARTITION BY country) AS median
FROM countryvac
WHERE daily_vaccinations IS NOT NULL)
UPDATE countryvac
SET countryvac.daily_vaccinations = MedianValues.mediaN FROM MedianValues 
WHERE countryvac.country = MedianValues.country
AND countryvac.daily_vaccinations IS NULL;

