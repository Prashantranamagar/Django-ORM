# Django QuerySets

## Basic Queries

- **Retrieve All Records:** `ModelName.objects.all()`
- **Retrieve a Single Record:** `ModelName.objects.get(id=1)`
- **Filter Records:** `ModelName.objects.filter(attribute=value)`
- **Exclude Records:** `ModelName.objects.exclude(attribute=value)`
- **Order Records:** `ModelName.objects.order_by('attribute')`
- **Chain Filters:** `ModelName.objects.filter().exclude().order_by()`
- **Limit QuerySet:** `ModelName.objects.all()[:10]`

## QuerySet Methods

- **all()** – Retrieve all records.
- **filter()** – Filter search to return only rows that match the search term.
- **values()** – Return each object as a Python dictionary.
- **value_set()** – Return only the specified columns.
- **order_by('-attribute')** – Order in descending order.
- **order_by('attribute')** – Order in ascending order.

## Field Lookups

- **Exact Match:** `attribute__exact=value`
- **Date Queries:** `attribute__date=date(YYYY, MM, DD)`
- **Year, Month, Day Queries:** `attribute__year=YYYY`

### Lookup Types

- `contains` – Contains the phrase
- `icontains` – Case-insensitive contains
- `date` – Matches a date
- `day` – Matches a day of the month (1-31)
- `endswith` – Ends with
- `iendswith` – Case-insensitive ends with
- `exact` – An exact match
- `iexact` – Case-insensitive exact match
- `in` – Matches one of the values
- `isnull` – Matches NULL values
- `gt` – Greater than
- `gte` – Greater than or equal to
- `hour` – Matches an hour (for datetimes)
- `lt` – Less than
- `lte` – Less than or equal to
- `minute` – Matches a minute (for datetimes)
- `month` – Matches a month
- `quarter` – Matches a quarter of the year (1-4)
- `range` – Match between
- `regex` – Matches a regular expression
- `iregex` – Case-insensitive regular expression match
- `second` – Matches a second (for datetimes)
- `startswith` – Starts with
- `istartswith` – Case-insensitive starts with
- `time` – Matches a time (for datetimes)
- `week` – Matches a week number (1-53)
- `week_day` – Matches a day of the week (1-7, with 1 being Sunday)
- `iso_week_day` – Matches an ISO 8601 day of the week (1-7, with 1 being Monday)
- `year` – Matches a year
- `iso_year` – Matches an ISO 8601 year
