from time import sleep

CONNECTION_RETRY = 3


class MaxRetryError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Reach maximum retry"


def task(i):
    if i < 3:
        raise Exception
    else:
        print("task")


def task_with_retry():
    for i in range(1, CONNECTION_RETRY + 1):
        try:
            task(i)
        except Exception as e:
            print(f"error:{e} retry:{i}/{CONNECTION_RETRY}")
            sleep(1)
        else:
            return True
    # return False
    raise MaxRetryError


if __name__ == '__main__':
    task_with_retry()
