from sys import stdin

def get_print_order(target_idx, docs): # 찾고자 하는 문서의 위치, 문서 중요도리스트 받음
    queue = [(idx, priority) for idx, priority in enumerate(docs)]  # 문서를 (문서 번호, 중요도) 쌍으로 큐에 저장, enumerate는 반복 가능 객체를 받아 각 요소와 그의 인덱스를 반환
    order = 0  # 인쇄 대기열에서 현재 문서가 몇 번째로 인쇄되어야 하는지를 저장하는 변수로서 초기화
    while queue: # queue가 비어있지 않는 동안 무한 루프
        cur_doc = queue.pop(0)  # 가장 앞쪽의 문서
        if any(cur_doc[1] < doc[1] for doc in queue):  # 큐 내부에서 any()함수를 사용하여 큐 내부를 순환하면서 현재 문서 중요도보다 높은 문서 있는지 확인
            queue.append(cur_doc)  # 있으면 현재 문서를 큐의 뒤쪽에 넣음
        else:  # 없으면 현재 문서를 인쇄함
            order += 1  # 인쇄한 문서의 순서 증가
            if cur_doc[0] == target_idx:  # 인쇄한 문서가 목표 문서라면
                return order  # 몇 번째로 인쇄되었는지 반환
    raise ValueError("Queue is empty")

T = int(input())

for _ in range(T):
    N, M = map(int, stdin.readline().split()) # N은 형식상 필요할 뿐 사용하지 않음
    arr = list(map(int, stdin.readline().split()))
    print(get_print_order(M, arr))
