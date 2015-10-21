'''
   This file is part of gitiscool.

    gitiscool is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    gitiscool is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
'''

import requests, json

from gitiscool import Repo, GitUser


class  RepoWrapper:

    repo_info_url =  "https://api.github.com/repos/%s/%s"

    def __init__(self):
        pass


    def get_repo(self, owner, reponame):
        url = self.repo_info_url % (owner, reponame)
        r = requests.get(url)
        json_object = json.loads(r.text)
        repository = Repo()
        repository.id = json_object["id"]
        repository.name = json_object["name"]

        owner_json = json_object["owner"]
        owner = GitUser()
        owner.avatar_url = owner_json["avatar_url"]
        owner.username = owner_json["login"]
        owner.id = owner_json["id"]
        repository.owner = owner

        print (repository)
        return repository


class UserWrapper:
    pass


