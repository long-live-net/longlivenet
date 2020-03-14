from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.core import paginator
from django.conf import settings
from django.urls import reverse_lazy

from .models import Topic
from .forms import ContactForm


class IndexView(generic.TemplateView):
    template_name = 'sitebase/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_list'] = Topic.objects.order_by('-release_day')[:5]
        return context


def paginate_queryset(page, queryset, count):
    pgn = paginator.Paginator(queryset, count)
    try:
        page_obj = pgn.page(page)
    except paginator.PageNotAnInteger:
        print("pageNotAnInteger")
        page_obj = pgn.page(1)
    except paginator.EmptyPage:
        print("EmptyPage")
        page_obj = pgn.page(pgn.num_pages)
    return page_obj


def news(request):
    count = settings.NEWS_PAGE_ITEM_COUNT
    page = request.GET.get('page') or '1'
    topicsall = Topic.objects.order_by('-release_day')
    page_obj = paginate_queryset(page, topicsall, count)
    context = {'page_obj': page_obj}
    return render(request, 'sitebase/news.html', context)


def newsdetail(request, topic_id):
    page = request.GET.get('page')
    news = get_object_or_404(Topic, pk=topic_id)
    context = {'news': news, 'page': page}
    return render(request, 'sitebase/news_detail.html', context)


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = "sitebase/contact.html"
    success_url = reverse_lazy('sitebase:contactdone')

    def form_valid(self, form):
        ctx = {'form': form}
        if self.request.POST.get('next', '') == 'confirm':
            return render(self.request, 'sitebase/contact_confirm.html', ctx)
        elif self.request.POST.get('next', '') == 'back':
            return render(self.request, 'sitebase/contact.html', ctx)
        elif self.request.POST.get('next', '') == 'send':
            form.send_email()
            return super().form_valid(form)
        else:
            return redirect(reverse_lazy('sitebase:contact'))


class ContactDoneView(generic.TemplateView):
    template_name = "sitebase/contact_done.html"
