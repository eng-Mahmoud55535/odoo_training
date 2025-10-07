class SubTask:
    def __init__(self, tags: str, projectDays: int):
        self.tags = tags
        if projectDays <= 365:
            raise ValueError("projectDays must be greater than 365")
        self.projectDays = projectDays

if __name__ == "__main__":
    try:
        subtask = SubTask("exampleTag", 400)
        print(f"Tags: {subtask.tags}, Project Days: {subtask.projectDays}")
    except ValueError as e:
        print(e)
