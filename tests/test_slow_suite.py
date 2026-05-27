import os
import time


def _run_shard(name: str) -> None:
    target_id = os.environ.get("KERRIGAN_TARGET_ID", "local-devkit")
    duration = int(os.environ.get("KERRIGAN_SHARD_DURATION_SEC", "0"))
    fail_shard = os.environ.get("KERRIGAN_FAIL_SHARD", "")
    print(f"{name} starting on {target_id}", flush=True)
    time.sleep(duration)
    if fail_shard == name:
        raise AssertionError(f"{name} intentionally failed on {target_id}")
    print(f"{name} completed on {target_id}", flush=True)


def test_manual_shard_a() -> None:
    _run_shard("manual-shard-a")


def test_manual_shard_b() -> None:
    _run_shard("manual-shard-b")


def test_manual_shard_c() -> None:
    _run_shard("manual-shard-c")


def test_manual_shard_d() -> None:
    _run_shard("manual-shard-d")


def test_manual_shard_e() -> None:
    _run_shard("manual-shard-e")


def test_manual_shard_f() -> None:
    _run_shard("manual-shard-f")
