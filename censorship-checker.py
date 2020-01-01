import ast
import json

f = open('keywords_china.txt', 'r', encoding="utf-8")
keywords = f.read().splitlines()
f.close()


f = open('tweet4.json', 'r', encoding="utf-8")
tweets_whole = f.read().splitlines()
f.close()

tweets = []
for line in tweets_whole:
    json_data = ast.literal_eval(line)
    tweets.append(json_data['text'])
    
    
print('tweets: ', len(tweets))
print('keywords: ', len(keywords)) 

    
matching = [s for s in tweets if any(xs.lower() in s.lower() for xs in keywords)]
print('Censored tweets: ', len(matching))
print('Censorship level: ', len(matching)/len(tweets) * 100, '%')
