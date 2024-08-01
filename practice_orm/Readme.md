# Django QuerySets

## Terminology

Models: Django models are Python classes that define the structure and behavior of database tables. They encapsulate fields and relationships and provide methods to interact with the data.

QuerySets: QuerySets are objects that allow you to retrieve, filter, and manipulate data from the database. They are lazy, meaning that they only fetch data when needed, and can be chained together to form complex queries.

Managers: Managers provide methods for working with QuerySets. They allow you to create reusable queries and define custom methods to retrieve data from the database.

Fields: Fields define the type of data that can be stored in a model’s attribute or database column. They provide validation and conversion of input data and map to the appropriate SQL type.

Migrations: Migrations allow you to modify the database schema and keep track of changes to models over time. They provide a convenient way to manage changes to the database schema and apply them to the database.

Database routers: Database routers allow you to specify which database to use for different models or queries. They allow you to distribute data across multiple databases or use different databases for read and write operations.

Aggregation: Aggregation provides methods for performing calculations on QuerySets, such as Sum, Count, Avg, and Max. They are used to retrieve statistics or summary information about the data in the database.

Annotations: Annotations allow you to add calculated fields to QuerySets based on database functions or other fields. They are used to add computed or aggregated data to QuerySets.

Meta options: Meta options provide additional settings for models, such as ordering, database table names, and unique constraints. They allow you to customize the behavior of models at the class level.


## Basic Queries


| Query                                      | Description                                |
|--------------------------------------------|--------------------------------------------|
| `ModelName.objects.all()`                  | Retrieve all records                       |
| `ModelName.objects.get(id=1)`              | Retrieve a single record                   |
| `ModelName.objects.filter(attribute=value)`| Filter records                             |
| `ModelName.objects.exclude(attribute=value)` | Exclude records                           |
| `ModelName.objects.order_by('attribute')` | Order records                              |
| `ModelName.objects.filter().exclude().order_by()` | Chain filters                        |
| `ModelName.objects.all()[:10]`             | Limit QuerySet                             |


## QuerySet Methods

| Method                | Description                                                |
|-----------------------|------------------------------------------------------------|
| `all()`               | Retrieve all records                                       |
| `get(**kwargs)`               | Retrieve a single record by primary key or unique criteria |
| `filter(**kwargs)`            | Filter search to return only rows that match the search term |
| `exclude(**kwargs)`            | Returns a new QuerySet containing objects that do not match the given lookup parameters. |

| `value_list()`         | Return only the specified columns                          |
| `values()`            | Return each object as a Python dictionary                  |
| `order_by('-attribute')` | Order in descending order                              |
| `order_by('attribute')`  | Order in ascending order                               |
| `exist()`               | query existence test                                       |
| `none()`               | Used when you want to explicitly create a QuerySet that contains no results |
| `only()`               | Fetches only specified fields from the database.|
| `differ()`               | Excludes specified fields from the initial query, fetching them later if accessed. |
| `select_related()`       | Joins tables in a single query for single-valued relationships |
| `prefetch_related()`     |  Performs separate queries for multi-valued relationships and combines them in Python. |
| `distinct()`          |  Removes duplicate records from the query results. |
| `distinct('field')`          |  Distinct on field |
| `bulk_create()`          |  bulk creation |
| `bulk_update()`          |  bulk update |
| `bulk_delete()`          |  bulk delete |
| `latest('date_field)`    |  Retrieves the most recent record based on a specified date or datetime field. |
| `earliest('date_field)`  |  Retrieves the earliest record based on a specified date or datetime field. |




## Field Lookups Example 

`ModelName.objects.filter(attribute__exact=value)`

`ModelName.objects.filter(attribute__date=date(YYYY, MM, DD))`

`ModelName.objects.filter(attribute__year=YYYY)`  


## Field Lookups

### Most Used

