## Variables static
$apiKeyNewsApi = '31f7c625c967479087b3472e0481ec30'
$urlNewsApi = 'https://newsapi.org/v2/everything'

## variables configurable
$scriptName = 'SBI'
$srcs = 'indiatimes.com,moneycontrol.com'
$from = '2018-08-27'

## NewsApi.org API
$news_var = Invoke-RestMethod -uri "${urlNewsApi}?q=${scriptName}&county=in&sortBy=publishedAt&from=${from}&domains=${srcs}&apiKey=${apiKeyNewsApi}"

$publishedAt = $news_var.articles.publishedAt
$urlArticles = $news_var.articles.url

$urlCount = $urlArticles.count

foreach($newsUrls in $urlCount){

## Variables static
$urlMeaningCloud = 'https://api.meaningcloud.com/sentiment-2.1'
$apiKeyMeaningCloud = '6750539d361ed8c80752e9568d1b762f'

## meaningcloud api
$mean = Invoke-RestMethod -uri "${urlMeaningCloud}?key=${apiKeyMeaningCloud}&of=json&url=${urlArticles}&lang=en"

$sentiment = $mean.score_tag
$confidence = $mean.confidence

for($i=1;$i -lt $urlCount){

write-host $urlArticles[$i],$sentiment, $confidence, $publishedAt[$i]
$finalDate = $publishedAt[$i]
$finalUrl =  $urlArticles[$i]
$searchID = Get-Date -UFormat "%d%m%y%H%M"
$query = @"
insert into sentimentTag
values ('$scriptName', '$finalUrl','$finalDate', $confidence,'$sentiment',0,$searchID)
go
"@

Invoke-Sqlcmd -Database SentiMenti -ServerInstance localhost -Username odin -Password odin -Query $query


$i = $i + 1
}

}

########################################################################################






