import com.restfb.types.User
import FacebookUtils.{presentOnScreen, logToFile, getTimestamp}
import scala.concurrent.Future
import scala.util.{Success, Failure}
import scala.concurrent.ExecutionContext.Implicits.global

trait FacebookClient:
  def getUser(id: String): Future[User]

object FacebookService:
  // Mapping a Future for Both Success and Failure
  // https://www.baeldung.com/scala/future-success-failure

  def compareLikes(facebookClient: FacebookClient, logFile: String, usersIds: String*): Future[Unit] =
    val userFutures: Seq[Future[Unit]] =
      usersIds.map(id =>
        facebookClient.getUser(id).transform {
          case Success(user) =>
            presentOnScreen(user)
            logToFile(logFile, s"[$getTimestamp] Successfully fetched user $id")
            Success(())
          case Failure(ex) =>
            println(s"Failed to fetch user $id")
            val shortMsg = ex.getMessage.split(", URL:").head
            logToFile(logFile, s"[$getTimestamp] Failed to fetch user $id: $shortMsg")
            Success(())
        })

    Future.sequence(userFutures).map(_ => ())
