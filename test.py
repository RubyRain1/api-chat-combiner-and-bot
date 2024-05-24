from twitchio.ext import pubsub
import config
user_token = config.api_key
user_channel_id = config.user_id
topic = pubsub.channel_points(user_token)[user_channel_id]