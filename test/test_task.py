import unittest
from logic.task_logic import EventScheduler

class EventCreationTest(unittest.TestCase):

    def test_event_creation_process(self):
        scheduler = EventScheduler(self.driver)
        scheduler.goToAddEvent()
        scheduler.inputTitle("metting with tzahi")
        scheduler.inputDescription("working on final project")
        scheduler.pickTime("9", "30")
        scheduler.pickDate("27", "March", "2024")
        scheduler.chooseCategory("Important")
        scheduler.confirmSaveEvent()

