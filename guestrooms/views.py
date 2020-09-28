from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
	"""docstring for ClassName"""
	template_name = 'home.html'


class AboutPageView(TemplateView):
	"""docstring for AboutPageView"""
	
	template_name = 'about.html'
		