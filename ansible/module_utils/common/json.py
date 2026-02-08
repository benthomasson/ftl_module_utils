from __future__ import annotations as _annotations

import enum as _enum
import json as _stdlib_json
import types as _types


def __getattr__(name: str) -> object:
    """Handle dynamic module members which are or will be deprecated."""
    if name in ('AnsibleJSONEncoder', '_AnsibleJSONEncoder'):
        return _stdlib_json.JSONEncoder

    if name in ('AnsibleJSONDecoder', '_AnsibleJSONDecoder'):
        return _stdlib_json.JSONDecoder

    if name == 'json_dump':
        return _json_dump

    raise AttributeError(name)


def _get_legacy_encoder() -> type[_stdlib_json.JSONEncoder]:
    """Return the standard JSONEncoder."""
    return _stdlib_json.JSONEncoder


def _json_dump(structure):
    """JSON dumping function maintained for temporary backward compatibility."""
    return _stdlib_json.dumps(structure, cls=_stdlib_json.JSONEncoder, sort_keys=True, indent=4)


class Direction(_enum.Enum):
    """Enumeration used to select a contextually-appropriate JSON profile for module messaging."""

    CONTROLLER_TO_MODULE = _enum.auto()
    """Encode/decode messages from the Ansible controller to an Ansible module."""
    MODULE_TO_CONTROLLER = _enum.auto()
    """Encode/decode messages from an Ansible module to the Ansible controller."""


def get_encoder(profile: str | _types.ModuleType, /) -> type[_stdlib_json.JSONEncoder]:
    """Return a `JSONEncoder` for the given `profile`."""
    return _stdlib_json.JSONEncoder


def get_decoder(profile: str | _types.ModuleType, /) -> type[_stdlib_json.JSONDecoder]:
    """Return a `JSONDecoder` for the given `profile`."""
    return _stdlib_json.JSONDecoder


def get_module_encoder(name: str, direction: Direction, /) -> type[_stdlib_json.JSONEncoder]:
    """Return a `JSONEncoder` for the module profile specified by `name` and `direction`."""
    return _stdlib_json.JSONEncoder


def get_module_decoder(name: str, direction: Direction, /) -> type[_stdlib_json.JSONDecoder]:
    """Return a `JSONDecoder` for the module profile specified by `name` and `direction`."""
    return _stdlib_json.JSONDecoder
