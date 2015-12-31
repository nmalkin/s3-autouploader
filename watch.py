"""
This module manages watching a directory for new files and executing requested
code when they appear.
"""

from logger import logger
from time import sleep
from watchdog.observers.polling import PollingObserver
from watchdog.events import FileSystemEventHandler

class NewFileWatcher:
    """
    Watch given directory for new files and execute callback when one is seen

    The callback will be called with one argument: the path of the new file.
    """
    def __init__(self, directory, callback, sleep_time=1):
        self.directory = directory
        self.callback = callback
        self.sleep_time = sleep_time

    def watch(self):
        """
        Start watching
        """
        logger.info('Watching directory %s' % self.directory)

        # Set up handler for when we see new files
        callback = self.callback
        class NewFileEventHandler(FileSystemEventHandler):
            def on_created(self, event):
                if not event.is_directory:
                    logger.info('Detected new file: %s' % event.src_path)
                    callback(event.src_path)
        event_handler = NewFileEventHandler()

        # Use polling observer (rather than filesystem-specific observers),
        # because it is more reliable.
        observer = PollingObserver(timeout=self.sleep_time)

        # Start the observer
        observer.schedule(event_handler, self.directory, recursive=False)
        observer.start()

        # Wait while the observer is running
        try:
            while True:
                sleep(self.sleep_time)
        # Exit gracefully
        except KeyboardInterrupt:
            logger.info('Detected interrupt. Stopping observer.')
            observer.stop()
        observer.join()

# Demo functionality: watch the current directory and print any new files
if __name__ == "__main__":
    directory = '.'
    NewFileWatcher(directory, lambda path: print(path)).watch()
