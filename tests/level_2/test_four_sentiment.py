from functions.level_2.four_sentiment import check_tweet_sentiment


def test__check_tweet_sentiment__negative(bad_words, good_words):
    negative_tweet = "The more I use @salesforce the more I dislike it. It's slow and full of bugs. " \
                     "There are elements of the UI that look like they haven't been updated since 2006. " \
                     "Current frustration: app exchange pages won't stop refreshing every 10 seconds "

    assert check_tweet_sentiment(text=negative_tweet, good_words=good_words, bad_words=bad_words) == 'BAD'


def test__check_tweet_sentiment__positive(bad_words, good_words):
    positive_tweet = "That’s what I love about @salesforce. " \
                     "That it’s about relationships and about caring about people " \
                     "and it’s not only about business and money. " \
                     "Thanks for caring about #TrailblazerCommunity "

    assert check_tweet_sentiment(text=positive_tweet, good_words=good_words, bad_words=bad_words) == 'GOOD'


def test__check_tweet_sentiment__neutral(bad_words, good_words):
    neutral_tweet = "Coming Home: #Dreamforce Returns to San Francisco for 20th Anniversary. " \
                    "Learn more: http://bit.ly/3AgwO0H via @Salesforce"

    assert check_tweet_sentiment(text=neutral_tweet, good_words=good_words, bad_words=bad_words) is None
