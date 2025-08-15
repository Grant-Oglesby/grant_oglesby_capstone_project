import sys
import subprocess
import os


def main():
    select = sys.argv[1]

    # Identify which tests to execute based on system argument
    tests_select = {
        "unit": {"dir": "tests/unit_tests", "cov": ["config", "src"]},
        "integration": {"dir": "tests/integration_tests", "cov": []},
        "component": {"dir": "tests/component_tests", "cov": []},
        "e2e": {"dir": "tests/e2e_tests", "cov": []},
        "all": {"dir": "tests", "cov": ["config", "src"]}
    }

    # Confirm selection supplied
    if select == "all":
        # Begin unit tests first
        # Setup env for subprocess
        env = os.environ.copy()
        env["ENV"] = "test"

        # Run coverage tests
        unit_cov = (
            "ENV=test coverage run --source=config,src "
            "--omit=*/__init__.py -m pytest --verbose tests/unit_tests "
            "&& coverage report -m && coverage html "
            "&& coverage report --fail-under=90"
        )
        subprocess.run(unit_cov, shell=True, env=env)

        # Run other tests that do not require coverage report
        for tests in ["integration", "component", "e2e"]:
            test_dir = tests_select[tests]["dir"]
            subprocess.run(
                f"ENV=test pytest --verbose {test_dir}", shell=True, env=env
            )

    elif select in tests_select:
        test_dir = tests_select[select]["dir"]
        cov_source = ",".join(tests_select[select]["cov"])

        # Run coverage test
        if cov_source:
            cov_command = (
                f"ENV=test coverage run --source={cov_source} "
                f"--omit=*/__init__.py -m pytest --verbose {test_dir} "
                "&& coverage report -m && coverage html "
                "&& coverage report --fail-under=90"
            )
        else:
            cov_command = f"ENV=test pytest --verbose {test_dir}"

        # Setup env for subprocess
        env = os.environ.copy()
        env["ENV"] = "test"
        subprocess.run(cov_command, shell=True, env=env)

    elif select == "lint":
        subprocess.run(["flake8", "."])

    else:
        raise ValueError(f"Command not recognised: {select}")


if __name__ == "__main__":
    main()
