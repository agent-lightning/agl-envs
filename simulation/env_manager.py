class EnvironmentManager:

    def __init__(self, env_name, config, env_fn):
        self.config = config
        self.env = env_fn()  # Initialize the environment
        self.env_name = env_name

        self.mission = None

    def get_instruction_prompt(self, info=None):
        env_map = {
            "scienceworld": ("envs.scienceworld", {"env": self.env, "mission": self.mission}),
        }

        if self.env_name not in env_map:
            raise ValueError(f"Unknown environment: {self.env_name}")

        module_name, kwargs = env_map[self.env_name]
        module = __import__(module_name, fromlist=["get_instruction_prompt"])
        get_prompt = getattr(module, "get_instruction_prompt")
        return get_prompt(**kwargs)

    def get_single_obs_template(self):
        if self.env_name == "scienceworld":
            from agl_envs.simulation.scienceworld import get_single_obs_template

            return get_single_obs_template(self.mission)

        elif self.env_name == "alfworld":
            from agl_envs.simulation.alfworld import get_single_obs_template

            return get_single_obs_template(self.mission)

    def get_obs(self):
        if self.prompt_type == "chat":
            obs = self.prompt_builder.get_chat_prompt()
        elif self.prompt_type == "single":
            obs = self.prompt_builder.get_single_prompt()
        return obs

    def get_success_score(self):
        return self.env.get_success_score()

    def step(self, llm_output, use_reasoning=True, use_success_rate=False):
        reasoning, executed_action, is_valid, metrics = self.env.extract_action(llm_output, use_reasoning)
        env_obs, reward, terminated, truncated, info = self.env.step(executed_action)

        available_actions_hint = self.env.available_actions_hint

        if use_success_rate:
            reward = self.get_success_score()

        info["metrics"] = metrics

        return env_obs, executed_action, is_valid, reward, terminated, truncated, info, available_actions_hint

    def get_mission(self, env_obs, info):
        if self.env_name == "scienceworld":
            mission = info["taskDesc"].split("Task Description:\n")[-1]
        if self.env_name == "alfworld":
            mission = env_obs.split("Your task is to: ")[-1]

        return mission

    def reset(self):
        env_obs, info = self.env.reset()

        self.mission = self.get_mission(env_obs, info)

        available_actions_hint = self.env.available_actions_hint

        return env_obs, info, available_actions_hint

    def close(self):
        self.env.close()