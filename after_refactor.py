"""
Refactored Student Grade Analysis System
Author: Manik Kukkar
University: JECRC University, Jaipur
Description: Clean, modular, type-annotated, and PEP 8 compliant implementation
             refactored with AI assistance.
"""

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class StudentRecord:
    """Represents a student with marks and age."""
    name: str
    scores: List[float]
    age: int

    @property
    def average_score(self) -> float:
        """Calculate mean score for the student."""
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)

    @property
    def letter_grade(self) -> str:
        """Return letter grade based on average score."""
        avg = self.average_score
        if avg >= 90:
            return "A"
        if avg >= 75:
            return "B"
        if avg >= 50:
            return "C"
        return "F"

class GradeReport:
    """Handles reporting and analysis across a cohort of students."""
    def __init__(self, students: List[StudentRecord]):
        self.students = students

    def get_top_performing_student(self) -> Optional[StudentRecord]:
        """Find the student with the highest average score."""
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.average_score)

    def print_summary(self) -> None:
        """Output formatted performance table."""
        print(f"{'Student Name':<15} | {'Average':<8} | {'Grade':<5}")
        print("-" * 35)
        for s in self.students:
            print(f"{s.name:<15} | {s.average_score:<8.2f} | {s.letter_grade:<5}")
        print("-" * 35)
        top = self.get_top_performing_student()
        if top:
            print(f"Top Performer: {top.name} ({top.average_score:.2f})")

def main():
    cohort = [
        StudentRecord(name="Alice", scores=[85.0, 90.0, 78.0], age=20),
        StudentRecord(name="Bob", scores=[50.0, 60.0, 55.0], age=21),
        StudentRecord(name="Charlie", scores=[95.0, 100.0, 92.0], age=19),
        StudentRecord(name="David", scores=[40.0, 35.0, 45.0], age=22),
    ]

    report = GradeReport(cohort)
    report.print_summary()

if __name__ == "__main__":
    main()
