import os, json

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

class Repo:

    def __init__(self):
        self.id = None
        self.owner = None #GitUser
        self.main_repo = False
        self.name = None
        self.forks = []

    def __str__(self):
        output = "id: %s\nname: %s\nowner: %s" % (str(self.id), self.name, self.owner.username)
        return output

    def add_fork(self, fork):
        self.forks.append(fork)

class GitUser:

    def __init__(self):
        self.id = None
        self.username = None
        self.avatar_url = None
        self.email = None

class Student(GitUser):

    def __init__(self):
        self.repo = None

class Problem:

    def __init__(self):
        self.number = None
        self.description = None
        self.committed_score = None
        self.first_solution_score = None
        self.datetime = None


class Solution:

    def __init__(self):
        self.problem = None
        self.student = None
        self.is_first_solution = False
        self.datetime = None

