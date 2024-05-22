-- a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT DISTINCT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE NOT EXISTS (
    SELECT 1
    FROM tv_show_genres
    JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_shows.title = 'Dexter' 
    AND tv_show_genres.genre_id = tv_genres.id
)
ORDER BY tv_genres.name
