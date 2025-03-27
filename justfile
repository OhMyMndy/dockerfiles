build:
    # COMPOSE_BAKE=true
    docker compose build

push:
    docker compose push

up:
    docker compose up -d

logs:
    docker compose logs -f --tail 100

act:
    gh act --reuse --container-options "--privileged"

act-fresh:
    gh act --container-options "--privileged"

check:
  hadolint **/Dockerfile

lint:
  docker run --rm \
    -e LINTER_RULES_PATH=./ \
    -e LOG_LEVEL=WARN \
    -e RUN_LOCAL=true \
    -e DEFAULT_BRANCH=main \
    -e CREATE_LOG_FILE=true \
    -e IGNORE_GITIGNORED_FILES=true \
    -e FIX_SHELL_SHFMT=true \
    -e FIX_JSON=true \
    -e FIX_JSON_PRETTIER=true \
    -e FIX_YAML_PRETTIER=true \
    -e FIX_MARKDOWN=true \
    -e FIX_MARKDOWN_PRETTIER=true \
    -e VALIDATE_CHECKOV=false \
    -e VALIDATE_KUBERNETES_KUBECONFORM=false \
    -e VALIDATE_PYTHON=false \
    -e VALIDATE_PYTHON_ISORT=false \
    -e VALIDATE_PYTHON_MYPY=false \
    -e VALIDATE_PYTHON_FLAKE8=false \
    -e VALIDATE_PYTHON_BLACK=false \
    -e VALIDATE_PYTHON_PYINK=false \
    -e VALIDATE_PYTHON_PYLINT=false \
    -e VALIDATE_PYTHON_RUFF=false \
    -e VALIDATE_GIT_COMMITLINT=false \
    -u $(id -u):$(id -g) \
    -v $PWD:/tmp/lint \
    ghcr.io/super-linter/super-linter:latest