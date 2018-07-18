from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render,get_object_or_404
from django.contrib.contenttypes.models import ContentType
from .models import Post,Question,Answer
from . forms import QuestionForm,AnswerForm
from comment.models import Comment
from comment.forms import CommentForm
from django.views.generic  import RedirectView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
import rest_framework
from django.shortcuts import redirect


# Create your views here.
def postView(request,q_id=None):
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


def qdetail(request, quiz_id=None):
    question = get_object_or_404(Question, id=quiz_id)
    # using comments inside post
    content_type = ContentType.objects.get_for_model(Question)
    obj_id = quiz_id
    initial_data = {
        "content_type": question.get_content_type,
        "object_id": question.id
    }
    A_form = CommentForm(request.POST or None, initial=initial_data)

    if A_form.is_valid() and request.user.is_authenticated:
        c_type = A_form.cleaned_data.get("content_type")
        contnt_type = ContentType.objects.get(model=c_type)
        obj_id = A_form.cleaned_data.get("object_id")
        content_data = A_form.cleaned_data.get("body")
        new_answer, created = Answer.objects.get_or_create(user=request.user,
                                                             content_type=contnt_type,
                                                             object_id=obj_id,
                                                             body=content_data
                                                             )
        if created:
            A_form = AnswerForm()
    answers = Answer.objects.filter(content_type=content_type, object_id=obj_id)
    return render(request, 'forum/detail/qdetail.html', {'question': question,
                                                         'answers': answers,
                                                         'A_form': A_form}
                  )
# like function


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


class PostLikeApi(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        """
        returnin likes
        """
        id = self.kwargs.get("id")
        obj = get_object_or_404(Post, id=id)
        url_ = obj.get_absolute_url()
        user = self.request.user
        updated=False
        liked=False
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                liked=True
                obj.likes.add(user)
            updated=True
        data = {
            'updated':updated,
            'liked':liked
        }
        return Response(data)
