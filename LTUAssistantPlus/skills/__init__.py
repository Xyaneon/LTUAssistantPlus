#!/usr/bin/python3

import importlib
import logging
import os
import pkgutil

from services.assistant_services_base import AssistantServicesBase
from .skill import Skill

_all_skills = []
available_skills = []
skills_directory = os.path.abspath(os.path.dirname(__file__))


def init_skills(services: AssistantServicesBase):
    global _all_skills
    global available_skills
    for (module_finder, name, ispkg) in pkgutil.iter_modules([skills_directory]):
        if name.endswith("_skill"):
            print("Importing skill: " + name)
            importlib.import_module("." + name, __package__)
    _all_skills = [created_skill() for created_skill in Skill.__subclasses__()]
    print(str(len(_all_skills)) + " skills imported.")
    for created_skill in _all_skills:
        try:
            created_skill.perform_setup(services)
            available_skills.append(created_skill)
        except Exception:
            print("Error during setup of " + created_skill.__class__.__name__ + ":")
            print(logging.traceback.format_exc())
    print(str(len(available_skills)) + " skills available for use.")
