#!/usr/bin/env python3
from Soup import Soup
from Helpers import Helpers

if __name__ == '__main__':
    soup = Soup('art_dailydose')

    username = soup.find_many('h2', '_aacl _aacs _aact _aacx _aada')[0].text
    name = soup.find_many('span', '_aacl _aacp _aacw _aacx _aad7 _aade')[0].text
    photo = soup.find_many('img', 'x6umtig x1b1mbwd xaqea5y xav7gou xk390pu x5yr21d xpdipgo xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x11njtxf xh8yej3')[0].attrs['src']
    rating = soup.find_many('span', '_ac2a')
    total_posts = int(Helpers.replace(',', '', rating[0].span.text))
    followers = int(Helpers.replace(',', '', rating[1].attrs['title']))
    followed = int(Helpers.replace(',', '', rating[2].span.text))
    
    ugly_posts = soup.find_many('div', '_aabd _aa8k _aanf')[:6]

    posts = map(
        lambda post: post.a.div.select(f'div._aagv')[0].img.attrs['src'],
        ugly_posts
    )
    
    state = {
        'username': username,
        'name': name,
        'photo': photo,
        'rating': {
            'posts': total_posts,
            'followers': followers,
            'followed': followed
        },
        'posts': list(posts)
    }

    print(state)
