$apiUrl = 'http://api.meaningcloud.com/summarization-1.0'
$apiKey = '6750539d361ed8c80752e9568d1b762f'
$urlForSummarization = 'https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx'
$numberSentences = '5'

$var = Invoke-RestMethod "${apiUrl}?key=${apiKey}&url=${urlForSummarization}&sentences=${numberSentences}"
$var.summary

