## Variables static
$url = 'https://api.meaningcloud.com/sentiment-2.1'
$key = '6750539d361ed8c80752e9568d1b762f'

## variables configurable
$srcUrl = 'https://www.moneycontrol.com/news/business/sbi-changes-names-ifsc-codes-of-nearly-1300-branches-check-if-your-branch-is-on-the-list-2886091.html'

## meaningcloud api
$var = Invoke-RestMethod -uri "${url}?key=${key}&of=json&url=${srcUrl}&lang=en"
$var
#$var.score_tag
#$var.confidence