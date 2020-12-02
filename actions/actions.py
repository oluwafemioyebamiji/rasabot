# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Dict, Text, Union, Optional, List, Any
from rasa_sdk.forms import FormAction

class BuyHomeForm(FormAction):
    def name(self):
        return "buy_form"
    
    def required_slots(self, tracker) -> List[Text]:
        return ["cost","bedrooms","bathrooms","property_type","email"]
    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "cost":[self.from_text(),],
            "bedrooms":[self.from_text(),],
            "bathrooms":[self.from_text(),],
            "property_type":[self.from_text(),],
            "email":[self.from_text(),],
        }

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any],) -> List[Dict]:
        dispatcher.utter_message(text="Hello World!")
        return []
