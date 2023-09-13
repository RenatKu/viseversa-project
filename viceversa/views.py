# from django.http import HttpResponse
from django.shortcuts import render

# def about(request):
# 	return HttpResponse('This is about page')

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	# print(test_get_text)
	reversed_text = user_text[::-1]
	len_split_text_rev = len(reversed_text.split(' '))
	text_n_words = 'Original text  has {}'.format(len_split_text_rev) + ' words'
	print(text_n_words)
	return render(request, 'reverse.html', {'usertext': user_text, 'textnwords':text_n_words,  'reversedtext': reversed_text})

