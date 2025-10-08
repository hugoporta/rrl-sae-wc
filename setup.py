from setuptools import setup, find_packages

setup(
    name="rrl-sae-wc",
    version="0.1.0",
    description="Reusable RRL-SAE for Weather and Climate",
    packages=find_packages(include=["rrl_sae_wc", "rrl_sae_wc.*"]),
    install_requires=[],
)
