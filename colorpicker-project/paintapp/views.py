from django.shortcuts import render
from django.views import View

from paintapp.forms import ColorPickerForm

# Create your views here.
class ColorPickerView(View):
    def get(self, request):
        """Present the color picker form and color the user"""
        form = ColorPickerForm()

        context = {
            'form': form,
            'red': 255,
            'green': 255,
            'blue': 255,
        }

        return render(request, 'paint.html', context=context)
    
    def post(self, request):
        """Display the user's chosen color"""
        form = ColorPickerForm(request.POST)

        red = int(request.POST['red_amount'])
        green = int(request.POST['green_amount'])
        blue = int(request.POST['blue_amount'])

        context = {
            'form': form,
            'red': red,
            'green': green,
            'blue': blue,
        }

        return render(request, 'paint.html', context=context)
