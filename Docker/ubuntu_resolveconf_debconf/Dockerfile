# Snippet

# For automated build containers or other scenarios where you don not care to use a container interactively,
# setting the following is the easiest way to automate answering dialogs prompted by package installs.
ENV DEBIAN_FRONTEND noninteractive

# A better solution would be to use ARG, which will not persist the environment variable in the built image:
ARG DEBIAN_FRONTEND=noninteractive

# Regardless, it is not uncommon to see a lot of debconf errors in your Dockerfile execution when building
# on top of a Ubuntu base image. The following line resolves this:
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# Similarly, for resolveconf errors, the following is a fix:
RUN echo "resolvconf resolvconf/linkify-resolvconf boolean false" | debconf-set-selections

# Both of the above should be placed before the first package installation of the script.

# End Snippet