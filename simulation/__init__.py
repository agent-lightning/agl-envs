# __init__.py
"""
Public API for agl_envs.simulation
- make_env
- make_env_manager
"""


__all__ = [
    "make_env",
    "make_env_manager",
]


def make_env(env_name, task, config):
    """Create an environment instance with the appropriate wrapper based on the environment name.

    Args:
        env_name (str): The name of the environment to create.
        task (str): The specific task within the environment.
        config (dict): Configuration settings for the environment.

    Returns:
        EnvWrapper: A wrapped environment instance.

    Raises:
        ValueError: If the environment name is not recognized.
    """

    # Non-gym-based environments (no EnvWrapper)
    if env_name == "scienceworld":
        from agl_envs.simulation.scienceworld.scienceworld_env import make_scienceworld_env
        return make_scienceworld_env(env_name, task, config)

    elif env_name == "alfworld":
        from agl_envs.simulation.alfworld.alfworld_env import make_alfworld_env
        return make_alfworld_env(env_name, task, config)

    else:
        raise ValueError(f"Unknown environment: {env_name}")


def make_env_manager(env_name, task, config):
    """
    Creates an EnvironmentManager instance with the appropriate factory function.

    EnvironmentManager is imported lazily to avoid circular import issues.
    """

    from agl_envs.simulation.env_manager import EnvironmentManager

    # Lazy env init function
    def get_env_fn():
        return lambda: make_env(env_name, task, config)

    env = EnvironmentManager(
        env_name=env_name,
        config=config,
        env_fn=get_env_fn(),
    )
    return env