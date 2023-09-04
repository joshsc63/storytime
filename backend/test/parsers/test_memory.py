from parsers.memory import MemoryActionRecall, MemoryRecall, parse_into_memory


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
        MemoryRecall("Created a beautiful painting", "50 days ago"),
        MemoryRecall("Went to the Robot Workshop", "10 days ago"),
        MemoryRecall("Explored the Dark Forest", "5 days ago"),
        MemoryRecall("Built a robot companion named Sparky", "2 days ago"),
        MemoryRecall(
            "Discovered a hidden cave filled with rare minerals", "1 day ago"),
        MemoryActionRecall("Built a robot army", 8),
        MemoryActionRecall("Chased squirrels", 4),
        MemoryActionRecall("Sniffed a new rock", 3),
        MemoryActionRecall("Barked excitedly at a new invention", 7),
        MemoryActionRecall("Got distracted by a passing robot", 5),
    ]

    output = parse_into_memory(input)
    for i in range(len(expected_output)):
        assert str(expected_output[i]) == str(output[i])