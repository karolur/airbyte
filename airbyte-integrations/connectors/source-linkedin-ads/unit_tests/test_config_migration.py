#
# Copyright (c) 2024 Airbyte, Inc., all rights reserved.
#

import os

from conftest import get_source, load_config
from source_linkedin_ads.config_migrations import MigrateCredentials


def test_credentials_config_migration():
    config_path = f"{os.path.dirname(__file__)}/test_configs/test_config_without_credentials.json"
    initial_config = load_config(config_path)
    migration_instance = MigrateCredentials
    source = get_source(initial_config)
    migration_instance.migrate(["check", "--config", config_path], source)
    test_migrated_config = load_config(config_path)
    assert test_migrated_config["credentials"]["access_token"] == initial_config["access_token"]
