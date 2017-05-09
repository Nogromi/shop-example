from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Comment
from .forms import CommentForm
from datetime import datetime, timedelta, date
from datetime import datetime, timedelta
import 

def product_list(request):

    object_list = Product.objects.all()

    paginator= Paginator(object_list, 5)
    page= request.GET.get('page')
    try:
        products=paginator.page(page)
    except PageNotAnInteger:

        products=paginator.page(1)
    except EmptyPage:

        products=paginator.page(paginator.num_pages)

    context={
        'page': page,
        'products': products
    }
    return render(request, 'product/products/list.html', context)


def load_comments(self):
    print("created")
    print("datetime", datetime.today())
    if self.created - datetime.today():
        self.active = False


def product_detail(request, slug):
    product = get_object_or_404(Product,slug=slug)


    # List of active comments for this post
    # comments = product.comments.filter(active=True)

    now = datetime.now() - timedelta(days=1)
    comments =  product.comments.filter(
         created__gte=now)
    created= comments[0].created
    now = datetime.now()
    print("created.day ", created.day)
    print("now.day ", now.day)



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
    else:
        comment_form = CommentForm()

    return render(request, 'product/products/detail.html', {'product': product,
                                                            'comments': comments,
                                                            'comment_form': comment_form})
