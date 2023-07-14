#!/bin/env bash

set -o errexit

projects=("blog" "bugbounty-wordlist" "bugbounty-tools" "unbound-install" "view-pdf-in-browser" "unbound-config" "wordpress-plugin-download" "hacks" "dotfiles" "sublert-http")
for project in ${projects[@]}; do
    echo $project
    if [[ -d $project ]]; then
        cd $project
        git stash
        git pull
        cd ..
    fi
done
