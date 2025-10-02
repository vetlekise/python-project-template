from .greeter import Greeter


def run_app():
    """Main entry point for the application.

    Instantiates a Greeter and prints a message.
    """
    greeter = Greeter()
    message = greeter.say_hello("World")
    print(message)
    return 0


if __name__ == "__main__":
    run_app()
