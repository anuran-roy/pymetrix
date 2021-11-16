class DuplicateError(Exception):
    """Raised when a duplicate is entered in a FlowLayer
    object, or found in a Flow Graph.

    Please check if you're trying to add multiple copies
    of the same object to compose the super object.

    """
    def __init__(self, what=None, where=None):
        self.object_id = what
        self.super_id = where

        super().__init__(self.object_id, self.super_id)

    def __str__(self):
        return f"{self.object_id} already present in {self.super_id}"
