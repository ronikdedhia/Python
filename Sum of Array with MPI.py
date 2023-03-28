from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
arr = [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]
if (rank == 0):
    per_process_element = len(arr)/size
    # print("Perprocess",per_process_element)
    for x in range(1, size):
        index = x * per_process_element
        print(int(index), int(index+per_process_element))
        comm.send(arr[int(index): int(index+per_process_element)], dest=x, tag=7)
    sum = 0
    for i in range(0, int(per_process_element)):
        print(arr[i], end=" ")
        sum += arr[i]
    # print("|",rank,sum)
    for z in range(1, size):
        sum += comm.recv(source=MPI.ANY_SOURCE, tag=10)
    print("\nSum of array:", sum)
else:
    data = comm.recv(source=0, tag=7)
    par_sum = 0
    for ele in data:
        print(ele, end=" ")
        par_sum += ele
    print("|", rank, par_sum)
    comm.send(par_sum, dest=0, tag=10)
