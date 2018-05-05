# static-code-analysis

## Run Analysis
### Pylint
To run `pylint` on a whole package or a single file, run:

    pylint [<package>|<file>]
    
The used configuration is in the `.pylintrc` file.

## Docker
Build Docker image

    docker build -t <name> .
    
Run analysis for all python files and packages in `<local folder>`

    docker run -v <local folder>:/modules <name>