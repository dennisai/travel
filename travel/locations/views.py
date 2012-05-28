from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson
from locations.models import Relevance

def search(request):
    if not request.is_ajax():
        return render_to_response("search.html", {},
            RequestContext(request))
            
    relevance_lists = []
    final_scores = []
    for q in request.GET:
        relevance_lists.append(
            Relevance.objects.filter(concept=q).values())

    for r in relevance_lists[0]:
        score = r['relevance']
        for rlist in relevance_lists:
            try:
                score = score * rlist.get(concept=r['concept']).relevance
            except:
                pass
        
        if score:
            final_scores.append({ 'location': r['location'],
                                  'score': score })
    
    sorted_scores = sorted(final_scores, key=lambda k: k['score'])
    
    return HttpResponse(simplejson.dumps(sorted_scores),
        mimetype = "application/json")
