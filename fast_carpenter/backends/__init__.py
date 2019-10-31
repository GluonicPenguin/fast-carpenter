"""
Provides a common interface to select a backend

Each backend is wrapped in a function so that it is only imported if requested
"""
def get_alphatwirl():
    from . import alphatwirl
    return alphatwirl


def get_coffea():
    from . import coffea
    return coffea


known_backends = {"alphatwirl": get_alphatwirl,
                  "coffea": get_coffea,
                  }


def get_backend(name):
    if name not in known_backends:
        raise ValueError("Unknown backend requested, '%s'" % name)
    return known_backends[name]()
