from app.core import failsafe
from app import logger
from app import version


def show_logo():
    """Printing art and version"""
    print(version.ASCII)
    print(f"Version {version.__version__}")


def main():
    """Main function"""
    show_logo()
    logger.setup_logger()
    failsafe.start_failsafe()


if __name__ == "__main__":
    main()
