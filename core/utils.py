"""
Contains utility methods that can be used anywhere in the package
"""
import uuid


def get_uuid_str() -> str:
    return str(uuid.uuid4())
