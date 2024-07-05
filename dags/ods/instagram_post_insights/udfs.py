import logging
import os
from datetime import datetime
from typing import List, Optional

import requests
from airflow.models import Variable
from google.cloud import bigquery

logger = logging.getLogger(__name__)


def create_table_if_needed(table_id: str, schema: List[bigquery.SchemaField]) -> None:


def save_instagram_posts_and_insights()->None: