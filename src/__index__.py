from Models.Soup import Soup

if __name__ == '__main__':
    soup = Soup('art_dailydose')
    soup.destroy_tags('script')
    soup.echo()