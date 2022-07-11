import tweepy
import time

#keys e token da api dp twitter para dar acesso a conta pelo codigo
auth = tweepy.OAuthHandler("RXv2Kthb2RHTFDgsp9fMOGwMu","kOdDq4IDWQpOngvb6FcU2FfR7k5Sfmc6OkKcKHivH5bdGHt10B")
auth.set_access_token("1546240167744360454-k6Y7sHy7b2qWvwfzZfbuV7h0Dkr2qd","eLfWHDe0o5HHfjGaLBuTyJAqKz0o5i7ZWQ9bHrzaqImfz")
#limite de vezes que o bot retuita
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()

#variavel de busca da api
search = "2022"

#numero de tweet maximo
numberTweets = 100

#loping para ficar pesquisando os twit e cursor ( que recebe um metodo e um parametro da propia API)
for tweet in tweepy.Cursor(api.search, search).items(numeroDeTweets):
    try:
        print('tweet retuitado e favoritado')
        tweet.retweet()
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
