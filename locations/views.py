from django.http import HttpResponse
from django.utils import simplejson
from locations.models import Relevance

def rank(request):
    relevance_lists = []
    final_scores = []
    for q in request.GET:
        relevance_lists.append(
            Relevance.objects.filter(concept=q).values())

    for r in relevance_lists[0]:
        score = r['relevance']
        for rlist in relevance_lists:
            try:
                score = score * rlist.get(concept=r['concept'])
            except:
                pass
        
        if score:
            final_scores.append({ 'concept': r['concept'],
                                  'score': score })
    
    sorted_scores = sorted(final_scores, key=lambda k: k['score'])
    
    return HttpResponse(simplejson.dumps(sorted_scores),
        mimetype = "application/json")
