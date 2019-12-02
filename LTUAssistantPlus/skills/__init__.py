#!/usr/bin/python3

import importlib
import os
import pkgutil

from .skill import Skill

available_skills = []
skills_directory = os.path.abspath(os.path.dirname(__file__))

for (module_finder, name, ispkg) in pkgutil.iter_modules([skills_directory]):
    if name.endswith("_skill"):
        print("Importing skill: " + name)
        importlib.import_module("." + name, __package__)
available_skills = [created_skill() for created_skill in Skill.__subclasses__()]
print(str(len(available_skills)) + " skills loaded.")
