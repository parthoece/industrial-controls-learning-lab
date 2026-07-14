from industrial_controls_lab.cli import LABS, run_lab


def test_all_lab_runners_return_results() -> None:
    for name in LABS:
        result = run_lab(name)
        assert isinstance(result, dict)
        assert result
