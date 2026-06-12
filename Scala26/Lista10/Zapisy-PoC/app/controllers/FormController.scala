package controllers

import javax.inject._
import play.api.mvc._
import models.DB

@Singleton
class FormController @Inject()(val controllerComponents: ControllerComponents)
  extends BaseController:

  def index = Action:
    Ok(views.html.index())

  def students = Action:
    Ok(views.html.students())

  def student(index: String) = Action:
    index.toIntOption match
      case Some(idx) =>

        DB.Students.find(_.index == idx) match
          case Some(student) =>

            val studentLectures =
              DB.Enrollments
                .filter(_.students.contains(student))
                .flatMap(enrollment =>
                  DB.Lectures.find(_.id == enrollment.id)
                )

            Ok(views.html.student(student, studentLectures))
          case None =>
            NotFound(s"Student with index $index not found")
      case None =>
        NotFound(s"Not a valid index")

  def lectures = Action:
    Ok(views.html.lectures())

  def lecture(id: String) = Action:
    DB.Lectures.find(_.id == id) match
      case Some(lecture) =>

        val enrolledStudents =
          DB.Enrollments
            .find(_.id == id)
            .map(_.students)
            .getOrElse(List.empty)

        Ok(views.html.lecture(lecture, enrolledStudents))
      case None =>
        NotFound(s"Lecture with ID $id not found")
