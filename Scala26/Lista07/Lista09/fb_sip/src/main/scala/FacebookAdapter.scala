import io.github.cdimascio.dotenv.Dotenv
import com.restfb.{DefaultFacebookClient, Version}
import com.restfb.types.User
import com.restfb.Parameter

import scala.concurrent.Future
import scala.concurrent.ExecutionContext.Implicits.global

object FacebookAdapter extends FacebookClient:
  private val dotenv = Dotenv.load()

  private val myAppSecret = dotenv.get("APP_SECRET")

  private val accessToken = dotenv.get("ACCESS_TOKEN")

  class MyFacebookClient(currentAccessToken: String)
    extends DefaultFacebookClient(currentAccessToken, myAppSecret, Version.VERSION_25_0)

  // Import Parameter and specify fields to get info about likes.
  // It's necesarry to wrap `with` in backticks or it won't work.

  def getUser(id: String): Future[User] = Future {
    val client = new MyFacebookClient(accessToken)
      client.fetchObject(id, classOf[User], Parameter.`with`("fields", "id,name,likes"))
  }
