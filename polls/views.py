from django.shortcuts import render
from polls.models import Question, Choice
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from django.urls import reverse

def index(request):
    latest_question_list=Question.objects.order_by("-pub_date")[:5]
    output=", ".join([q.question_text for q in latest_question_list])

    template=loader.get_template("polls/index.html")
    context={"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context,request))



def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"polls/details.html",{"question":question})
    

def results(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    
    return render(request,"polls/resutls.html",{"question":question})

def vote(request, question_id):

    question=get_object_or_404(Question,pk=question_id)
    try:
        selectecd_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/details.html",
            {
                "question":question,
                "error_message":"you didn't select a choice"
            }
        )
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


