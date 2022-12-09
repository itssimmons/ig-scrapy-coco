#!/usr/bin/env python3

from Models.Soup import Soup

if __name__ == '__main__':
    soup = Soup('art_dailydose')
    h2 = soup.find('h2', '_aacl _aacs _aact _aacx _aada')
    print('HOLA')
