from django.views.generic import ListView
from djangoproject.domains.models import DomainName

class OldDomainListView(ListView):

    context_object_name = 'domain_list'
    queryset = DomainName.objects.all().order_by('creation_date')[:200]
    template_name = 'domains/domain_list.html'