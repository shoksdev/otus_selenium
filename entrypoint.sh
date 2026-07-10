#!/bin/bash
set -e
mkdir -p logs screenshots allure-results

exec pytest "$@"