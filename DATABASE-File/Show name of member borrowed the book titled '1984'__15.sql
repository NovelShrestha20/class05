SELECT Members.name 
FROM Members 
INNER JOIN Borrowings ON Members.member_id = Borrowings.member_id 
INNER JOIN Books ON Borrowings.book_id = Books.book_id 
WHERE Books.title = '1984';