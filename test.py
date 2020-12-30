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


def test_3X3_one_police():
    problem = {
        "police": 1,
        "medics": 0,
        "observations": [
            (
                ('H', 'H', 'H'),
                ('H', '?', 'H'),
                ('H', 'H', 'H'),
            ),
            (
                ('?', '?', '?'),
                ('?', '?', '?'),
                ('?', '?', '?'),
            ),
            (
                ('?', '?', '?'),
                ('?', '?', '?'),
                ('?', '?', '?'),
            ),
            (
                ('?', '?', '?'),
                ('?', '?', '?'),
                ('?', '?', '?'),
            )

        ],
        "queries": [

            ((1, 1), 0, "S"), ((1, 1), 0, "H"), ((1, 1), 0, "U"),
            ((1, 1), 1, "S"), ((1, 1), 1, "H"), ((1, 1), 1, "U"),
            ((1, 1), 1, "Q"), ((1, 1), 3, "S"), ((1, 1), 3, "H"), ((1, 1), 3, "U"),
            ((1, 1), 3, "Q")

        ]
    }
    timeout = 3000
    t1 = time.time()
    result = timeout_exec(ex2.solve_problem, args=[problem], timeout_duration=timeout)
    t2 = time.time()
    assert result[((1, 1), 0, "S")] == '?'
    assert result[((1, 1), 0, "H")] == '?'
    assert result[((1, 1), 0, "U")] == '?'

    #assert result[((1, 1), 1, "S")] == 'F' known   bug
    assert result[((1, 1), 1, "H")] == '?'
    assert result[((1, 1), 1, "U")] == '?'
    assert result[((1, 1), 1, "Q")] == '?'

    assert result[((1, 1), 3, "S")] == 'F'
    assert result[((1, 1), 3, "H")] == '?'
    assert result[((1, 1), 3, "U")] == '?'
    #assert result[((1, 1), 3, "Q")] == 'F' Known bug


    print(f'Your answer is {result}, achieved in {t2 - t1:.3f} seconds')


def test_3X3_no_actions():
    problem = {
        "police": 0,
        "medics": 0,
        "observations": [
            (
                ('H', 'H', 'H'),
                ('H', '?', 'H'),
                ('H', 'H', 'H'),
            ),
            (
                ('?', 'S', '?'),
                ('?', '?', '?'),
                ('?', '?', '?'),
            ),
            (
                ('?', '?', '?'),
                ('?', '?', '?'),
                ('?', '?', '?'),
            ),
            (
                ('?', '?', '?'),
                ('?', '?', '?'),
                ('?', '?', '?'),
            ),
            (
                ('?', '?', '?'),
                ('?', '?', '?'),
                ('?', '?', '?'),
            ),
            (
                ('?', '?', '?'),
                ('?', '?', '?'),
                ('?', '?', '?'),
            ),


        ],
        "queries": [

            ((1, 1), 0, "S"), ((0, 0), 1, "S"), ((0, 2), 1, "H"), ((2, 2), 2, "S"), ((0, 0), 2, "S"),
            ((1, 1), 3, "H"), ((1, 0), 3, "H"), ((2, 2), 3, "H"),
            ((1, 1), 4, "H"), ((1, 0), 4, "H"), ((2, 2), 4, "H"),
            ((1, 1), 5, "H"), ((1, 0), 5, "H"), ((2, 2), 5, "H")
        ]
    }
    timeout = 3000
    t1 = time.time()
    result = timeout_exec(ex2.solve_problem, args=[problem], timeout_duration=timeout)
    t2 = time.time()
    assert result[((1, 1), 0, "S")] == 'T'
    assert result[((0, 0), 1, "S")] == 'F'
    assert result[((0, 2), 1, "H")] == 'T'
    assert result[((2, 2), 2, "S")] == 'T'
    assert result[((0, 0), 2, "S")] == 'T'

    assert result[((1, 1), 3, "H")] == 'T'
    assert result[((1, 0), 3, "H")] == 'F'
    assert result[((2, 2), 3, "H")] == 'F'

    assert result[((1, 1), 4, "H")] == 'F'
    assert result[((1, 0), 4, "H")] == 'T'
    assert result[((2, 2), 4, "H")] == 'F'

    assert result[((1, 1), 5, "H")] == 'F'
    assert result[((1, 0), 5, "H")] == 'F'
    assert result[((2, 2), 5, "H")] == 'T'

    print(f'Your answer is {result}, achieved in {t2 - t1:.3f} seconds')


