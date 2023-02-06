if __name__ == "__main__":
    n,k = map(int,input().split())
    tasks = list(map(int,input().split()))
    multitap, cnt, cursor = [0] * n, 0, 0

    for idx,task in enumerate(tasks):
        if task not in multitap:
            if 0 in multitap:
                multitap[multitap.index(0)] = task
            else:
                task_idx = 0
                for val in multitap:
                    if val not in tasks[idx:]:
                        cursor = val
                        break

                    elif tasks[idx:].index(val) > task_idx:
                        print(tasks[idx:].index(val), idx)
                        cursor = val
                        task_idx = tasks[idx:].index(val)

                multitap[multitap.index(cursor)] = task
                cnt+=1
    print(cnt)