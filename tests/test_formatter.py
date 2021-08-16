import pytest


@pytest.mark.timeout(1)
def test_box_abbreviates_long_words():
    from text_formatter import formatter
    formatter.box('..........'
                  '..........'
                  '..........'
                  '..........'
                  '..........'
                  '..........'
                  '..........'
                  '..........'
                  '..........'
                  '..........')