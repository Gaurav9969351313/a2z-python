import twitter 

access_token  ="3235720159-F4ILIpW9Cs6EpPrbWdoUhpPjMulWVBPfeeMSM7K"
acess_token_secreat  ="E6lr1ugJW31zubl3pkqcHzVL6T3qYPCSyaEdgojenfarO"
consumer_key  ="EtjeEzlJ34Bm63maJmaHe65Kc"
costumer_secreat  ="GGRkSxCDZVMCerupLswyda8zrSUvHMbASwp1c8Ac5gHYfA6iUf"

t = twitter.Api(consumer_key,costumer_secreat,access_token,acess_token_secreat)
#t.statuses.update(status = "hii this is gaurav from python")
try:
        status = t.PostUpdate("Communication Initiated #Prudent Controls")

except:
        print "Could not post Tweet to Twitter"
pass
