from pathlib import Path

from django.conf import settings


def add_package(base_folder: Path, package_name: str) -> Path:
    package_folder = base_folder / package_name
    package_folder.mkdir(exist_ok=True)
    init_file = package_folder / "__init__.py"
    init_file.touch()
    return package_folder


def create_files(folder: Path, file_names: list) -> None:
    for file_name in file_names:
        file = folder / file_name
        file.touch()


def delete_existing_app_folder(app_folder: Path) -> None:
    if app_folder.exists():
        delete_folder = input("Do you want to delete it? (y/n)")
        if delete_folder.lower() == "y":
            app_folder.unlink()


def run(*args) -> None:
    """d-manage runscript dj_start_app --script-args new_app_name."""
    app_folder = settings.APPS_DIR / args[0]
    delete_existing_app_folder(app_folder)

    package_folder = add_package(settings.APPS_DIR, args[0])
    create_files(package_folder, ["admin.py", "apps.py", "models.py", "urls.py", "views_legacy.py"])

    api_folder = add_package(package_folder, "api")
    create_files(api_folder, ["serializers.py", "urls.py", "views_legacy.py"])

    add_package(package_folder, "migrations")

    tests_folder = add_package(package_folder, "tests")
    create_files(
        tests_folder,
        [
            "factories.py",
        ],
    )

    unit_tests_folder = add_package(tests_folder, "unit")
    create_files(unit_tests_folder, ["test_models.py", "test_views.py"])
