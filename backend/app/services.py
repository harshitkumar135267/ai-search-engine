from .data import search_data

def search_results(query,limit):
    results = search_data.get(query.lower(), [])
    return results[:limit]