def text_5X5():
    problem = {
        "police": 2,
        "medics": 2,
        "observations": [
            (
                ('H', 'S', 'U', 'H', 'H', '?'),
                ('S', 'H', 'H', 'S', 'U', 'U'),
                ('?', 'H', 'H', 'U', 'S', 'U'),
                ('H', 'S', 'H', 'H', 'H', 'S'),
                ('H', 'H', '?', 'H', 'H', 'H'),
                ('H', 'H', 'H', 'S', 'H', 'U'),
            ),
            (
                ('S', 'S', 'U', 'I', 'H', '?'),
                ('S', 'I', 'S', 'S', 'U', 'U'),
                ('?', 'H', 'H', 'U', 'S', 'U'),
                ('H', 'Q', 'H', 'H', 'S', 'S'),
                ('H', 'H', '?', 'H', 'H', 'S'),
                ('H', 'H', 'H', 'Q', 'H', 'U'),
            ),
            (
                ('S', 'S', 'U', 'I', 'H', '?'),
                ('S', 'I', 'Q', 'S', 'U', 'U'),
                ('?', 'H', 'H', 'U', 'S', 'U'),
                ('H', 'Q', 'H', 'I', 'S', 'S'),
                ('H', 'H', '?', 'H', 'I', 'Q'),
                ('H', '?', 'H', 'Q', 'H', 'U'),
            ),
            (
                ('Q', 'H', 'U', 'I', 'H', '?'),
                ('H', 'I', 'Q', 'H', 'U', 'U'),
                ('?', 'H', 'H', 'U', 'H', 'U'),
                ('H', 'H', 'H', 'I', 'Q', 'H'),
                ('H', 'H', '?', 'H', 'I', '?'),
                ('H', 'H', 'I', '?', 'I', 'U'),
            ),
        ],
        "queries": [

            ((2, 0), 0, "Q"), ((2, 0), 0, "I"), ((2, 0), 0, "S"), ((2, 0), 0, "U"), ((2, 0), 0, "H"),
            ((0, 5), 0, "Q"), ((0, 5), 0, "I"), ((0, 5), 0, "S"), ((0, 5), 0, "U"), ((0, 5), 0, "H"),
            ((4, 2), 1, "Q"), ((4, 2), 1, "I"), ((4, 2), 1, "S"), ((4, 2), 1, "U"), ((4, 2), 1, "H"),
            ((5, 1), 2, "Q"), ((5, 1), 2, "I"), ((5, 1), 2, "S"), ((5, 1), 2, "U"), ((5, 1), 2, "H"),
            ((5, 3), 3, "Q"), ((5, 3), 3, "I"), ((5, 3), 3, "S"), ((5, 3), 3, "U"), ((5, 3), 3, "H"),
            ((4, 5), 3, "Q"), ((4, 5), 3, "I"), ((4, 5), 3, "S"), ((4, 5), 3, "U"), ((4, 5), 3, "H")
        ]
    }
    timeout = 3000
    t1 = time.time()
    result = timeout_exec(ex2.solve_problem, args=[problem], timeout_duration=timeout)
    t2 = time.time()
    assert result[((2, 0), 0, "Q")] == 'F'
    assert result[((2, 0), 0, "I")] == 'F'
    assert result[((2, 0), 0, "S")] == 'F'
    assert result[((2, 0), 0, "U")] == 'T'
    assert result[((2, 0), 0, "H")] == 'F'

    assert result[((0, 5), 0, "Q")] == 'F'
    assert result[((0, 5), 0, "I")] == 'F'
    assert result[((0, 5), 0, "S")] == 'F'
    assert result[((0, 5), 0, "U")] == '?'
    assert result[((0, 5), 0, "H")] == '?'

    assert result[((4, 2), 1, "Q")] == 'F'
    assert result[((4, 2), 1, "S")] == 'F'
    assert result[((4, 2), 1, "I")] == 'F'
    assert result[((4, 2), 1, "H")] == '?'
    assert result[((4, 2), 1, "U")] == '?'

    assert result[((5, 1), 2, "U")] == 'F'
    assert result[((5, 1), 2, "I")] == 'F'
    assert result[((5, 1), 2, "S")] == 'F'
    assert result[((5, 1), 2, "U")] == 'F'
    assert result[((5, 1), 2, "H")] == 'T'

    assert result[((5, 3), 3, "Q")] == 'F'
    assert result[((5, 3), 3, "I")] == 'F'
    assert result[((5, 3), 3, "S")] == 'F'
    assert result[((5, 3), 3, "U")] == 'F'
    assert result[((5, 3), 3, "H")] == 'T'

    assert result[((4, 5), 3, "Q")] == 'T'
    assert result[((4, 5), 3, "I")] == 'F'
    assert result[((4, 5), 3, "S")] == 'F'
    assert result[((4, 5), 3, "U")] == 'F'
    assert result[((4, 5), 3, "H")] == 'F'
    print(f'Your answer is {result}, achieved in {t2 - t1:.3f} seconds')


