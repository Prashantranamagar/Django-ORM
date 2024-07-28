"""
Django ORM Optimization Tips

"""

"""

Use Djagno tool bar for monitering query performance.
Use filter and exclude instead of filtering using python code.
Use selected_related for 1to1 and foreign key relation and prefetch related for many to many and  one to many i.e.reverse foreignkey when you need everything.
Use F expression to update values.
Avoid database query in a loop
Use Aggregate funciton. for calculation min, max, avg, sum etc
use value_list to retrive selected column only.
Use defer() and only() when you know you won't need certain fields.
Use count() and exists() when you don't need the contents of the QuerySet.
Use bulk_create() when possible.



"""


# ---------------------------------------------------------------------------
# 1. Profile
# ---------------------------------------------------------------------------

## Use these tools:
## * django-debug-toolbar
## * QuerySet.explain()


# ---------------------------------------------------------------------------
# 2. Be aware of QuerySet's lazy evaluation.
# ---------------------------------------------------------------------------

## 2a. When QuerySets are evaluated

# Iteration
for person in Person.objects.all():
    # Some logic

# Slicing/Indexing
Person.objects.all()[0]

# Pickling (i.e. serialization)
pickle.dumps(Person.objects.all())

# Evaluation functions
repr(Person.objects.all())
len(Person.objects.all())
list(Person.objects.all())
bool(Person.objects.all())

# Other
[person for person in Person.objects.all()]  # List comprehensions
person in Person.objects.all()  # `in` checks

## 2b. When QuerySets are cached/not cached

### Not Cached

# Not reusing evaluated QuerySets
print([p.name for p in Person.objects.all()])  # QuerySet evaluated and cached
print([p.name for p in Person.objects.all()])  # New QuerySet is evaluated and cached

# Slicing/indexing unevaluated QuerySets
queryset = Person.objects.all()
print(queryset[0])  # Queries the database
print(queryset[0])  # Queries the database again

# Printing
print(Person.objects.all())

### Cached

# Reusing an evaluated QuerySet
queryset = Person.objects.all()
print([p.name for p in queryset])  # QuerySet evaluated and cached
print([p.name for p in queryset])  # Cached results are used

# Slicing/indexing evaluated QuerySets
queryset = Person.objects.all()
list(queryset)  # Queryset evaluated and cached
print(queryset[0])  # Cache used
print(queryset[0])  # Cache used


# ---------------------------------------------------------------------------
# 3. Be aware of which attributes are not cached.
# ---------------------------------------------------------------------------

## Not initially retrieved/cached

# Foreign-key related objects
person = Person.objects.get(id=1)
person.father  # foreign object is retrieved and cached
person.father  # cached version is used

## Never cached

# Callable attributes
person = Person.objects.get(id=1)
person.children.all()  # Database hit
person.children.all()  # Another database hit


# ---------------------------------------------------------------------------
# 4. Use select_related() and prefetch_related() when you will need everything.
# ---------------------------------------------------------------------------

# DON'T
queryset = Person.objects.all()
for person in queryset:
    person.father  # Foreign key relationship results in a database hit each iteration

# DO
queryset = Person.objects.all().select_related('father')  # Foreign key object is included in query and cached
for person in queryset:
    person.father  # Hits the cache instead of the database


# ---------------------------------------------------------------------------
# 5. Try to avoid database queries in a loop.
# ---------------------------------------------------------------------------

# DON'T (contrived example)
filtered = Person.objects.filter(first_name='Shallan', last_name='Davar')
for age in range(18):
    person = filtered.get(age=age)  # Database query on each iteration

# DO (contrived example)
filtered = Person.objects.filter(  # Narrow down the QuerySet to only what you need
    first_name='Shallan',
    last_name='Davar',
    age_gte=0,
    age_lte=18,
)
lookup = {person.age: person for person in filtered}  # Evaluate the QuerySet and construct lookup
for age in range(18):
    person = lookup[age]  # No database query


