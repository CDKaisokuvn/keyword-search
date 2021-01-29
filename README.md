# keyword-django-first-app

### API

1. `/api/keyword`

Method: `Post`
Data: 
* kw[]:
  * Type: array of strings
  * Examples: Keyword Planner, Best Keyword Tool.
  * List of keywords to get data for. You can query up to 100 keywords at a time. 
  
* country:
  * Type: string
  * Examples: us, nz.
  * The country to get metrics for. If not specified, global data is shown. Get the full list of countries supported by calling the countries endpoint. 
 * currency:
   * Type: string
   * Examples: usd, gbp.
   * The currency to use. The currencies endpoint returns a list of supported currencies. 
 * dataSource:
   * Type: string
   * Available values: gkp, cli.
   * If gkp is chosen then we show data only from Google Keyword Planner. If cli is chosen then we show data from Google Keyword Planner & Clickstream data. 
