import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch A list of words from a URL"""
    story = urlopen(url)
    story_word = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_word.append(word)
    story.close()

def print_items(story_word):
    for word in story_word:
        print(word)

def main(url):  
    # if not url:
    #    url = 'http://sixty-north.com/c/t.txt'
    words = fetch_words(url)
    print_items(words)

if __name__ == "__main__":
    main(sys.argv[1])