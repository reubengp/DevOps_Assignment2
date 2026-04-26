# Version History

This project uses the same ACEest Fitness & Gym code base across incremental CI/CD improvements.

## Application Entry Point

- `ACEest_Fitness.py`: assignment-friendly Flask entry point
- `app.py`: existing Flask entry point retained for compatibility

Both files run the same Flask application created by `app.create_app()`.

## Incremental Versions

### Version 1
- Basic Flask application structure
- Routes for home, workouts, members, and plans

### Version 2
- Added Pytest-based route tests
- Added Docker containerization support

### Version 3
- Added Jenkins pipeline and SonarQube integration
- Added Kubernetes manifests for deployment

### Version 4
- Updated GitHub Actions workflow for current runner compatibility
- Added rollback documentation for Rolling Update deployment
