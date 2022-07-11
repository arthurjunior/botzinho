import tweepy
import time

#keys e token da api dp twitter para dar acesso a conta pelo codigo
auth = tweepy.OAutHandler("RXv2Kthb2RHTFDgsp9fMOGwMu","kOdDq4IDWQpOngvb6FcU2FfR7k5Sfmc6OkKcKHivH5bdGHt10B")
auth.set_acess_token("1546240167744360454-k6Y7sHy7b2qWvwfzZfbuV7h0Dkr2qd","eLfWHDe0o5HHfjGaLBuTyJAqKz0o5i7ZWQ9bHrzaqImfz")
#limite de vezes que o bot retuita
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()

#variavel de busca da api
search = ""

#numero de tweet maximo
numberTweets = 100

#loping para ficar pesquisando os twit e cursor ( que recebe um metodo e um parametro da propia API)
for tweet in tweepy.Cursor(api.serach, search).items(numberTweets):
    try:
        #mensagem pra verificar no console se esta funcionado
        print('tweet retuitado e favoritado')
        tweet.retweet()
        tweepy.favorite()
        time.sleep(60)
     except tweepy.TweetError as e:   
        print(e.reason)
     except StopIteration 
        break  
