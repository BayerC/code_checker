#!/usr/bin/env python3
import subprocess

import click


@click.command()
@click.argument("python_path", type=click.Path(exists=True))
def checker(python_path: str) -> None:
    print("========== Running flake8 ==========")
    with subprocess.Popen(["python3", "-m", "flake8", python_path]):
        pass
    print("========== Running pylint ==========")
    with subprocess.Popen(["python3", "-m", "pylint", python_path]):
        pass
    print("========== Running mypy ==========")
    with subprocess.Popen(["python3", "-m", "mypy", python_path]):
        pass


@click.command()
@click.argument("python_path", type=click.Path(exists=True))
def fixer(python_path: str) -> None:
    print("========== Running black ==========")
    with subprocess.Popen(["python3", "-m", "black", python_path]):
        pass
    print("========== Running isort ==========")
    with subprocess.Popen(["python3", "-m", "isort", python_path]):
        pass
