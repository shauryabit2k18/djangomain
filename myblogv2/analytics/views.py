from django.shortcuts import render
from django.http import Http404

"""# Create your views here.
from django.views.generic import ListView , DetailView
from analytics.models import View
from .models import BlogPost

class BlogListView(ListView):
    model = BlogPost

class BlogDetailView(DetailView):
    model = BlogPost

    def get_object(self):
        post_pk = self.kwargs.get("pk")
        if post_pk:
            post_query = BlogPost.objects.filter(pk = post_pk)
            if post_query.exists():
                post_object = post_query.first()
                view, created = View.object.get_or_create(
                    user = self.request.user,
                    post = post_object
                )
                if created:
                    view.views_count += 1
                    view.save()

                return post_object
        raise Http404"""

from django.http import JsonResponse
from django.shortcuts import render

from .models import View

def analytics_view(request):
	context = {
		'views': 10
	}
	return JsonResponse(context)