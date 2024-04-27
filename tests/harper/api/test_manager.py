from unittest.mock import MagicMock

import pytest

from actions_helper.coverage.api.v1.info.router import manager
from actions_helper.coverage.api.v1.schemas import CoverageInfo
from actions_helper.coverage.utils import CoverageInfo, PickleCoverageStorage


def test_get_manager():
    name = "blablabla"
    if manager.storage._get(name):
        manager.storage._remove(name)
    value = manager.get_coverage_value(name)
    assert value == 0


def test_set_manager():
    count_of_info = len(manager.storage.data)
    cov = CoverageInfo(name="blablabla", total_coverage=100)
    assert manager.get_coverage_value(cov.name) == 0
    manager.set_coverage_value(cov)
    manager.storage._set(cov)
    assert count_of_info + 1 == len(manager.storage.data)
    assert manager.storage.data.get(cov.name)
    assert manager.get_coverage_value(cov.name) == cov.total_coverage
    manager.remove_coverage_info(cov.name)


def test_remove_info():
    count_of_info = len(manager.storage.data)
    cov = CoverageInfo(name="blablabla", total_coverage=100)

    manager.set_coverage_value(cov)
    assert manager.storage._get(cov.name) == cov.total_coverage
    assert manager.storage.data.get(cov.name)
    assert count_of_info + 1 == len(manager.storage.data)
    manager.remove_coverage_info(cov.name)
    assert not manager.storage.data.get(cov.name)
    assert count_of_info == len(manager.storage.data)


# Фикстура для создания временного файла
@pytest.fixture
def temp_file(tmp_path):
    return tmp_path / "tempfile.pkl"


# Фикстура для PickleCoverageStorage с моком файла
@pytest.fixture
def storage(temp_file):
    storage = PickleCoverageStorage(path_to_file=temp_file)
    storage.save = MagicMock()  # Мок сохранения, чтобы не писать в файл
    return storage


# Тестирование инициализации
def test_initialization(storage):
    assert isinstance(storage, PickleCoverageStorage)
    assert storage.path_to_file.exists()


# Тестирование установки значения
def test_set(storage):
    coverage = CoverageInfo(name="test_repo", total_coverage=75)
    storage._set(coverage)
    storage.save.assert_called_once()
    assert storage.data["test_repo"] == 75


# Тестирование получения значения
def test_get(storage):
    storage.data["test_repo"] = 90
    assert storage._get("test_repo") == 90
    assert storage._get("non_existing_repo") is None


# Тестирование удаления
def test_remove(storage):
    storage.data["test_repo"] = 90
    storage._remove("test_repo")
    storage.save.assert_called_once()
    assert "test_repo" not in storage.data
