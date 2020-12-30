import time
import ex2


def timeout_exec(func, args=(), kwargs={}, timeout_duration=10, default=None):
    """This function will spawn a thread and run the given function
    using the args, kwargs and return the given default value if the
    timeout_duration is exceeded.
    """
    import threading

    class InterruptableThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = default

        def run(self):
            # remove try if you want program to abort at error
            # try:
            self.result = func(*args, **kwargs)
            # except Exception as e:
            #    self.result = (-3, -3, e)

    it = InterruptableThread()
    it.start()
    it.join(timeout_duration)
    if it.is_alive():
        return default
    else:
        return it.result


def test3X3_less_H_than_medics():
    problem = {
        "police": 0,
        "medics": 3,
        "observations": [
            (
                ('H', 'S', 'U'),
                ('S', '?', '?'),
                ('S', 'S', 'U'),
            ),
            (
                ('I', 'S', '?'),
                ('S', '?', '?'),
                ('S', 'S', 'U'),
            ),
            (
                ('?', 'S', '?'),
                ('?', '?', 'I'),
                ('?', 'S', 'U'),
            )
        ],
        "queries": [

            ((1, 1), 0, "S"), ((1, 1), 0, "H"), ((1, 1), 0, "U"),
            ((0, 2), 1, "S"), ((0, 2), 1, "H"), ((0, 2), 1, "U"), ((0, 2), 1, "I"),
            ((1, 2), 1, "S"), ((1, 2), 1, "H"), ((1, 2), 1, "U"), ((1, 2), 1, "I"),
            ((0, 0), 2, "H"), ((0, 0), 2, "S"), ((0, 0), 2, "I"), ((1, 1), 2, "I")

        ]
    }
    timeout = 3000
    t1 = time.time()
    result = timeout_exec(ex2.solve_problem, args=[problem], timeout_duration=timeout)
    t2 = time.time()

    print(f'Your answer is {result}, achieved in {t2 - t1:.3f} seconds')

def test3X3_less_S_than_police():
    problem = {
        "police": 4,
        "medics": 0,
        "observations": [
            (
                ('H', 'S', '?'),
                ('?', 'H', 'H'),
                ('H', '?', 'H'),
            ),
            (
                ('?', 'Q', '?'),
                ('?', 'H', '?'),
                ('?', '?', '?'),
            ),
            (
                ('?', '?', 'U'),
                ('?', '?', '?'),
                ('?', 'Q', '?'),
            )
        ],
        "queries": [

            ((0, 2), 0, "S"), ((0, 2), 0, "H"), ((0, 2), 0, "U"),
            ((1, 0), 1, "S"), ((1, 0), 1, "H"), ((1, 0), 1, "U"), ((1, 0), 1, "Q"),
            ((1, 2), 1, "S"), ((1, 2), 1, "H"), ((1, 2), 1, "U"), ((1, 2), 1, "Q"),
            ((2, 1), 1, "H"), ((2, 1), 1, "S"), ((2, 1), 1, "U"), ((2, 1), 1, "Q")

        ]
    }
    timeout = 3000
    t1 = time.time()
    result = timeout_exec(ex2.solve_problem, args=[problem], timeout_duration=timeout)
    t2 = time.time()

    print(f'Your answer is {result}, achieved in {t2 - t1:.3f} seconds')
def text_5X5():
    problem = {
        "police": 2,
        "medics": 2,
        "observations": [
            (
                ('S', 'S', 'U', 'H', 'S', 'S'),
                ('S', 'H', 'H', 'H', 'H', 'S'),
                ('S', 'U', 'U', 'U', 'S', 'S'),
                ('S', 'H', 'U', 'H', 'S', 'S'),
                ('S', 'H', '?', 'H', 'S', 'S'),
                ('S', 'S', 'S', 'S', 'S', 'S'),
            ),
            (
                ('S', 'Q', 'U', 'H', 'Q', 'S'),
                ('S', 'S', 'H', 'H', 'I', 'S'),
                ('S', 'U', 'U', 'U', 'S', 'S'),
                ('S', 'S', 'U', 'S', 'S', 'S'),
                ('S', 'S', '?', 'S', 'S', 'S'),
                ('S', 'S', 'S', 'S', 'S', 'S'),
            )
        ],
        "queries": [

            ((4, 2), 0, "S"), ((4, 2), 0, "U"), ((4, 2), 0, "H"),
            ((4, 2), 1, "S"), ((4, 2), 1, "U"), ((4, 2), 1, "H"),((4, 2), 1, "Q"), ((4, 2), 1, "I")
        ]
    }
    timeout = 3000
    t1 = time.time()
    result = timeout_exec(ex2.solve_problem, args=[problem], timeout_duration=timeout)
    t2 = time.time()

    print(f'Your answer is {result}, achieved in {t2 - t1:.3f} seconds')

def main():
    #test3X3_less_H_than_medics()
    test3X3_less_S_than_police()
    #text_5X5()



if __name__ == '__main__':
    main()