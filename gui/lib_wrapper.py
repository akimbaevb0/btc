"""Minimal stub wrapper for the libbtctools library.

This module demonstrates how the GUI could interact with the underlying
C++ library. In this sandbox environment the actual shared library may be
absent, so the functions simply return placeholder values.
"""

from __future__ import annotations

import ctypes
from pathlib import Path


def _load_library() -> ctypes.CDLL | None:
    lib_path = Path(__file__).resolve().parent.parent / "build" / "libbtctools.so"
    if lib_path.exists():
        return ctypes.CDLL(str(lib_path))
    return None


_lib = _load_library()


def scan() -> str:
    """Simulate invoking a scan function from the library."""
    if _lib is None:
        return "library not found"
    # In a real implementation you would call the actual C function here
    return "scan invoked"
