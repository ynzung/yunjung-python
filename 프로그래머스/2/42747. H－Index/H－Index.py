def solution(citations):
    citations.sort()
    length = len(citations)
    for i, citation in enumerate(citations):
        paper_count = length - i
        if citation >= paper_count:
            return paper_count
    return 0