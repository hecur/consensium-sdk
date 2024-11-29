#!/bin/bash
set -e

# Check if there are any changes in git
stash_created=false
if ! git diff-index --quiet HEAD --; then
    echo "Stashing changes before version increment..."
    git stash push -m "Automated stash before version increment"
    stash_created=true
fi

# Increment patch version in pyproject.toml
current_version=$(grep "version = " pyproject.toml | cut -d'"' -f2)
new_version=$(echo $current_version | awk -F. '{$NF = $NF + 1;}1' OFS=.)
sed -i '' "s/version = \"$current_version\"/version = \"$new_version\"/" pyproject.toml

# Commit version increment
git add pyproject.toml
git commit -m "Build: increment version to ${new_version}"

python -m pip install --upgrade build
python -m build
python -m pip install --upgrade twine
python -m twine upload --repository testpypi dist/*

# Pop stash if it was created
if [ "$stash_created" = true ]; then
    echo "Restoring stashed changes..."
    git stash pop
fi
