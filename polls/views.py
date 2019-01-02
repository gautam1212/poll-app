from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'question_list'

	def get_queryset(self):
		return Question.objects.all()

# def index(request):
	# questions = Question.objects.all()
	# return render(request, 'polls/index.html', {'question_list': questions})

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

# def detail(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/detail.html', {'question': question})
    # return HttpResponse("You're looking at question %s." % question_id)

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

# def results(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/results.html', {'question': question})
    # return HttpResponse("You're looking at the results of question %s." % question_id)

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	# print(request.POST['chices'])
	try:
		selected = question.choice_set.get(pk=request.POST['choices'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
		'question': question,
		'error_message': "No choice selected",
		})
	print('ok')
	selected.votes += 1
	selected.save()

	return HttpResponseRedirect(reverse('polls:results',
		args=(question.id,)))

    # return HttpResponse("You're voting on question %s." % question_id)
