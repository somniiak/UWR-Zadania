package models

object DB:
    val Students: List[Student] = List(
        Student(245678, "Majira Strawberry", 2),
        Student(256789, "Kurt Cobain", 2),
        Student(284576, "Gregor Samsa", 1),
        Student(342489, "Allison Burgers", 3),
        Student(299999, "Humbert Humbert", 3),
        Student(288888, "Dale Cooper", 1),
        Student(200666, "John Kramer", 3),
        Student(243543, "Nick Wilde", 2),
        Student(254355, "Pawbert Lynxley", 1),
        Student(323433, "David Lynch", 2),
        Student(324423, "Laura Palmer", 1),
        Student(300133, "Fluke Husky", 3)
    )

    val Lectures: List[Lecture] = List(
        Lecture("SIP", "Scala in Practice"),
        Lecture("DSA", "Data Structures and Algorithms"),
        Lecture("FP", "Functional Programming"),
        Lecture("DM", "Discrete Mathematics"),
        Lecture("STAT", "Probability and Statistics")
    )

    val Enrollments: List[Enrollment] = List(
        Enrollment(
            "SIP",
            List(
                Students(0), Students(1), Students(7), Students(9), Students(11)
            )
        ),

        Enrollment(
            "DSA",
            List(
                Students(2), Students(3), Students(5), Students(8), Students(10)
            )
        ),

        Enrollment(
            "FP",
            List(
                Students(0), Students(4), Students(6), Students(9), Students(10)
            )
        ),

        Enrollment(
            "DM",
            List(
                Students(1), Students(2), Students(5), Students(8), Students(11)
            )
        ),

        Enrollment(
            "STAT",
            List(
                Students(3), Students(4), Students(6), Students(7), Students(9)
            )
        )
    )
