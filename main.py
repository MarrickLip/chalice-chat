# {
#    "checksum": "string",
#    "createVersion": boolean,
#    "description": "string",
#    "enumerationValues": [
#       {
#          "synonyms": [ "string" ],
#          "value": "string"
#       }
#    ],
#    "parentSlotTypeSignature": "string",
#    "slotTypeConfigurations": [
#       {
#          "regexConfiguration": {
#             "pattern": "string"
#          }
#       }
#    ],
#    "valueSelectionStrategy": "string"
# }

from dataclasses import dataclass
from typing import Optional, Union, Sequence


@dataclass()
class SlotType:
    name: Optional[str] = None  # required by Lex API; fall back to self.__name__
    description: Optional[str] = None
    values: Optional[Sequence[Union[  # provide a range of types to support synonyms:
        str,  # just a value
        Sequence[str],  # [value, *synonyms]
        Sequence[Union[str, Sequence[str]]]  # [value, [synonyms]]
    ]]] = None
    pattern: Optional[str] = None
    originalValue: bool = True


class Message: pass

class PlainText(Message): pass

class SSML(Message): pass

class CustomPayload(Message): pass


Age = SlotType()

MessageOrString = Union[PlainText, SSML, CustomPayload, str]

@dataclass()
class Slot:
    prompts: Union[MessageOrString, Sequence[MessageOrString]]

    name: Optional[str] = None
    description: Optional[str] = None
    required: bool = False


# class Intent:
#     age: Age = Slot('What is your age?')
#     age = Age('What is your age?')


#     description: str = None
#
#     rejection_message: Message = None





    utterances = [
        f'my {age} is 23!'
    ]



def Intent(): pass
def Slot(): pass


class Intent:
    name = 'abcs'
    age = 12


class A(Intent):
    age = 12

    sample_utterances = f'dasds'