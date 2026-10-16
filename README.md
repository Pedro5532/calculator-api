# Calculator API Docs
## CURL Examples
<code>
~ $ curl "pedro5532.pythonanywhere.com/api/calculate/add?firstNumber=6&amp;secondNumber=8"
14
~ $ curl "pedro5532.pythonanywhere.com/api/calculate/subtract?firstNumber=9&amp;secondNumber=14"
-5
~ $ curl "pedro5532.pythonanywhere.com/api/calculate/multiply?firstNumber=-3&amp;secondNumber=2"
-6
~ $ curl "pedro5532.pythonanywhere.com/api/calculate/divide?firstNumber=128&amp;secondNumber=16"
8
~ $ curl "pedro5532.pythonanywhere.com/api/calculate/power?firstNumber=2&amp;secondNumber=10"
1024
</code>
## Endpoints
<code>/api/calculate/add</code></br>
<code>/api/calculate/subtract</code></br>
<code>/api/calculate/multiply</code></br>
<code>/api/calculate/divide</code></br>
<code>/api/calculate/power</code></br>
## Error codes
200: success
403: forbidden(happens when powering by numbers higher that 1000)
404: bad request(happens when param/params is/are missing or isn't/aren't numbers)
404: not found
422: unprocessable content(happens when dividing by 0)
## Required request params
<code>firstNumber</code>
<code>secondNumber</code>
