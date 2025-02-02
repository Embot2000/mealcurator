from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from meals.models import mstr_recipe
from stewpot.models import share_meal
from mealcurator.helperfuncs import check_blank

# TODO:  Let edits happen for things people shared
# TODO:  Let someone add a shared recipe to a list/make a list
# TODO: Let Admins make multiple recipes and make a blogpost about them


# Landing page for capturing title and text from user
@login_required
def start_share(request, meal_id):
    meal = mstr_recipe.objects.get(meal_id=meal_id)
    template = 'stewpot/share.html'
    context = {'meal': meal, 'start': True}
    return render(request, template, context)


# Create share_meal and redirect to view of it
@login_required
def save_share(request):
    if request.method == 'POST':
        shared_title = check_blank(request.POST.get('shared_title'), 'A shared recipe from mealCurator')
        shared_text = check_blank(request.POST.get('shared_text'), 'I found this on mealCurator and wanted to share it with you')
        shared_meal = mstr_recipe.objects.get(meal_id=request.POST.get('shared_meal'))

        shared = share_meal.objects.create(
                    title=shared_title,
                    creator=request.user,
                    text=shared_text,
                    meal=shared_meal,
                    )
    return redirect('view-shared', shared.id)


# View a shared meal
def view_share(request, share_id):
    shared = (share_meal.objects.values('id',
                                        'title',
                                        'text',
                                        'meal_id',
                                        'meal__title',
                                        'meal__vegan',
                                        'meal__vegetarian',
                                        'meal__meal_time',
                                        'meal__cooking_time',
                                        'meal__dish_type',
                                        'meal__cooking_method',
                                        'meal__protein_type',
                                        'meal__rec_url')
                                .filter(id=share_id))
    context = {'shared_meals': shared,
               'view': True
               }
    template = 'stewpot/share.html'
    return render(request, template, context)
