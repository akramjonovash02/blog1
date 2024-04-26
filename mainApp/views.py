from hashlib import new

from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import *

class Home(View):
    def get(self, request):
        return render(request, "home.html")

class About(View):
    def get(self, request):
        return render(request, "about.html")

class BlogView(View):
    def get(self, request):
        months_list = ['None', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September','October', 'November', 'December']
        all_blogs = Blog.objects.order_by('-date')
        all_dates = Blog.objects.all().values('date').distinct().order_by('-date')
        years_months = [{'year': date['date'].year, 'month': date['date'].month} for date in all_dates]
        blogs_by_year_month = {}
        months = {
            1: 'Yanvar',
            2: 'Fevral',
            3: 'Mart',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December'
        }
        for ym in years_months:
            month_blogs = all_blogs.filter(date__year=ym['year'], date__month=ym['month'])
            if month_blogs.exists():
                if ym['year'] not in blogs_by_year_month:
                    blogs_by_year_month[ym['year']] = {}
                blogs_by_year_month[ym['year']][ym['month']] = {
                    'month': ym['month'],
                    'blogs': month_blogs
                }
        context = {
            'blogs_by_year_month': blogs_by_year_month
        }
        return render(request, 'blog.html', context)


class TalksView(View):
    def get(self, request):
        talks = Talks.objects.order_by('-date')
        context = {
            'talks':talks
        }
        return render(request, 'talks.html', context)

class MaqolaView(View):
    def get(self, request, pk):
        maqola = Blog.objects.get(id=pk)
        months = {
            1: 'Yanvar',
            2: 'Fevral',
            3: 'Mart',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December'
        }
        context = {
            'maqola': maqola,
            'month': months[maqola.date.month],
        }
        return render(request, 'maqola.html', context)