# ---------------------------------------------------------------------------
# 6. Use iterator() to iterate through a very large QuerySet only once.
# ---------------------------------------------------------------------------

# Save memory by not caching anything
for person in Person.objects.iterator():
    # Some logic


# ---------------------------------------------------------------------------
# 7. Do work in the database rather than in Python.
# ---------------------------------------------------------------------------

## 7a. Use filter() and exclude()

# DON'T
for person in Person.objects.all():
    if person.age >= 18:
        # Do something

# DO
for person in Person.objects.filter(age__gte=18):
    # Do something

## 7b. Use F expressions

# DON'T
for person in Person.objects.all():
    person.age += 1
    person.save()

# DO
Person.objects.update(age=F('age') + 1)

## 7c. Do aggregation in the database, if possible

# DON'T
max_age = 0
for person in Person.objects.all():
    if person.age > max_age:
        max_age = person.age

# DO
max_age = Person.objects.all().aggregate(Max('age'))['age__max']


# ---------------------------------------------------------------------------
# 8. Use values() and values_list() to get only the things you need.
# ---------------------------------------------------------------------------

## 8a. Use values()

# DON'T
age_lookup = {
    person.name: person.age
    for person in Person.objects.all()
}

# DO
age_lookup = {
    person['name']: person['age']
    for person in Person.objects.values('name', 'age')
}

## 8b. Use values_list()

# DON'T
person_ids = [person.id for person in Person.objects.all()]

# DO
person_ids = Person.objects.values_list('id', flat=True)


# ---------------------------------------------------------------------------
# 9. Use defer() and only() when you know you won't need certain fields.
#
# * Use when you need a QuerySet instead of a list of dicts from values().
# * Really only useful to defer fields that require significant processing to convert to a python object.
# ---------------------------------------------------------------------------

## 9a. Use defer()

queryset = Person.objects.defer('age')  # Imagine age is computationally expensive
for person in queryset:
    print(person.id)
    print(person.name)

## 9b. Use only()

queryset = Person.objects.only('name')
for person in queryset:
    print(person.name)


# ---------------------------------------------------------------------------
# 10. Use count() and exists() when you don't need the contents of the QuerySet.
#
# * Caveat: Only use these when you don't need to evaluate the QuerySet.
# ---------------------------------------------------------------------------

## 10a. Use count()

# DON'T
count = len(Person.objects.all())  # Evaluates the entire queryset

# DO
count = Person.objects.count()  # Executes more efficient SQL to determine count

## 10b. Use exists()

# DON'T
exists = len(Person.objects.all()) > 0

# DO
exists = Person.objects.exists()


# ---------------------------------------------------------------------------
# 11. Use delete() and update() when possible.
# ---------------------------------------------------------------------------

## 11a. Use delete()

# DON'T
for person in Person.objects.all():
    person.delete()

# DO
Person.objects.all().delete()

## 11b. Use update()

# DON'T
for person in Person.objects.all():
    person.age = 0
    person.save()

# DO
Person.objects.update(age=0)


# ---------------------------------------------------------------------------
# 12. Use bulk_create() when possible.
#
# * Caveats: https://docs.djangoproject.com/en/2.1/ref/models/querysets/#django.db.models.query.QuerySet.bulk_create
# ---------------------------------------------------------------------------

# Bulk Create
names = ['Jeff', 'Beth', 'Tim']
creates = []
for name in names:
    creates.append(
        Person(name=name, age=0)
    )
Person.objects.bulk_create(creates)

# Bulk add to many-to-many fields
person = Person.objects.get(id=1)
person.jobs.add(job1, job2, job3)


# ---------------------------------------------------------------------------
# 13. Use foreign key values directly.
# ---------------------------------------------------------------------------

# DON'T
father_id = Person.objects.get(id=1).father.id  # Causes a needless database query

# DO
father_id = Person.objects.get(id=1).father_id  # The foreign key is already cached. No query