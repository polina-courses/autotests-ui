from enum import Enum


class AllureStory(str, Enum):
    AUTHORIZATION = "Authorization"
    REGISTRATION = "Registration"
    DASHBOARD = "Dashboard"
    COURSES = "Courses"
