class MyCustomError(TypeError):
    """
    Exception raised with specific error code
    """
    def __init__(self, message, code) -> None:
        super().__init__(f'Error code {code}: {message}')
        self.code = code

err = MyCustomError('An error', 500)
print(err.__doc__)