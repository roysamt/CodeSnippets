# Ubuntu Locale Resolution

When creating Ubuntu-based images in Docker, you don't run through the Ubuntu set-up process that you ordinarily would when interactively booting for the first time. The locale settings are therefore never configured, and this can result in difficult to track errors in Ubuntu Docker containers. Adding this snippet to Dockerfiles resolves this issue.