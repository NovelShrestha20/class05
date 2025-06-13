SELECT category, COUNT(*) AS total_books 
FROM Books 
GROUP BY category;