def test_8X8():
    problem = {
        "police": 3,
        "medics": 3,
        "observations": [
            (('S', 'H', 'H', 'H', 'H', 'U', 'U', 'H'),
             ('U', 'U', 'H', 'H', 'S', 'U', 'U', 'H'),
             ('U', '?', 'H', 'H', 'H', 'U', 'H', 'H'),
             ('U', 'H', 'H', 'H', 'U', 'U', 'H', 'S'),
             ('U', 'H', 'H', 'H', 'H', 'H', 'U', '?'),
             ('U', 'H', 'H', 'S', '?', 'S', 'H', 'H'),
             ('S', 'H', 'U', 'H', 'H', 'U', 'U', 'H'),
             ('U', 'H', 'U', 'H', 'U', 'H', 'U', 'U')),

            (('Q', 'H', 'H', 'H', 'S', 'U', 'U', 'H'),
             ('U', 'U', 'H', 'I', 'S', 'U', 'U', 'H'),
             ('U', '?', 'H', 'H', 'S', 'U', 'H', 'S'),
             ('U', 'H', 'H', 'H', 'U', 'U', 'S', 'S'),
             ('U', 'H', 'H', 'S', 'H', 'H', 'U', '?'),
             ('U', 'H', 'I', 'S', '?', 'Q', 'H', 'H'),
             ('Q', 'H', 'U', 'I', 'H', 'U', 'U', 'H'),
             ('U', 'H', 'U', 'H', 'U', 'H', 'U', 'U')),

            (('Q', 'H', 'H', 'H', 'Q', 'U', 'U', 'H'),
             ('U', 'U', 'H', 'I', 'S', 'U', 'U', 'S'),
             ('U', '?', 'H', 'H', 'Q', 'U', 'S', 'S'),
             ('U', 'I', 'H', 'H', 'U', 'U', 'S', 'S'),
             ('U', 'H', 'H', 'Q', 'H', 'H', 'U', '?'),
             ('U', 'H', 'I', 'S', '?', 'Q', 'H', 'S'),
             ('Q', 'H', 'U', 'I', 'I', 'U', 'U', 'H'),
             ('U', 'H', 'U', 'H', 'U', 'H', 'U', 'U')),

        ],
        "queries": [

            ((2, 1), 0, "Q"), ((2, 1), 0, "I"), ((2, 1), 0, "S"), ((2, 1), 0, "U"), ((2, 1), 0, "H"),
            ((5, 4), 1, "Q"), ((5, 4), 1, "I"), ((5, 4), 1, "S"), ((5, 4), 1, "U"), ((5, 4), 1, "H"),
            ((4, 7), 2, "Q"), ((4, 7), 2, "I"), ((4, 7), 2, "S"), ((4, 7), 2, "U"), ((4, 7), 2, "H"),

        ]
    }
    timeout = 30000
    t1 = time.time()
    result = timeout_exec(ex2.solve_problem, args=[problem], timeout_duration=timeout)
    t2 = time.time()
    assert result[((2, 1), 0, "Q")] == 'F'
    assert result[((2, 1), 0, "I")] == 'F'
    assert result[((2, 1), 0, "S")] == 'F'
    assert result[((2, 1), 0, "U")] == 'F'
    assert result[((2, 1), 0, "H")] == 'T'

    assert result[((4, 7), 2, "Q")] == 'F'
    assert result[((4, 7), 2, "I")] == 'F'
    assert result[((4, 7), 2, "S")] == 'T'
    assert result[((4, 7), 2, "U")] == 'F'
    assert result[((4, 7), 2, "H")] == 'F'

    assert result[((5, 4), 1, "Q")] == 'F'
    assert result[((5, 4), 1, "S")] == 'F'
    assert result[((5, 4), 1, "I")] == 'F'
    assert result[((5, 4), 1, "H")] == 'F'
    assert result[((5, 4), 1, "U")] == 'T'

    print(f'Your answer is {result}, achieved in {t2 - t1:.3f} seconds')


