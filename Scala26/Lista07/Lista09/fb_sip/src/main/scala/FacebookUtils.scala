import os.*
import com.restfb.types.User

import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

object FacebookUtils:
  def presentOnScreen(user: User): Unit =
    val likes = Option(user.getLikes)
      .map(_.getData.size())
      .getOrElse(0)

    println(s"${user.getName}, likes: $likes")

  // Easy appending to a file using os library
  // https://docs.scala-lang.org/toolkit/os-write-file.html

  def logToFile(logFile: String, msg: String): Unit =
    os.write.append(os.Path(logFile, os.pwd), msg + "\n")

  def getTimestamp: String =
    LocalDateTime.now.format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"))
