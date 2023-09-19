import pytest

from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.mark.parametrize(
    'text,expected',
    [
        ('dislike slow bugs frustration', 'BAD'),
        ('love caring', 'GOOD'),
        ('Coming Home Learn more', None),
    ],
)
def test__check_tweet_sentiment(text, good_words, bad_words, expected):
    assert check_tweet_sentiment(text, good_words, bad_words) == expected
