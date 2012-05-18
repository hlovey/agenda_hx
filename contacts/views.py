from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

from django.template import RequestContext

from contacts.models import Person


# Create your views here.

def contact_list(request):

    contacts = Person.objects.all()

    for contact in contacts:
        contact.phones = contact.phone_set.all().count()
        contact.addresses = contact.address_set.all().count()

    return render_to_response('contacts/list.html',
        {
            'contacts': contacts,
        },
        context_instance=RequestContext(request))

def contact_add(request):
    return HttpResponse('add')

def contact_view(request, person_id):
    return HttpResponse('view %s' % person_id)

def contact_edit(request, person_id):
    return HttpResponse('edit %s' % person_id)
