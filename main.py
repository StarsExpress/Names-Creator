from app import App
import threading


if __name__ == '__main__':
    lock = threading.Lock()

    app = App()
    app.execute(lock)
