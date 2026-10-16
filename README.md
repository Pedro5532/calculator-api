# Calculator API Docs
## CURL Examples

<code>~ $ curl "pedro5532.pythonanywhere.com/api/calculate/add?firstNumber=6&amp;secondNumber=8"
14
~ $ curl "pedro5532.pythonanywhere.com/api/calculate/subtract?firstNumber=9&amp;secondNumber=14"
-5
~ $ curl "pedro5532.pythonanywhere.com/api/calculate/multiply?firstNumber=-3&amp;secondNumber=2"
-6
~ $ curl "pedro5532.pythonanywhere.com/api/calculate/divide?firstNumber=128&amp;secondNumber=16"
8
~ $ curl "pedro5532.pythonanywhere.com/api/calculate/power?firstNumber=2&amp;secondNumber=10"
1024</code>

## Endpoints

<code>/api/calculate/add</code>
<code>/api/calculate/subtract</code>
<code>/api/calculate/multiply</code>
<code>/api/calculate/divide</code>
<code>/api/calculate/power</code>

## Error codes

<code>200</code>: success

<code>403</code>: forbidden(happens when powering by numbers higher that 1000)

<code>404</code>: bad request(happens when param/params is/are missing or isn't/aren't numbers)

<code>404</code>: not found

<code>422</code>: unprocessable content(happens when dividing by 0)

## Required request params

<code>firstNumber</code>
<code>secondNumber</code>
