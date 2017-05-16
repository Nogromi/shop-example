from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginForm, UserRegistrationForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Comment, Profile
from .forms import CommentForm, LoginForm
from datetime import datetime, timedelta, date
from datetime import datetime, timedelta
from  django.contrib import messages

def index(request):
    return redirect("/products/")
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authentddsicated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            profile = Profile.objects.create(user=new_user)

            return render(request,
                          'registration/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


#
# @login_required
# def dashboard(request):
#     return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def product_list(request):
    object_list = Product.objects.all()

    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:

        products = paginator.page(1)
    except EmptyPage:

        products = paginator.page(paginator.num_pages)

    context = {
        'page': page,
        'products': products
    }
    return render(request, 'product/products/list.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    # List of active comments for this post
    # comments = product.comments.filter(active=True)
    now = datetime.now() - timedelta(days=1)
    comments = product.comments.filter(
        created__gte=now)

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.product = product
            # Save the comment to the database
            new_comment.save()
            messages.success(request, 'Thank you for the comment')

    else:
        comment_form = CommentForm(
            initial={'name': request.user.username if request.user.is_authenticated else "anonymous"})

    return render(request, 'product/products/detail.html', {'product': product,
                                                            'comments': comments,
                                                            'comment_form': comment_form})


@require_POST
def product_like(request):
    if request.user.is_authenticated():
        product_id = request.POST['id']
        action = request.POST['action']

        if product_id and action:
            try:
                product = Product.objects.get(id=product_id)
                if action == 'like':
                    product.users_like.add(request.user)
                elif action == 'unlike':
                    product.users_like.remove(request.user)

                return JsonResponse({
                    'status': 'ok'
                })
            except Product.DoesNotExist:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Not found'
                })

    else:
        messages.error(request, 'Please login or register to put your like ')
        return HttpResponse('error, Please login or register to put your like')
