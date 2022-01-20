import imp
from .models import Catg_Foods
def catg_det(request):
    categories = Catg_Foods.objects.all()
    return dict(catg = categories)