import math
import pytest

import practice


def test_greet():
    assert practice.greet("Ada") == "Hello, Ada!"


def test_mean_basic():
    assert practice.mean([1, 3, 5]) == 3.0



def test_normalize_basic():
    out = practice.normalize([1, 1, 2])
    assert out == [0.25, 0.25, 0.5]
    assert math.isclose(sum(out), 1.0, rel_tol=0, abs_tol=1e-12)



def test_main_prints_two_lines(capsys):
    # We don't want to *execute* __main__ import-time, so call main directly
    practice.main()
    captured = capsys.readouterr().out.strip().splitlines()
    assert captured == ["Hello, Gradescope!", "4.0"]
