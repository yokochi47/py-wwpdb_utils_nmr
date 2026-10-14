# ============================================================
# Stage 1: Builder
# ============================================================
FROM python:3.14-slim AS builder

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Ignore irrelevant warning of pip
ENV PIP_ROOT_USER_ACTION=ignore

# Minimal build deps
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy the repository
COPY . /opt/py-wwpdb_utils_nmr

# Move working directory to the repo directory
WORKDIR /opt/py-wwpdb_utils_nmr

# System version information holder file under the current working directory
ENV VER_INFO=.ver_info

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies for resource update
RUN pip install \
        --no-cache-dir \
        -r standalone_update_requirements.txt

# Set Python path for standalone mode
ENV PYTHONPATH=/opt/py-wwpdb_utils_nmr/wwpdb/utils

# Extract package version information -> UTILS_NMR_VER
RUN grep version wwpdb/utils/nmr/__init__.py \
    | sed -e 's/__version__ = /export UTILS_NMR_VER=/' \
    | sed -e 's/"//g' > ${VER_INFO}

# Run ChemCompUpdater.py
# This creates: wwpdb/utils/nmr/ligand_dict
# Release date of Chemical Component Dictionary (CCD) -> CCD_REL
RUN CCD_REL_DATE_FILE=wwpdb/utils/nmr/ligand_dict/.ccd_rel_date \
    && python wwpdb/utils/nmr/ChemCompUpdater.py \
    && CCD_REL=`cat ${CCD_REL_DATE_FILE}` \
    && rm -f ${CCD_REL_DATE_FILE} \
    && echo "export CCD_REL=${CCD_REL}" >> ${VER_INFO}

# Run BMRBCsStatUpdater.py
# This updates: wwpdb/utils/nmr/bmrb_cs_stat
# Release date of BMRB chemical shift statistics -> CS_STAT_REL
RUN CS_STAT_REL_DATE_FILE=wwpdb/utils/nmr/bmrb_cs_stat/.cs_stat_rel_date \
    && python wwpdb/utils/nmr/BmrbCsStatUpdater.py \
    && CS_STAT_REL=`cat ${CS_STAT_REL_DATE_FILE}` \
    && rm -f ${CS_STAT_REL_DATE_FILE} \
    && echo "export CS_STAT_REL=${CS_STAT_REL}" >> ${VER_INFO}

# Install Python dependencies for runtime
RUN CFLAGS="-Wno-implicit-function-declaration -Wno-int-conversion" pip install \
        --no-cache-dir \
        --target=/install \
        -r standalone_runtime_requirements.txt

# Compile the speedy-antlr-tool C++ parser accelerators, which run the ANTLR4
# lexer/parser via the C++ target instead of the (much slower) Python runtime.
# The generated C++ and the bundled ANTLR4 C++ runtime are tracked in the repo,
# so this needs only the C++ toolchain installed above - no Java, no network, no
# .g4 grammars. Stripping matters: it takes each accelerator from ~25 MB to ~2 MB.
# If this step is removed the readers still work, falling back to the ANTLR
# Python runtime (see wwpdb/utils/nmr/AntlrParseUtil.py).
# WWPDB_NMR_BUILD_C_ACCEL additionally compiles the small C accelerator for
# wwpdb/utils/nmr/mr/ParserListenerUtil.py (copyFactor/copyPolySeq/atomKey/factorKey);
# ParserListenerUtil keeps the Python bodies and rebinds only when it imports.
RUN WWPDB_NMR_BUILD_SPEEDY_ANTLR=1 WWPDB_NMR_BUILD_C_ACCEL=1 \
    python setup.py build_clib build_ext --inplace -j "$(nproc)" \
    && find wwpdb/utils/nmr -name 'sa_*_cpp_parser*.so' -exec strip --strip-unneeded {} + \
    && rm -rf build

# Remove micellaneous files to reduce image size
RUN rm -f .dockerignore \
          Dockerfile \
          *.txt \
          setup.py \
          wwpdb/utils/nmr/components.cif.gz \
          wwpdb/utils/nmr/ChemCompUpdater.py \
          wwpdb/utils/nmr/BmrbCsStatUpdater.py \
    && rm -rf tools \
    && rm -rf wwpdb/utils/nmr/cpp_src

# ============================================================
# Stage 2: Runtime (minimal, non-root)
# ============================================================
FROM python:3.14-slim

# Runtime OS deps
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m -u 1000 appuser

# Copy installed Python environment
COPY --from=builder /install /opt/py-packages

# Set Python path for standalone mode
ENV PYTHONPATH=/opt/py-packages:/opt/py-wwpdb_utils_nmr/wwpdb/utils

# Copy application code with generated ligand_dict
COPY --from=builder --chown=appuser:appuser /opt/py-wwpdb_utils_nmr /opt/py-wwpdb_utils_nmr

# Create entrypoint script executable with exporting version information
RUN echo "#!/bin/sh" > /opt/entrypoint.sh && \
    echo "set -e" >> /opt/entrypoint.sh && \
    cat /opt/py-wwpdb_utils_nmr/.ver_info >> /opt/entrypoint.sh && \
    echo 'exec "$@"' >> /opt/entrypoint.sh && \
    chmod +x /opt/entrypoint.sh && \
    rm -f /opt/py-wwpdb_utils_nmr/.ver_info

# Set working directory
WORKDIR /mnt

# Switch to no-root user
USER appuser

# Set the entrypoint
ENTRYPOINT ["/opt/entrypoint.sh"]
