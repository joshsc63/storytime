from parsers.memory import ActionMemory, RecallMemory, parse_into_memory


def test_parse_memory():
    input = """
Memory: Created a beautiful painting (50 days ago)
Memory: Went to the Robot Workshop (10 days ago)
Memory: Explored the Dark Forest (5 days ago)
Memory: Built a robot companion named Sparky (2 days ago)
Memory: Discovered a hidden cave filled with rare minerals (1 day ago)

Action: Built a robot army (8)
Action: Chased squirrels (4)
Action: Sniffed a new rock (3)
Action: Barked excitedly at a new invention (7)
Action: Got distracted by a passing robot (5)
"""

    expected_output = [
        RecallMemory(memory="Created a beautiful painting",
                     time_ago="50 days ago"),
        RecallMemory(memory="Went to the Robot Workshop",
                     time_ago="10 days ago"),
        RecallMemory(memory="Explored the Dark Forest", time_ago="5 days ago"),
        RecallMemory(memory="Built a robot companion named Sparky",
                     time_ago="2 days ago"),
        RecallMemory(
            memory="Discovered a hidden cave filled with rare minerals", time_ago="1 day ago"),
        ActionMemory(action="Built a robot army", importance=8),
        ActionMemory(action="Chased squirrels", importance=4),
        ActionMemory(action="Sniffed a new rock", importance=3),
        ActionMemory(
            action="Barked excitedly at a new invention", importance=7),
        ActionMemory(
            action="Got distracted by a passing robot", importance=5),
    ]

    output = parse_into_memory(input)
    for i in range(len(expected_output)):
        assert str(expected_output[i]) == str(output[i])
