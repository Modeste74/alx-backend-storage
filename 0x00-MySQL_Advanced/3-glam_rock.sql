-- list all bands with Glam rock as main style,
-- rankd by their longevity.
-- column name must be: band_name and lifespan in years
-- until 2022 while using 2022 instead of YEAR(CURDATE())
-- We'll be using the following attributes: formed and split
-- for computing the lifespan.
SELECT band_name,
       CASE
           WHEN split IS NOT NULL THEN (split - formed)
           ELSE (2022 - formed)
       END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