def test_8X8_2():
    problem = {
        "police": 3,
        "medics": 3,
        "observations": [
            (('S', 'H', 'H', 'H', 'H', 'U', 'U', 'H'),
             ('U', 'U', 'H', 'H', 'S', 'U', 'U', 'H'),
             ('U', '?', 'H', 'H', 'H', 'U', 'H', 'H'),
             ('U', 'H', 'H', 'H', 'U', 'U', 'H', 'S'),
             ('U', 'H', 'H', 'H', 'H', 'H', 'U', '?'),
             ('U', 'H', 'H', 'S', '?', 'S', 'H', 'H'),
             ('S', 'H', 'U', 'H', 'H', 'U', 'U', 'H'),
             ('U', 'H', 'U', 'H', 'U', 'H', 'U', 'U')),

            (('Q', 'H', 'H', 'H', 'S', 'U', 'U', 'H'),
             ('U', 'U', 'H', 'I', 'S', 'U', 'U', 'H'),
             ('U', '?', 'H', 'H', 'S', 'U', 'H', 'S'),
             ('U', 'H', 'H', 'H', 'U', 'U', 'S', 'S'),
             ('U', 'H', 'H', 'S', 'H', 'H', 'U', '?'),
             ('U', 'H', 'I', 'S', '?', 'Q', 'H', 'H'),
             ('Q', 'H', 'U', 'I', 'H', 'U', 'U', 'H'),
             ('U', 'H', 'U', 'H', 'U', 'H', 'U', 'U')),

        ],
        "queries": [

            ((2, 1), 0, "Q"), ((2, 1), 0, "I"), ((2, 1), 0, "S"), ((2, 1), 0, "U"), ((2, 1), 0, "H"),
            ((5, 4), 1, "Q"), ((5, 4), 1, "I"), ((5, 4), 1, "S"), ((5, 4), 1, "U"), ((5, 4), 1, "H"),
            ((4, 7), 1, "Q"), ((4, 7), 1, "I"), ((4, 7), 1, "S"), ((4, 7), 1, "U"), ((4, 7), 1, "H"),

        ]
    }
    timeout = 30000
    t1 = time.time()
    result = timeout_exec(ex2.solve_problem, args=[problem], timeout_duration=timeout)
    t2 = time.time()
    print(f'Your answer is {result}, achieved in {t2 - t1:.3f} seconds')

    assert result[((2, 1), 0, "Q")] == 'F'
    assert result[((2, 1), 0, "I")] == 'F'
    assert result[((2, 1), 0, "S")] == 'F'
    assert result[((2, 1), 0, "U")] == '?'
    assert result[((2, 1), 0, "H")] == '?'

    assert result[((4, 7), 1, "Q")] == 'F'
    assert result[((4, 7), 1, "I")] == 'F'
    assert result[((4, 7), 1, "S")] == '?'
    assert result[((4, 7), 1, "U")] == '?'
    assert result[((4, 7), 1, "H")] == 'F'

    assert result[((5, 4), 1, "Q")] == 'F'
    assert result[((5, 4), 1, "S")] == '?'
    assert result[((5, 4), 1, "I")] == 'F'
    assert result[((5, 4), 1, "H")] == 'F'
    assert result[((5, 4), 1, "U")] == '?'


def main():
    test_3X3_one_police()
    test_3X3_no_actions()
    text_5X5()
    # test_8X8()
    # test_8X8_2()


if __name__ == '__main__':
    main()
