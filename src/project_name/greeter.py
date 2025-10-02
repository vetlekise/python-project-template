class Greeter:
    """A simple class to create greetings."""

    def say_hello(self, name: str) -> str:
        """Generates a greeting message.

        Args:
            name (str): The name to greet.

        Returns:
            str: The greeting message.
        """
        return f"Hello, {name}!"
