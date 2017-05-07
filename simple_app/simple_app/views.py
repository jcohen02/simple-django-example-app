from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(View):
    template_name = "index.html"
    
    def get(self, request, *args, **kwargs):
        # Undertake any logic required to prepare data to
        # return to the template. Parameters for use in 
        # template processing should be returned in the 
        # dict passed as the third parameter to render.
        return render(request, self.template_name, {})

class SignedInIndexView(LoginRequiredMixin, View):
    template_name = "secure_index.html"
    
    def get(self, request, *args, **kwargs):
        # Undertake any logic required to prepare data to
        # return to the template. Parameters for use in 
        # template processing should be returned in the 
        # dict passed as the third parameter to render.
        return render(request, self.template_name, {})

