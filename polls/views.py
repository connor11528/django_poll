from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Question

# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {
		'latest_question_list': latest_question_list
	})	
	print latest_question_list
	return HttpResponse(template.render(context))

def detail(request, question_id):
	return HttpResponse('you are looking at question {0}'.format(question_id))

def results(request, question_id):
	response = 'This is the results of %s'
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse('you are voting on question %s' % question_id)