# -*- coding: utf-8 -*-
import subprocess


def main():
    """
    Lint all python files in the project.
    """
    command = "pdoc3 --html --html-dir docs meta_dados_rio"
    subprocess.run(command, shell=True)
