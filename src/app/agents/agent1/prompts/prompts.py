"""Prompt functions for Agent 1."""


def get_agent_system_prompt() -> str:
    """
    Get the system prompt for Agent 1.

    Returns:
        str: The system prompt defining Agent 1's behavior and capabilities.
    """
    return """You are Agent 1, a specialized agent designed to [describe Agent 1's purpose].

Your responsibilities:
- [Task 1]
- [Task 2]
- [Task 3]

Always follow these principles:
- Be precise and accurate
- Provide clear reasoning for decisions
- Handle errors gracefully
"""


def get_task_prompt(task_description: str, context: dict | None = None) -> str:
    """
    Generate a task-specific prompt for Agent 1.

    Args:
        task_description: Description of the task to be performed.
        context: Optional context dictionary with additional information.

    Returns:
        str: The formatted task prompt.
    """
    context = context or {}

    prompt = f"""Task for Agent 1:
{task_description}

"""

    if context:
        prompt += "Context:\n"
        for key, value in context.items():
            prompt += f"- {key}: {value}\n"

    return prompt

