import src.media
import pytest


def test_constructor_fail():
    with pytest.raises(ValueError) as e:
        mov = src.media.Movie('title',
                              'my beautiful storyline',
                              'my poster url',
                              'https://www.youtube.com/watch?v=m8e-FF8MsqU')
    assert str(e.value) == 'The object should receive a valid poster URI'

    with pytest.raises(ValueError) as e:
        mov = src.media.Movie('title', 'my beautiful storyline',
                              'https://www.linke.com.br/image.jpg',
                              'trailer link')
    assert str(e.value) == 'The object should receive a valid trailer URI'


def test_constructor_pass():
    mov = src.media.Movie('Matrix',
                          'A computer hacker learns from mysterious rebels about the true nature of his reality '
                          'and his role in the war against its controllers.',
                          'https://www.linke.com.br/image.jpg',
                          'https://www.youtube.com/watch?v=m8e-FF8MsqU')
    title = mov.title
    story = mov.storyline
    poster = mov.poster_image_url
    trailer = mov.trailer_youtube_url
    assert title == 'Matrix'
    assert story == 'A computer hacker learns from mysterious rebels about the true nature of his reality ' \
                    'and his role in the war against its controllers.'
    assert poster == 'https://www.linke.com.br/image.jpg'
    assert trailer == 'https://www.youtube.com/watch?v=m8e-FF8MsqU'