| Lookup Type     | Description                                                    |
|-----------------|----------------------------------------------------------------|
| `exact`         | An exact match                                                 |
| `iexact`        | Case-insensitive exact match                                   |
| `contains`      | Contains the phrase                                            |
| `icontains`     | Case-insensitive contains                                      |
| `in`            | Matches one of the values                                      |
| `isnull`        | Matches NULL values                                            |
| `gt`            | Greater than                                                   |
| `gte`           | Greater than or equal to                                       |
| `lt`            | Less than                                                      |
| `lte`           | Less than or equal to                                          |
| `startswith`    | Starts with                                                    |
| `istartswith`   | Case-insensitive starts with                                   |
| `endswith`      | Ends with                                                      |
| `iendswith`     | Case-insensitive ends with                                     |
| `date`          | Matches a date                                                 |
| `time`          | Matches a time (for datetimes)                                 |
| `day`           | Matches a day of the month (1-31)                              |
| `month`         | Matches a month                                                |
| `year`          | Matches a year                                                 |
| `range`         | Match between                                                  |

### Least Used

| Lookup Type     | Description                                                    |
|-----------------|----------------------------------------------------------------|
| `regex`         | Matches a regular expression                                   |
| `iregex`        | Case-insensitive regular expression match                      |
| `hour`          | Matches an hour (for datetimes)                                |
| `minute`        | Matches a minute (for datetimes)                               |
| `second`        | Matches a second (for datetimes)                               |
| `week`          | Matches a week number (1-53)                                   |
| `week_day`      | Matches a day of the week (1-7, with 1 being Sunday)           |
| `iso_week_day`  | Matches an ISO 8601 day of the week (1-7, with 1 being Monday) |
| `quarter`       | Matches a quarter of the year (1-4)                            |
| `iso_year`      | Matches an ISO 8601 year            


## Querying Related Objects
    ● Select Related for Foreign Key:
    ModelName.objects.select_related('related_name').all()

    ● Prefetch Related for Many-to-Many or Reverse Foreign Key:
    ModelName.objects.prefetch_related('related_name').all()
    By: Waleed Mousa

    ● Filter on Related Fields:
    ModelName.objects.filter(related_name__field=value)

    ● Chaining Filters on Related Fields:
    ModelName.objects.filter(related_name__field1=value1,
    related_name__field2=value2)

    ● Related Fields Greater/Less Than:
    ModelName.objects.filter(related_name__field__gt=value)


## Aggregation and Annotation
    Aggregation --> compute summary statistics or calculations over a set of records in a QuerySet. Count, Sum, Avg, Min, Max
    Example:
    total_price = Book.objects.aggregate(total_price=Sum('price'))
    print(total_price)  # Output: {'total_price': 12345.67}

    Annotation -->  Add additional information to each object in the QuerySet based on calculations. Adds new columns to each row in the QuerySet with its calculated value.
    Example:
    books = Book.objects.annotate(discounted_price=F('price') * 0.9)
    for book in books:
        print(f"{book.title} - Discounted Price: {book.discounted_price}")

    publishers = Publisher.objects.annotate(num_books=Count('book'))
    for publisher in publishers:
        print(f"{publisher.name} has {publisher.num_books} books")


## Complex Queries with Q Objects
    ● AND Conditions: ModelName.objects.filter(Q(field1=value1) &
    Q(field2=value2))

    ● OR Conditions: ModelName.objects.filter(Q(field1=value1) |
    Q(field2=value2))

    ● NOT Conditions: ModelName.objects.filter(~Q(field=value))


## Updating and Deleting
    ● Update Records:
    ModelName.objects.filter(attribute=value).update(field=new_value)

    ● Delete Records: ModelName.objects.filter(attribute=value).delete()


## Handling Transactions
    ● Atomic Transactions: with transaction.atomic(): # your operations


