from task import Task

if __name__ == '__main__':
    task2 = Task()
    task2.configure_parameters(
        a=0,
        b=2,
        N=101,
        omega=3
    )
    task2.configure_boundary_conditions(
        left=0,
        right=1
    )
    task2.execute()
    task2.write_file('../res/result.txt')
