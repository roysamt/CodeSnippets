# Ubuntu Resolveconf and Debconf

This snippet addresses three related issues:

1. Installing packages in Dockerfile on top of Ubuntu base image without warnings or interruptions from dialogs
2. Avoiding `debconf` errors when adding packages to Ubuntu base images
3. Avoiding `resolveconf` errors in the same situation