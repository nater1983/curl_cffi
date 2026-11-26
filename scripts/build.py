from pathlib import Path

from cffi import FFI

# this is the upstream libcurl-impersonate version
__version__ = "2.2.2"

ffibuilder = FFI()
root_dir = Path(__file__).parent.parent

ffibuilder.set_source(
    "curl_cffi._wrapper",
    """
        #include "shim.h"
    """,
    library_dirs=["/usr/lib"],
    libraries=["curl-impersonate"],
    extra_objects=[],
    source_extension=".c",
    include_dirs=[
        str(root_dir / "include"),
        str(root_dir / "ffi"),
    ],
    sources=[
        str(root_dir / "ffi/shim.c"),
    ],
    extra_compile_args=[],
    extra_link_args=["-lstdc++"],
)

with open(root_dir / "ffi/cdef.c") as f:
    cdef_content = f.read()
    ffibuilder.cdef(cdef_content)


if __name__ == "__main__":
    ffibuilder.compile(verbose=False)
