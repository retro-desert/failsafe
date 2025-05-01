import threading
from app import failsafe
from app import logger
from app import version


if __name__ == "__main__":
    # Printing art and version
    print(version.ASCII)
    print(f"\nVersion {version.VERSION}\n")

    # Setup logging
    logger.setup_logger()

    # Setup threads
    t1 = threading.Thread(target=failsafe.countdown, daemon=True)
    t2 = threading.Thread(target=failsafe.listen_input, daemon=True)

    t1.start()
    t2.start()

    # Handling threads interruption
    try:
        t1.join()
        t2.join()
    except KeyboardInterrupt:
        failsafe.exit_event.set()
        print("\nKeyboardInterrupt")
