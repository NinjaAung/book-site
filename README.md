# book-site

1. How would we filter for all books with titles containing the word ‘Django’? 
    > book.objects.filter(books__name='Django')
2. How would we filter for all books with tag ‘Fiction’?
    > book.objects.filter(title='Fiction)
3. How would we filter for all authors who have written books containing the word ‘Django’? HINT: We can use the book field to refer to an author’s books, even though the Author model doesn’t explicitly contain it!
    > book.objects.filter(book__contains='Django)