## Custom Manager Methods
    ● Custom QuerySet Method in Manager: ModelName.objects.custom_method()

    Raw SQL Queries
    ● Raw SQL Query: ModelName.objects.raw('SELECT * FROM app_modelname')

    Database Functions
    ● Concatenate Fields: ModelName.objects.annotate(new_field=Concat('field1',
    Value(' '), 'field2'))
    ● Length Function:
    ModelName.objects.annotate(text_length=Length('textfield'))
    ● Lower, Upper Functions:
    ModelName.objects.annotate(lower_field=Lower('field'))
    ● Coalesce Function:
    ModelName.objects.annotate(field_or_default=Coalesce('field',
    Value('default')))
    ● Cast Function: ModelName.objects.annotate(cast_field=Cast('char_field',
    IntegerField()))


## Pagination with QuerySets
    ● Paginator: paginator = Paginator(ModelName.objects.all(), 10) # 10 items
    per page


## Conditional Expressions
    By: Waleed Mousa
    ● Case/When: ModelName.objects.annotate(new_field=Case(When(condition,
    then=Value('result')), default=Value('default')))
    ● Conditional Update:
    ModelName.objects.filter(condition).update(field=Case(When(sub_condition,
    then=Value('value')), default=Value('default')))


## Database Schema Queries
    ● Get SQL Schema of a Model:
    str(ModelName.objects.model._meta.sql_schema())


## F Expressions for Dynamic Data Handling
    ● Dynamic Field Operations: ModelName.objects.update(field=F('other_field')
    * 2)


## Database Locking
    ● Select for Update:
    ModelName.objects.select_for_update().filter(attribute=value)


## Extra Queries
    ● Using Extra: ModelName.objects.extra(select={'is_recent': "pub_date >
    '2020-01-01'"})


## Combining QuerySets
    ● Union of QuerySets: qs1.union(qs2)
    ● Intersection of QuerySets: qs1.intersection(qs2)
    ● Difference of QuerySets: qs1.difference(qs2)


## Specific Database Operations
    ● Using Specific Database: ModelName.objects.using('database_name').all()


## Model Instance Creation
    ● Create and Save Instance: instance = ModelName(field=value);
    instance.save()
    ● Create with Objects.create(): instance =
    ModelName.objects.create(field=value)



 ## Advanced Usage of F Expressions
    ● Updating with F Expressions:
    ModelName.objects.update(field=F('other_field') + 1)
    ● Filtering with F Expressions:
    ModelName.objects.filter(field__gt=F('other_field'))



 ## Working with GeoDjango
    ● GeoDjango Distance Filter:
    ModelName.objects.filter(location__distance_lte=(point, D(km=5)))
    ● GeoDjango Area Calculation:
    ModelName.objects.annotate(area=Area('geometry'))


## Model Inheritance Handling
    ● Querying Child Models:
    ParentModel.objects.select_related('childmodel').all()


## Database Index Related Queries
    ● Forcing a Specific Index:
    ModelName.objects.force_index('index_name').filter()


## Query Hints for Optimizations
    ● Using Query Hints: ModelName.objects.using_hint('hint_name').filter()


## Complex Joins and Subqueries
    ● Subquery in QuerySet: subquery =
    Subquery(AnotherModel.objects.filter(relation=F('outer_ref_field')).value
    s('field')[:1])


## Working with JSON Fields
    ● Filtering on JSON Field: ModelName.objects.filter(json_field__key=value)
    ● Querying Inside a JSON Field Array:
    ModelName.objects.filter(json_field__contains=[{'key': 'value'}])


## Raw Queries and Expressions
    ● Using Raw SQL Queries: ModelName.objects.raw('SELECT * FROM
    myapp_modelname WHERE condition')
    ● Raw SQL for Updates: ModelName.objects.raw('UPDATE myapp_modelname SET
    field=value WHERE condition')


## Caching QuerySets
    ● Caching Results of QuerySets: from django.core.cache import cache;
    cache.set('my_key', ModelName.objects.all(), 300)


## Query Optimization Techniques`  
    ● Select Only for Performance: ModelName.objects.only('field1', 'field2')
    By: Waleed Mousa
    ● Defer Fields Not Needed Immediately:
    ModelName.objects.defer('large_field')


## Advanced Date/Time Handling
    ● Truncating Dates: ModelName.objects.annotate(date=Trunc('pub_date',
    'day', output_field=DateField()))
