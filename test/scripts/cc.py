#!/usr/bin/env python3
import os
import sys
import yaml
import shutil
import argparse
import subprocess


def run(cmd, cwd=None):
    print(">>>", " ".join(cmd))
    subprocess.check_call(cmd, cwd=cwd)


def build_one(cfg):
    name = cfg.get("name")
    generator = cfg.get("generator", "auto")
    jobs = cfg.get("jobs", os.cpu_count() or 4)
    build_type = cfg.get("build_type", "Debug")

    build_dir = f"build/{name}"
    os.makedirs(build_dir, exist_ok=True)

    if generator == "auto":
        generator = "ninja" if shutil.which("ninja") else "make"

    if generator == "ninja":
        gen_flag = ["-G", "Ninja"]
        build_cmd = ["ninja", f"-j{jobs}"]
    else:
        gen_flag = ["-G", "Unix Makefiles"]
        build_cmd = ["make", f"-j{jobs}"]

    cmake_args = gen_flag + [f"-DCMAKE_BUILD_TYPE={build_type}"]

    print(f"🔧 配置中: {build_dir}")
    run(["cmake", "../.."] + cmake_args, cwd=build_dir)

    print(f"⚙️  开始编译 {name} ...")
    run(build_cmd, cwd=build_dir)


def main():
    parser = argparse.ArgumentParser(description="Build project based on config.yaml")
    parser.add_argument("--target", help="只构建指定 name 的 build")
    args = parser.parse_args()

    cfg_path = "config/config.yaml"
    if not os.path.exists(cfg_path):
        print(f"❌ {cfg_path} not found")
        sys.exit(1)

    with open(cfg_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    build_cfgs = config.get("build", [])
    if args.target:
        build_cfgs = [cfg for cfg in build_cfgs if cfg.get("name") == args.target]

    for cfg in build_cfgs:
        print(f"\n🔹 开始构建: {cfg.get('name')}")
        build_one(cfg)


if __name__ == "__main__":
    main()
