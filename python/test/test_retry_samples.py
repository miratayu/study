from utils.retry.retry_samples import task_with_retry


def test_retry_samples():
    assert task_with_retry()
