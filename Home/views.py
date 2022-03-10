from django.shortcuts import render
import tweepy
import time
import webbrowser
import itertools
import threading
from decouple import config

# Create your views here.

def get_twitter_api():
   auth = tweepy.OAuthHandler(config('api_key'), config('api_secret'))
   auth.set_access_token(config('access_token'), config('access_token_secret'))
   api = tweepy.API(auth, wait_on_rate_limit=True)

   return api


def index(request):
   
   api = get_twitter_api()

   # Post method views
   if request.method == 'POST' and 'tweetPost' in request.POST:
      tweet = request.POST['tweet']
      success = 1
      if len(tweet) == 0 or len(tweet) > 140:
             success = 2
             return render(request, 'index.html', {'success': success})
      else:      
         try:
            api.update_status(tweet)
            success = 1
            return render(request, 'index.html', {'success': success})
         except tweepy.errors.TweepError as error:
            success = 0
            if error.api_code == 187:
               return render(request, 'index.html', {'success': success})
            else:
               raise error
   
      #  Get user
   if request.method == 'POST' and 'userSearch' in request.POST:
      user = request.POST['user']
      user_obj = api.get_user(screen_name=user)
      FollowingStatus = False
      if user_obj.following == True:
         return render(request, 'index.html', {'isFollwer': True, 'name':user})
      else:
         try:
            api.create_friendship(screen_name=user_obj.screen_name)
            FollowingStatus = True
            return render(request, 'index.html', {'FollowingStatus': FollowingStatus,'name':user})
         except  tweepy.errors.TweepyException as error:
            return render(request, 'index.html', {'FollowingStatusError': error})
   
   if request.method == 'POST' and 'DontFollowBack' in request.POST:
      user = api.verify_credentials()
      
      dont_follow_back = DontFollowBack(user.screen_name)
     
      return render(request, 'index.html',{'dont_follow_back':dont_follow_back, 'countOfFollower' :len(dont_follow_back)})
   
   if request.method == 'POST' and 'usernameSearch' in request.POST:
      username = request.POST['username']

      return render(request, 'index.html',{'Followers':''})


   if request.method == 'POST' and 'unfollow' in request.POST:
      alluser = request.POST.getlist('userDontFollow')
      threads = []

      for user in alluser:
         try:
            t = threading.Thread(target=Sleep5Sec)
            t.start()
            threads.append(t)
            api.destroy_friendship(screen_name=user)
         except tweepy.errors.TweepyException as error:
            if error.api_code == 162:
               print('already unfollowed')
            else:
               raise error

      for thread in threads:
         thread.join()

      finish = time.perf_counter()
      print(finish)
  
  
  
   return render(request, 'index.html', {'success': ''})


def tweet(request):

   # Post method views
   if request.method == 'POST' and 'tweetPostForm' in request.POST:
      tweetpost = request.POST['tweetpostbox']

      print(tweetpost)

   return render(request, 'tweet.html')


def Sleep5Sec():
   time.sleep(5)


def DontFollowBack(username):
   api = get_twitter_api()
   user_obj = api.get_user(screen_name=username)

   followers = api.get_follower_ids(user_id=user_obj.id)
   friends = api.get_friend_ids(user_id=user_obj.id)

   dontFollow_id = []

   for friend in friends:
      if friend not in followers:
         dontFollow_id.append(friend)


   followersList = []

   for page in paginate(dontFollow_id, 100):
      results = api.lookup_users(user_id=page)
      for result in results:
         followersList.append(result.screen_name)
      
   return followersList

def paginate(iterable, page_size):
    while True:
        i1, i2 = itertools.tee(iterable)
        iterable, page = (itertools.islice(i1, page_size, None),
                list(itertools.islice(i2, page_size)))
        if len(page) == 0:
            break
        yield page

def DontFollowBackUserName(dontFollow_id):
   api = get_twitter_api()

   dontFollow_username = []

   for user in dontFollow_id:
      dontFollow_username.append(api.get_user(user_id=user).screen_name)

   return dontFollow_username


# def get_followers_id(person):

   #  foloowersid = []
   #  count=0

#     influencer=api.get_user( screen_name=person)
#     influencer_id=influencer.id

#     number_of_followers=influencer.followers_count

#     print("number of followers count : ",number_of_followers,'\n','user id : ',influencer_id)


   #  for i in range(0,number_of_followers):
   #      try:
   #          user=next(status)
   #          foloowersid.append([user])
   #          count += 1
   #      except tweepy.TweepError:
   #          print('error limite of twiter sleep for 15 min')
   #          timestamp = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime())
   #          print(timestamp)
   #          if len(foloowersid)>0 :
   #              print('the number get until this time :', count,'all folloers count is : ',number_of_followers)
   #              foloowersid = []
   #          time.sleep(15*60)
   #          next(status)
   #      except :
   #          print('end of foloowers ', count, 'all followers count is : ', number_of_followers)
   #          foloowersid = []
#     return foloowersid

   

   # client = tweepy.Client(bearer_token=config('bearer_token'), consumer_key=config('api_key'), consumer_secret=config('api_secret'), access_token=config('access_token'), access_token_secret=config('access_token_secret'), wait_on_rate_limit=True)


      # public_tweets = api.home_timeline()
   # user = api.get_user(screen_name='GayanKodX')

   # for tweet in public_tweets:
   #    print(tweet.text)

   # print(user.screen_name)
   # print(user.followers_count)

   # for friend in user.friends():
   #    print(friend.screen_name)

   
   # x = tweepy.Cursor(api.get_followers)


#!Work
   # public_tweets = api.get_oembed('https://twitter.com/ojasvikhurana/status/1486092184176586753?s=20&t=cfd11tR6Smu-EKWFhQg-7Q')

   # for tweet in public_tweets:
   #    print(tweet," : ",public_tweets[tweet],"\n")

#! Get retweeter id 
# retweeter = api.get_retweeter_ids('1486022657443184642')
  
#    print(retweeter)
#    print(len(retweeter))

#! Get retweeter user 
   # retweeter = api.get_retweets('1486022657443184642')

   # for tw in retweeter:
   #       print(tw.user.screen_name)
   #       print(tw.user.name)


   # api.update_status(tweet)
         
   #       if api.update_status(tweet):
   #             return render(request, 'index.html', {'success': success})
   #       else:
   #             success = False
   #             return render(request, 'index.html', {'success': success})


   # client = tweepy.Client(bearer_token=config('bearer_token'), consumer_key=config('api_key'), consumer_secret=config('api_secret'), access_token=config('access_token'), access_token_secret=config('access_token_secret'), wait_on_rate_limit=True)