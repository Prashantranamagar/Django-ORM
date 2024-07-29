
from practice_orm.models import Author, Books, Publisher, User

from datetime import date
from django.db.models import Sum, Avg

def practice_orm():

    #  Query 1: Fetching all books from the database
    q1 = Author.objects.all()
    # print(q1)


    #  Query 2: Fetching selected columns from the Books table
    q2 = Books.objects.all().values_list('title', 'genre')
    # print(q2)


    # Query 3: Filtering records based on a condition
    q3 = Books.objects.filter(title__icontains="arr").values_list('title')
    # print(q3)


    # Filtering records based on multiple conditions
    q3 = Books.objects.filter(title__icontains="arr", genre__istartswith='a').values_list('title', 'genre')
    # print(q3)



    # Query 5: Searching records based on a substring
    # filter using contains for casesensitive, use icontains for caseinsensitive.


    # Query 6: Retrieve authors with specific primary keys
    q4 = Author.objects.filter(pk__in=[1, 2, 3, 4])
    # print(q4)


    # Query 7: Retrieve authors who joined after a specific date

    q5 = Author.objects.filter(joindate__gt=date(year=2000, month=10, day=10)).values_list('firstname', 'joindate')
    # print(q5)


    # Note: distinct() --> remove duplicates row from a Queryset.
    # Query 8: Retrieve distinct publisher last name
    q6 = Publisher.objects.values_list('lastname').distinct()
    # print(q6)


    # Query 9: Retrieve the latest joined author and the earliest joined publisher
    latest = Publisher.objects.all().order_by('-joindate').first()
    earliest = Publisher.objects.all().order_by('-joindate').last()
    # print(latest, earliest)

    # Query 10: Retrieve the first name, last name, and join date of the most recently joined author.
    latest1 = Publisher.objects.all().order_by('-joindate').values_list('firstname', 'lastname', 'joindate').first()
    # print(latest1)

    # Query 11: Retrieve Authors Joined After 2013
    q = Author.objects.filter(joindate__year__gt=2013)
    # print(q)

    # Query 12: Calculate Total Price of Books Written by Popular Authors
    q = Books.objects.filter(author__popularity_score__gte=5).aggregate(total_price=Sum('price'))
    # print(q)

    # Query 13: Retrieve Titles of Books. Books Written by Authors with ‘a’ in their Firstname
    q = Books.objects.filter(author__firstname__icontains='a').values_list('title', flat=True)
    # print(q)



    # Query 14: Calculate Average Book Price of Selected Authors
    q = Books.objects.filter(author__pk__in=[1, 2, 3]).aggregate(avg_price=Avg('price'))
    # print(q)


    # Query 15: Retrieve first name of authors and their recommended author’s first name
    q = Author.objects.all().values_list('firstname', 'recommendedby__firstname')
    # print(q)


    # Query 16: Retrieve authors whose books are published by a specific publisher
    q = Author.objects.filter(books__publisher__pk=1)
    # print(q)


    # Query 17: Add followers to an author
    # user1 = User.objects.get(pk=1)
    # user2 = User.objects.get(pk=2)
    # q = Author.objects.get(pk=q).followers.add(user2)  #Error


    # Query 18: Set followers for an author
    # user = User.objects.get(id=1)
    # q = Author.objects.get(id=3).followers.set(user)  #Error


    # Query 20: Remove a follower from an author
    # q = Author.objects.get(id=3).followers.remove(user)
    # print(q)  #Error

    # Query 21: Retrieve the first names of all authors followed by the user with primary key (pk) equal to 1
    # q = User.objects.get(pk=1).followed_authors.all().values_list('firstname', flat=True)
    # print(q)
    # Query 22: Retrieve all authors who have books with titles containing the string “tle”
    # q = Author.objects.filter(books__title__icontains='tle')
    # print(q)

    # Query 23: Retrieve all authors whose first name starts with the letter “a” and either have a popularity score greater than 5 or joined the platform after the year 2014
    # q = Author.objects.filter(Q(first_name__startswith='a') & Q(popularity_score__gt=5) | Q(joindate__gt=2014))
    # print(q)

    # Query 24: Retrieve the author with primary key (pk) equal to 1
    # q = Author.objects.filter(pk=1)
    # print(q)


    # Query 25: Retrieve the first 10 authors in the database
    q = Author.objects.all()[:10]
    print(q)

    # Query 26: Retrieve the first and last author in the database with a popularity score of 7.
    

    # Query 27: Retrieve all authors whose joindate year is greater than or equal to 2012, popularity_score is greater than or equal to 4, joindate day is greater than or equal to 12, and firstname starts with ‘a’
    # Query 28: Retrieve all authors whose joindate year is not equal to 2012
    # Query 29: Retrieve the oldest joindate among all authors, the newest joindate among all authors, the average popularity_score of all authors, and the sum of price of all books
    # Query 30: Retrieve all authors who have not been recommended by anyone
    # Query 31: Retrieve all books that have an author, and all books that have an author who has not been recommended by anyone
    # Query 32: Calculate the sum of the price of all books authored by the author with primary key (pk) equal to 1
    # Query 33: Retrieve the title of the most recently published book
    # Query 34: Calculate the average price of all books
    # Query 35: Calculate the maximum popularity score of all the publishers that have published a book written by the author with primary key 1
    # Query 36: Count Authors with Books containing ‘ab’ in the title
    # Query 37: Filter Authors by Number of Followers
    # Query 38: Average Popularity Score of Authors who joined after 20th Sep 2014
    # Query 39: Filter Books by Authors who have written more than 10 Books
    # Query 40: Filter Books by Title Count
