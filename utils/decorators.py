def trace_step(step_name):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            print(f"[TRACE] Step: {step_name}")
            return func(self, *args, **kwargs)

        return wrapper

    return decorator
