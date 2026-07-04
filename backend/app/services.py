from .data import search_data
from .history import search_history

def search_results(query,limit):
      
    results=[]
    for key in search_data:
        if query.lower() in key:
            search_history.append(key)
            results.extend(search_data[key]) 
            
    return results[:limit]
def get_top_searches():
    counts={}
    for query in search_history:
        if query in counts:
            counts[query]+=1
        else:
            counts[query]=1
    return counts
            