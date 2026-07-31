from pathlib import Path


def create_package_files(src_directory: Path) -> None:
    """src 아래의 모든 디렉터리에 __init__.py를 생성한다."""

    if not src_directory.exists():
        raise FileNotFoundError(
            f"src 디렉터리를 찾을 수 없습니다: {src_directory}"
        )

    directories = [src_directory]

    for path in src_directory.rglob("*"):
        if path.is_dir():
            directories.append(path)

    for directory in directories:
        init_file = directory / "__init__.py"

        if init_file.exists():
            print(f"[기존 파일] {init_file}")
            continue

        init_file.write_text(
            '"""제조 Physical AI 하네스 패키지."""\n',
            encoding="utf-8",
        )

        print(f"[파일 생성] {init_file}")


if __name__ == "__main__":
    create_package_files(Path("src"))