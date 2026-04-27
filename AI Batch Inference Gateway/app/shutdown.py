# app/shutdown.py
import asyncio
import signal

shutdown_event = asyncio.Event()

def setup_shutdown():
    loop = asyncio.get_event_loop()

    def stop():
        shutdown_event.set()

    loop.add_signal_handler(signal.SIGINT, stop)
    loop.add_signal_handler(signal.SIGTERM, stop)