if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    sem_duplicata = set(list(arr))
    ordenado = sorted(sem_duplicata)
    print(ordenado[-2])