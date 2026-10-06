from agent_loops.cli import dispatch


def main() -> int:
    return dispatch("actor_critic")
