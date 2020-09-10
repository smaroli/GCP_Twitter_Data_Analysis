import tweepy as tw
from google.cloud import pubsub_v1
import json

consumer_key= 'Input_key_twitter_developer_account'
consumer_secret= 'Input_key_twitter_developer_account'
access_token= 'Input_key_twitter_developer_account'
access_token_secret= 'Input_key_twitter_developer_account'
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)



class MyStreamListener(tw.StreamListener):
	client = pubsub_v1.PublisherClient()
	topic_path = client.topic_path('windy-backbone-267320', 'twitter')
	def on_status(self, status):
		#print(status._json.keys())
		#if 'retweeted_status' in status._json.keys():
			#print('yes')
		#else:
			#print('no')

		if 'retweeted_status' in status._json.keys():
			text = status.text
			retweets = status.retweet_count
			is_retweeted_text = True
			orig_text = status.retweeted_status.text
			retweets_orig = status.retweeted_status.retweet_count
			created_on = status.created_at.strftime("%m/%d/%Y")
			source = status.source
			user = status.user.name
			user_verified = status.user.verified
			loc = status.user.location
			bio = status.user.description
			twdict = dict(text=text,retweets=retweets,is_retweeted_text=is_retweeted_text,orig_text=orig_text,retweets_orig=retweets_orig,created_on=created_on,source=source,username=user,user_verified=user_verified,userlocation=loc,userbio=bio)
			twjson = json.dumps(twdict)
			print(twjson)
			#twencode = base64.urlsafe_b64encode(bytearray(twjson, 'utf-8'))
			twencode = twjson.encode('utf-8')
			self.client.publish(self.topic_path, data=twencode)
			print("done")
		else:
			text = status.text
			retweets = status.retweet_count
			is_retweeted_text = False
			orig_text = ''
			retweets_orig = status.retweet_count
			created_on = status.created_at.strftime("%m/%d/%Y")
			source = status.source
			user = status.user.name
			user_verified = status.user.verified
			loc = status.user.location
			bio = status.user.description
			twdict = dict(text=text,retweets=retweets,is_retweeted_text=is_retweeted_text,orig_text=orig_text,retweets_orig=retweets_orig,created_on=created_on,source=source,username=user,user_verified=user_verified,userlocation=loc,userbio=bio)
			twjson = json.dumps(twdict)
			print(twjson)
			#twencode = base64.urlsafe_b64encode(bytearray(twjson, 'utf-8'))
			twencode = twjson.encode('utf-8')
			self.client.publish(self.topic_path, data=twencode)
			print("done")
		

myStream = tw.Stream(auth = api.auth, listener=MyStreamListener(),tweet_mode="extended")
myStream.filter(track=['moet hennesssey','lvmh','#moethennessey','#lvmh','wine'])
