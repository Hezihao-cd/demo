#!/usr/bin/env bash
# 用法:
# source cm.bash               -> 构建全部配置
# source cm.bash build_linux   -> 构建指定 name 的 build

TARGET=$1

if [ -n "$TARGET" ]; then
    python3 ./scripts/cc.py --target "$TARGET"
else
    python3 ./scripts/cc.py
fi
