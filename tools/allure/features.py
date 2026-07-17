from enum import Enum


class AllureFeature(str, Enum):
    AUTHENTICATION = "Authentication"
    DASHBOARD = "Dashboard"
    COURSES = "Courses"
