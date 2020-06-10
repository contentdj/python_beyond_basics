import contextlib
import sys

class LoggingContextManager:
    def __enter__(self):
        print('LoggingContextManager.__enter__()')
        return "You're in a with-block!"

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('LoggingContextManager.__exit__: '
                  'normal exit detected')
        else:
            print('LoggingContextManager.__exit__: '
                  'Exception detected! '
                  'type={}, value={}, traceback={}'.format(
                      exc_type, exc_val, exc_tb))
        return True

@contextlib.contextmanager
def logging_context_manager():
    print('logging_context_manager: enter')
    try:
        yield "You're in a with-block!"
        print('logging_context_manager: normal exit')
    except Exception:
        print('logging_context_manager: exceptional exit',
              sys.exc_info())
        raise

if __name__ == '__main__':
    # x is bound to __enter__ return value
    with LoggingContextManager() as x:
        print(x)

    # __exit__ handles exceptions
    # with LoggingContextManager() as x:
    #     raise ValueError("errors!")

    with logging_context_manager() as x:
        print(x)
            
    try:
        with LoggingContextManager() as x:
            raise ValueError("errors!")
    except ValueError:
        print("ValueError detected")
        
    # if __exit__ returns False, the exception is propagated. Return true will swallow the exception
    
