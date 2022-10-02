from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .models import raw_recipe, mstr_recipe, changes


def index(request):
    return render(request, 'font_style.html', context=None)


def howto(request):
    return render(request, 'howto.html', context=None)


def about(request):
    return render(request, 'about.html', context=None)


def change_log(request):
    change_list = (changes.objects
                          .values('version', 'change', 'entry_date',
                                  'change_desc', 'version__implemented')
                          .order_by('-version__implemented', 'version',
                                    'change',  'entry_date'))
    context = {'changes': change_list}
    return render(request, 'changelog.html', context=context)


class get_recipe(CreateView):
    login_required = True
    model = raw_recipe
    fields = ['title', 'rec_url', 'vegan', 'vegetarian', 'meal_time',
              'dish_type', 'cooking_method', 'protein_type', 'cooking_time']
    success_url = reverse_lazy('get-recipe')

    def form_valid(self, form):
        raw = form.save(commit=False)
        outcome = raw.pull_mstr()
        if outcome:
            raw.mstr_flag = True
        else:
            raw.error_flag = True
        raw.save()
        return redirect('get-recipe')


class update_recipe(UpdateView):
    login_required = True
    model = raw_recipe
    fields = ['title', 'rec_url', 'vegan', 'vegetarian', 'meal_time',
              'dish_type', 'cooking_method', 'cooking_time']
    template_name_suffix = '_update'


class delete_recipe(DeleteView):
    login_required = True
    model = raw_recipe
    template_name_suffix = '_delete'


def show_recipe(request):
    meals = mstr_recipe.objects.all()
    context = {'meals': meals}
    template = 'meals/showmeals.html'
    return render(request, template, context)
