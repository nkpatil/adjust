# Adjust Assignment
The task is to expose the sample dataset through a single generic HTTP API which is capable of filtering, grouping and sorting.

#### Client of this API should be able to:

- filter by time range (date_from / date_to is enough), channels, countries, operating systems
- group by one or more columns: date, channel, country, operating system
- sort by any column in ascending or descending order
- see derived metric CPI (cost per install) which is calculated as cpi = spend / installs

### Common API use-cases:

1. Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.
   API: http://localhost:8000/api/v1/data/?selection_fields=impressions__sum,clicks__sum&grouping_fields=channel,country&date__lte=2017-06-01&ordering=-clicks
   

2. Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.
   API: http://localhost:8000/api/v1/data/?selection_fields=installs__sum&grouping_fields=date&os=ios&date__gte=2017-05-01&date__lt=2017-06-01&ordering=date


3. Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.
   API: http://localhost:8000/api/v1/data/?selection_fields=revenue__sum&grouping_fields=os&country=US&date=2017-06-01&ordering=-revenue

4. Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order.
   API: http://localhost:8000/api/v1/data/?selection_fields=cpi_val__sum,spend__sum&grouping_fields=channel&country=CA&ordering=-cpi_val


### Below are the few points to understand the implementationa and usage:
- Extra calculated field cpi (spend/installs) is used as cpi_val.
- Logics defined for group by are: sum, avg, count, min, max. We can define more by using the logic_dict.
  ```
      logic_dict = {
          'avg': Avg,
          'sum': Sum,
          'count': Count,
          'max': Max,
          'min': Min
      }
- for group by feature, custom handling is done and used selection_fields(comma separated values with field and logic separated by '__') and grouping_fields (comma separated fields to be used for grouping). Example can be seen in the above APIs.
- For ordering acending and decending of fields, ordering=<field_name> can be used for acending and ordering=-<field_name> can be used for decending.
- requirements.txt contains the dependencies to run the project.
- import-export is used to import and export the bulk data into database tables. this is configured in admin.py

#### Filters:
- `COMPARE_FILTERS = ['lte', 'gte', 'lt', 'gt', 'exact']`
  where lt/lte => less than / less than equal to,
  gt/gte => greater than / greater than equal to,
  exact => exact value
  
- `MATCH_FILTERS = ['exact', 'in']` where 'in' is to check search filter in the list.

- date field is configured as compare filters and channelm country and os are configured as match filters.

