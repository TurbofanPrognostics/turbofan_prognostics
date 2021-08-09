#FROM python:3.7.8
#COPY requirements.txt .
#RUN pip install -r requirements.txt

#COPY . /turbofan_prognostics
#EXPOSE 8443
#CMD ["/bin/bash"]

# Start from a core stack version
FROM jupyter/datascience-notebook:33add21fab64
# Install from requirements.txt file
COPY --chown=${NB_UID}:${NB_GID} . requirements.txt /tmp/
RUN pip install --quiet --no-cache-dir --requirement /tmp/requirements.txt && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

COPY --chown=${NB_UID}:${NB_GID} . /work/turbofan_prognostics
