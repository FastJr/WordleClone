from django.shortcuts import render
from django.http import HttpResponse
from urllib.request import urlopen
from .utils import get_random_word

# mit_website_text = urlopen("https://www.mit.edu/~ecprice/wordlist.10000").read()
# WORDS = mit_website_text.splitlines()
# for i in range(len(WORDS)):
#     print(WORDS[i].decode('utf-8'))

# Create your views here.
def gurdle(request):
    mit_website_text = urlopen("https://www.mit.edu/~ecprice/wordlist.10000").read()
    WORDS = mit_website_text.splitlines()
    decoded_words = [word.decode('utf-8') for word in WORDS]
    random_word = get_random_word(decoded_words)
    return render(request, 'gurdle.html', {'WORDS': decoded_words, 'RandomWord': random_word})
