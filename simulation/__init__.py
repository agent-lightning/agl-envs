# Here we should have an environment manager function that can be used to instantiate
# environments with the correct wrappers.
# from gym import spaces

from examples.simulation.captioners import create_prompt_builder


def make_env(env_name, task, config, render_mode=None):
    """Create an environment instance with the appropriate wrapper based on the environment name.

    Args:
        env_name (str): The name of the environment to create.
        task (str): The specific task within the environment.
        config (dict): Configuration settings for the environment.
        render_mode (str, optional): Rendering mode for the environment. Defaults to None.

    Returns:
        EnvWrapper: A wrapped environment instance.

    Raises:
        ValueError: If the environment name is not recognized.
    """

    # --- Non-gym-based environments (no EnvWrapper) ---
    if env_name == "scienceworld":
        from agl_envs.simulation.scienceworld.scienceworld_env import make_scienceworld_env

        return make_scienceworld_env(env_name, task, config, render_mode=render_mode)
    elif env_name == "alfworld":
        from agl_envs.simulation.alfworld.alfworld_env import make_alfworld_env

        return make_alfworld_env(env_name, task, config, render_mode=render_mode)
    else:
        raise ValueError(f"Unknown environment: {env_name}")


def make_env_manager(env_name, task, config, render_mode=None):
    from agl_envs.simulation.env_manager import EnvironmentManager

    def get_env_fn():
        def init_env():
            return make_env(env_name, task, config, render_mode=render_mode)

        return init_env

    prompt_builder = create_prompt_builder(config.captioner)
    env = EnvironmentManager(
        env_name=env_name,
        config=config,
        env_fn=get_env_fn(),
        prompt_builder=prompt_builder,
    )
    return env
