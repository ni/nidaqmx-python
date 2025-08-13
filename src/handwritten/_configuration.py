"""nidaqmx configuration options."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Any, Callable, NamedTuple, TypeVar

from decouple import AutoConfig, Undefined, undefined

from nidaqmx._dotenvpath import get_dotenv_search_path

if TYPE_CHECKING:
    if sys.version_info >= (3, 11):
        from typing import Self
    else:
        from typing_extensions import Self


_PREFIX = "NIDAQMX"

_config = AutoConfig(str(get_dotenv_search_path()))

if TYPE_CHECKING:
    # Work around decouple's lack of type hints.
    _T = TypeVar("_T")

    def _config(
        option: str,
        default: _T | Undefined = undefined,
        cast: Callable[[str], _T] | Undefined = undefined,
    ) -> _T: ...


