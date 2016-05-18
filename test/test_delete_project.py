import random
from model.project import Project


def test_delete_project(app):
    app.session.login("administrator", "root")
    if len(app.project.get_project_list()) == 0:
        app.project.add(Project(name=app.project.random_name(), description=app.project.random_description()))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete(project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.name) == sorted(new_projects, key=Project.name)
    assert app.soap.is_project_deleted("administrator", "root", project.id)
