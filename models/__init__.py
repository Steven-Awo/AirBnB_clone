#!/usr/bin/python3
"""__init__ magic method that is for the models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
