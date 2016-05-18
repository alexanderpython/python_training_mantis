from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    old_projects = app.project.get_project_list()
    project = Project(name=app.project.random_name(), description=app.project.random_description())
    app.project.add(project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.name) == sorted(new_projects, key=Project.name)
    assert app.soap.is_project_added("administrator", "root", project)
