"""
Drill 2: Utilizing the Ecosystem

Drill: drill-14 Challenge: ex02
Goal

Python has a massive "ecosystem" of pre-built tools and libraries. If we want our toaster to print a daily weather forecast on the bread, we don't have to build a weather system from scratch!

Your Task: Write the exact line of Python code (as a string) that lets our program use a pre-built library named weather_service. (Hint: It uses the import command followed by a space and the library name).
Files to submit

    ex02/solution.py

Allowed functions

    class
    def
    self
    return
"""

# solution

class Ecosystem:
    def import_weather(self):
        # Return the exact Python import command as a string
        return "import weather_service"


def test_ecosystem():
    # Do not modify this testing wrapper
    eco = Ecosystem()
    return eco.import_weather()

def solution():
    return "import weather_service"
