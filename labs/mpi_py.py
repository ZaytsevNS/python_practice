from mpi4py import MPI
from random import randint


# коммуникатор, который группирует процессы при запуске программы
comm = MPI.COMM_WORLD
# получаем ранги процесса
rank = comm.Get_rank()

if rank == 0: 
    # формирую список из случайных чисел
    random_list: list = [randint(0, 50) for i in range(15)]
    print(f'Source list: {random_list}')
    # вызываю блокирующие функции send(). Процесс будет ждать, пока сообщение не будет получено соответствующим recv()
    comm.send(random_list, dest=1, tag=1)
    comm.send(random_list, dest=2, tag=2)
elif rank == 1:
    # вызываю соответствующий recv()
    even: list = [k for i, k in enumerate(comm.recv(source=0, tag=1)) if not i % 2 and not k % 2] 
    print(f'Number of even elements in even places: {len(even)}. New even list: {even}')
elif rank == 2:
    # вызываю соответствующий recv()
    odd: list = [k for i, k in enumerate(comm.recv(source=0, tag=2)) if i % 2 and k % 2]
    print(f'Number of odd elements in odd places: {len(odd)}. New odd list: {odd}')