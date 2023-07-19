-- lists all shows contained in database hbtn_0d_tvshows
-- displays NULL for shows without genres
-- records are in ascending order of tv_shows.title and tv_show_genres.genre_id
SELECT s.`title`, g.`genre_id`
	FROM `tv_shows` AS s
		LEFT JOIN `tv_show_genres` AS g
		ON s.`id` = g.`show_id`
	ORDER BY s.`title`, g.`genre_id`;