import tweepy

consumer_key = 'gTiPLgk2vTDinaqrReBRclXL2 '
consumer_secret = 'eXIAzMG55KzwfhHXX1IYpSJBGTflqD5TBhMDnoy0KtPrLcKhwv'
access_token = '1105856153542635522-ZSIoWLgd4ixD14lBKHUFYoxPBMpk3g'
access_token_secret = '7iHFDm8ddK5eOAnqHt66a8TUyGCmnJiGxD9kvzqWZCU9I '

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter_api = tweepy.API(auth)

print('Logged in as {}'.format(twitter_api.me().name))
Tweets contain a lot of information
https://goo.gl/ogbn3D tweet