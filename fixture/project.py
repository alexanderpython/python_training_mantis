import re
import string

import random
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def add(self, project):
        wd = self.app.wd
        self.open_manage_proj()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)
        wd.find_element_by_css_selector("input[value='Add Project']").click()

    def delete(self, project):
        wd = self.app.wd
        self.open_manage_proj()
        wd.find_element_by_link_text("%s" % project.name).click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()

    def open_manage_proj(self):
        wd = self.app.wd
        if not wd.current_url.endswith("manage_proj_page.php"):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def get_project_list(self):
        wd = self.app.wd
        self.open_manage_proj()
        project_list = []
        for element in wd.find_elements_by_css_selector("table[class='width100'] tbody tr[class='row-1']"):
            cells = element.find_elements_by_tag_name("td")
            id = self.extract_id(cells[0].find_element_by_tag_name("a").get_attribute("href"))
            name = cells[0].find_element_by_tag_name("a").text
            description = cells[4].text
            project_list.append(Project(id=id, name=name, description=description))
        for element in wd.find_elements_by_css_selector("table[class='width100'] tbody tr[class='row-2']"):
            cells = element.find_elements_by_tag_name("td")
            id = self.extract_id(cells[0].find_element_by_tag_name("a").get_attribute("href"))
            name = cells[0].find_element_by_tag_name("a").text
            description = cells[4].text
            project_list.append(Project(id=id, name=name, description=description))
        return project_list

    def extract_id(self, link):
        return re.sub('(.*)=', "", link)

    def random_name(self):
        digits = string.digits
        return "name" + "".join([random.choice(digits) for i in range(5)])

    def random_description(self):
        symbols = string.ascii_letters
        return "".join([random.choice(symbols) for i in range(20)])
