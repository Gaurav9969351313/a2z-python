## Variables static
$apiKeyNewsApi = '31f7c625c967479087b3472e0481ec30'
$urlNewsApi = 'https://newsapi.org/v2/everything'

## variables configurable
$scriptName = 'SBI'
$srcs = 'indiatimes.com,moneycontrol.com'
$from = '2018-08-27'
$to = '2018-08-29'

## NewsApi.org API
$news_var = Invoke-RestMethod -uri "${urlNewsApi}?q=${scriptName}&county=in&from=${from}&to=${to}&sortBy=publishedAt&domains=${srcs}&apiKey=${apiKeyNewsApi}"

## Output
$publishedAt = $news_var.articles.publishedAt
$urlArticles = $news_var.articles.url

$1_publishedAt = $publishedAt[0]
$1_urlArticles = $urlArticles[0]

########################################################################################

## Variables static
$urlMeaningCloud = 'https://api.meaningcloud.com/sentiment-2.1'
$apiKeyMeaningCloud = '6750539d361ed8c80752e9568d1b762f'

## meaningcloud api
$1_mean = Invoke-RestMethod -uri "${urlMeaningCloud}?key=${apiKeyMeaningCloud}&of=json&url=${1_urlArticles}&lang=en"

$1_sentiment = $1_mean.score_tag
$1_confidence = $1_mean.confidence

########################################################################################

$query = @"
insert into sentimentTag
values ('$scriptName', '$1_urlArticles', '$1_publishedAt', '$1_confidence', '$1_sentiment')
go
"@

Invoke-Sqlcmd -Database SentiMenti -ServerInstance localhost -Username odin -Password odin -Query $query



