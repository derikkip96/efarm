from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render,get_object_or_404
from django.contrib.contenttypes.models import ContentType
from .models import Post,Question,Answer
from . forms import QuestionForm,AnswerForm
from comment.models import Comment
from comment.forms import CommentForm
from django.views.generic  import RedirectView


# Create your views here.
def postView(request,post_ids=None):
    posts = Post.objects.all()
    questions = Question.objects.all()
    new_questions=Question.objects.order_by('-asked')[0:4]


    # pagination
    paginator = Paginator(questions, 10)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    if request.method =='POST':
        Q_form=QuestionForm(request.POST)
        if Q_form.is_valid():
            cd = Q_form.cleaned_data
            Q_form.save()

    else:
        Q_form=QuestionForm()

    return render(request, 'forum/blog.html', {'posts': posts,
                                               'Q_form':Q_form,
                                               'questions':questions,
                                               'new_questions':new_questions,
                                               }
                  )

def QuestionDetails(request,Q_id=None):
    question=get_object_or_404(Question,id=Q_id)
    # list of all answers to this question
    # answering question
    content_type = ContentType.objects.get_for_model(Question)
    obj_id = Q_id
    initial_data = {
        "content_type": question.content_type,
        "object_id":question.id
    }
    answers= Answer.objects.filter(content_type=content_type, object_id=obj_id)
    if request.method =='POST':
        # an answer has been posted
        A_form = AnswerForm(request.POST or None ,initial=initial_data)
        if A_form.is_valid()and request.user.is_authenticated:
            cd = A_form.cleaned_data.get("content_type")
            contnt_type = ContentType.objects.get(model=cd)
            obj_id = A_form.cleaned_data.get("object_id")
            content_data = A_form.cleaned_data.get("body")
            new_answer, created = Answer.objects.get_or_create(user=request.user,
                                                                 content_type=contnt_type,
                                                                 object_id=obj_id,
                                                                 body=content_data
                                                                 )
            if created:
                A_form = AnswerForm()

    return render(request,'forum/blog.html',{'question':question,
                                                'answers':answers}
                  )
def postDetails(request,post_id=None):
    post=get_object_or_404(Post,id=post_id)
    # using comments inside post
    content_type=ContentType.objects.get_for_model(Post)
    obj_id =post_id
    initial_data={
        "content_type":post.get_content_type,
        "object_id":post.id
    }
    Comment_form = CommentForm(request.POST or None,initial=initial_data)
    # add authentication later
    if Comment_form.is_valid() and request.user.is_authenticated:
        c_type=Comment_form.cleaned_data.get("content_type")
        contnt_type=ContentType.objects.get(model=c_type)
        obj_id= Comment_form.cleaned_data.get("object_id")
        content_data=Comment_form.cleaned_data.get("body")
        new_comment,created=Comment.objects.get_or_create(user=request.user,
                                                          content_type=contnt_type,
                                                          object_id=obj_id,
                                                          body=content_data
                                                          )
        if created:
            Comment_form=CommentForm()
    comments = Comment.objects.filter(content_type=content_type,object_id=obj_id)
    return render(request,'forum/detail.html',{'post':post,
                                               'comments':comments,
                                               'Comment_form':Comment_form})
class PostLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        id=self.kwargs.get("id")
        obj=get_object_or_404(Post,id=id)
        url_=obj.get_absolute_url()
        user=self.request.user
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)
        return url_
