-- a script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT DISTINCT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
WHERE NOT EXISTS (
	SELECT 1
	FROM tv_show_genres
	JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
	WHERE tv_genres.name = "Comedy"
	AND tv_show_genres.show_id = tv_shows.id
)
ORDER BY tv_shows.title
