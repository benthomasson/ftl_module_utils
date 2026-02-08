# -*- coding: utf-8 -*-
# Copyright (c) 2019 Ansible Project
# Simplified BSD License (see licenses/simplified_bsd.txt or https://opensource.org/licenses/BSD-2-Clause)

from __future__ import annotations as _annotations

import typing as _t


def warn(
    warning: str,
    *,
    help_text: str | None = None,
    obj: object | None = None,
) -> None:
    """Record a warning to be returned with the module result."""
    if warning not in _global_warnings:
        _global_warnings.append(warning)


def error_as_warning(
    msg: str | None,
    exception: BaseException,
    *,
    help_text: str | None = None,
    obj: object = None,
) -> None:
    """Display an exception as a warning."""
    warning = f"{msg}: {exception}" if msg else str(exception)
    if warning not in _global_warnings:
        _global_warnings.append(warning)


def deprecate(
    msg: str,
    version: str | None = None,
    date: str | None = None,
    collection_name: str | None = None,
    *,
    deprecator: object | None = None,
    help_text: str | None = None,
    obj: object | None = None,
) -> None:
    """
    Record a deprecation warning.
    Specify `version` or `date`, but not both.
    If `date` is a string, it must be in the form `YYYY-MM-DD`.
    """
    entry = {"msg": msg}
    if version is not None:
        entry["version"] = version
    if date is not None:
        entry["date"] = date
    if collection_name is not None:
        entry["collection_name"] = collection_name

    # Deduplicate by msg
    if not any(d["msg"] == msg for d in _global_deprecations):
        _global_deprecations.append(entry)


def get_warning_messages() -> tuple[str, ...]:
    """Return a tuple of warning messages accumulated over this run."""
    return tuple(_global_warnings)


def get_deprecation_messages() -> tuple[dict[str, _t.Any], ...]:
    """Return a tuple of deprecation warning messages accumulated over this run."""
    return tuple(_global_deprecations)


def get_warnings() -> list[str]:
    """Return a list of warning messages accumulated over this run."""
    return list(_global_warnings)


def get_deprecations() -> list[dict[str, _t.Any]]:
    """Return a list of deprecations accumulated over this run."""
    return list(_global_deprecations)


_global_warnings: list[str] = []
"""Global, ordered, de-duplicated storage of accumulated warnings for the current module run."""

_global_deprecations: list[dict[str, _t.Any]] = []
"""Global, ordered, de-duplicated storage of accumulated deprecations for the current module run."""
