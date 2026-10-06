import argparse
from importlib import import_module


def dispatch(loop: str, argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--provider", choices=("codex", "claude", "gemini"), default="codex")
    args, provider_args = parser.parse_known_args(argv)
    provider = import_module(f"agent_loops.{args.provider}.{loop}")
    return provider.main(provider_args)
