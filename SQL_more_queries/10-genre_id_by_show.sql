-- Show all shows
SELECT title, tv_show_genres.genre_id
FROM tv_shows FULL JOIN tv_show_genres ON id = tv_show_genres.show_id
ORDER BY title, tv_show_genres.genre_id;
