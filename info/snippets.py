from google.appengine.ext import ndb
from tweet import Tweet
class MyUser(ndb.Model):
    USERNAME = ndb.StringProperty()
    NAME = ndb.StringProperty()
    AGE = ndb.IntegerProperty()
    SEX = ndb.StringProperty()
    BIO = ndb.StringProperty()
    COUNTOFFOLLOWERS = ndb.IntegerProperty()
    COUNTOFFOLLOWING = ndb.IntegerProperty()
    BIRTHDATE = ndb.DateProperty()

class TweetHandler(ndb.Model):
    USERNAME= ndb.StringProperty()
    TWEETPROPERTY = ndb.StructuredProperty(Tweet, repeated=True)
    FOLLOWERS = ndb.StringProperty(repeated=True)
    FOLLOWING = ndb.StringProperty(repeated=True)
