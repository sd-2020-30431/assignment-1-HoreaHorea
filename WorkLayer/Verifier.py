from datetime import timedelta, date


def stringVerifier(elem):
    if not elem or elem is None or not elem.isalnum():
        raise ValueError  # Will become error message
    else:
        return elem


def numberVerifier(elem):
    if not elem or elem is None or elem > 1e9:
        raise ValueError  # Will become error message
    else:
        return elem


def dateVerifier(elem):
    if elem is not None or elem:
        try:
            date.fromisoformat(elem)
        except ValueError:
            raise ValueError
    else:
        return elem
