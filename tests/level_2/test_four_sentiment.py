import pytest

from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.mark.parametrize(
    'text,expected,id',
    [
        ('dislike slow bugs frustration', 'BAD', 'negative'),
        ('love caring', 'GOOD', 'positive'),
        ('Coming Home Learn more', None, 'neutral'),
    ],
)
def test__check_tweet_sentiment(text, good_words, bad_words, expected, id):
    assert check_tweet_sentiment(
        text=text,
        good_words=good_words,
        bad_words=bad_words
    ) == expected
