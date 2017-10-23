from core import es
from constants import ELASTICSEARCH_INDEX_NAME, PAGE_SIZE

def paginated_results(query, page_no):
    result = es.search(index=ELASTICSEARCH_INDEX_NAME, body=query)
    total = result['hits']['total']
    start = (page_no - 1) * PAGE_SIZE
    end = start + PAGE_SIZE
    final_result = []
    if (start > total):
        return final_result
    if (total < end):
        end = total
    for i in range(start, end):
        final_result.append(result['hits']['hits'][i])
    return final_result