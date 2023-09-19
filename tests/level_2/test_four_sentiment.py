import pytest

from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.mark.parametrize(
    'text,expected',
    [
        pytest.param('dislike slow bugs frustration', 'BAD', id='negative'),
        pytest.param('love caring', 'GOOD', id='positive'),
        pytest.param('Coming Home Learn more', None, id='neutral'),
    ],
)
def test__check_tweet_sentiment(text, good_words, bad_words, expected):
    assert check_tweet_sentiment(
        text=text,
        good_words=good_words,
        bad_words=bad_words
    ) == expected
